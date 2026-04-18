from datetime import datetime
from enum import Enum
from typing import Any, Optional, Union, cast

import aiohttp

import geoguessr_async.geo_utils as gu


class GeoguessrStr:
    def to_tree(self, indent: int=0):
        """Convert the object to a tree-like string representation.

        Args:
            indent (int): Number of spaces to indent each level. Defaults to 0.

        Returns:
            str: Tree-like string representation of the object.
        """
        lines: list[str] = []

        for name, value in self.__dict__.items():
            attrSpaces = "    " * indent

            if isinstance(value, (int, float, str, bool, type(None))):
                lines.append(f"{attrSpaces}{name} ({value.__class__.__name__}) = {value!r}")

            elif isinstance(value, GeoguessrStr):
                lines.append(f"{attrSpaces}{name} ({value.__class__.__name__}):")
                lines.append(value.to_tree(indent + 2))

            elif isinstance(value, list):
                value = cast(list[Any], value)
                lines.append(f"{attrSpaces}{name} ({value.__class__.__name__}):")
                for item in value:
                    if isinstance(item, GeoguessrStr):
                        lines.append(item.to_tree(indent + 2))
                    else:
                        lines.append(f"{'    ' * (indent + 2)}{item!r}")
                    lines.append(f"{'    ' * (indent + 1)}--")
                lines.pop()

            elif isinstance(value, dict):
                value = cast(dict[str, Any], value)
                lines.append(f"{attrSpaces}{name} ({value.__class__.__name__}):")
                for key, item in value.items():
                    if hasattr(item, "to_tree"):
                        lines.append(f"{'    ' * (indent + 2)}{key!r}:")
                        lines.append(item.to_tree(indent + 3))
                    elif isinstance(item, list):
                        item = cast(list[Any], item)
                        lines.append(f"{'    ' * (indent + 2)}{key!r} ({item.__class__.__name__}):")
                        for listItem in item:
                            if hasattr(listItem, "to_tree"):
                                lines.append(listItem.to_tree(indent + 3))
                            else:
                                lines.append(f"{'    ' * (indent + 3)}{listItem!r}")
                    else:
                        lines.append(f"{'    ' * (indent + 2)}{key!r} = {item!r}")

            else:
                lines.append(f"{attrSpaces}{name} ({value.__class__.__name__}) = {value!r}")

        return "\n".join(lines)

    def __str__(self):
        return self.to_tree()


class GeoguessrStats(GeoguessrStr):
    """Represents Geoguessr user statistics.

    Attributes:
        battleRoyaleRankRank (int): Battle Royale rank.
        battleRoyaleRankRating (int): Battle Royale rating.
        # ... other stats attributes
    """

    def __init__(self, datas: dict[str, Any]) -> None:
        """Initialize GeoguessrStats.

        Args:
            datas (dict[str, Any]): Raw stats data from API.
        """
        # Ranked Team Duels
        self.rankedTeamDuelsStandard: Optional[GeoguessrStatsRankedTeamDuelsStandard] = GeoguessrStatsRankedTeamDuelsStandard(
            datas["rankedTeamDuelsStandard"]
        ) if datas.get("rankedTeamDuelsStandard") else None
        self.rankedTeamDuelsNoMove: Optional[GeoguessrStatsRankedTeamDuelsNoMove] = GeoguessrStatsRankedTeamDuelsNoMove(
            datas["rankedTeamDuelsNoMove"]
        ) if datas.get("rankedTeamDuelsNoMove") else None
        self.rankedTeamDuelsNmpz: Optional[GeoguessrStatsRankedTeamDuelsNmpz] = GeoguessrStatsRankedTeamDuelsNmpz(
            datas["rankedTeamDuelsNmpz"]
        ) if datas.get("rankedTeamDuelsNmpz") else None
        self.rankedTeamDuelsTotal: Optional[GeoguessrStatsRankedTeamDuelsTotal] = GeoguessrStatsRankedTeamDuelsTotal(
            datas["rankedTeamDuelsTotal"]
        ) if datas.get("rankedTeamDuelsTotal") else None

        # Battle Royale
        self.battleRoyaleDistance: Optional[GeoguessrStatsBattleRoyaleDistance] = GeoguessrStatsBattleRoyaleDistance(
            datas["battleRoyaleDistance"]
        ) if datas.get("battleRoyaleDistance") else None
        self.battleRoyaleCountry: Optional[GeoguessrStatsBattleRoyaleCountry] = GeoguessrStatsBattleRoyaleCountry(
            datas["battleRoyaleCountry"]
        ) if datas.get("battleRoyaleCountry") else None
        self.battleRoyaleMedals: Optional[GeoguessrStatsBattleRoyaleMedals] = GeoguessrStatsBattleRoyaleMedals(
            datas["battleRoyaleMedals"]
        ) if datas.get("battleRoyaleMedals") else None

        # Competitive
        self.competitiveCityStreaks: Optional[GeoguessrStatsCompetitiveCityStreaks] = GeoguessrStatsCompetitiveCityStreaks(
            datas["competitiveCityStreaks"]
        ) if datas.get("competitiveCityStreaks") else None
        self.competitiveStreaksMedals: Optional[GeoguessrStatsCompetitiveStreaksMedals] = GeoguessrStatsCompetitiveStreaksMedals(
            datas["competitiveStreaksMedals"]
        ) if datas.get("competitiveStreaksMedals") else None

        # Duels
        self.duels: Optional[GeoguessrStatsDuels] = GeoguessrStatsDuels(datas["duels"]) if datas.get("duels") else None
        self.duelsNoMove: Optional[GeoguessrStatsDuelsNoMove] = GeoguessrStatsDuelsNoMove(datas["duelsNoMove"]) if datas.get("duelsNoMove") else None
        self.duelsNmpz: Optional[GeoguessrStatsDuelsNmpz] = GeoguessrStatsDuelsNmpz(datas["duelsNmpz"]) if datas.get("duelsNmpz") else None
        self.duelsTotal: Optional[GeoguessrStatsDuelsTotal] = GeoguessrStatsDuelsTotal(datas["duelsTotal"]) if datas.get("duelsTotal") else None
        self.duelsMedals: Optional[GeoguessrStatsDuelsMedals] = GeoguessrStatsDuelsMedals(datas["duelsMedals"]) if datas.get("duelsMedals") else None

        # Unranked Duels
        self.unrankedDuels: Optional[GeoguessrStatsUnrankedDuels] = GeoguessrStatsUnrankedDuels(datas["unrankedDuels"]) if datas.get("unrankedDuels") else None
        self.unrankedDuelsNoMove: Optional[GeoguessrStatsUnrankedDuelsNoMove] = GeoguessrStatsUnrankedDuelsNoMove(
            datas["unrankedDuelsNoMove"]
        ) if datas.get("unrankedDuelsNoMove") else None
        self.unrankedDuelsNmpz: Optional[GeoguessrStatsUnrankedDuelsNmpz] = GeoguessrStatsUnrankedDuelsNmpz(
            datas["unrankedDuelsNmpz"]
        ) if datas.get("unrankedDuelsNmpz") else None
        self.unrankedDuelsTotal: Optional[GeoguessrStatsUnrankedDuelsTotal] = GeoguessrStatsUnrankedDuelsTotal(
            datas["unrankedDuelsTotal"]
        ) if datas.get("unrankedDuelsTotal") else None

        # Progression & Stats
        self.lifeTimeXpProgression: Optional[GeoguessrStatsLifeTimeXpProgression] = GeoguessrStatsLifeTimeXpProgression(
            datas["lifeTimeXpProgression"]
        ) if datas.get("lifeTimeXpProgression") else None

        self.totalMedals: Optional[GeoguessrStatsTotalMedals] = GeoguessrStatsTotalMedals(datas["totalMedals"]) if datas.get("totalMedals") else None
        self.teamDuels: Optional[GeoguessrStatsTeamDuels] = GeoguessrStatsTeamDuels(datas["teamDuels"]) if datas.get("teamDuels") else None
        self.teamDuelsQuickplay: Optional[GeoguessrStatsTeamDuelsQuickplay] = GeoguessrStatsTeamDuelsQuickplay(
            datas["teamDuelsQuickplay"]
        ) if datas.get("teamDuelsQuickplay") else None
        self.party: Optional[GeoguessrStatsParty] = GeoguessrStatsParty(datas["party"]) if datas.get("party") else None

        # Direct stats
        self.quickplayFlawlessVictories: Optional[int] = gu.int_or_none(datas.get("quickplayFlawlessVictories"))
        self.perfectRounds: Optional[int] = gu.int_or_none(datas.get("perfectRounds"))


class GeoguessrCompetitionMedals(GeoguessrStr):
    def __init__(self, datas: dict[str, Any]) -> None:
        self.bronze: Optional[int] = gu.int_or_none(datas.get("bronze"))
        self.silver: Optional[int] = gu.int_or_none(datas.get("silver"))
        self.gold: Optional[int] = gu.int_or_none(datas.get("gold"))
        self.platinum: Optional[int] = gu.int_or_none(datas.get("platinum"))


class GeoguessrPin(GeoguessrStr):
    def __init__(self, datas: dict[str, Any]) -> None:
        self.url: Optional[str] = gu.str_or_none(datas.get("pin", {}).get("url"))
        self.anchor: Optional[str] = gu.str_or_none(datas.get("pin", {}).get("anchor"))
        self.isDefault: Optional[bool] = gu.bool_or_none(datas.get("pin", {}).get("isDefault"))
        self.customImage: Optional[str] = datas.get("customImage")
        self.fullBody: Optional[str] = gu.str_or_none(datas.get("fullBodyPin"))
        self.borderUrl: Optional[str] = gu.str_or_none(datas.get("borderUrl"))


class GeoguessrDivision(GeoguessrStr):
    def __init__(self, datas: dict[str, Any]) -> None:
        self.type: Optional[int] = gu.int_or_none(datas.get("type"))
        self.startRating: Optional[int] = gu.int_or_none(datas.get("startRating"))
        self.endRating: Optional[int] = gu.int_or_none(datas.get("endRating"))


class GeoguessrCompetitive(GeoguessrStr):
    """Deprecated"""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.elo: Optional[int] = gu.int_or_none(datas.get("elo"))
        self.rating: Optional[int] = gu.int_or_none(datas.get("rating"))
        self.lastRatingChange: Optional[int] = gu.int_or_none(datas.get("lastRatingChange"))
        self.division: GeoguessrDivision = GeoguessrDivision(datas.get("division", {}))
        self.onLeaderboard: Optional[bool] = gu.bool_or_none(datas.get("onLeaderboard"))


class GeoguessrLevelProgress(GeoguessrStr):
    def __init__(self, datas: dict[str, Any]) -> None:
        self.level: Optional[int] = gu.int_or_none(datas.get("level"))
        self.xp: Optional[int] = gu.int_or_none(datas.get("xp"))
        self.levelXpStart: Optional[int] = gu.int_or_none(datas.get("levelXp"))
        self.nextLevelXp: Optional[int] = gu.int_or_none(datas.get("nextLevelXp"))
        self.nextLevel: Optional[int] = gu.int_or_none(datas.get("nextLevel"))
        self.title: Optional[GeoguessrXpTitle] = GeoguessrXpTitle(datas["title"]) if datas.get("title") else None
        self.competitionMedals: Optional[GeoguessrCompetitionMedals] = GeoguessrCompetitionMedals(datas["competitionMedals"]) if datas.get("competitionMedals") else None


class GeoguessrProfile(GeoguessrStr):
    """Represents a Geoguessr user profile.

    Attributes:
        nick (str): User nickname.
        created (str): Account creation date.
        isProUser (bool): Whether user has pro account.
        # ... other profile attributes
    """

    def __init__(self, datas: dict[str, Any]) -> None:
        """Initialize GeoguessrProfile.

        Args:
            datas (dict[str, Any]): Raw profile data from API.
        """
        self.nick: str = datas["nick"]
        self.createdAt: datetime = gu.to_datetime(datas["created"])
        self.isProUser: bool = datas["isProUser"]
        self.type: Optional[str] = gu.str_or_none(datas.get("type"))
        self.isVerified: bool =datas["isVerified"]
        self.pin: GeoguessrPin = GeoguessrPin(datas)
        self.color: Optional[int] = gu.int_or_none(datas.get("color"))
        self.url: str = datas["url"]
        self.id: str = datas["id"]
        self.countryCode: Optional[str] = gu.str_or_none(datas.get("countryCode"))
        self.battleRoyaleLevel: Optional[int] = gu.int_or_none(datas.get("br", {}).get("level"))
        self.battleRoyaleDivision: Optional[int] = gu.int_or_none(datas.get("br", {}).get("division"))
        self.streakProgress: Optional[Any] = datas.get("streakProgress")
        self.explorerProgress: Optional[Any] = datas.get("explorerProgress")
        self.dailyChallengeProgress: Optional[int] = gu.int_or_none(datas.get("dailyChallengeProgress"))
        self.progress: Optional[GeoguessrLevelProgress] = GeoguessrLevelProgress(datas["progress"]) if datas.get("progress") else None
        self.competitive: Optional[GeoguessrCompetitive] = GeoguessrCompetitive(datas["competitive"]) if datas.get("competitive") else None
        self.lastNameChange: datetime = gu.to_datetime(datas["lastNameChange"])
        self.lastNickOrCountryChange: datetime = gu.to_datetime(datas["lastNickOrCountryChange"])
        self.isBanned: bool = datas["isBanned"]
        self.chatBan: bool = datas["chatBan"]
        self.nameChangeAvailableAt: Optional[datetime] = gu.datetime_or_none(datas.get("nameChangeAvailableAt"))
        self.avatarUrl: Optional[str] = datas.get("avatar", {}).get("fullbodypath")
        self.isBotUser: bool = datas["isBotUser"]
        self.suspendedUntil: Optional[datetime] = gu.datetime_or_none(datas.get("suspendedUntil"))
        self.wallet: Optional[int] = gu.int_or_none(datas.get("wallet"))
        self.flair: Optional[int] = gu.int_or_none(datas.get("flair"))
        self.isCreator: Optional[bool] = gu.bool_or_none(datas.get("isCreator"))
        self.isAppAnonymous: Optional[bool] = gu.bool_or_none(datas.get("isAppAnonymous"))
        self.steamUserType: Optional[int] = gu.int_or_none(datas.get("steamUserType"))
        self.stats: Optional[GeoguessrStats] = None

    def add_stats(self, stats: GeoguessrStats) -> None:
        """Add stats to the profile."""
        self.stats = stats


class GeoguessrChallenge(GeoguessrStr):
    """Represents a Geoguessr challenge.

    Attributes:
        challengeToken (str): Challenge identifier.
        challengeMapslug (str): Map slug.
        challengeRoundcount (int): Number of rounds.
        # ... other challenge attributes
    """

    def __init__(self, datas: dict[str, Any]) -> None:
        """Initialize GeoguessrChallenge.

        Args:
            datas (dict[str, Any]): Raw challenge data from API.
        """
        self.token: str = datas["token"]
        self.mapSlug: str = datas["mapSlug"]
        self.roundCount: int = datas["roundCount"]
        self.timeLimit: int = datas["timeLimit"]
        self.movementOptions: GeoguessrMovementOptions = GeoguessrMovementOptions(datas)
        self.guessMapType: str = datas["guessMapType"]
        self.numberOfParticipants: Optional[int] = gu.int_or_none(datas.get("numberOfParticipants"))
        self.gameMode: str = datas["gameMode"]
        self.challengeType: int = datas["challengeType"]
        self.streakType: Optional[str] = gu.str_or_none(datas.get("streakType"))
        self.accessLevel: Optional[int] = gu.int_or_none(datas.get("accessLevel"))
        self.locationOrder: int = datas["locationOrder"]
        self.timeLimitStr: str = (
            "No time limit"
            if self.timeLimit == 0
            else f"{(str(int(self.timeLimit / 60)) + ' min ') if int(self.timeLimit / 60) != 0 else ''}{(str(int(self.timeLimit % 60)) + ' sec') if int(self.timeLimit % 60) != 0 else ''}".strip()
        )


class GeoguessrChallengeRound(GeoguessrStr):
    """Represents a single round in a Geoguessr challenge.

    Attributes:
        number (int): Round number.
        lat (float): Latitude of the location.
        long (float): Longitude of the location.
        # ... other round attributes
    """

    def __init__(self, roundData: dict[str, Any], roundNumber: int) -> None:
        """Initialize GeoguessrChallengeRound.

        Args:
            roundData (dict[str, Any]): Raw round data from API.
            roundNumber (int): Round number (1-based).
        """
        self.number: int = roundNumber
        self.lat: float = roundData["lat"]
        self.long: float = roundData["lng"]
        self.panoId: Optional[str] = gu.str_or_none(roundData.get("panoId"))
        self.heading: float = roundData["heading"]
        self.pitch: float = roundData["pitch"]
        self.zoom: float = roundData["zoom"]
        self.streakLocationCode: Optional[str] = roundData.get("streakLocationCode")
        self.startTime: datetime = gu.to_datetime(roundData["startTime"])


class GeoguessrScore(GeoguessrStr):
    """Represents a round score in Geoguessr.

    Attributes:
        amount (float): Score amount.
        unit (str): Score unit.
        percentage (float): Score percentage.
    """

    def __init__(self, scoreData: dict[str, Any]) -> None:
        """Initialize GeoguessrScore.

        Args:
            scoreData (dict[str, Any]): Raw score data from API.
        """
        self.amount: float = scoreData["amount"]
        self.unit: Optional[str] = gu.str_or_none(scoreData.get("unit"))
        self.percentage: Optional[float] = gu.float_or_none(scoreData.get("percentage"))


class GeoguessrDistance(GeoguessrStr):
    """Represents distance measurements in Geoguessr.

    Attributes:
        meters (float): Distance in meters.
        kilometers (float): Distance in kilometers.
        miles (float): Distance in miles.
    """

    def __init__(self, distanceData: dict[str, Any]) -> None:
        """Initialize GeoguessrDistance.

        Args:
            distanceData (dict[str, Any]): Raw distance data from API.
        """
        metersDistance: dict[str, Any] = distanceData["meters"]
        self.meters: float = metersDistance["amount"] * (1000 if metersDistance["unit"] == "km" else 1)
        self.kilometers: float = self.meters / 1000
        self.miles: float = self.meters / 1609.34


class GeoguessrTime(GeoguessrStr):
    """Represents time measurements in Geoguessr.

    Attributes:
        seconds (float): Time in seconds.
        minutes (float): Time in minutes.
        hours (float): Time in hours.
    """

    def __init__(
        self, seconds: Optional[float] = None, minutes: Optional[float] = None, hours: Optional[float] = None
    ) -> None:
        """Initialize GeoguessrTime.

        Args:
            seconds (Optional[float]): Time in seconds.
            minutes (Optional[float]): Time in minutes.
            hours (Optional[float]): Time in hours.
        """
        seconds = seconds if seconds is not None else None
        minutes = minutes if minutes is not None else None
        hours = hours if hours is not None else None
        if seconds is not None:
            self.seconds = seconds
            self.minutes = seconds / 60
            self.hours = seconds / 3600
        elif minutes is not None:
            self.seconds = minutes * 60
            self.minutes = minutes
            self.hours = minutes / 60
        elif hours is not None:
            self.seconds = hours * 3600
            self.minutes = hours * 60
            self.hours = hours


class GeoguessrPlayerGuesses(GeoguessrStr):
    """Represents a player's guess in a round.

    Attributes:
        number (int): Round number.
        lat (float): Guess latitude.
        long (float): Guess longitude.
        timedOut (bool): Whether player timed out.
        # ... other guess attributes
    """

    def __init__(self, guessData: dict[str, Any], roundNumber: int) -> None:
        """Initialize GeoguessrPlayerGuesses.

        Args:
            guessData (dict[str, Any]): Raw guess data from API.
            roundNumber (int): Round number (1-based).
        """
        self.number: int = roundNumber
        self.lat: float = guessData["lat"]
        self.long: float = guessData["lng"]
        self.timedOut: bool = guessData["timedOut"]
        self.timedOutWithGuess: bool = guessData["timedOutWithGuess"]
        self.skippedRound: bool = guessData["skippedRound"]
        self.roundScore: GeoguessrScore = GeoguessrScore(guessData["roundScore"])
        self.roundScoreInPercentage: int = guessData["roundScoreInPercentage"]
        self.roundScoreInPoints: int = guessData["roundScoreInPoints"]
        self.distance: GeoguessrDistance = GeoguessrDistance(guessData["distance"])
        self.distanceInMeters: float = guessData["distanceInMeters"]
        self.stepsCount: int = guessData["stepsCount"]
        self.streakLocationCode: Optional[str] = gu.str_or_none(guessData.get("streakLocationCode"))
        self.time: GeoguessrTime = GeoguessrTime(guessData.get("time"))


class GeoguessrGameBounds(GeoguessrStr):
    def __init__(self, datas: dict[str, dict[str, float]]) -> None:
        self.minLat: float = datas["min"]["lat"]
        self.minLng: float = datas["min"]["lng"]
        self.maxLat: float = datas["max"]["lat"]
        self.maxLng: float = datas["max"]["lng"]


class GeoguessrLevel(GeoguessrStr):
    def __init__(self, datas: dict[str, Any]) -> None:
        self.level: int = datas["level"]
        self.xpStart: int = datas["xpStart"]


class GeoguessrXpTitle(GeoguessrStr):
    def __init__(self, datas: dict[str, Any]) -> None:
        self.id: int = datas["id"]
        self.tierId: int = datas["tierId"]
        self.minimumLevel: int = datas.get("minimumLevel", 0)
        self.name: str = datas.get("name", "")


class GeoguessrScorePlayerInfo(GeoguessrStr):
    def __init__(self, playerDatas: dict[str, Any], progressionDatas: dict[str, Any]) -> None:
        self.isLeader: bool = playerDatas.get("isLeader", False)
        self.id: str = playerDatas["id"]
        self.nick: str = playerDatas["nick"]
        self.isVerified: bool = playerDatas.get("isVerified", False)
        self.flair: Optional[int] = gu.int_or_none(playerDatas.get("flair"))
        self.countryCode: Optional[str] = playerDatas.get("countryCode", "")
        self.pinUrl: Optional[str] = gu.str_or_none(playerDatas.get("pin", {}).get("url"))
        if progressionDatas and progressionDatas.get("xpProgressions"):
            self.xpBeforeChallenge: Optional[int] = gu.int_or_none(
                progressionDatas.get("xpProgressions", [{}, {}])[0].get("xp")
            )
            self.xpAfterChallenge: Optional[int] = gu.int_or_none(
                progressionDatas.get("xpProgressions", [{}, {}])[1].get("xp")
            )
            self.xpGained: Optional[int] = self.xpAfterChallenge - self.xpBeforeChallenge if self.xpAfterChallenge is not None and self.xpBeforeChallenge else None
            self.levelBeforeChallenge: Optional[GeoguessrLevel] = GeoguessrLevel(
                progressionDatas.get("xpProgressions", [{}, {}])[0].get("currentLevel")
            ) if isinstance(progressionDatas.get("xpProgressions", [{}, {}])[0].get("currentLevel"), dict) else None
            self.levelAfterChallenge: Optional[GeoguessrLevel] = GeoguessrLevel(
                progressionDatas.get("xpProgressions", [{}, {}])[1].get("currentLevel")
            ) if isinstance(progressionDatas.get("xpProgressions", [{}, {}])[1].get("currentLevel"), dict) else None
            self.titleBeforeChallenge: Optional[GeoguessrXpTitle] = GeoguessrXpTitle(
                progressionDatas.get("xpProgressions", [{}, {}])[0].get("currentTitle")
            ) if isinstance(progressionDatas.get("xpProgressions", [{}, {}])[0].get("currentTitle"), dict) else None
            self.titleAfterChallenge: Optional[GeoguessrXpTitle] = GeoguessrXpTitle(
                progressionDatas.get("xpProgressions", [{}, {}])[1].get("currentTitle")
            ) if isinstance(progressionDatas.get("xpProgressions", [{}, {}])[1].get("currentTitle"), dict) else None
        else:
            self.xpBeforeChallenge: Optional[int] = None
            self.xpAfterChallenge: Optional[int] = None
            self.xpGained: Optional[int] = None
            self.levelBeforeChallenge: Optional[GeoguessrLevel] = None
            self.levelAfterChallenge: Optional[GeoguessrLevel] = None
            self.titleBeforeChallenge: Optional[GeoguessrXpTitle] = None
            self.titleAfterChallenge: Optional[GeoguessrXpTitle] = None


class GeoguessrChallengePlayerTotalResult(GeoguessrStr):
    def __init__(self, datas: dict[str, Any]) -> None:
        self.totalScore: GeoguessrScore = GeoguessrScore(datas.get("totalScore", {}))
        self.totalDistance: GeoguessrDistance = GeoguessrDistance(datas.get("totalDistance", {}))
        self.totalStepsCount: Optional[int] = gu.int_or_none(datas.get("totalStepsCount"))
        self.totalTime: GeoguessrTime = GeoguessrTime(seconds=datas.get("totalTime"))
        self.totalStreak: Optional[int] = gu.int_or_none(datas.get("totalStreak"))
        self.guesses: list[GeoguessrPlayerGuesses] = [
            GeoguessrPlayerGuesses(guess, i + 1) for i, guess in enumerate(datas.get("guesses", [])) if guess is not None
        ]


class GeoguessrChallengeResult(GeoguessrStr):
    def __init__(self, datas: dict[str, Any]) -> None:
        gameDatas: Optional[dict[str, Any]] = datas.get("game")
        if gameDatas is None:
            raise ValueError("The game key is missing in the data.")
        self.player: GeoguessrScorePlayerInfo = GeoguessrScorePlayerInfo(
            gameDatas.get("player", {}), gameDatas.get("progressChange", {})
        )
        self.type: str = gameDatas["type"]
        self.mode: str = gameDatas["mode"]
        self.state: Optional[str] = gu.str_or_none(gameDatas.get("state"))
        self.roundCount: int = gameDatas["roundCount"]
        self.streakType: Optional[str] = gu.str_or_none(gameDatas.get("streakType"))
        self.map: str = gameDatas["map"]
        self.mapname: str = gameDatas["mapName"]
        self.panoramaprovider: Optional[int] = gu.int_or_none(gameDatas.get("panoramaprovider"))
        self.bounds: GeoguessrGameBounds = GeoguessrGameBounds(gameDatas["bounds"])
        self.rounds: list[GeoguessrChallengeRound] = [
            GeoguessrChallengeRound(round, i + 1)
            for i, round in enumerate(gameDatas.get("rounds", []))
            if round is not None
        ]
        self.playerTotalScore: GeoguessrChallengePlayerTotalResult = GeoguessrChallengePlayerTotalResult(
            gameDatas.get("player", {})
        )


class GeoguessMapAvatar(GeoguessrStr):
    def __init__(self, datas: dict[str, Any]) -> None:
        self.background: str = datas["background"]
        self.decoration: str = datas["decoration"]
        self.ground: str = datas["ground"]
        self.landscape: str = datas["landscape"]


class GeoguessrMap(GeoguessrStr):
    def __init__(self, datas: dict[str, Any]) -> None:
        self.id: str = datas["id"]
        self.name: str = datas["name"]
        self.slug: str = datas["slug"]
        self.description: Optional[str] = gu.str_or_none(datas.get("description"))
        self.url: str = datas["url"]
        self.playUrl: str = datas["playUrl"]
        self.published: bool = datas["published"]
        self.banned: bool = datas["banned"]
        self.backGround: Optional[str] = gu.str_or_none(datas.get("images", {}).get("backgroundLarge"))
        self.bounds: GeoguessrGameBounds = GeoguessrGameBounds(datas["bounds"])
        self.customCoordinates: Optional[Any] = datas.get("customCoordinates")
        self.coordinatesCount: Optional[str] = gu.str_or_none(datas.get("coordinateCount"))
        self.regions: Optional[Any] = datas.get("regions")
        self.creator: Optional[GeoguessrProfile] = (
            GeoguessrProfile(datas.get("creator", {})) if datas.get("creator") else None
        )
        self.createdAt: datetime = gu.to_datetime(datas["createdAt"])
        self.updatedAt: datetime = gu.to_datetime(datas["updatedAt"])
        self.numFinishedGames: Optional[int] = gu.int_or_none(datas.get("numFinishedGames"))
        self.likedByUser: Optional[Any] = datas.get("likedByUser")
        self.averageScore: Optional[int] = gu.int_or_none(datas.get("averageScore"))
        self.avatar: GeoguessMapAvatar = GeoguessMapAvatar(datas["avatar"])
        self.difficulty: str = datas["difficulty"]
        self.difficultyLevel: int = datas["difficultyLevel"]
        self.highscore: Any = datas["highscore"]
        self.deleted: bool = datas["deleted"]
        self.free: bool = datas["free"]
        self.panoramaprovider: Optional[str] = gu.str_or_none(datas.get("panoramaProvider"))
        self.inExplorerMode: bool = datas["inExplorerMode"]
        self.maxErrorDistance: int = datas["maxErrorDistance"]
        self.likes: int = datas["likes"]
        self.locationSelectionMode: int = datas["locationSelectionMode"]
        self.tags: list[Any] = datas["tags"]
        self.collaborators: Any = datas["collaborators"]
        self.flair: Optional[int] = gu.int_or_none(datas.get("flair"))
        self.mapSize: Optional[dict[str, Any]] = datas.get("mapSize")


class GeoguessrActivities(GeoguessrStr):
    """Represents Geoguessr activities data.

    Attributes:
        entries (list): List of activity entries.
    """

    def __init__(self, entries: list[Any]) -> None:
        """Initialize GeoguessrActivities.

        Args:
            entries (list): List of activity entries.
        """
        self.entries = entries


class GeoguessrUserELO(GeoguessrStr):
    """Represents Geoguessr user ELO ratings.

    Attributes:
        divisionNumber (int): Division number.
        divisionName (str): Division name.
        rating (int): User rating.
        tier (str): Tier name.
        gameModeRatingsStandardduels (int): Standard duels rating.
        gameModeRatingsNmpzduels (int): NMPZ duels rating.
        gameModeRatingsNomoveduels (int): No-move duels rating.
    """

    def __init__(self, datas: dict[str, Any]) -> None:
        """Initialize GeoguessrUserELO.

        Args:
            datas (dict[str, Any]): Raw ELO data from API.
        """
        self.divisionNumber: Optional[int] = gu.int_or_none(datas.get("divisionNumber"))
        self.divisionName: Optional[str] = gu.str_or_none(datas.get("divisionName"))
        self.rating: Optional[int] = gu.int_or_none(datas.get("rating"))
        self.tier: Optional[str] = gu.str_or_none(datas.get("tier"))
        self.gameModeRatingsStandardduels: Optional[int] = gu.int_or_none(datas.get("gameModeRatings", {}).get("standardDuels"))
        self.gameModeRatingsNmpzduels: Optional[int] = gu.int_or_none(datas.get("gameModeRatings", {}).get("nmpzDuels"))
        self.gameModeRatingsNomoveduels: Optional[int] = gu.int_or_none(datas.get("gameModeRatings", {}).get("noMoveDuels"))
        self.guessedFirstRate: Optional[int] = gu.int_or_none(datas.get("guessedFirstRate"))
        self.winStreak: Optional[int] = gu.int_or_none(datas.get("winStreak"))
        self.latestGamesVictory: Optional[list[bool]] = datas.get("latestGames")
        self.bestCountries: Optional[list[str]] = datas.get("bestCountries")
        self.worstCountries: Optional[list[str]] = datas.get("worstCountries")


class GeoguessrStatsRankedTeamDuelsStandard(GeoguessrStr):
    """Represents ranked team duels standard statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.numGamesPlayed: int = datas["numGamesPlayed"]
        self.numWins: int = datas["numWins"]
        self.winRatio: float = datas["winRatio"]


class GeoguessrStatsRankedTeamDuelsNoMove(GeoguessrStr):
    """Represents ranked team duels no move statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.numGamesPlayed: int = datas["numGamesPlayed"]
        self.numWins: int = datas["numWins"]
        self.winRatio: float = datas["winRatio"]


class GeoguessrStatsRankedTeamDuelsNmpz(GeoguessrStr):
    """Represents ranked team duels NMPZ statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.numGamesPlayed: int = datas["numGamesPlayed"]
        self.numWins: int = datas["numWins"]
        self.winRatio: float = datas["winRatio"]


class GeoguessrStatsRankedTeamDuelsTotal(GeoguessrStr):
    """Represents ranked team duels total statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.numGamesPlayed: int = datas["numGamesPlayed"]
        self.numWins: int = datas["numWins"]
        self.winRatio: float = datas["winRatio"]


class GeoguessrStatsBattleRoyaleDistance(GeoguessrStr):
    """Represents battle royale distance statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.numGamesPlayed: int = datas["numGamesPlayed"]
        self.avgPosition: float = datas["avgPosition"]
        self.numWins: int = datas["numWins"]
        self.winRatio: float = datas["winRatio"]
        self.avgGuessDistance: float = datas["avgGuessDistance"]
        self.numGuesses: int = datas["numGuesses"]


class GeoguessrStatsBattleRoyaleCountry(GeoguessrStr):
    """Represents battle royale country statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.numGamesPlayed: int = datas["numGamesPlayed"]
        self.avgPosition: float = datas["avgPosition"]
        self.numWins: int = datas["numWins"]
        self.winRatio: float = datas["winRatio"]
        self.numGuesses: int = datas["numGuesses"]
        self.avgCorrectGuesses: float = datas["avgCorrectGuesses"]


class GeoguessrStatsBattleRoyaleMedals(GeoguessrStr):
    """Represents battle royale medals statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.medalCountGold: int = datas["medalCountGold"]
        self.medalCountSilver: int = datas["medalCountSilver"]
        self.medalCountBronze: int = datas["medalCountBronze"]


class GeoguessrStatsCompetitiveCityStreaks(GeoguessrStr):
    """Represents competitive city streaks statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.numGamesPlayed: int = datas["numGamesPlayed"]
        self.avgPosition: float = datas["avgPosition"]
        self.numWins: int = datas["numWins"]
        self.winRatio: float = datas["winRatio"]
        self.numGuesses: int = datas["numGuesses"]
        self.avgCorrectGuesses: float = datas["avgCorrectGuesses"]


class GeoguessrStatsCompetitiveStreaksMedals(GeoguessrStr):
    """Represents competitive streaks medals statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.medalCountGold: int = datas["medalCountGold"]
        self.medalCountSilver: int = datas["medalCountSilver"]
        self.medalCountBronze: int = datas["medalCountBronze"]


class GeoguessrStatsDuels(GeoguessrStr):
    """Represents duels statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.numGamesPlayed: int = datas["numGamesPlayed"]
        self.avgPosition: float = datas["avgPosition"]
        self.numWins: int = datas["numWins"]
        self.winRatio: float = datas["winRatio"]
        self.avgGuessDistance: float = datas["avgGuessDistance"]
        self.numGuesses: int = datas["numGuesses"]
        self.numFlawlessWins: int = datas["numFlawlessWins"]


class GeoguessrStatsDuelsNoMove(GeoguessrStr):
    """Represents duels no move statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.numGamesPlayed: int = datas["numGamesPlayed"]
        self.avgPosition: float = datas["avgPosition"]
        self.numWins: int = datas["numWins"]
        self.winRatio: float = datas["winRatio"]
        self.avgGuessDistance: float = datas["avgGuessDistance"]
        self.numGuesses: int = datas["numGuesses"]
        self.numFlawlessWins: int = datas["numFlawlessWins"]


class GeoguessrStatsDuelsNmpz(GeoguessrStr):
    """Represents duels NMPZ statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.numGamesPlayed: int = datas["numGamesPlayed"]
        self.avgPosition: float = datas["avgPosition"]
        self.numWins: int = datas["numWins"]
        self.winRatio: float = datas["winRatio"]
        self.avgGuessDistance: float = datas["avgGuessDistance"]
        self.numGuesses: int = datas["numGuesses"]
        self.numFlawlessWins: int = datas["numFlawlessWins"]


class GeoguessrStatsDuelsTotal(GeoguessrStr):
    """Represents duels total statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.numGamesPlayed: int = datas["numGamesPlayed"]
        self.avgPosition: float = datas["avgPosition"]
        self.numWins: int = datas["numWins"]
        self.winRatio: float = datas["winRatio"]
        self.avgGuessDistance: float = datas["avgGuessDistance"]
        self.numGuesses: int = datas["numGuesses"]
        self.numFlawlessWins: int = datas["numFlawlessWins"]


class GeoguessrStatsDuelsMedals(GeoguessrStr):
    """Represents duels medals statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.medalCountGold: int = datas["medalCountGold"]
        self.medalCountSilver: int = datas["medalCountSilver"]
        self.medalCountBronze: int = datas["medalCountBronze"]


class GeoguessrStatsUnrankedDuels(GeoguessrStr):
    """Represents unranked duels statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.numGamesPlayed: int = datas["numGamesPlayed"]
        self.avgPosition: float = datas["avgPosition"]
        self.numWins: int = datas["numWins"]
        self.winRatio: float = datas["winRatio"]
        self.avgGuessDistance: float = datas["avgGuessDistance"]
        self.numGuesses: int = datas["numGuesses"]
        self.numFlawlessWins: int = datas["numFlawlessWins"]


class GeoguessrStatsUnrankedDuelsNoMove(GeoguessrStr):
    """Represents unranked duels no move statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.numGamesPlayed: int = datas["numGamesPlayed"]
        self.avgPosition: float = datas["avgPosition"]
        self.numWins: int = datas["numWins"]
        self.winRatio: float = datas["winRatio"]
        self.avgGuessDistance: float = datas["avgGuessDistance"]
        self.numGuesses: int = datas["numGuesses"]
        self.numFlawlessWins: int = datas["numFlawlessWins"]


class GeoguessrStatsUnrankedDuelsNmpz(GeoguessrStr):
    """Represents unranked duels NMPZ statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.numGamesPlayed: int = datas["numGamesPlayed"]
        self.avgPosition: float = datas["avgPosition"]
        self.numWins: int = datas["numWins"]
        self.winRatio: float = datas["winRatio"]
        self.avgGuessDistance: float = datas["avgGuessDistance"]
        self.numGuesses: int = datas["numGuesses"]
        self.numFlawlessWins: int = datas["numFlawlessWins"]


class GeoguessrStatsUnrankedDuelsTotal(GeoguessrStr):
    """Represents unranked duels total statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.numGamesPlayed: int = datas["numGamesPlayed"]
        self.avgPosition: float = datas["avgPosition"]
        self.numWins: int = datas["numWins"]
        self.winRatio: float = datas["winRatio"]
        self.avgGuessDistance: float = datas["avgGuessDistance"]
        self.numGuesses: int = datas["numGuesses"]
        self.numFlawlessWins: int = datas["numFlawlessWins"]


class GeoguessrStatsLifeTimeXpProgression(GeoguessrStr):
    """Represents lifetime XP progression statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.xp: int = datas["xp"]
        self.currentLevel: GeoguessrLevel = GeoguessrLevel(datas["currentLevel"])
        self.nextLevel: GeoguessrLevel = GeoguessrLevel(datas["nextLevel"])
        self.currentTitle: GeoguessrXpTitle = GeoguessrXpTitle(datas["currentTitle"])


class GeoguessrStatsTotalMedals(GeoguessrStr):
    """Represents total medals statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.medalCountGold: int = datas["medalCountGold"]
        self.medalCountSilver: int = datas["medalCountSilver"]
        self.medalCountBronze: int = datas["medalCountBronze"]


class GeoguessrStatsTeamDuels(GeoguessrStr):
    """Represents team duels statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.numGamesPlayed: int = datas["numGamesPlayed"]
        self.numWins: int = datas["numWins"]
        self.winRatio: float = datas["winRatio"]


class GeoguessrStatsTeamDuelsQuickplay(GeoguessrStr):
    """Represents team duels quickplay statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.numGamesPlayed: int = datas["numGamesPlayed"]
        self.numWins: int = datas["numWins"]


class GeoguessrDuelData(GeoguessrStr):
    """Represents complete Geoguessr duel data."""

    def __init__(self, datas: dict[str, Any]) -> None:
        """Initialize GeoguessrDuelData.

        Args:
            datas (dict[str, Any]): Raw duel data from API.
        """
        self.gameId: str = datas["gameId"]
        self.context: Optional[Any] = datas.get("context")
        self.teams: list[GeoguessrDuelTeam] = [GeoguessrDuelTeam(team) for team in datas.get("teams", [])]
        self.rounds: list[GeoguessrDuelRound] = [GeoguessrDuelRound(round) for round in datas.get("rounds", [])]
        self.totalRoundCount: int = datas["currentRoundNumber"]
        self.status: str = datas["status"]
        self.version: int = datas["version"]
        self.options: GeoguessrDuelOptions = GeoguessrDuelOptions(datas["options"])
        self.initialHealth: int = datas["initialHealth"]
        self.maxNumberOfRounds: int = datas["maxNumberOfRounds"]
        self.result: GeoguessrDuelResult = GeoguessrDuelResult(datas["result"])
        self.isPaused: bool = datas["isPaused"]
        self.gameServerNodeId: str = datas["gameServerNodeId"]
        self.tournamentId: Optional[str] = gu.str_or_none(datas.get("tournamentId"))
        self.playersId = [player.playerId for team in self.teams for player in team.players]
        self.replays: dict[str, list[GeoguessrDuelReplay]] = {playerId: [] for playerId in self.playersId}

    async def set_replays(self, session: aiohttp.ClientSession) -> None:
        """Get the replays of the duel."""
        for playerId in self.playersId:
            for i in range(self.totalRoundCount):
                async with session.get(
                    f"https://game-server.geoguessr.com/api/replays/{playerId}/{self.gameId}/{i+1}"
                ) as r:
                    self.replays[playerId].append(GeoguessrDuelReplay(await r.json()))


class GeoguessrDuelReplay(GeoguessrStr):
    """Represente a player replay in a duel."""

    class Type(Enum):
        """Type of replay."""

        PANOPOSITION = "PanoPosition"
        PANOPOV = "PanoPov"
        PANOZOOM = "PanoZoom"
        MAPZOOM = "MapZoom"
        MAPPOSITION = "MapPosition"
        GUESSWITHLATLNG = "GuessWithLatLng"
        PINPOSITION = "PinPosition"
        TIMER = "Timer"
        MAPDISPLAY = "MapDisplay"

    def __init__(self, datas: dict[str, dict[str, Any]]) -> None:
        self.datas: list[GeoguessrDuelReplayStep] = [GeoguessrDuelReplayStep(step) for step in datas.values()]


class GeoguessrDuelReplayStep(GeoguessrStr):

    class GeoguessrDuelReplayPanoPositionPayload(GeoguessrStr):
        """Represents PanoPosition type payload data."""

        def __init__(self, datas: dict[str, Any]) -> None:
            self.lat: dict[str, float] = datas["lat"]
            self.lng: dict[str, float] = datas["lng"]
            self.panoId: str = datas["panoId"]


    class GeoguessrDuelReplayPanoPovPayload(GeoguessrStr):
        """Represents PanoPov type payload data."""

        def __init__(self, datas: dict[str, Any]) -> None:
            self.heading: float = datas["heading"]
            self.pitch: float = datas["pitch"]


    class GeoguessrDuelReplayPanoZoomPayload(GeoguessrStr):
        """Represents PanoZoom type payload data."""

        def __init__(self, datas: dict[str, Any]) -> None:
            self.zoom: float = datas["zoom"]


    class GeoguessrDuelReplayMapZoomPayload(GeoguessrStr):
        """Represents MapZoom type payload data."""

        def __init__(self, datas: dict[str, Any]) -> None:
            self.zoom: int = datas["zoom"]


    class GeoguessrDuelReplayMapPositionPayload(GeoguessrStr):
        """Represents MapPosition type payload data."""

        def __init__(self, datas: dict[str, Any]) -> None:
            self.lat: float = datas["lat"]
            self.lng: float = datas["lng"]


    class GeoguessrDuelReplayGuessWithLatLngPayload(GeoguessrStr):
        """Represents GuessWithLatLng type payload data."""

        def __init__(self, datas: dict[str, Any]) -> None:
            self.lat: float = datas["lat"]
            self.lng: float = datas["lng"]


    class GeoguessrDuelReplayPinPositionPayload(GeoguessrStr):
        """Represents PinPosition type payload data."""

        def __init__(self, datas: dict[str, Any]) -> None:
            self.lat: float = datas["lat"]
            self.lng: float = datas["lng"]


    class GeoguessrDuelReplayTimerPayload(GeoguessrStr):
        """Represents Timer type payload data."""

        def __init__(self, datas: dict[str, Any]) -> None:
            self.time: int = datas["time"]


    class GeoguessrDuelReplayMapDisplayPayload(GeoguessrStr):
        """Represents MapDisplay type payload data."""

        def __init__(self, datas: dict[str, Any]) -> None:
            self.isActive: bool = datas["isActive"]
            self.isSticky: bool = datas["isSticky"]
            self.size: int = datas["size"]

    def __init__(self, datas: dict[str, Any]) -> None:
        self.time: datetime = datetime.fromtimestamp(float(datas["time"]) / 1000)
        self.type: GeoguessrDuelReplay.Type = GeoguessrDuelReplay.Type(datas.get("type"))
        self.payload: Union[
                GeoguessrDuelReplayStep.GeoguessrDuelReplayPanoPositionPayload,
                GeoguessrDuelReplayStep.GeoguessrDuelReplayPanoPovPayload,
                GeoguessrDuelReplayStep.GeoguessrDuelReplayPanoZoomPayload,
                GeoguessrDuelReplayStep.GeoguessrDuelReplayMapZoomPayload,
                GeoguessrDuelReplayStep.GeoguessrDuelReplayMapPositionPayload,
                GeoguessrDuelReplayStep.GeoguessrDuelReplayGuessWithLatLngPayload,
                GeoguessrDuelReplayStep.GeoguessrDuelReplayPinPositionPayload,
                GeoguessrDuelReplayStep.GeoguessrDuelReplayTimerPayload,
                GeoguessrDuelReplayStep.GeoguessrDuelReplayMapDisplayPayload
            ]

        payloadTypes = {
            GeoguessrDuelReplay.Type.PANOPOSITION: GeoguessrDuelReplayStep.GeoguessrDuelReplayPanoPositionPayload,
            GeoguessrDuelReplay.Type.PANOPOV: GeoguessrDuelReplayStep.GeoguessrDuelReplayPanoPovPayload,
            GeoguessrDuelReplay.Type.PANOZOOM: GeoguessrDuelReplayStep.GeoguessrDuelReplayPanoZoomPayload,
            GeoguessrDuelReplay.Type.MAPZOOM: GeoguessrDuelReplayStep.GeoguessrDuelReplayMapZoomPayload,
            GeoguessrDuelReplay.Type.MAPPOSITION: GeoguessrDuelReplayStep.GeoguessrDuelReplayMapPositionPayload,
            GeoguessrDuelReplay.Type.GUESSWITHLATLNG: GeoguessrDuelReplayStep.GeoguessrDuelReplayGuessWithLatLngPayload,
            GeoguessrDuelReplay.Type.PINPOSITION: GeoguessrDuelReplayStep.GeoguessrDuelReplayPinPositionPayload,
            GeoguessrDuelReplay.Type.TIMER: GeoguessrDuelReplayStep.GeoguessrDuelReplayTimerPayload,
            GeoguessrDuelReplay.Type.MAPDISPLAY: GeoguessrDuelReplayStep.GeoguessrDuelReplayMapDisplayPayload,
        }
        payloadType = payloadTypes.get(self.type)

        if payloadType is not None:
            self.payload = payloadType(datas["payload"])

class GeoguessrDuelTeam(GeoguessrStr):
    """Represents a team in a duel."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.id: str = datas["id"]
        self.name: str = datas["name"]
        self.healthAtEnd: int = datas["health"]
        self.players: list[GeoguessrDuelPlayer] = [GeoguessrDuelPlayer(player) for player in datas.get("players", [])]
        self.roundResults: list[GeoguessrDuelTeamRoundResult] = [
            GeoguessrDuelTeamRoundResult(result) for result in datas.get("roundResults", [])
        ]
        self.isMultiplierActive: bool = datas["isMultiplierActive"]
        self.multiplierAtEnd: float = datas["currentMultiplier"]


class GeoguessrDuelPlayer(GeoguessrStr):
    """Represents a player in a duel."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.playerId: str = datas["playerId"]
        self.guesses: list[GeoguessrDuelPlayerGuess] = [
            GeoguessrDuelPlayerGuess(guess) for guess in datas.get("guesses", [])
        ]
        self.rating: int = datas["rating"]
        self.countryCode: Optional[str] = gu.str_or_none(datas.get("countryCode"))
        self.progressChange: Optional[GeoguessrDuelProgressChange] = GeoguessrDuelProgressChange(datas["progressChange"]) if datas.get("progressChange") else None
        self.helpRequested: bool = datas["helpRequested"]
        self.isSteam: bool = datas["isSteam"]


class GeoguessrDuelPlayerGuess(GeoguessrStr):
    """Represents a player's guess in a duel."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.roundNumber: int = datas["roundNumber"]
        self.lat: float = self.__parse_big_number(datas.get("lat"))
        self.lng: float = self.__parse_big_number(datas.get("lng"))
        self.distance: float = self.__parse_big_number(datas.get("distance"))
        self.created: datetime = gu.to_datetime(datas["created"])
        self.isTeamsBestGuessOnRound: bool = datas["isTeamsBestGuessOnRound"]
        self.score: int = datas["score"]

    def __parse_big_number(self, value: Any) -> float:
        """Parse Big Number format or regular number."""
        if (
            isinstance(value, dict) and all(key in value for key in ["type", "value"])
            and value["type"] == "Big Number"
        ):
            v: dict[str, Any] = value
            return float(str(v["value"]).replace("n", ""))

        if isinstance(value, (int, float)):
            return float(value)

        return 0.0


class GeoguessrDuelTeamRoundResult(GeoguessrStr):
    """Represents round result for a team."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.roundNumber: int = datas["roundNumber"]
        self.score: int = datas["score"]
        self.healthBefore: int = datas["healthBefore"]
        self.healthAfter: int = datas["healthAfter"]
        self.bestGuess: GeoguessrDuelPlayerGuess = GeoguessrDuelPlayerGuess(datas["bestGuess"])
        self.activeMultiplier: bool = datas["activeMultiplier"]
        self.damageDealt: int = datas["damageDealt"]
        self.multiplier: float = datas["multiplier"]


class GeoguessrDuelRound(GeoguessrStr):
    """Represents a duel round."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.roundNumber: int = datas["roundNumber"]
        self.panorama: GeoguessrDuelPanorama = GeoguessrDuelPanorama(datas["panorama"])
        self.hasProcessedRoundTimeout: bool = datas["hasProcessedRoundTimeout"]
        self.isHealingRound: bool = datas["isHealingRound"]
        self.multiplier: float = datas["multiplier"]
        self.damageMultiplier: float = datas["damageMultiplier"]
        self.startTime: datetime = gu.to_datetime(datas["startTime"])
        self.endTime: datetime = gu.to_datetime(datas["endTime"])
        self.timerStartTime: datetime = gu.to_datetime(datas["timerStartTime"])


class GeoguessrDuelPanorama(GeoguessrStr):
    """Represents round panorama data."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.panoId: str = datas["panoId"]
        self.lat: float = self.__parse_big_number(datas["lat"])
        self.lng: float = self.__parse_big_number(datas["lng"])
        self.countryCode: str = datas["countryCode"]
        self.heading: float = self.__parse_big_number(datas["heading"])
        self.pitch: float = self.__parse_big_number(datas["pitch"])
        self.zoom: int = datas["zoom"]

    def __parse_big_number(self, value: Any) -> float:
        """Parse Big Number format or regular number."""
        if (
            isinstance(value, dict) and all(key in value for key in ["type", "value"])
            and value["type"] == "Big Number"
        ):
            v: dict[str, Any] = value
            return float(str(v["value"]).replace("n", ""))

        if isinstance(value, (int, float)):
            return float(value)

        return 0.0


class GeoguessrDuelProgressChange(GeoguessrStr):
    """Represents a player's progression."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.xpAtStart: Optional[GeoguessrDuelXpProgression] = (
            GeoguessrDuelXpProgression(datas["xpProgressions"][0])
        ) if datas.get("xpProgressions") else None
        self.xpAtEnd: Optional[GeoguessrDuelXpProgression] = (
            GeoguessrDuelXpProgression(datas["xpProgressions"][1])
        ) if datas.get("xpProgressions") else None
        self.awardedXp: Optional[GeoguessrDuelAwardedXp] = GeoguessrDuelAwardedXp(datas["awardedXp"]) if datas.get("awardedXp") else None
        self.medal: Optional[str] = gu.str_or_none(datas.get("medal"))
        self.competitiveProgress: Optional[Any] = datas.get("competitiveProgress")
        self.rankedSystemProgress: Optional[GeoguessrDuelRankedSystemProgress] = GeoguessrDuelRankedSystemProgress(
            datas["rankedSystemProgress"]
        ) if datas.get("rankedSystemProgress") else None
        self.rankedTeamDuelsProgress: Optional[Any] = datas.get("rankedTeamDuelsProgress")
        self.quickplayDuelsProgress: Optional[Any] = datas.get("quickplayDuelsProgress")


class GeoguessrDuelXpProgression(GeoguessrStr):
    """Represents XP progression."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.xp: int = datas["xp"]
        self.currentLevel: GeoguessrLevel = GeoguessrLevel(datas["currentLevel"])
        self.nextLevel: GeoguessrLevel = GeoguessrLevel(datas["nextLevel"])
        self.currentTitle: GeoguessrXpTitle = GeoguessrXpTitle(datas["currentTitle"])


class GeoguessrDuelAwardedXp(GeoguessrStr):
    """Represents awarded XP."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.totalAwardedXp: int = datas["totalAwardedXp"]
        self.xpAwards: list[GeoguessrDuelXpAward] = [GeoguessrDuelXpAward(award) for award in datas.get("xpAwards", [])]


class GeoguessrDuelXpAward(GeoguessrStr):
    """Represents an XP reward."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.xp: int = datas["xp"]
        self.reason: str = datas["reason"]
        self.count: int = datas["count"]


class GeoguessrDuelRankedSystemProgress(GeoguessrStr):
    """Represents ranked system progression."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.points: dict[str, int] = datas["points"]
        self.totalWeeklyPoints: int = datas["totalWeeklyPoints"]
        self.weeklyCap: int = datas["weeklyCap"]
        self.gamesPlayedWithinWeeklyCap: int = datas["gamesPlayedWithinWeeklyCap"]
        self.positionBefore: Optional[int] = gu.int_or_none(datas.get("positionBefore"))
        self.positionAfter: Optional[int] = gu.int_or_none(datas.get("positionAfter"))
        self.ratingBefore: int = datas["ratingBefore"]
        self.ratingAfter: int = datas["ratingAfter"]
        self.winStreak: int = datas["winStreak"]
        self.bucketSortedBy: str = datas["bucketSortedBy"]
        self.gameMode: str = datas["gameMode"]
        self.gameModeRatingBefore: int = datas["gameModeRatingBefore"]
        self.gameModeRatingAfter: int = datas["gameModeRatingAfter"]
        self.gameModeGamesPlayed: int = datas["gameModeGamesPlayed"]
        self.gameModeGamesRequired: int = datas["gameModeGamesRequired"]
        self.placementGamesPlayed: int = datas["placementGamesPlayed"]
        self.placementGamesRequired: int = datas["placementGamesRequired"]


class GeoguessrDuelOptions(GeoguessrStr):
    """Represents duel options."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.initialHealth: int = datas["initialHealth"]
        self.individualInitialHealth: bool = datas["individualInitialHealth"]
        self.initialHealthTeamOne: int = datas["initialHealthTeamOne"]
        self.initialHealthTeamTwo: int = datas["initialHealthTeamTwo"]
        self.roundTime: int = datas["roundTime"]
        self.maxRoundTime: int = datas["maxRoundTime"]
        self.gracePeriodTime: int = datas["gracePeriodTime"]
        self.gameTimeOut: int = datas["gameTimeOut"]
        self.maxNumberOfRounds: int = datas["maxNumberOfRounds"]
        self.healingRounds: list[int] = datas.get("healingRounds", [])
        self.movementOptions: GeoguessrMovementOptions = GeoguessrMovementOptions(datas["movementOptions"])
        self.mapSlug: str = datas["mapSlug"]
        self.isRated: bool = datas["isRated"]
        self.map: GeoguessrDuelMap = GeoguessrDuelMap(datas["map"])
        self.duelRoundOptions: list[Any] = datas["duelRoundOptions"]
        self.roundsWithoutDamageMultiplier: int = datas["roundsWithoutDamageMultiplier"]
        self.disableMultipliers: bool = datas["disableMultipliers"]
        self.multiplierIncrement: int = datas["multiplierIncrement"]
        self.disableHealing: bool = datas["disableHealing"]
        self.isTeamDuels: bool = datas["isTeamDuels"]
        self.gameContext: GeoguessrDuelGameContext = GeoguessrDuelGameContext(datas["gameContext"])
        self.roundStartingBehavior: str = datas["roundStartingBehavior"]
        self.flashbackRounds: list[Any] = datas["flashbackRounds"]
        self.competitiveGameMode: str = datas["competitiveGameMode"]
        self.countAllGuesses: bool = datas["countAllGuesses"]
        self.masterControlAutoStartRounds: bool = datas["masterControlAutoStartRounds"]
        self.consumedLocationsIdentifier: str = datas["consumedLocationsIdentifier"]
        self.useCuratedLocations: bool = datas["useCuratedLocations"]
        self.extraWaitTimeBetweenRounds: int = datas["extraWaitTimeBetweenRounds"]
        self.roundCountdownDelay: int = datas["roundCountdownDelay"]
        self.guessMapType: str = datas["guessMapType"]
        self.botBehaviors: Optional[Any] = datas.get("botBehaviors")
        self.activeMultiplier: bool = datas["activeMultiplier"]
        self.roundWinMultiplierIncrement: int = datas["roundWinMultiplierIncrement"]


class GeoguessrMovementOptions(GeoguessrStr):
    """Represents movement options."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.forbidMoving: bool = datas["forbidMoving"]
        self.forbidZooming: bool = datas["forbidZooming"]
        self.forbidRotating: bool = datas["forbidRotating"]


class GeoguessrDuelMap(GeoguessrStr):
    """Represents duel map."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.name: str = datas["name"]
        self.slug: str = datas["slug"]
        self.bounds: GeoguessrDuelMapBounds = GeoguessrDuelMapBounds(datas["bounds"])
        self.maxErrorDistance: int = datas["maxErrorDistance"]


class GeoguessrDuelMapBounds(GeoguessrStr):
    """Represents map bounds."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.min: GeoguessrDuelCoordinate = GeoguessrDuelCoordinate(datas["min"])
        self.max: GeoguessrDuelCoordinate = GeoguessrDuelCoordinate(datas["max"])


class GeoguessrDuelCoordinate(GeoguessrStr):
    """Represents a geographic coordinate."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.lat: float = self.__parse_big_number(datas["lat"])
        self.lng: float = self.__parse_big_number(datas["lng"])

    def __parse_big_number(self, value: Any) -> float:
        """Parse Big Number format or regular number."""
        if (
            isinstance(value, dict) and all(key in value for key in ["type", "value"])
            and value["type"] == "Big Number"
        ):
            v: dict[str, Any] = value
            return float(str(v["value"]).replace("n", ""))

        if isinstance(value, (int, float)):
            return float(value)

        return 0.0


class GeoguessrDuelGameContext(GeoguessrStr):
    """Represents game context."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.type: str = datas["type"]
        self.id: str = datas["id"]


class GeoguessrDuelResult(GeoguessrStr):
    """Represents duel result."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.isDraw: bool = datas["isDraw"]
        self.winningTeamId: str = datas["winningTeamId"]
        self.winnerStyle: str = datas["winnerStyle"]


class GeoguessrStatsParty(GeoguessrStr):
    """Represents party statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.total: int = datas["total"]
        self.duels: int = datas["duels"]
        self.teamDuels: int = datas["teamDuels"]
        self.battleRoyaleCountries: int = datas["battleRoyaleCountries"]
        self.battleRoyaleDistance: int = datas["battleRoyaleDistance"]
        self.cityStreaks: int = datas["cityStreaks"]
        self.liveChallenges: int = datas["liveChallenges"]
        self.bullseye: int = datas["bullseye"]
        self.quizzes: int = datas["quizzes"]


class GeoguessrClub(GeoguessrStr):
    """Represents a Geoguessr club."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.clubId: str = datas["clubId"]
        self.name: str = datas["name"]
        self.members: list[GeoguessrClubMember] = [GeoguessrClubMember(member) for member in datas["members"]]
        self.joinRule: int = datas["joinRule"]
        self.tag: str = datas["tag"]
        self.description: Optional[str] = datas.get("description")
        self.createdAt: datetime = gu.to_datetime(datas["createdAt"])
        self.language: str = datas["language"]
        self.memberCount: int = datas["memberCount"]
        self.maxMemberCount: int = datas["maxMemberCount"]
        self.level: int = datas["level"]
        self.xp: int = datas["xp"]
        self.labels: list[str] = datas.get("labels", [])
        self.logo: GeoguessrClubLogo = GeoguessrClubLogo(datas["logo"])
        self.stats: GeoguessrClubStats = GeoguessrClubStats(datas["stats"])
        self.backgroundUrl: str = datas["backgroundUrl"]


class GeoguessrClubMember(GeoguessrStr):
    """Represents user information for a club member."""

    class Role(Enum):
        ADMIN = 1
        MEMBER = 2

    def __init__(self, datas: dict[str, Any]) -> None:
        self.userId: str = datas["user"]["userId"]
        self.nick: str = datas["user"]["nick"]
        self.avatar: str = datas["user"]["avatar"]
        self.fullbodyAvatar: str = datas["user"]["fullbodyAvatar"]
        self.borderUrl: Optional[str] = datas["user"].get("borderUrl")
        self.isVerified: bool = datas["user"].get("isVerified")
        self.flair: int = datas["user"].get("flair")
        self.countryCode: str = datas["user"].get("countryCode")
        self.tierId: int = datas["user"].get("tierId")
        self.clubUserType: int = datas["user"].get("clubUserType")
        self.role: GeoguessrClubMember.Role = GeoguessrClubMember.Role(datas["role"])
        self.joinedAt: datetime = datas["joinedAt"]
        self.xp: int = datas["xp"]
        self.weeklyXp: int = datas["weeklyXp"]


class GeoguessrClubLogo(GeoguessrStr):
    """Represents a Geoguessr club logo."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.logoIconId: int = datas["logoIconId"]
        self.logoIconSize: int = datas["logoIconSize"]
        self.logoIconOpacity: int = datas["logoIconOpacity"]
        self.logoIconColorId: int = datas["logoIconColorId"]
        self.backgroundIconId: int = datas["backgroundIconId"]
        self.backgroundIconSize: int = datas["backgroundIconSize"]
        self.backgroundIconOpacity: int = datas["backgroundIconOpacity"]
        self.backgroundIconColorId: int = datas["backgroundIconColorId"]
        self.backgroundColorId: int = datas["backgroundColorId"]


class GeoguessrClubStats(GeoguessrStr):
    """Represents Geoguessr club statistics."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.clubId: str = datas["clubId"]
        self.totalXp: int = datas["totalXp"]
        self.changePercentXp: float = datas["changePercentXp"]
        self.totalGamesPlayed: int = datas["totalGamesPlayed"]
        self.changePercentGamesPlayed: float = datas["changePercentGamesPlayed"]
        self.totalWins: int = datas["totalWins"]
        self.changePercentWins: float = datas["changePercentWins"]
        self.totalPerfectGuesses: int = datas["totalPerfectGuesses"]
        self.changePercentPerfectGuesses: float = datas["changePercentPerfectGuesses"]
        self.globalXpRank: int = datas["globalXpRank"]
        self.totalClubs: int = datas["totalClubs"]
        self.averageDivision: GeoguessrClubDivision = GeoguessrClubDivision(datas["averageDivision"])


class GeoguessrClubDivision(GeoguessrStr):
    """Represents a club's average division."""

    def __init__(self, datas: dict[str, Any]) -> None:
        self.number: int = datas["number"]
        self.name: str = datas["name"]
        self.tier: int = datas["tier"]
