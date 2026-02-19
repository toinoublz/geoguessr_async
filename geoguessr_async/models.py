from datetime import datetime
from enum import Enum
from typing import Any, Optional, Union

import aiohttp

import geoguessr_async.geo_utils as gu


class GeoguessrStr:
    def to_tree(self, indent=0):
        """Convert the object to a tree-like string representation.

        Args:
            indent (int): Number of spaces to indent each level. Defaults to 0.

        Returns:
            str: Tree-like string representation of the object.
        """
        lines = []

        for name, value in self.__dict__.items():
            attrSpaces = "    " * indent

            if isinstance(value, (int, float, str, bool, type(None))):
                lines.append(f"{attrSpaces}{name} ({value.__class__.__name__}) = {value!r}")

            elif hasattr(value, "to_tree"):
                lines.append(f"{attrSpaces}{name} ({value.__class__.__name__}):")
                lines.append(value.to_tree(indent + 2))

            elif isinstance(value, list):
                lines.append(f"{attrSpaces}{name} ({value.__class__.__name__}):")
                for item in value:
                    if hasattr(item, "to_tree"):
                        lines.append(item.to_tree(indent + 2))
                    else:
                        lines.append(f"{'    ' * (indent + 2)}{item!r}")

            elif isinstance(value, dict):
                lines.append(f"{attrSpaces}{name} ({value.__class__.__name__}):")
                for key, item in value.items():
                    if hasattr(item, "to_tree"):
                        lines.append(f"{'    ' * (indent + 2)}{key!r}:")
                        lines.append(item.to_tree(indent + 3))
                    elif isinstance(item, list):
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

    def __init__(self, datas: dict) -> None:
        """Initialize GeoguessrStats.

        Args:
            datas (dict): Raw stats data from API.
        """
        # Ranked Team Duels
        self.rankedTeamDuelsStandard: GeoguessrStatsRankedTeamDuelsStandard = GeoguessrStatsRankedTeamDuelsStandard(
            datas.get("rankedTeamDuelsStandard", {})
        )
        self.rankedTeamDuelsNoMove: GeoguessrStatsRankedTeamDuelsNoMove = GeoguessrStatsRankedTeamDuelsNoMove(
            datas.get("rankedTeamDuelsNoMove", {})
        )
        self.rankedTeamDuelsNmpz: GeoguessrStatsRankedTeamDuelsNmpz = GeoguessrStatsRankedTeamDuelsNmpz(
            datas.get("rankedTeamDuelsNmpz", {})
        )
        self.rankedTeamDuelsTotal: GeoguessrStatsRankedTeamDuelsTotal = GeoguessrStatsRankedTeamDuelsTotal(
            datas.get("rankedTeamDuelsTotal", {})
        )

        # Battle Royale
        self.battleRoyaleDistance: GeoguessrStatsBattleRoyaleDistance = GeoguessrStatsBattleRoyaleDistance(
            datas.get("battleRoyaleDistance", {})
        )
        self.battleRoyaleCountry: GeoguessrStatsBattleRoyaleCountry = GeoguessrStatsBattleRoyaleCountry(
            datas.get("battleRoyaleCountry", {})
        )
        self.battleRoyaleMedals: GeoguessrStatsBattleRoyaleMedals = GeoguessrStatsBattleRoyaleMedals(
            datas.get("battleRoyaleMedals", {})
        )

        # Competitive
        self.competitiveCityStreaks: GeoguessrStatsCompetitiveCityStreaks = GeoguessrStatsCompetitiveCityStreaks(
            datas.get("competitiveCityStreaks", {})
        )
        self.competitiveStreaksMedals: GeoguessrStatsCompetitiveStreaksMedals = GeoguessrStatsCompetitiveStreaksMedals(
            datas.get("competitiveStreaksMedals", {})
        )

        # Duels
        self.duels: GeoguessrStatsDuels = GeoguessrStatsDuels(datas.get("duels", {}))
        self.duelsNoMove: GeoguessrStatsDuelsNoMove = GeoguessrStatsDuelsNoMove(datas.get("duelsNoMove", {}))
        self.duelsNmpz: GeoguessrStatsDuelsNmpz = GeoguessrStatsDuelsNmpz(datas.get("duelsNmpz", {}))
        self.duelsTotal: GeoguessrStatsDuelsTotal = GeoguessrStatsDuelsTotal(datas.get("duelsTotal", {}))
        self.duelsMedals: GeoguessrStatsDuelsMedals = GeoguessrStatsDuelsMedals(datas.get("duelsMedals", {}))

        # Unranked Duels
        self.unrankedDuels: GeoguessrStatsUnrankedDuels = GeoguessrStatsUnrankedDuels(datas.get("unrankedDuels", {}))
        self.unrankedDuelsNoMove: GeoguessrStatsUnrankedDuelsNoMove = GeoguessrStatsUnrankedDuelsNoMove(
            datas.get("unrankedDuelsNoMove", {})
        )
        self.unrankedDuelsNmpz: GeoguessrStatsUnrankedDuelsNmpz = GeoguessrStatsUnrankedDuelsNmpz(
            datas.get("unrankedDuelsNmpz", {})
        )
        self.unrankedDuelsTotal: GeoguessrStatsUnrankedDuelsTotal = GeoguessrStatsUnrankedDuelsTotal(
            datas.get("unrankedDuelsTotal", {})
        )

        # Progression & Stats
        self.lifeTimeXpProgression: GeoguessrStatsLifeTimeXpProgression = GeoguessrStatsLifeTimeXpProgression(
            datas.get("lifeTimeXpProgression", {})
        )
        self.totalMedals: GeoguessrStatsTotalMedals = GeoguessrStatsTotalMedals(datas.get("totalMedals", {}))
        self.teamDuels: GeoguessrStatsTeamDuels = GeoguessrStatsTeamDuels(datas.get("teamDuels", {}))
        self.teamDuelsQuickplay: GeoguessrStatsTeamDuelsQuickplay = GeoguessrStatsTeamDuelsQuickplay(
            datas.get("teamDuelsQuickplay", {})
        )
        self.party: GeoguessrStatsParty = GeoguessrStatsParty(datas.get("party", {}))

        # Direct stats
        self.quickplayFlawlessVictories: Optional[int] = gu.int_or_none(datas.get("quickplayFlawlessVictories"))
        self.perfectRounds: Optional[int] = gu.int_or_none(datas.get("perfectRounds"))


class GeoguessrCompetitionMedals(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        self.bronze: Optional[int] = gu.int_or_none(datas.get("bronze"))
        self.silver: Optional[int] = gu.int_or_none(datas.get("silver"))
        self.gold: Optional[int] = gu.int_or_none(datas.get("gold"))
        self.platinum: Optional[int] = gu.int_or_none(datas.get("platinum"))


class GeoguessrPin(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        print(datas)
        self.url: Optional[str] = gu.str_or_none(datas.get("pin", {}).get("url"))
        self.anchor: Optional[str] = gu.str_or_none(datas.get("pin", {}).get("anchor"))
        self.isDefault: Optional[bool] = gu.bool_or_none(datas.get("pin", {}).get("isDefault"))
        self.customImage: Optional[str] = datas.get("customImage")
        self.fullBody: Optional[str] = gu.str_or_none(datas.get("fullBodyPin"))
        self.borderUrl: Optional[str] = gu.str_or_none(datas.get("borderUrl"))


class GeoguessrDivision(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        self.type: Optional[int] = gu.int_or_none(datas.get("type"))
        self.startRating: Optional[int] = gu.int_or_none(datas.get("startRating"))
        self.endRating: Optional[int] = gu.int_or_none(datas.get("endRating"))


class GeoguessrCompetitive(GeoguessrStr):
    """Deprecated"""

    def __init__(self, datas: dict) -> None:
        self.elo: Optional[int] = gu.int_or_none(datas.get("elo"))
        self.rating: Optional[int] = gu.int_or_none(datas.get("rating"))
        self.lastRatingChange: Optional[int] = gu.int_or_none(datas.get("lastRatingChange"))
        self.division: GeoguessrDivision = GeoguessrDivision(datas.get("division"))
        self.onLeaderboard: Optional[bool] = gu.bool_or_none(datas.get("onLeaderboard"))


class GeoguessrLevelProgress(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        self.level: Optional[int] = gu.int_or_none(datas.get("level"))
        self.xp: Optional[int] = gu.int_or_none(datas.get("xp"))
        self.levelXpStart: Optional[int] = gu.int_or_none(datas.get("levelXp"))
        self.nextLevelXp: Optional[int] = gu.int_or_none(datas.get("nextLevelXp"))
        self.nextLevel: Optional[int] = gu.int_or_none(datas.get("nextLevel"))
        self.title: GeoguessrXpTitle = GeoguessrXpTitle(datas.get("title"))
        self.competitionMedals: GeoguessrCompetitionMedals = GeoguessrCompetitionMedals(datas.get("competitionMedals"))


class GeoguessrProfile(GeoguessrStr):
    """Represents a Geoguessr user profile.

    Attributes:
        nick (str): User nickname.
        created (str): Account creation date.
        isProUser (bool): Whether user has pro account.
        # ... other profile attributes
    """

    def __init__(self, datas: dict) -> None:
        """Initialize GeoguessrProfile.

        Args:
            datas (dict): Raw profile data from API.
        """
        self.nick: str = gu.str_or_none(datas.get("nick"))
        self.createdAt: datetime = datetime.strptime(datas.get("created").split(".")[0], "%Y-%m-%dT%H:%M:%S")
        self.isProUser: bool = gu.bool_or_none(datas.get("isProUser"))
        self.type: Optional[str] = gu.str_or_none(datas.get("type"))
        self.isVerified: bool = gu.bool_or_none(datas.get("isVerified"))
        self.pin: GeoguessrPin = GeoguessrPin(datas)
        self.color: Optional[int] = gu.int_or_none(datas.get("color"))
        self.url: str = gu.str_or_none(datas.get("url"))
        self.id: str = gu.str_or_none(datas.get("id"))
        self.countryCode: Optional[str] = gu.str_or_none(datas.get("countryCode"))
        self.battleRoyaleLevel: Optional[int] = gu.int_or_none(datas.get("br", {}).get("level"))
        self.battleRoyaleDivision: Optional[int] = gu.int_or_none(datas.get("br", {}).get("division"))
        self.streakProgress: Optional[Any] = datas.get("streakProgress")
        self.explorerProgress: Optional[Any] = datas.get("explorerProgress")
        self.dailyChallengeProgress: Optional[int] = gu.int_or_none(datas.get("dailyChallengeProgress"))
        self.progress: GeoguessrLevelProgress = GeoguessrLevelProgress(datas.get("progress"))
        self.competitive: Optional[GeoguessrCompetitive] = (
            GeoguessrCompetitive(datas.get("competitive")) if datas.get("competitive") else None
        )
        self.lastNameChange: datetime = datetime.strptime(
            datas.get("lastNameChange").split(".")[0], "%Y-%m-%dT%H:%M:%S"
        )
        self.lastNickOrCountryChange: datetime = datetime.strptime(
            datas.get("lastNickOrCountryChange").split(".")[0], "%Y-%m-%dT%H:%M:%S"
        )
        self.isBanned: bool = gu.bool_or_none(datas.get("isBanned"))
        self.chatBan: bool = gu.bool_or_none(datas.get("chatBan"))
        self.nameChangeAvailableAt: Optional[datetime] = (
            datetime.strptime(datas.get("nameChangeAvailableAt").split(".")[0], "%Y-%m-%dT%H:%M:%S")
            if datas.get("nameChangeAvailableAt")
            else None
        )
        self.avatarUrl: Optional[str] = datas.get("avatar", {}).get("fullbodypath")
        self.isBotUser: bool = gu.bool_or_none(datas.get("isBotUser"))
        self.suspendedUntil: Optional[datetime] = (
            datetime.strptime(datas.get("suspendedUntil").split(".")[0], "%Y-%m-%dT%H:%M:%S")
            if datas.get("suspendedUntil")
            else None
        )
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

    def __init__(self, datas: dict) -> None:
        """Initialize GeoguessrChallenge.

        Args:
            datas (dict): Raw challenge data from API.
        """
        self.token: str = gu.str_or_none(datas.get("token"))
        self.mapSlug: str = gu.str_or_none(datas.get("mapSlug"))
        self.roundCount: int = gu.int_or_none(datas.get("roundCount"))
        self.timeLimit: int = gu.int_or_none(datas.get("timeLimit"))
        self.movementOptions: GeoguessrMovementOptions = GeoguessrMovementOptions(datas)
        self.guessMapType: str = gu.str_or_none(datas.get("guessMapType"))
        self.numberOfParticipants: Optional[int] = gu.int_or_none(datas.get("numberOfParticipants"))
        self.gameMode: str = gu.str_or_none(datas.get("gameMode"))
        self.challengeType: int = gu.int_or_none(datas.get("challengeType"))
        self.streakType: Optional[str] = gu.str_or_none(datas.get("streakType"))
        self.accessLevel: Optional[int] = gu.int_or_none(datas.get("accessLevel"))
        self.locationOrder: int = gu.int_or_none(datas.get("locationOrder"))


class GeoguessrChallengeRound(GeoguessrStr):
    """Represents a single round in a Geoguessr challenge.

    Attributes:
        number (int): Round number.
        lat (float): Latitude of the location.
        long (float): Longitude of the location.
        # ... other round attributes
    """

    def __init__(self, roundData: dict, roundNumber: Optional[int]) -> None:
        """Initialize GeoguessrChallengeRound.

        Args:
            roundData (dict): Raw round data from API.
            roundNumber (int): Round number (1-based).
        """
        self.number: int = roundNumber
        self.lat: float = gu.float_or_none(roundData.get("lat"))
        self.long: float = gu.float_or_none(roundData.get("lng"))
        self.panoId: Optional[str] = gu.str_or_none(roundData.get("panoId"))
        self.heading: float = gu.float_or_none(roundData.get("heading"))
        self.pitch: float = gu.float_or_none(roundData.get("pitch"))
        self.zoom: float = gu.float_or_none(roundData.get("zoom"))
        self.streakLocationCode: Optional[str] = roundData.get("streakLocationCode")
        self.startTime: datetime = datetime.strptime(roundData.get("startTime", "").split(".")[0], "%Y-%m-%dT%H:%M:%S")


class GeoguessrScore(GeoguessrStr):
    """Represents a round score in Geoguessr.

    Attributes:
        amount (float): Score amount.
        unit (str): Score unit.
        percentage (float): Score percentage.
    """

    def __init__(self, scoreData: dict) -> None:
        """Initialize GeoguessrScore.

        Args:
            scoreData (dict): Raw score data from API.
        """
        self.amount: float = gu.float_or_none(scoreData.get("amount"))
        self.unit: Optional[str] = gu.str_or_none(scoreData.get("unit"))
        self.percentage: Optional[float] = gu.float_or_none(scoreData.get("percentage"))


class GeoguessrDistance(GeoguessrStr):
    """Represents distance measurements in Geoguessr.

    Attributes:
        meters (float): Distance in meters.
        kilometers (float): Distance in kilometers.
        miles (float): Distance in miles.
    """

    def __init__(self, distanceData: dict) -> None:
        """Initialize GeoguessrDistance.

        Args:
            distanceData (dict): Raw distance data from API.
        """
        metersDistance: dict = distanceData.get("meters", {})
        self.meters: float = gu.float_or_none(metersDistance.get("amount")) * (
            1000 if metersDistance.get("unit") == "km" else 1
        )
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

    def __init__(self, guessData: dict[str, str], roundNumber: Optional[int]) -> None:
        """Initialize GeoguessrPlayerGuesses.

        Args:
            guessData (dict): Raw guess data from API.
            roundNumber (int): Round number (1-based).
        """
        self.number: int = roundNumber
        self.lat: float = gu.float_or_none(guessData.get("lat"))
        self.long: float = gu.float_or_none(guessData.get("lng"))
        self.timedOut: bool = gu.bool_or_none(guessData.get("timedOut"))
        self.timedOutWithGuess: bool = gu.bool_or_none(guessData.get("timedOutWithGuess"))
        self.skippedRound: bool = gu.bool_or_none(guessData.get("skippedRound"))
        self.roundScore: GeoguessrScore = GeoguessrScore(guessData.get("roundScore"))
        self.roundScoreInPercentage: int = gu.int_or_none(guessData.get("roundScoreInPercentage"))
        self.roundScoreInPoints: int = gu.int_or_none(guessData.get("roundScoreInPoints"))
        self.distance: GeoguessrDistance = GeoguessrDistance(guessData.get("distance"))
        self.distanceInMeters: float = gu.float_or_none(guessData.get("distanceInMeters"))
        self.stepsCount: int = gu.int_or_none(guessData.get("stepsCount"))
        self.streakLocationCode: Optional[str] = guessData.get("streakLocationCode")
        self.time: GeoguessrTime = GeoguessrTime(guessData.get("time"))


class GeoguessrGameBounds(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        self.minLat: float = gu.float_or_none(datas.get("min", {}).get("lat"))
        self.minLng: float = gu.float_or_none(datas.get("min", {}).get("lng"))
        self.maxLat: float = gu.float_or_none(datas.get("max", {}).get("lat"))
        self.maxLng: float = gu.float_or_none(datas.get("max", {}).get("lng"))


class GeoguessrLevel(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        self.level: int = gu.int_or_none(datas.get("level"))
        self.xpStart: int = gu.int_or_none(datas.get("xpStart"))


class GeoguessrXpTitle(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        self.id: int = gu.int_or_none(datas.get("id"))
        self.tierId: int = gu.int_or_none(datas.get("tierId"))
        self.minimumLevel: int = gu.int_or_none(datas.get("minimumLevel", None))
        self.name: str = gu.str_or_none(datas.get("name"))


class GeoguessrScorePlayerInfo(GeoguessrStr):
    def __init__(self, playerDatas: dict, progressionDatas: dict) -> None:
        self.isLeader: bool = gu.bool_or_none(playerDatas.get("isLeader"))
        self.id: str = gu.str_or_none(playerDatas.get("id"))
        self.nick: str = gu.str_or_none(playerDatas.get("nick"))
        self.isVerified: bool = gu.bool_or_none(playerDatas.get("isVerified"))
        self.flair: Optional[int] = gu.int_or_none(playerDatas.get("flair"))
        self.countryCode: Optional[str] = gu.str_or_none(playerDatas.get("countryCode"))
        self.pinUrl: Optional[str] = gu.str_or_none(playerDatas.get("pin", {}).get("url"))
        self.xpBeforeChallenge: Optional[int] = gu.int_or_none(
            progressionDatas.get("xpProgressions", [{}, {}])[0].get("xp")
        )
        self.xpAfterChallenge: Optional[int] = gu.int_or_none(
            progressionDatas.get("xpProgressions", [{}, {}])[1].get("xp")
        )
        self.xpGained: Optional[int] = self.xpAfterChallenge - self.xpBeforeChallenge
        self.levelBeforeChallenge: GeoguessrLevel = GeoguessrLevel(
            progressionDatas.get("xpProgressions", [{}, {}])[0].get("currentLevel")
        )
        self.levelAfterChallenge: GeoguessrLevel = GeoguessrLevel(
            progressionDatas.get("xpProgressions", [{}, {}])[1].get("currentLevel")
        )
        self.titleBeforeChallenge: GeoguessrXpTitle = GeoguessrXpTitle(
            progressionDatas.get("xpProgressions", [{}, {}])[0].get("currentTitle")
        )
        self.titleAfterChallenge: GeoguessrXpTitle = GeoguessrXpTitle(
            progressionDatas.get("xpProgressions", [{}, {}])[1].get("currentTitle")
        )


class GeoguessrChallengePlayerTotalResult(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        self.totalScore: GeoguessrScore = GeoguessrScore(datas.get("totalScore"))
        self.totalDistance: GeoguessrDistance = GeoguessrDistance(datas.get("totalDistance"))
        self.totalStepsCount: Optional[int] = gu.int_or_none(datas.get("totalStepsCount"))
        self.totalTime: GeoguessrTime = GeoguessrTime(seconds=datas.get("totalTime"))
        self.totalStreak: Optional[int] = gu.int_or_none(datas.get("totalStreak"))
        self.guesses: list[GeoguessrPlayerGuesses] = [
            GeoguessrPlayerGuesses(guess, i + 1) for i, guess in enumerate(datas.get("guesses")) if guess is not None
        ]


class GeoguessrChallengeResult(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        gameDatas: Optional[dict] = datas.get("game")
        if gameDatas is None:
            raise ValueError("The game key is missing in the data.")
        self.player: GeoguessrScorePlayerInfo = GeoguessrScorePlayerInfo(
            gameDatas.get("player"), gameDatas.get("progressChange")
        )
        self.type: str = gu.str_or_none(gameDatas.get("type"))
        self.mode: str = gu.str_or_none(gameDatas.get("mode"))
        self.state: Optional[str] = gu.str_or_none(gameDatas.get("state"))
        self.roundCount: int = gu.int_or_none(gameDatas.get("roundCount"))
        self.streakType: Optional[str] = gu.str_or_none(gameDatas.get("streakType"))
        self.map: str = gu.str_or_none(gameDatas.get("map"))
        self.mapname: str = gu.str_or_none(gameDatas.get("mapName"))
        self.panoramaprovider: Optional[int] = gu.int_or_none(gameDatas.get("panoramaprovider"))
        self.bounds: GeoguessrGameBounds = GeoguessrGameBounds(gameDatas.get("bounds"))
        self.rounds: list[GeoguessrChallengeRound] = [
            GeoguessrChallengeRound(round, i + 1)
            for i, round in enumerate(gameDatas.get("rounds"))
            if round is not None
        ]
        self.playerTotalScore: GeoguessrChallengePlayerTotalResult = GeoguessrChallengePlayerTotalResult(
            gameDatas.get("player")
        )


class GeoguessMapAvatar(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        self.background: str = gu.str_or_none(datas.get("background"))
        self.decoration: str = gu.str_or_none(datas.get("decoration"))
        self.ground: str = gu.str_or_none(datas.get("ground"))
        self.landscape: str = gu.str_or_none(datas.get("landscape"))


class GeoguessrMap(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        self.id: str = gu.str_or_none(datas.get("id"))
        self.name: str = gu.str_or_none(datas.get("name"))
        self.slug: str = gu.str_or_none(datas.get("slug"))
        self.description: Optional[str] = gu.str_or_none(datas.get("description"))
        self.url: str = gu.str_or_none(datas.get("url"))
        self.playUrl: str = gu.str_or_none(datas.get("playUrl"))
        self.published: bool = gu.bool_or_none(datas.get("published"))
        self.banned: bool = gu.bool_or_none(datas.get("banned"))
        self.backGround: Optional[str] = gu.str_or_none(datas.get("images", {}).get("backgroundLarge"))
        self.bounds: GeoguessrGameBounds = GeoguessrGameBounds(datas.get("bounds"))
        self.customCoordinates: Optional[Any] = datas.get("customCoordinates")
        self.coordinatesCount: Optional[str] = gu.str_or_none(datas.get("coordinateCount"))
        self.regions: Optional[Any] = datas.get("regions")
        self.creator: Optional[GeoguessrProfile] = (
            GeoguessrProfile(datas.get("creator")) if datas.get("creator") is not None else None
        )
        self.createdAt: datetime = gu.datetime_or_none(datas.get("createdAt"))
        self.updatedAt: datetime = gu.datetime_or_none(datas.get("updatedAt"))
        self.numFinishedGames: Optional[int] = gu.int_or_none(datas.get("numFinishedGames"))
        self.likedByUser: Optional[Any] = datas.get("likedByUser")
        self.averageScore: Optional[int] = gu.int_or_none(datas.get("averageScore"))
        self.avatar: GeoguessMapAvatar = GeoguessMapAvatar(datas.get("avatar")) if datas.get("avatar") else None
        self.difficulty: str = gu.str_or_none(datas.get("difficulty"))
        self.difficultyLevel: int = gu.int_or_none(datas.get("difficultyLevel"))
        self.highscore: Any = datas.get("highscore")
        self.deleted: bool = gu.bool_or_none(datas.get("deleted"))
        self.free: bool = gu.bool_or_none(datas.get("free"))
        self.panoramaprovider: Optional[str] = gu.str_or_none(datas.get("panoramaProvider"))
        self.inExplorerMode: bool = gu.bool_or_none(datas.get("inExplorerMode"))
        self.maxErrorDistance: int = gu.int_or_none(datas.get("maxErrorDistance"))
        self.likes: int = gu.int_or_none(datas.get("likes"))
        self.locationSelectionMode: int = gu.int_or_none(datas.get("locationSelectionMode"))
        self.tags: list = datas.get("tags")
        self.collaborators: Any = datas.get("collaborators")
        self.flair: Optional[int] = gu.int_or_none(datas.get("flair"))
        self.mapSize: Optional[dict] = datas.get("mapSize")


class GeoguessrActivities(GeoguessrStr):
    """Represents Geoguessr activities data.

    Attributes:
        entries (list): List of activity entries.
    """

    def __init__(self, entries: list) -> None:
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

    def __init__(self, datas: dict) -> None:
        """Initialize GeoguessrUserELO.

        Args:
            datas (dict): Raw ELO data from API.
        """
        datas = gu.flatten_dict(datas)
        self.divisionNumber: int = gu.int_or_none(datas.get("divisionNumber"))
        self.divisionName: str = gu.str_or_none(datas.get("divisionName"))
        self.rating: int = gu.int_or_none(datas.get("rating"))
        self.tier: str = gu.str_or_none(datas.get("tier"))
        self.gameModeRatingsStandardduels: int = gu.int_or_none(datas.get("gameModeRatingsStandardduels"))
        self.gameModeRatingsNmpzduels: int = gu.int_or_none(datas.get("gameModeRatingsNmpzduels"))
        self.gameModeRatingsNomoveduels: int = gu.int_or_none(datas.get("gameModeRatingsNomoveduels"))


class GeoguessrStatsRankedTeamDuelsStandard(GeoguessrStr):
    """Represents ranked team duels standard statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: int = gu.int_or_none(datas.get("numGamesPlayed"))
        self.numWins: int = gu.int_or_none(datas.get("numWins"))
        self.winRatio: float = gu.float_or_none(datas.get("winRatio"))


class GeoguessrStatsRankedTeamDuelsNoMove(GeoguessrStr):
    """Represents ranked team duels no move statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: int = gu.int_or_none(datas.get("numGamesPlayed"))
        self.numWins: int = gu.int_or_none(datas.get("numWins"))
        self.winRatio: float = gu.float_or_none(datas.get("winRatio"))


class GeoguessrStatsRankedTeamDuelsNmpz(GeoguessrStr):
    """Represents ranked team duels NMPZ statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: int = gu.int_or_none(datas.get("numGamesPlayed"))
        self.numWins: int = gu.int_or_none(datas.get("numWins"))
        self.winRatio: float = gu.float_or_none(datas.get("winRatio"))


class GeoguessrStatsRankedTeamDuelsTotal(GeoguessrStr):
    """Represents ranked team duels total statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: int = gu.int_or_none(datas.get("numGamesPlayed"))
        self.numWins: int = gu.int_or_none(datas.get("numWins"))
        self.winRatio: float = gu.float_or_none(datas.get("winRatio"))


class GeoguessrStatsBattleRoyaleDistance(GeoguessrStr):
    """Represents battle royale distance statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: int = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: float = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: int = gu.int_or_none(datas.get("numWins"))
        self.winRatio: float = gu.float_or_none(datas.get("winRatio"))
        self.avgGuessDistance: float = gu.float_or_none(datas.get("avgGuessDistance"))
        self.numGuesses: int = gu.int_or_none(datas.get("numGuesses"))


class GeoguessrStatsBattleRoyaleCountry(GeoguessrStr):
    """Represents battle royale country statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: int = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: float = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: int = gu.int_or_none(datas.get("numWins"))
        self.winRatio: float = gu.float_or_none(datas.get("winRatio"))
        self.numGuesses: int = gu.int_or_none(datas.get("numGuesses"))
        self.avgCorrectGuesses: float = gu.float_or_none(datas.get("avgCorrectGuesses"))


class GeoguessrStatsBattleRoyaleMedals(GeoguessrStr):
    """Represents battle royale medals statistics."""

    def __init__(self, datas: dict) -> None:
        self.medalCountGold: int = gu.int_or_none(datas.get("medalCountGold"))
        self.medalCountSilver: int = gu.int_or_none(datas.get("medalCountSilver"))
        self.medalCountBronze: int = gu.int_or_none(datas.get("medalCountBronze"))


class GeoguessrStatsCompetitiveCityStreaks(GeoguessrStr):
    """Represents competitive city streaks statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: int = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: float = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: int = gu.int_or_none(datas.get("numWins"))
        self.winRatio: float = gu.float_or_none(datas.get("winRatio"))
        self.numGuesses: int = gu.int_or_none(datas.get("numGuesses"))
        self.avgCorrectGuesses: float = gu.float_or_none(datas.get("avgCorrectGuesses"))


class GeoguessrStatsCompetitiveStreaksMedals(GeoguessrStr):
    """Represents competitive streaks medals statistics."""

    def __init__(self, datas: dict) -> None:
        self.medalCountGold: int = gu.int_or_none(datas.get("medalCountGold"))
        self.medalCountSilver: int = gu.int_or_none(datas.get("medalCountSilver"))
        self.medalCountBronze: int = gu.int_or_none(datas.get("medalCountBronze"))


class GeoguessrStatsDuels(GeoguessrStr):
    """Represents duels statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: int = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: float = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: int = gu.int_or_none(datas.get("numWins"))
        self.winRatio: float = gu.float_or_none(datas.get("winRatio"))
        self.avgGuessDistance: float = gu.float_or_none(datas.get("avgGuessDistance"))
        self.numGuesses: int = gu.int_or_none(datas.get("numGuesses"))
        self.numFlawlessWins: int = gu.int_or_none(datas.get("numFlawlessWins"))


class GeoguessrStatsDuelsNoMove(GeoguessrStr):
    """Represents duels no move statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: int = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: float = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: int = gu.int_or_none(datas.get("numWins"))
        self.winRatio: float = gu.float_or_none(datas.get("winRatio"))
        self.avgGuessDistance: float = gu.float_or_none(datas.get("avgGuessDistance"))
        self.numGuesses: int = gu.int_or_none(datas.get("numGuesses"))
        self.numFlawlessWins: int = gu.int_or_none(datas.get("numFlawlessWins"))


class GeoguessrStatsDuelsNmpz(GeoguessrStr):
    """Represents duels NMPZ statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: int = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: float = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: int = gu.int_or_none(datas.get("numWins"))
        self.winRatio: float = gu.float_or_none(datas.get("winRatio"))
        self.avgGuessDistance: float = gu.float_or_none(datas.get("avgGuessDistance"))
        self.numGuesses: int = gu.int_or_none(datas.get("numGuesses"))
        self.numFlawlessWins: int = gu.int_or_none(datas.get("numFlawlessWins"))


class GeoguessrStatsDuelsTotal(GeoguessrStr):
    """Represents duels total statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: int = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: float = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: int = gu.int_or_none(datas.get("numWins"))
        self.winRatio: float = gu.float_or_none(datas.get("winRatio"))
        self.avgGuessDistance: float = gu.float_or_none(datas.get("avgGuessDistance"))
        self.numGuesses: int = gu.int_or_none(datas.get("numGuesses"))
        self.numFlawlessWins: int = gu.int_or_none(datas.get("numFlawlessWins"))


class GeoguessrStatsDuelsMedals(GeoguessrStr):
    """Represents duels medals statistics."""

    def __init__(self, datas: dict) -> None:
        self.medalCountGold: int = gu.int_or_none(datas.get("medalCountGold"))
        self.medalCountSilver: int = gu.int_or_none(datas.get("medalCountSilver"))
        self.medalCountBronze: int = gu.int_or_none(datas.get("medalCountBronze"))


class GeoguessrStatsUnrankedDuels(GeoguessrStr):
    """Represents unranked duels statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: int = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: float = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: int = gu.int_or_none(datas.get("numWins"))
        self.winRatio: float = gu.float_or_none(datas.get("winRatio"))
        self.avgGuessDistance: float = gu.float_or_none(datas.get("avgGuessDistance"))
        self.numGuesses: int = gu.int_or_none(datas.get("numGuesses"))
        self.numFlawlessWins: int = gu.int_or_none(datas.get("numFlawlessWins"))


class GeoguessrStatsUnrankedDuelsNoMove(GeoguessrStr):
    """Represents unranked duels no move statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: int = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: float = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: int = gu.int_or_none(datas.get("numWins"))
        self.winRatio: float = gu.float_or_none(datas.get("winRatio"))
        self.avgGuessDistance: float = gu.float_or_none(datas.get("avgGuessDistance"))
        self.numGuesses: int = gu.int_or_none(datas.get("numGuesses"))
        self.numFlawlessWins: int = gu.int_or_none(datas.get("numFlawlessWins"))


class GeoguessrStatsUnrankedDuelsNmpz(GeoguessrStr):
    """Represents unranked duels NMPZ statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: int = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: float = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: int = gu.int_or_none(datas.get("numWins"))
        self.winRatio: float = gu.float_or_none(datas.get("winRatio"))
        self.avgGuessDistance: float = gu.float_or_none(datas.get("avgGuessDistance"))
        self.numGuesses: int = gu.int_or_none(datas.get("numGuesses"))
        self.numFlawlessWins: int = gu.int_or_none(datas.get("numFlawlessWins"))


class GeoguessrStatsUnrankedDuelsTotal(GeoguessrStr):
    """Represents unranked duels total statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: int = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: float = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: int = gu.int_or_none(datas.get("numWins"))
        self.winRatio: float = gu.float_or_none(datas.get("winRatio"))
        self.avgGuessDistance: float = gu.float_or_none(datas.get("avgGuessDistance"))
        self.numGuesses: int = gu.int_or_none(datas.get("numGuesses"))
        self.numFlawlessWins: int = gu.int_or_none(datas.get("numFlawlessWins"))


class GeoguessrStatsLifeTimeXpProgression(GeoguessrStr):
    """Represents lifetime XP progression statistics."""

    def __init__(self, datas: dict) -> None:
        self.xp: int = gu.int_or_none(datas.get("xp"))
        self.currentLevel: GeoguessrLevel = GeoguessrLevel(datas.get("currentLevel"))
        self.nextLevel: GeoguessrLevel = GeoguessrLevel(datas.get("nextLevel"))
        self.currentTitle: GeoguessrXpTitle = GeoguessrXpTitle(datas.get("currentTitle"))


class GeoguessrStatsTotalMedals(GeoguessrStr):
    """Represents total medals statistics."""

    def __init__(self, datas: dict) -> None:
        self.medalCountGold: int = gu.int_or_none(datas.get("medalCountGold"))
        self.medalCountSilver: int = gu.int_or_none(datas.get("medalCountSilver"))
        self.medalCountBronze: int = gu.int_or_none(datas.get("medalCountBronze"))


class GeoguessrStatsTeamDuels(GeoguessrStr):
    """Represents team duels statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: int = gu.int_or_none(datas.get("numGamesPlayed"))
        self.numWins: int = gu.int_or_none(datas.get("numWins"))
        self.winRatio: float = gu.float_or_none(datas.get("winRatio"))


class GeoguessrStatsTeamDuelsQuickplay(GeoguessrStr):
    """Represents team duels quickplay statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: int = gu.int_or_none(datas.get("numGamesPlayed"))
        self.numWins: int = gu.int_or_none(datas.get("numWins"))


class GeoguessrDuelData(GeoguessrStr):
    """Représente les données complètes d'un duel Geoguessr."""

    def __init__(self, datas: dict) -> None:
        """Initialize GeoguessrDuelData.

        Args:
            datas (dict): Raw duel data from API.
        """
        self.gameId: str = gu.str_or_none(datas.get("gameId"))
        self.context: Optional[Any] = datas.get("context")
        self.teams: list[GeoguessrDuelTeam] = [GeoguessrDuelTeam(team) for team in datas.get("teams", [])]
        self.rounds: list[GeoguessrDuelRound] = [GeoguessrDuelRound(round) for round in datas.get("rounds", [])]
        self.totalRoundCount: int = gu.int_or_none(datas.get("currentRoundNumber"))
        self.status: str = gu.str_or_none(datas.get("status"))
        self.version: int = gu.int_or_none(datas.get("version"))
        self.options: GeoguessrDuelOptions = GeoguessrDuelOptions(datas.get("options", {}))
        self.initialHealth: int = gu.int_or_none(datas.get("initialHealth"))
        self.maxNumberOfRounds: int = gu.int_or_none(datas.get("maxNumberOfRounds"))
        self.result: GeoguessrDuelResult = GeoguessrDuelResult(datas.get("result", {}))
        self.isPaused: bool = gu.bool_or_none(datas.get("isPaused"))
        self.gameServerNodeId: str = gu.str_or_none(datas.get("gameServerNodeId"))
        self.tournamentId: str = gu.str_or_none(datas.get("tournamentId"))
        self.playersId = [player.playerId for team in self.teams for player in team.players]
        self.replays: Optional[dict[str, list[GeoguessrDuelReplay]]] = {playerId: [] for playerId in self.playersId}

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

    def __init__(self, datas: dict) -> None:
        self.datas: list[GeoguessrDuelReplayStep] = [GeoguessrDuelReplayStep(step) for step in datas]


class GeoguessrDuelReplayStep(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        self.time: datetime = datetime.fromtimestamp(float(datas.get("time")) / 1000)
        self.type: GeoguessrDuelReplay.Type = GeoguessrDuelReplay.Type(datas.get("type"))
        self.payload: Optional[
            Union[
                GeoguessrDuelReplayPanoPositionPayload,
                GeoguessrDuelReplayPanoPovPayload,
                GeoguessrDuelReplayPanoZoomPayload,
                GeoguessrDuelReplayMapZoomPayload,
                GeoguessrDuelReplayMapPositionPayload,
                GeoguessrDuelReplayGuessWithLatLngPayload,
                GeoguessrDuelReplayPinPositionPayload,
                GeoguessrDuelReplayTimerPayload,
            ]
        ] = None
        payloadType = (
            GeoguessrDuelReplayPanoPositionPayload
            if self.type == GeoguessrDuelReplay.Type.PANOPOSITION
            else (
                GeoguessrDuelReplayPanoPovPayload
                if self.type == GeoguessrDuelReplay.Type.PANOPOV
                else (
                    GeoguessrDuelReplayPanoZoomPayload
                    if self.type == GeoguessrDuelReplay.Type.PANOZOOM
                    else (
                        GeoguessrDuelReplayMapZoomPayload
                        if self.type == GeoguessrDuelReplay.Type.MAPZOOM
                        else (
                            GeoguessrDuelReplayMapPositionPayload
                            if self.type == GeoguessrDuelReplay.Type.MAPPOSITION
                            else (
                                GeoguessrDuelReplayGuessWithLatLngPayload
                                if self.type == GeoguessrDuelReplay.Type.GUESSWITHLATLNG
                                else (
                                    GeoguessrDuelReplayPinPositionPayload
                                    if self.type == GeoguessrDuelReplay.Type.PINPOSITION
                                    else (
                                        GeoguessrDuelReplayTimerPayload
                                        if self.type == GeoguessrDuelReplay.Type.TIMER
                                        else (
                                            GeoguessrDuelReplayMapDisplayPayload
                                            if self.type == GeoguessrDuelReplay.Type.MAPDISPLAY
                                            else None
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )

        if payloadType is not None:
            self.payload = payloadType(datas.get("payload"))


class GeoguessrDuelReplayPanoPositionPayload(GeoguessrStr):
    """Représente les données de payload de type PanoPosition."""

    def __init__(self, datas: dict) -> None:
        self.lat: dict = datas.get("lat")
        self.lng: dict = datas.get("lng")
        self.panoId: str = gu.str_or_none(datas.get("panoId"))


class GeoguessrDuelReplayPanoPovPayload(GeoguessrStr):
    """Représente les données de payload de type PanoPov."""

    def __init__(self, datas: dict) -> None:
        self.heading: float = gu.float_or_none(datas.get("heading"))
        self.pitch: float = gu.float_or_none(datas.get("pitch"))


class GeoguessrDuelReplayPanoZoomPayload(GeoguessrStr):
    """Représente les données de payload de type PanoZoom."""

    def __init__(self, datas: dict) -> None:
        self.zoom: float = gu.float_or_none(datas.get("zoom"))


class GeoguessrDuelReplayMapZoomPayload(GeoguessrStr):
    """Représente les données de payload de type MapZoom."""

    def __init__(self, datas: dict) -> None:
        self.zoom: int = gu.int_or_none(datas.get("zoom"))


class GeoguessrDuelReplayMapPositionPayload(GeoguessrStr):
    """Représente les données de payload de type MapPosition."""

    def __init__(self, datas: dict) -> None:
        self.lat: float = gu.float_or_none(datas.get("lat"))
        self.lng: float = gu.float_or_none(datas.get("lng"))


class GeoguessrDuelReplayGuessWithLatLngPayload(GeoguessrStr):
    """Représente les données de payload de type GuessWithLatLng."""

    def __init__(self, datas: dict) -> None:
        self.lat: float = gu.float_or_none(datas.get("lat"))
        self.lng: float = gu.float_or_none(datas.get("lng"))


class GeoguessrDuelReplayPinPositionPayload(GeoguessrStr):
    """Représente les données de payload de type PinPosition."""

    def __init__(self, datas: dict) -> None:
        self.lat: float = gu.float_or_none(datas.get("lat"))
        self.lng: float = gu.float_or_none(datas.get("lng"))


class GeoguessrDuelReplayTimerPayload(GeoguessrStr):
    """Représente les données de payload de type Timer."""

    def __init__(self, datas: dict) -> None:
        self.time: int = gu.int_or_none(datas.get("time"))


class GeoguessrDuelReplayMapDisplayPayload(GeoguessrStr):
    """Représente les données de payload de type MapDisplay."""

    def __init__(self, datas: dict) -> None:
        self.isActive: bool = gu.bool_or_none(datas.get("isActive"))
        self.isSticky: bool = gu.bool_or_none(datas.get("isSticky"))
        self.size: int = gu.int_or_none(datas.get("size"))


class GeoguessrDuelTeam(GeoguessrStr):
    """Représente une équipe dans un duel."""

    def __init__(self, datas: dict) -> None:
        self.id: str = gu.str_or_none(datas.get("id"))
        self.name: str = gu.str_or_none(datas.get("name"))
        self.healthAtEnd: int = gu.int_or_none(datas.get("health"))
        self.players: list[GeoguessrDuelPlayer] = [GeoguessrDuelPlayer(player) for player in datas.get("players", [])]
        self.roundResults: list[GeoguessrDuelTeamRoundResult] = [
            GeoguessrDuelTeamRoundResult(result) for result in datas.get("roundResults", [])
        ]
        self.isMultiplierActive: bool = gu.bool_or_none(datas.get("isMultiplierActive"))
        self.multiplierAtEnd: float = gu.float_or_none(datas.get("currentMultiplier"))


class GeoguessrDuelPlayer(GeoguessrStr):
    """Représente un joueur dans un duel."""

    def __init__(self, datas: dict) -> None:
        self.playerId: str = gu.str_or_none(datas.get("playerId"))
        self.guesses: list[GeoguessrDuelPlayerGuess] = [
            GeoguessrDuelPlayerGuess(guess) for guess in datas.get("guesses", [])
        ]
        self.rating: int = gu.int_or_none(datas.get("rating"))
        self.countryCode: str = gu.str_or_none(datas.get("countryCode"))
        self.progressChange: GeoguessrDuelProgressChange = GeoguessrDuelProgressChange(datas.get("progressChange", {}))
        self.helpRequested: bool = gu.bool_or_none(datas.get("helpRequested"))
        self.isSteam: bool = gu.bool_or_none(datas.get("isSteam"))


class GeoguessrDuelPlayerGuess(GeoguessrStr):
    """Représente une supposition d'un joueur dans un duel."""

    def __init__(self, datas: dict) -> None:
        self.roundNumber: int = gu.int_or_none(datas.get("roundNumber"))
        self.lat: float = self._parse_big_number(datas.get("lat"))
        self.lng: float = self._parse_big_number(datas.get("lng"))
        self.distance: float = self._parse_big_number(datas.get("distance"))
        self.created: datetime = gu.datetime_or_none(datas.get("created"))
        self.isTeamsBestGuessOnRound: bool = gu.bool_or_none(datas.get("isTeamsBestGuessOnRound"))
        self.score: int = gu.int_or_none(datas.get("score"))

    def _parse_big_number(self, value: Any) -> float:
        """Parse Big Number format or regular number."""
        if isinstance(value, dict) and value.get("type") == "Big Number":
            return float(str(value.get("value", "0")).replace("n", ""))
        elif isinstance(value, (int, float)):
            return float(value)
        return 0.0


class GeoguessrDuelTeamRoundResult(GeoguessrStr):
    """Représente le résultat d'une manche pour une équipe."""

    def __init__(self, datas: dict) -> None:
        self.roundNumber: int = gu.int_or_none(datas.get("roundNumber"))
        self.score: int = gu.int_or_none(datas.get("score"))
        self.healthBefore: int = gu.int_or_none(datas.get("healthBefore"))
        self.healthAfter: int = gu.int_or_none(datas.get("healthAfter"))
        self.bestGuess: GeoguessrDuelPlayerGuess = GeoguessrDuelPlayerGuess(datas.get("bestGuess", {}))
        self.activeMultiplier: bool = gu.bool_or_none(datas.get("activeMultiplier"))
        self.damageDealt: int = gu.int_or_none(datas.get("damageDealt"))
        self.multiplier: float = gu.float_or_none(datas.get("multiplier"))


class GeoguessrDuelRound(GeoguessrStr):
    """Représente une manche de duel."""

    def __init__(self, datas: dict) -> None:
        self.roundNumber: int = gu.int_or_none(datas.get("roundNumber"))
        self.panorama: GeoguessrDuelPanorama = GeoguessrDuelPanorama(datas.get("panorama", {}))
        self.hasProcessedRoundTimeout: bool = gu.bool_or_none(datas.get("hasProcessedRoundTimeout"))
        self.isHealingRound: bool = gu.bool_or_none(datas.get("isHealingRound"))
        self.multiplier: float = gu.float_or_none(datas.get("multiplier"))
        self.damageMultiplier: float = gu.float_or_none(datas.get("damageMultiplier"))
        self.startTime: datetime = gu.datetime_or_none(datas.get("startTime"))
        self.endTime: datetime = gu.datetime_or_none(datas.get("endTime"))
        self.timerStartTime: datetime = gu.datetime_or_none(datas.get("timerStartTime"))


class GeoguessrDuelPanorama(GeoguessrStr):
    """Représente les données de panorama d'une manche."""

    def __init__(self, datas: dict) -> None:
        self.panoId: str = gu.str_or_none(datas.get("panoId"))
        self.lat: float = self._parse_big_number(datas.get("lat"))
        self.lng: float = self._parse_big_number(datas.get("lng"))
        self.countryCode: str = gu.str_or_none(datas.get("countryCode"))
        self.heading: float = self._parse_big_number(datas.get("heading"))
        self.pitch: float = self._parse_big_number(datas.get("pitch"))
        self.zoom: int = gu.int_or_none(datas.get("zoom"))

    def _parse_big_number(self, value: Any) -> float:
        """Parse Big Number format or regular number."""
        if isinstance(value, dict) and value.get("type") == "Big Number":
            return float(str(value.get("value", "0")).replace("n", ""))
        elif isinstance(value, (int, float)):
            return float(value)
        return 0.0


class GeoguessrDuelProgressChange(GeoguessrStr):
    """Représente la progression d'un joueur."""

    def __init__(self, datas: dict) -> None:
        self.xpAtStart: GeoguessrDuelXpProgression = (
            GeoguessrDuelXpProgression(datas.get("xpProgressions", [])[0]) if datas.get("xpProgressions", []) else None
        )
        self.xpAtEnd: GeoguessrDuelXpProgression = (
            GeoguessrDuelXpProgression(datas.get("xpProgressions", [])[1]) if datas.get("xpProgressions", []) else None
        )
        self.awardedXp: GeoguessrDuelAwardedXp = GeoguessrDuelAwardedXp(datas.get("awardedXp", {}))
        self.medal: str = gu.str_or_none(datas.get("medal"))
        self.competitiveProgress: Optional[Any] = datas.get("competitiveProgress")
        self.rankedSystemProgress: GeoguessrDuelRankedSystemProgress = GeoguessrDuelRankedSystemProgress(
            datas.get("rankedSystemProgress", {})
        )
        self.rankedTeamDuelsProgress: Optional[Any] = datas.get("rankedTeamDuelsProgress")
        self.quickplayDuelsProgress: Optional[Any] = datas.get("quickplayDuelsProgress")


class GeoguessrDuelXpProgression(GeoguessrStr):
    """Représente la progression XP."""

    def __init__(self, datas: dict) -> None:
        self.xp: int = gu.int_or_none(datas.get("xp"))
        self.currentLevel: GeoguessrLevel = GeoguessrLevel(datas.get("currentLevel"))
        self.nextLevel: GeoguessrLevel = GeoguessrLevel(datas.get("nextLevel"))
        self.currentTitle: GeoguessrXpTitle = GeoguessrXpTitle(datas.get("currentTitle"))


class GeoguessrDuelAwardedXp(GeoguessrStr):
    """Représente les XP awardés."""

    def __init__(self, datas: dict) -> None:
        self.totalAwardedXp: int = gu.int_or_none(datas.get("totalAwardedXp"))
        self.xpAwards: list[GeoguessrDuelXpAward] = [GeoguessrDuelXpAward(award) for award in datas.get("xpAwards", [])]


class GeoguessrDuelXpAward(GeoguessrStr):
    """Représente une récompense XP."""

    def __init__(self, datas: dict) -> None:
        self.xp: int = gu.int_or_none(datas.get("xp"))
        self.reason: str = gu.str_or_none(datas.get("reason"))
        self.count: int = gu.int_or_none(datas.get("count"))


class GeoguessrDuelRankedSystemProgress(GeoguessrStr):
    """Représente la progression du système classé."""

    def __init__(self, datas: dict) -> None:
        self.points: dict = datas.get("points", {})
        self.totalWeeklyPoints: int = gu.int_or_none(datas.get("totalWeeklyPoints"))
        self.weeklyCap: int = gu.int_or_none(datas.get("weeklyCap"))
        self.gamesPlayedWithinWeeklyCap: int = gu.int_or_none(datas.get("gamesPlayedWithinWeeklyCap"))
        self.positionBefore: Optional[int] = gu.int_or_none(datas.get("positionBefore"))
        self.positionAfter: Optional[int] = gu.int_or_none(datas.get("positionAfter"))
        self.ratingBefore: int = gu.int_or_none(datas.get("ratingBefore"))
        self.ratingAfter: int = gu.int_or_none(datas.get("ratingAfter"))
        self.winStreak: int = gu.int_or_none(datas.get("winStreak"))
        self.bucketSortedBy: str = gu.str_or_none(datas.get("bucketSortedBy"))
        self.gameMode: str = gu.str_or_none(datas.get("gameMode"))
        self.gameModeRatingBefore: int = gu.int_or_none(datas.get("gameModeRatingBefore"))
        self.gameModeRatingAfter: int = gu.int_or_none(datas.get("gameModeRatingAfter"))
        self.gameModeGamesPlayed: int = gu.int_or_none(datas.get("gameModeGamesPlayed"))
        self.gameModeGamesRequired: int = gu.int_or_none(datas.get("gameModeGamesRequired"))
        self.placementGamesPlayed: int = gu.int_or_none(datas.get("placementGamesPlayed"))
        self.placementGamesRequired: int = gu.int_or_none(datas.get("placementGamesRequired"))


class GeoguessrDuelOptions(GeoguessrStr):
    """Représente les options d'un duel."""

    def __init__(self, datas: dict) -> None:
        self.initialHealth: int = gu.int_or_none(datas.get("initialHealth"))
        self.individualInitialHealth: bool = gu.bool_or_none(datas.get("individualInitialHealth"))
        self.initialHealthTeamOne: int = gu.int_or_none(datas.get("initialHealthTeamOne"))
        self.initialHealthTeamTwo: int = gu.int_or_none(datas.get("initialHealthTeamTwo"))
        self.roundTime: int = gu.int_or_none(datas.get("roundTime"))
        self.maxRoundTime: int = gu.int_or_none(datas.get("maxRoundTime"))
        self.gracePeriodTime: int = gu.int_or_none(datas.get("gracePeriodTime"))
        self.gameTimeOut: int = gu.int_or_none(datas.get("gameTimeOut"))
        self.maxNumberOfRounds: int = gu.int_or_none(datas.get("maxNumberOfRounds"))
        self.healingRounds: list[int] = datas.get("healingRounds", [])
        self.movementOptions: GeoguessrMovementOptions = GeoguessrMovementOptions(datas.get("movementOptions", {}))
        self.mapSlug: str = gu.str_or_none(datas.get("mapSlug"))
        self.isRated: bool = gu.bool_or_none(datas.get("isRated"))
        self.map: GeoguessrDuelMap = GeoguessrDuelMap(datas.get("map", {}))
        self.duelRoundOptions: list = datas.get("duelRoundOptions", [])
        self.roundsWithoutDamageMultiplier: int = gu.int_or_none(datas.get("roundsWithoutDamageMultiplier"))
        self.disableMultipliers: bool = gu.bool_or_none(datas.get("disableMultipliers"))
        self.multiplierIncrement: int = gu.int_or_none(datas.get("multiplierIncrement"))
        self.disableHealing: bool = gu.bool_or_none(datas.get("disableHealing"))
        self.isTeamDuels: bool = gu.bool_or_none(datas.get("isTeamDuels"))
        self.gameContext: GeoguessrDuelGameContext = GeoguessrDuelGameContext(datas.get("gameContext", {}))
        self.roundStartingBehavior: str = gu.str_or_none(datas.get("roundStartingBehavior"))
        self.flashbackRounds: list = datas.get("flashbackRounds", [])
        self.competitiveGameMode: str = gu.str_or_none(datas.get("competitiveGameMode"))
        self.countAllGuesses: bool = gu.bool_or_none(datas.get("countAllGuesses"))
        self.masterControlAutoStartRounds: bool = gu.bool_or_none(datas.get("masterControlAutoStartRounds"))
        self.consumedLocationsIdentifier: str = gu.str_or_none(datas.get("consumedLocationsIdentifier"))
        self.useCuratedLocations: bool = gu.bool_or_none(datas.get("useCuratedLocations"))
        self.extraWaitTimeBetweenRounds: int = gu.int_or_none(datas.get("extraWaitTimeBetweenRounds"))
        self.roundCountdownDelay: int = gu.int_or_none(datas.get("roundCountdownDelay"))
        self.guessMapType: str = gu.str_or_none(datas.get("guessMapType"))
        self.botBehaviors: Optional[Any] = datas.get("botBehaviors")
        self.activeMultiplier: bool = gu.bool_or_none(datas.get("activeMultiplier"))
        self.roundWinMultiplierIncrement: int = gu.int_or_none(datas.get("roundWinMultiplierIncrement"))


class GeoguessrMovementOptions(GeoguessrStr):
    """Représente les options de mouvement."""

    def __init__(self, datas: dict) -> None:
        self.forbidMoving: bool = gu.bool_or_none(datas.get("forbidMoving"))
        self.forbidZooming: bool = gu.bool_or_none(datas.get("forbidZooming"))
        self.forbidRotating: bool = gu.bool_or_none(datas.get("forbidRotating"))


class GeoguessrDuelMap(GeoguessrStr):
    """Représente la carte d'un duel."""

    def __init__(self, datas: dict) -> None:
        self.name: str = gu.str_or_none(datas.get("name"))
        self.slug: str = gu.str_or_none(datas.get("slug"))
        self.bounds: GeoguessrDuelMapBounds = GeoguessrDuelMapBounds(datas.get("bounds", {}))
        self.maxErrorDistance: int = gu.int_or_none(datas.get("maxErrorDistance"))


class GeoguessrDuelMapBounds(GeoguessrStr):
    """Représente les limites d'une carte."""

    def __init__(self, datas: dict) -> None:
        self.min: GeoguessrDuelCoordinate = GeoguessrDuelCoordinate(datas.get("min", {}))
        self.max: GeoguessrDuelCoordinate = GeoguessrDuelCoordinate(datas.get("max", {}))


class GeoguessrDuelCoordinate(GeoguessrStr):
    """Représente une coordonnée géographique."""

    def __init__(self, datas: dict) -> None:
        self.lat: float = self._parse_big_number(datas.get("lat"))
        self.lng: float = self._parse_big_number(datas.get("lng"))

    def _parse_big_number(self, value: Any) -> float:
        """Parse Big Number format or regular number."""
        if isinstance(value, dict) and value.get("type") == "Big Number":
            return float(str(value.get("value", "0")).replace("n", ""))
        elif isinstance(value, (int, float)):
            return float(value)
        return 0.0


class GeoguessrDuelGameContext(GeoguessrStr):
    """Représente le contexte de jeu."""

    def __init__(self, datas: dict) -> None:
        self.type: str = gu.str_or_none(datas.get("type"))
        self.id: str = gu.str_or_none(datas.get("id"))


class GeoguessrDuelResult(GeoguessrStr):
    """Représente le résultat d'un duel."""

    def __init__(self, datas: dict) -> None:
        self.isDraw: bool = gu.bool_or_none(datas.get("isDraw"))
        self.winningTeamId: str = gu.str_or_none(datas.get("winningTeamId"))
        self.winnerStyle: str = gu.str_or_none(datas.get("winnerStyle"))


class GeoguessrStatsParty(GeoguessrStr):
    """Represents party statistics."""

    def __init__(self, datas: dict) -> None:
        self.total: int = gu.int_or_none(datas.get("total"))
        self.duels: int = gu.int_or_none(datas.get("duels"))
        self.teamDuels: int = gu.int_or_none(datas.get("teamDuels"))
        self.battleRoyaleCountries: int = gu.int_or_none(datas.get("battleRoyaleCountries"))
        self.battleRoyaleDistance: int = gu.int_or_none(datas.get("battleRoyaleDistance"))
        self.cityStreaks: int = gu.int_or_none(datas.get("cityStreaks"))
        self.liveChallenges: int = gu.int_or_none(datas.get("liveChallenges"))
        self.bullseye: int = gu.int_or_none(datas.get("bullseye"))
        self.quizzes: int = gu.int_or_none(datas.get("quizzes"))
