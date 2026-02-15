import asyncio
import json
import logging
from datetime import datetime
from typing import Optional
from urllib import parse

import aiohttp

from .models import (
    GeoguessrActivities,
    GeoguessrChallenge,
    GeoguessrDuel,
    GeoguessrMap,
    GeoguessrProfile,
    GeoguessrScore,
    GeoguessrStats,
    GeoguessrUserELO,
)

logger = logging.getLogger(__name__)


class Geoguessr:
    """Represents a geoguessr connection that connects to the Geoguessr API.
    This class is used to interact with the Geoguess API/
    """

    def __init__(self, ncfa) -> None:
        self._ncfa  = ncfa
        self.headers = {
            "Content-Type": "application/json",
            "cookie": f"_ncfa={self._ncfa }",
        }
        self.session = aiohttp.ClientSession(headers=self.headers)
        self.me = None
        self.meStats = None
        self.friends = None
        self.activities = None
        self.meId = None
        self.meElo = None

    async def get_all_my_infos(self):
        """
        Retrieves all the necessary information for the current user.

        This function sends a GET request to the Geoguessr API to retrieve the user's profile information
        using the provided session. It then extracts the user's ID from the response and stores it in the
        'id' attribute of the class. The function also calls the 'get_user_infos' method to retrieve the
        user's detailed information, the 'get_user_stats' method to retrieve the user's stats, and the
        '__get_my_friends_list' method to retrieve the user's friends list.

        Parameters:
            self (object): The instance of the class that the method is called on.

        Returns:
            None
        """
        async with self.session.get("https://www.geoguessr.com/api/v3/profiles/") as r:
            self.meId = (await r.json())["user"]["id"]
        self.me = await self.get_user_infos(self.meId)
        self.meStats = await self.get_user_stats(self.meId)
        self.friends = await self.__get_my_friends_list()
        self.activities = await self.__get_activities()
        self.meElo = await self.get_user_elo(self.meId)

    async def __get_activities(self):
        r = await self.session.get("https://geoguessr.com/api/v4/feed/private")
        js = await r.json()

        entries = js["entries"]
        paginationToken = js["paginationToken"]

        while paginationToken is not None:
            link = f"https://geoguessr.com/api/v4/feed/private?count=1000&paginationToken={paginationToken}"
            async with self.session.get(link) as r:
                js = await r.json()

            entries += js["entries"]
            paginationToken = js["paginationToken"]
        return GeoguessrActivities(entries)

    async def __get_my_friends_list(self):
        async with self.session.get("https://www.geoguessr.com/api/v3/social/friends/summary?page=0&fast=true") as r:
            js = await r.json()
            return {friend["nick"]: friend["userId"] for friend in js["friends"]}

    async def get_user_infos(self, userId: str) -> Optional[GeoguessrProfile]:
        """Give you all Geoguessr profile information about a player with the player's id

        Args:
            userId (str): The Geoguessr Id of the player you want the informations of

        Returns:
            GeoguessrProfile: All the informations about the player's profile
        """
        async with self.session.get(f"https://www.geoguessr.com/api/v3/users/{userId}") as r:
            if r.status == 200:
                user = GeoguessrProfile(await r.json())
                user.add_stats(await self.get_user_stats(user.id))
                return user

    async def get_user_elo(self, userId: str) -> Optional[GeoguessrUserELO]:
        """Get the different ELOs of a player with geoguessr ID as input

        Args:
            userId (str): The Geoguessr Id of the player you want the stats of

        Returns:
            GeoguessrUserELO: All the ELOs of the player
            None if the page doesn't exist.
        """

        try:
            async with self.session.get(f"https://www.geoguessr.com/api/v4/ranked-system/progress/{userId}") as r:
                contentType = r.headers.get("Content-Type")
                if contentType and "application/json" in contentType:
                    return GeoguessrUserELO(await r.json())
                raise ValueError("Content-Type for JSON response not acceptable.")
        except Exception:
            print("The player doesn't have his Geoguessr ELO stats page initialised, only a 'global ELO'.")

    async def get_user_stats(self, userId: str) -> GeoguessrStats:
        """Give you all Geoguessr stats about a player with the player's id

        Args:
            userId (str): The Geoguessr Id of the player you want the stats of

        Returns:
            GeoguessrStats: All the stats about the player's profile
        """

        async with self.session.get(f"https://www.geoguessr.com/api/v4/stats/users/{userId}") as r:
            return GeoguessrStats(await r.json())

    async def play_challenge(self, challengeUrl: str):
        """Play a challenge with your account (5 guesses are in 0,0 coordinates by default)

        Args:
            challenge_url (str): The URL of the challenge you want to play
        """
        challengeToken = challengeUrl.split("/")[-1] if "/" in challengeUrl else challengeUrl
        for i in range(5):
            async with self.session.post(
                f"https://www.geoguessr.com/api/v3/challenges/{challengeToken}",
                json={},
            ) as r:
                js = await r.json()
                gameToken = js["token"]
            await self.__play_round(gameToken, i)

    async def __play_round(self, gameToken: str, roundNumber: int):
        requestData = {"token": gameToken, "lat": 0, "lng": 0, "timedOut": True}

        await self.session.post(f"https://www.geoguessr.com/api/v3/games/{gameToken}", json=requestData)
        if roundNumber != 4:
            await self.session.get(f"https://www.geoguessr.com/api/v3/games/{gameToken}?client=web")

    async def get_challenge_score(self, challengeUrl: str):
        """Get scores on a standard challenge

        Args:
            challenge_url (str): The URL of the challenge you want to get results of

        Returns:
            list[GeoguessrScore]: A list of different scores for the challenge
        """
        challengeToken = challengeUrl.split("/")[-1] if "/" in challengeUrl else challengeUrl

        link = f"https://geoguessr.com/api/v3/results/highscores/{challengeToken}?friends=false&limit=26&minRounds=1"
        r = await self.session.get(link)

        if r.status != 200:  # Map not already played
            await self.play_challenge(challengeUrl)
            r = await self.session.get(link)

        js = await r.json()

        results = js["items"]
        paginationToken = js["paginationToken"]

        while paginationToken is not None:
            link = f"https://geoguessr.com/api/v3/results/highscores/{challengeToken}?friends=false&limit=26&minRounds=1&paginationToken={parse.quote(paginationToken)}"
            async with self.session.get(link) as r:
                js = await r.json()

            results += js["items"]
            paginationToken = js["paginationToken"]

        logger.debug("Retrieved challenge scores: %s", results)

        return [GeoguessrScore(result) for result in results]

    async def get_challenge_infos(self, challengeUrl: str):
        """Get informations about a challenge

        Args:
            challenge_url (str): The URL of the challenge you want infos of

        Returns:
            GeoguessrChallenge: All infos about the challenge
        """
        challengeToken = challengeUrl.split("/")[-1] if "/" in challengeUrl else challengeUrl
        async with self.session.get(f"https://www.geoguessr.com/api/v3/challenges/{challengeToken}") as r:
            js = await r.json()

        seconds = js["challenge"]["timeLimit"]

        js["challenge"]["str_timeLimit"] = (
            "No time limit"
            if seconds == 0
            else f"{(str(int(seconds / 60)) + ' min ') if int(seconds / 60) != 0 else ''}{(str(int(seconds % 60)) + ' sec') if int(seconds % 60) != 0 else ''}".strip()
        )
        move = not js["challenge"]["forbidMoving"]
        pan = not js["challenge"]["forbidRotating"]
        zoom = not js["challenge"]["forbidZooming"]

        js["mode"] = "Unknown"

        if move and pan and zoom:
            js["mode"] = "Move"
        elif not move and pan and zoom:
            js["mode"] = "No Move"
        elif not (move or pan or zoom):
            js["mode"] = "NMPZ"

        return GeoguessrChallenge(js)

    async def get_map_infos(self, mapUrl: str):
        """Get informations about a map

        Args:
            map_url (str): The URL of the map you want info from

        Returns:
            GeoguessrMap: All infos about the map
        """
        mapToken = mapUrl.split("/")[-1] if "/" in mapUrl else mapUrl
        async with self.session.get(f"https://www.geoguessr.com/api/maps/{mapToken}") as r:
            js = await r.json()
        try:
            async with self.session.get(f"https://www.geoguessr.com/api/v3/search/map?q={mapToken}") as r:
                js["coordinateCount"] = (await r.json())[0]["coordinateCount"]
        except Exception:
            js["coordinateCount"] = 0

        return GeoguessrMap(js)

    async def generate_challenge(
        self,
        mapUrl: str,
        move: bool = True,
        pan: bool = True,
        zoom: bool = True,
        timeLimit: int = 120,
        playMap: bool = True,
        numRounds: int = 5,
    ) -> str:
        """
        Generates a challenge based on a given map URL.

        Parameters:
            map_url (str): The URL of the map to generate the challenge from.
            move (bool, optional): Whether moving is allowed in the challenge. Defaults to True.
            pan (bool, optional): Whether panning (rotating) is allowed in the challenge. Defaults to True.
            zoom (bool, optional): Whether zooming is allowed in the challenge. Defaults to True.
            timeLimit (int, optional): The time limit for the challenge in seconds. Defaults to 120.
            play_map (bool, optional): Whether to automatically play the generated challenge. Defaults to True.
            num_rounds (int, optional): The number of locations in the challenge. Must be between 1 and 10. Defaults to 5.

        Returns:
            str: The URL of the generated challenge.

        """
        mapId = mapUrl.split("/")[-1] if "/" in mapUrl else mapUrl
        url = "https://www.geoguessr.com/api/v3/challenges"
        if numRounds < 1 or numRounds > 10:
            raise ValueError("numRounds must be between 1 and 10")
        data = {
            "map": mapId,
            "forbidMoving": not move,
            "forbidRotating": not pan,
            "forbidZooming": not zoom,
            "timeLimit": timeLimit,
            "roundCount": numRounds,
        }

        async with self.session.post(url, json=data) as response:
            js = await response.json()

        challengeToken = js["token"]
        challengeLink = f"https://www.geoguessr.com/challenge/{challengeToken}"

        if playMap:
            await self.play_challenge(challengeLink)

        return challengeLink

    async def get_duel_info(self, duelUrl: str):
        """
        Gets information about a duel.

        Parameters:
            duel_url (str): The URL of the duel to get information about.

        Returns:
            GeoguessrDuel: An object containing information about the duel.
        """
        duelToken = duelUrl.split("/")[-2] if "/" in duelUrl else duelUrl
        async with self.session.get(f"https://game-server.geoguessr.com/api/duels/{duelToken}") as r:
            js = await r.json()

        return GeoguessrDuel(js)

    async def get_ranked_duel_activity(self):
        """
        Gets a list of ranked duel activities.

        Returns:
            list: A list of tuples, containing the time of the duel in the format '%d-%m-%Y %H:%M:%S' and the URL of the duel.
        """
        if not self.activities:
            self.activities = await self.__get_activities()
        duelList = []
        for entry in self.activities.entries:
            if entry.get("payload") is not None:
                payload = json.loads(entry["payload"])
                if entry["type"] == 6 and payload["gameMode"] == "Duels":  # Single Ranked Duel
                    time = datetime.strptime(entry["time"][:19], "%Y-%m-%dT%H:%M:%S").strftime("%d-%m-%Y %H:%M:%S")
                    gameURL = f'https://www.geoguessr.com/duels/{payload["gameId"]}/summary'
                    duelList.append((time, gameURL))
                elif entry["type"] == 7 and isinstance(payload, list):  # List of ranked
                    for game in payload:
                        if game["type"] == 6 and game["payload"]["gameMode"] == "Duels":  # Type 6 = Ranked
                            time = datetime.strptime(game["time"][:19], "%Y-%m-%dT%H:%M:%S").strftime(
                                "%d-%m-%Y %H:%M:%S"
                            )
                            gameURL = f'https://www.geoguessr.com/duels/{game["payload"]["gameId"]}/summary'
                            duelList.append((time, gameURL))
                else:
                    pass
        return duelList

    def __del__(self):
        asyncio.ensure_future(self.session.close())
