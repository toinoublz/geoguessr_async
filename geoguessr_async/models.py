from datetime import datetime
from typing import Any, Optional

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
        self.nick: Optional[str] = gu.str_or_none(datas.get("nick"))
        self.created: datetime = datetime.strptime(datas.get("created").split(".")[0], "%Y-%m-%dT%H:%M:%S")
        self.isProUser: Optional[bool] = gu.bool_or_none(datas.get("isProUser"))
        self.type: Optional[str] = gu.str_or_none(datas.get("type"))
        self.isVerified: Optional[bool] = gu.bool_or_none(datas.get("isVerified"))
        self.pin: GeoguessrPin = GeoguessrPin(datas)
        self.color: Optional[int] = gu.int_or_none(datas.get("color"))
        self.url: Optional[str] = gu.str_or_none(datas.get("url"))
        self.id: Optional[str] = gu.str_or_none(datas.get("id"))
        self.countryCode: Optional[str] = gu.str_or_none(datas.get("countryCode"))
        self.battleRoyaleLevel: Optional[int] = gu.int_or_none(datas.get("br", {}).get("level"))
        self.battleRoyaleDivision: Optional[int] = gu.int_or_none(datas.get("br", {}).get("division"))
        self.streakProgress: Optional[Any] = datas.get("streakProgress")
        self.explorerProgress: Optional[Any] = datas.get("explorerProgress")
        self.dailyChallengeProgress: Optional[int] = gu.int_or_none(datas.get("dailyChallengeProgress"))
        self.progress: GeoguessrLevelProgress = GeoguessrLevelProgress(datas.get("progress"))
        self.competitive: GeoguessrCompetitive = GeoguessrCompetitive(datas.get("competitive"))
        self.lastNameChange: datetime = datetime.strptime(
            datas.get("lastNameChange").split(".")[0], "%Y-%m-%dT%H:%M:%S"
        )
        self.lastNickOrCountryChange: datetime = datetime.strptime(
            datas.get("lastNickOrCountryChange").split(".")[0], "%Y-%m-%dT%H:%M:%S"
        )
        self.isBanned: Optional[bool] = gu.bool_or_none(datas.get("isBanned"))
        self.chatBan: Optional[bool] = gu.bool_or_none(datas.get("chatBan"))
        self.nameChangeAvailableAt: Optional[datetime] = (
            datetime.strptime(datas.get("nameChangeAvailableAt").split(".")[0], "%Y-%m-%dT%H:%M:%S")
            if datas.get("nameChangeAvailableAt")
            else None
        )
        self.avatarUrl: Optional[str] = datas.get("avatar", {}).get("fullbodypath")
        self.isBotUser: Optional[bool] = gu.bool_or_none(datas.get("isBotUser"))
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
        self.token: Optional[str] = gu.str_or_none(datas.get("token"))
        self.mapSlug: Optional[str] = gu.str_or_none(datas.get("mapSlug"))
        self.roundCount: Optional[int] = gu.int_or_none(datas.get("roundCount"))
        self.timeLimit: Optional[int] = gu.int_or_none(datas.get("timeLimit"))
        self.forbidMoving: Optional[bool] = gu.bool_or_none(datas.get("forbidMoving"))
        self.forbidZooming: Optional[bool] = gu.bool_or_none(datas.get("forbidZooming"))
        self.forbidRotating: Optional[bool] = gu.bool_or_none(datas.get("forbidRotating"))
        self.guessMapType: Optional[str] = gu.str_or_none(datas.get("guessMapType"))
        self.numberOfParticipants: Optional[int] = gu.int_or_none(datas.get("numberOfParticipants"))
        self.gameMode: Optional[str] = gu.str_or_none(datas.get("gameMode"))
        self.challengeType: Optional[int] = gu.int_or_none(datas.get("challengeType"))
        self.streakType: Optional[str] = gu.str_or_none(datas.get("streakType"))
        self.accessLevel: Optional[int] = gu.int_or_none(datas.get("accessLevel"))
        self.locationOrder: Optional[int] = gu.int_or_none(datas.get("locationOrder"))


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
        self.number: Optional[int] = roundNumber
        self.lat: Optional[float] = gu.float_or_none(roundData.get("lat"))
        self.long: Optional[float] = gu.float_or_none(roundData.get("lng"))
        self.panoId: Optional[str] = gu.str_or_none(roundData.get("panoId"))
        self.heading: Optional[float] = gu.float_or_none(roundData.get("heading"))
        self.pitch: Optional[float] = gu.float_or_none(roundData.get("pitch"))
        self.zoom: Optional[float] = gu.float_or_none(roundData.get("zoom"))
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
        self.amount: Optional[float] = gu.float_or_none(scoreData.get("amount"))
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
        metersDistance = distanceData.get("meters", {})
        self.meters: Optional[float] = gu.float_or_none(metersDistance.get("amount")) * (
            1000 if metersDistance.get("unit") == "km" else 1
        )
        self.kilometers: Optional[float] = self.meters / 1000
        self.miles: Optional[float] = self.meters / 1609.34


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
        self.number: Optional[int] = roundNumber
        self.lat: Optional[float] = gu.float_or_none(guessData.get("lat"))
        self.long: Optional[float] = gu.float_or_none(guessData.get("lng"))
        self.timedOut: Optional[bool] = gu.bool_or_none(guessData.get("timedOut"))
        self.timedOutWithGuess: Optional[bool] = gu.bool_or_none(guessData.get("timedOutWithGuess"))
        self.skippedRound: Optional[bool] = gu.bool_or_none(guessData.get("skippedRound"))
        self.roundScore: GeoguessrScore = GeoguessrScore(guessData.get("roundScore"))
        self.roundScoreInPercentage: Optional[int] = gu.int_or_none(guessData.get("roundScoreInPercentage"))
        self.roundScoreInPoints: Optional[int] = gu.int_or_none(guessData.get("roundScoreInPoints"))
        self.distance: GeoguessrDistance = GeoguessrDistance(guessData.get("distance"))
        self.distanceInMeters: Optional[float] = gu.float_or_none(guessData.get("distanceInMeters"))
        self.stepsCount: Optional[int] = gu.int_or_none(guessData.get("stepsCount"))
        self.streakLocationCode: Optional[str] = guessData.get("streakLocationCode")
        self.time: GeoguessrTime = GeoguessrTime(guessData.get("time"))


class GeoguessrGameBounds(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        self.minLat: Optional[float] = gu.float_or_none(datas.get("min", {}).get("lat"))
        self.minLng: Optional[float] = gu.float_or_none(datas.get("min", {}).get("lng"))
        self.maxLat: Optional[float] = gu.float_or_none(datas.get("max", {}).get("lat"))
        self.maxLng: Optional[float] = gu.float_or_none(datas.get("max", {}).get("lng"))


class GeoguessrLevel(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        self.level: Optional[int] = gu.int_or_none(datas.get("level"))
        self.xpStart: Optional[int] = gu.int_or_none(datas.get("xpStart"))


class GeoguessrXpTitle(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        self.id: Optional[int] = gu.int_or_none(datas.get("id"))
        self.tierId: Optional[int] = gu.int_or_none(datas.get("tierId"))
        self.minimumLevel = gu.int_or_none(datas.get("minimumLevel", None))
        self.name: Optional[str] = gu.str_or_none(datas.get("name"))


class GeoguessrScorePlayerInfo(GeoguessrStr):
    def __init__(self, playerDatas: dict, progressionDatas: dict) -> None:
        self.isLeader: Optional[bool] = gu.bool_or_none(playerDatas.get("isLeader"))
        self.id: Optional[str] = gu.str_or_none(playerDatas.get("id"))
        self.nick: Optional[str] = gu.str_or_none(playerDatas.get("nick"))
        self.isVerified: Optional[bool] = gu.bool_or_none(playerDatas.get("isVerified"))
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
        self.type: Optional[str] = gu.str_or_none(gameDatas.get("type"))
        self.mode: Optional[str] = gu.str_or_none(gameDatas.get("mode"))
        self.state: Optional[str] = gu.str_or_none(gameDatas.get("state"))
        self.roundCount: Optional[int] = gu.int_or_none(gameDatas.get("roundCount"))
        self.streakType: Optional[str] = gu.str_or_none(gameDatas.get("streakType"))
        self.map: Optional[str] = gu.str_or_none(gameDatas.get("map"))
        self.mapname: Optional[str] = gu.str_or_none(gameDatas.get("mapName"))
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
        self.background: Optional[str] = gu.str_or_none(datas.get("background"))
        self.decoration: Optional[str] = gu.str_or_none(datas.get("decoration"))
        self.ground: Optional[str] = gu.str_or_none(datas.get("ground"))
        self.landscape: Optional[str] = gu.str_or_none(datas.get("landscape"))


class GeoguessrMap(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        self.id: Optional[str] = gu.str_or_none(datas.get("id"))
        self.name: Optional[str] = gu.str_or_none(datas.get("name"))
        self.slug: Optional[str] = gu.str_or_none(datas.get("slug"))
        self.description: Optional[str] = gu.str_or_none(datas.get("description"))
        self.url: Optional[str] = gu.str_or_none(datas.get("url"))
        self.playUrl: Optional[str] = gu.str_or_none(datas.get("playUrl"))
        self.published: Optional[bool] = gu.bool_or_none(datas.get("published"))
        self.banned: Optional[bool] = gu.bool_or_none(datas.get("banned"))
        self.backGround: Optional[str] = gu.str_or_none(datas.get("images", {}).get("backgroundLarge"))
        self.bounds: GeoguessrGameBounds = GeoguessrGameBounds(datas.get("bounds"))
        self.customCoordinates: Optional[Any] = datas.get("customCoordinates")
        self.coordinatesCount: Optional[str] = gu.str_or_none(datas.get("coordinateCount"))
        self.regions: Optional[Any] = datas.get("regions")
        self.creator: Optional[GeoguessrProfile] = (
            GeoguessrProfile(datas.get("creator")) if datas.get("creator") is not None else None
        )
        self.createdAt: Optional[datetime] = gu.datetime_or_none(datas.get("createdAt"))
        self.updatedAt: Optional[datetime] = gu.datetime_or_none(datas.get("updatedAt"))
        self.numFinishedGames: Optional[int] = gu.int_or_none(datas.get("numFinishedGames"))
        self.likedByUser: Optional[Any] = datas.get("likedByUser")
        self.averageScore: Optional[int] = gu.int_or_none(datas.get("averageScore"))
        self.avatar: GeoguessMapAvatar = GeoguessMapAvatar(datas.get("avatar"))
        self.difficulty: Optional[str] = gu.str_or_none(datas.get("difficulty"))
        self.difficultyLevel: Optional[int] = gu.int_or_none(datas.get("difficultyLevel"))
        self.highscore: Optional[Any] = datas.get("highscore")
        self.deleted: Optional[bool] = gu.bool_or_none(datas.get("deleted"))
        self.free: Optional[bool] = gu.bool_or_none(datas.get("free"))
        self.panoramaprovider: Optional[str] = gu.str_or_none(datas.get("panoramaProvider"))
        self.inExplorerMode: Optional[bool] = gu.bool_or_none(datas.get("inExplorerMode"))
        self.maxErrorDistance: Optional[int] = gu.int_or_none(datas.get("maxErrorDistance"))
        self.likes: Optional[int] = gu.int_or_none(datas.get("likes"))
        self.locationSelectionMode: Optional[int] = gu.int_or_none(datas.get("locationSelectionMode"))
        self.tags: Optional[list] = datas.get("tags")
        self.collaborators: Optional[Any] = datas.get("collaborators")
        self.flair: Optional[int] = gu.int_or_none(datas.get("flair"))
        self.mapSize: Optional[dict] = datas.get("mapSize")


class GeoguessrDuel(GeoguessrStr):
    """Represents a Geoguessr duel game.

    Attributes:
        gameId (str): Unique game identifier.
        teams (list): List of teams.
        rounds (list): List of rounds.
        currentRoundNumber (int): Current round number.
        status (str): Game status.
        version (int): Game version.
        # ... other attributes
    """

    def __init__(self, datas: dict) -> None:
        """Initialize GeoguessrDuel.

        Args:
            datas (dict): Raw duel data from API.
        """
        datas = gu.flatten_dict(datas)
        self.gameId: Optional[str] = gu.str_or_none(datas.get("gameId"))
        self.teams: list = datas.get("teams")
        self.rounds: list = datas.get("rounds")
        self.currentRoundNumber: Optional[int] = gu.int_or_none(datas.get("currentRoundNumber"))
        self.status: Optional[str] = gu.str_or_none(datas.get("status"))
        self.version: Optional[int] = gu.int_or_none(datas.get("version"))
        self.optionsInitialhealth: Optional[int] = gu.int_or_none(datas.get("optionsInitialhealth"))
        self.optionsRoundtime: Optional[int] = gu.int_or_none(datas.get("optionsRoundtime"))
        self.optionsMaxroundtime: Optional[int] = gu.int_or_none(datas.get("optionsMaxroundtime"))
        self.optionsMaxnumberofrounds: Optional[int] = gu.int_or_none(datas.get("optionsMaxnumberofrounds"))
        self.optionsHealingrounds: list = datas.get("optionsHealingrounds")
        self.optionsMovementoptionsForbidmoving: Optional[bool] = gu.bool_or_none(
            datas.get("optionsMovementoptionsForbidmoving")
        )
        self.optionsMovementoptionsForbidzooming: Optional[bool] = gu.bool_or_none(
            datas.get("optionsMovementoptionsForbidzooming")
        )
        self.optionsMovementoptionsForbidrotating: Optional[bool] = gu.bool_or_none(
            datas.get("optionsMovementoptionsForbidrotating")
        )
        self.optionsMapslug: Optional[str] = gu.str_or_none(datas.get("optionsMapslug"))
        self.optionsIsrated: Optional[bool] = gu.bool_or_none(datas.get("optionsIsrated"))
        self.optionsMapName: Optional[str] = gu.str_or_none(datas.get("optionsMapName"))
        self.optionsMapSlug: Optional[str] = gu.str_or_none(datas.get("optionsMapSlug"))
        self.optionsMapBoundsMinLat: Optional[float] = gu.float_or_none(datas.get("optionsMapBoundsMinLat"))
        self.optionsMapBoundsMinLng: Optional[float] = gu.float_or_none(datas.get("optionsMapBoundsMinLng"))
        self.optionsMapBoundsMaxLat: Optional[float] = gu.float_or_none(datas.get("optionsMapBoundsMaxLat"))
        self.optionsMapBoundsMaxLng: Optional[float] = gu.float_or_none(datas.get("optionsMapBoundsMaxLng"))
        self.optionsMapMaxerrordistance: Optional[int] = gu.int_or_none(datas.get("optionsMapMaxerrordistance"))
        self.optionsDuelroundoptions: list = datas.get("optionsDuelroundoptions")
        self.optionsRoundswithoutdamagemultiplier: Optional[int] = gu.int_or_none(
            datas.get("optionsRoundswithoutdamagemultiplier")
        )
        self.optionsDisablemultipliers: Optional[bool] = gu.bool_or_none(datas.get("optionsDisablemultipliers"))
        self.optionsMultiplierincrement: Optional[int] = gu.int_or_none(datas.get("optionsMultiplierincrement"))
        self.optionsDisablehealing: Optional[bool] = gu.bool_or_none(datas.get("optionsDisablehealing"))
        self.optionsIsteamduels: Optional[bool] = gu.bool_or_none(datas.get("optionsIsteamduels"))
        self.optionsGamecontextType: Optional[str] = gu.str_or_none(datas.get("optionsGamecontextType"))
        self.optionsGamecontextId: Optional[str] = gu.str_or_none(datas.get("optionsGamecontextId"))
        self.optionsManuallystartrounds: Optional[bool] = gu.bool_or_none(datas.get("optionsManuallystartrounds"))
        self.optionsFlashbackrounds: list = datas.get("optionsFlashbackrounds")
        self.movementOptionsForbidmoving: Optional[bool] = gu.bool_or_none(datas.get("movementOptionsForbidmoving"))
        self.movementOptionsForbidzooming: Optional[bool] = gu.bool_or_none(datas.get("movementOptionsForbidzooming"))
        self.movementOptionsForbidrotating: Optional[bool] = gu.bool_or_none(datas.get("movementOptionsForbidrotating"))
        self.mapBoundsMinLat: Optional[float] = gu.float_or_none(datas.get("mapBoundsMinLat"))
        self.mapBoundsMinLng: Optional[float] = gu.float_or_none(datas.get("mapBoundsMinLng"))
        self.mapBoundsMaxLat: Optional[float] = gu.float_or_none(datas.get("mapBoundsMaxLat"))
        self.mapBoundsMaxLng: Optional[float] = gu.float_or_none(datas.get("mapBoundsMaxLng"))
        self.initialHealth: Optional[int] = gu.int_or_none(datas.get("initialHealth"))
        self.maxNumberOfRounds: Optional[int] = gu.int_or_none(datas.get("maxNumberOfRounds"))
        self.resultIsdraw: Optional[bool] = gu.bool_or_none(datas.get("resultIsdraw"))
        self.resultWinningteamid: Optional[str] = gu.str_or_none(datas.get("resultWinningteamid"))
        self.resultWinnerstyle: Optional[str] = gu.str_or_none(datas.get("resultWinnerstyle"))


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
        self.divisionNumber: Optional[int] = gu.int_or_none(datas.get("divisionNumber"))
        self.divisionName: Optional[str] = gu.str_or_none(datas.get("divisionName"))
        self.rating: Optional[int] = gu.int_or_none(datas.get("rating"))
        self.tier: Optional[str] = gu.str_or_none(datas.get("tier"))
        self.gameModeRatingsStandardduels: Optional[int] = gu.int_or_none(datas.get("gameModeRatingsStandardduels"))
        self.gameModeRatingsNmpzduels: Optional[int] = gu.int_or_none(datas.get("gameModeRatingsNmpzduels"))
        self.gameModeRatingsNomoveduels: Optional[int] = gu.int_or_none(datas.get("gameModeRatingsNomoveduels"))


class GeoguessrStatsRankedTeamDuelsStandard(GeoguessrStr):
    """Represents ranked team duels standard statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: Optional[int] = gu.int_or_none(datas.get("numGamesPlayed"))
        self.numWins: Optional[int] = gu.int_or_none(datas.get("numWins"))
        self.winRatio: Optional[float] = gu.float_or_none(datas.get("winRatio"))


class GeoguessrStatsRankedTeamDuelsNoMove(GeoguessrStr):
    """Represents ranked team duels no move statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: Optional[int] = gu.int_or_none(datas.get("numGamesPlayed"))
        self.numWins: Optional[int] = gu.int_or_none(datas.get("numWins"))
        self.winRatio: Optional[float] = gu.float_or_none(datas.get("winRatio"))


class GeoguessrStatsRankedTeamDuelsNmpz(GeoguessrStr):
    """Represents ranked team duels NMPZ statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: Optional[int] = gu.int_or_none(datas.get("numGamesPlayed"))
        self.numWins: Optional[int] = gu.int_or_none(datas.get("numWins"))
        self.winRatio: Optional[float] = gu.float_or_none(datas.get("winRatio"))


class GeoguessrStatsRankedTeamDuelsTotal(GeoguessrStr):
    """Represents ranked team duels total statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: Optional[int] = gu.int_or_none(datas.get("numGamesPlayed"))
        self.numWins: Optional[int] = gu.int_or_none(datas.get("numWins"))
        self.winRatio: Optional[float] = gu.float_or_none(datas.get("winRatio"))


class GeoguessrStatsBattleRoyaleDistance(GeoguessrStr):
    """Represents battle royale distance statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: Optional[int] = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: Optional[float] = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: Optional[int] = gu.int_or_none(datas.get("numWins"))
        self.winRatio: Optional[float] = gu.float_or_none(datas.get("winRatio"))
        self.avgGuessDistance: Optional[float] = gu.float_or_none(datas.get("avgGuessDistance"))
        self.numGuesses: Optional[int] = gu.int_or_none(datas.get("numGuesses"))


class GeoguessrStatsBattleRoyaleCountry(GeoguessrStr):
    """Represents battle royale country statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: Optional[int] = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: Optional[float] = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: Optional[int] = gu.int_or_none(datas.get("numWins"))
        self.winRatio: Optional[float] = gu.float_or_none(datas.get("winRatio"))
        self.numGuesses: Optional[int] = gu.int_or_none(datas.get("numGuesses"))
        self.avgCorrectGuesses: Optional[float] = gu.float_or_none(datas.get("avgCorrectGuesses"))


class GeoguessrStatsBattleRoyaleMedals(GeoguessrStr):
    """Represents battle royale medals statistics."""

    def __init__(self, datas: dict) -> None:
        self.medalCountGold: Optional[int] = gu.int_or_none(datas.get("medalCountGold"))
        self.medalCountSilver: Optional[int] = gu.int_or_none(datas.get("medalCountSilver"))
        self.medalCountBronze: Optional[int] = gu.int_or_none(datas.get("medalCountBronze"))


class GeoguessrStatsCompetitiveCityStreaks(GeoguessrStr):
    """Represents competitive city streaks statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: Optional[int] = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: Optional[float] = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: Optional[int] = gu.int_or_none(datas.get("numWins"))
        self.winRatio: Optional[float] = gu.float_or_none(datas.get("winRatio"))
        self.numGuesses: Optional[int] = gu.int_or_none(datas.get("numGuesses"))
        self.avgCorrectGuesses: Optional[float] = gu.float_or_none(datas.get("avgCorrectGuesses"))


class GeoguessrStatsCompetitiveStreaksMedals(GeoguessrStr):
    """Represents competitive streaks medals statistics."""

    def __init__(self, datas: dict) -> None:
        self.medalCountGold: Optional[int] = gu.int_or_none(datas.get("medalCountGold"))
        self.medalCountSilver: Optional[int] = gu.int_or_none(datas.get("medalCountSilver"))
        self.medalCountBronze: Optional[int] = gu.int_or_none(datas.get("medalCountBronze"))


class GeoguessrStatsDuels(GeoguessrStr):
    """Represents duels statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: Optional[int] = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: Optional[float] = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: Optional[int] = gu.int_or_none(datas.get("numWins"))
        self.winRatio: Optional[float] = gu.float_or_none(datas.get("winRatio"))
        self.avgGuessDistance: Optional[float] = gu.float_or_none(datas.get("avgGuessDistance"))
        self.numGuesses: Optional[int] = gu.int_or_none(datas.get("numGuesses"))
        self.numFlawlessWins: Optional[int] = gu.int_or_none(datas.get("numFlawlessWins"))


class GeoguessrStatsDuelsNoMove(GeoguessrStr):
    """Represents duels no move statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: Optional[int] = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: Optional[float] = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: Optional[int] = gu.int_or_none(datas.get("numWins"))
        self.winRatio: Optional[float] = gu.float_or_none(datas.get("winRatio"))
        self.avgGuessDistance: Optional[float] = gu.float_or_none(datas.get("avgGuessDistance"))
        self.numGuesses: Optional[int] = gu.int_or_none(datas.get("numGuesses"))
        self.numFlawlessWins: Optional[int] = gu.int_or_none(datas.get("numFlawlessWins"))


class GeoguessrStatsDuelsNmpz(GeoguessrStr):
    """Represents duels NMPZ statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: Optional[int] = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: Optional[float] = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: Optional[int] = gu.int_or_none(datas.get("numWins"))
        self.winRatio: Optional[float] = gu.float_or_none(datas.get("winRatio"))
        self.avgGuessDistance: Optional[float] = gu.float_or_none(datas.get("avgGuessDistance"))
        self.numGuesses: Optional[int] = gu.int_or_none(datas.get("numGuesses"))
        self.numFlawlessWins: Optional[int] = gu.int_or_none(datas.get("numFlawlessWins"))


class GeoguessrStatsDuelsTotal(GeoguessrStr):
    """Represents duels total statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: Optional[int] = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: Optional[float] = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: Optional[int] = gu.int_or_none(datas.get("numWins"))
        self.winRatio: Optional[float] = gu.float_or_none(datas.get("winRatio"))
        self.avgGuessDistance: Optional[float] = gu.float_or_none(datas.get("avgGuessDistance"))
        self.numGuesses: Optional[int] = gu.int_or_none(datas.get("numGuesses"))
        self.numFlawlessWins: Optional[int] = gu.int_or_none(datas.get("numFlawlessWins"))


class GeoguessrStatsDuelsMedals(GeoguessrStr):
    """Represents duels medals statistics."""

    def __init__(self, datas: dict) -> None:
        self.medalCountGold: Optional[int] = gu.int_or_none(datas.get("medalCountGold"))
        self.medalCountSilver: Optional[int] = gu.int_or_none(datas.get("medalCountSilver"))
        self.medalCountBronze: Optional[int] = gu.int_or_none(datas.get("medalCountBronze"))


class GeoguessrStatsUnrankedDuels(GeoguessrStr):
    """Represents unranked duels statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: Optional[int] = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: Optional[float] = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: Optional[int] = gu.int_or_none(datas.get("numWins"))
        self.winRatio: Optional[float] = gu.float_or_none(datas.get("winRatio"))
        self.avgGuessDistance: Optional[float] = gu.float_or_none(datas.get("avgGuessDistance"))
        self.numGuesses: Optional[int] = gu.int_or_none(datas.get("numGuesses"))
        self.numFlawlessWins: Optional[int] = gu.int_or_none(datas.get("numFlawlessWins"))


class GeoguessrStatsUnrankedDuelsNoMove(GeoguessrStr):
    """Represents unranked duels no move statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: Optional[int] = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: Optional[float] = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: Optional[int] = gu.int_or_none(datas.get("numWins"))
        self.winRatio: Optional[float] = gu.float_or_none(datas.get("winRatio"))
        self.avgGuessDistance: Optional[float] = gu.float_or_none(datas.get("avgGuessDistance"))
        self.numGuesses: Optional[int] = gu.int_or_none(datas.get("numGuesses"))
        self.numFlawlessWins: Optional[int] = gu.int_or_none(datas.get("numFlawlessWins"))


class GeoguessrStatsUnrankedDuelsNmpz(GeoguessrStr):
    """Represents unranked duels NMPZ statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: Optional[int] = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: Optional[float] = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: Optional[int] = gu.int_or_none(datas.get("numWins"))
        self.winRatio: Optional[float] = gu.float_or_none(datas.get("winRatio"))
        self.avgGuessDistance: Optional[float] = gu.float_or_none(datas.get("avgGuessDistance"))
        self.numGuesses: Optional[int] = gu.int_or_none(datas.get("numGuesses"))
        self.numFlawlessWins: Optional[int] = gu.int_or_none(datas.get("numFlawlessWins"))


class GeoguessrStatsUnrankedDuelsTotal(GeoguessrStr):
    """Represents unranked duels total statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: Optional[int] = gu.int_or_none(datas.get("numGamesPlayed"))
        self.avgPosition: Optional[float] = gu.float_or_none(datas.get("avgPosition"))
        self.numWins: Optional[int] = gu.int_or_none(datas.get("numWins"))
        self.winRatio: Optional[float] = gu.float_or_none(datas.get("winRatio"))
        self.avgGuessDistance: Optional[float] = gu.float_or_none(datas.get("avgGuessDistance"))
        self.numGuesses: Optional[int] = gu.int_or_none(datas.get("numGuesses"))
        self.numFlawlessWins: Optional[int] = gu.int_or_none(datas.get("numFlawlessWins"))


class GeoguessrStatsLifeTimeXpProgression(GeoguessrStr):
    """Represents lifetime XP progression statistics."""

    def __init__(self, datas: dict) -> None:
        self.xp: Optional[int] = gu.int_or_none(datas.get("xp"))
        self.currentLevel: GeoguessrLevel = GeoguessrLevel(datas.get("currentLevel"))
        self.nextLevel: GeoguessrLevel = GeoguessrLevel(datas.get("nextLevel"))
        self.currentTitle: GeoguessrXpTitle = GeoguessrXpTitle(datas.get("currentTitle"))


class GeoguessrStatsTotalMedals(GeoguessrStr):
    """Represents total medals statistics."""

    def __init__(self, datas: dict) -> None:
        self.medalCountGold: Optional[int] = gu.int_or_none(datas.get("medalCountGold"))
        self.medalCountSilver: Optional[int] = gu.int_or_none(datas.get("medalCountSilver"))
        self.medalCountBronze: Optional[int] = gu.int_or_none(datas.get("medalCountBronze"))


class GeoguessrStatsTeamDuels(GeoguessrStr):
    """Represents team duels statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: Optional[int] = gu.int_or_none(datas.get("numGamesPlayed"))
        self.numWins: Optional[int] = gu.int_or_none(datas.get("numWins"))
        self.winRatio: Optional[float] = gu.float_or_none(datas.get("winRatio"))


class GeoguessrStatsTeamDuelsQuickplay(GeoguessrStr):
    """Represents team duels quickplay statistics."""

    def __init__(self, datas: dict) -> None:
        self.numGamesPlayed: Optional[int] = gu.int_or_none(datas.get("numGamesPlayed"))
        self.numWins: Optional[int] = gu.int_or_none(datas.get("numWins"))


class GeoguessrStatsParty(GeoguessrStr):
    """Represents party statistics."""

    def __init__(self, datas: dict) -> None:
        self.total: Optional[int] = gu.int_or_none(datas.get("total"))
        self.duels: Optional[int] = gu.int_or_none(datas.get("duels"))
        self.teamDuels: Optional[int] = gu.int_or_none(datas.get("teamDuels"))
        self.battleRoyaleCountries: Optional[int] = gu.int_or_none(datas.get("battleRoyaleCountries"))
        self.battleRoyaleDistance: Optional[int] = gu.int_or_none(datas.get("battleRoyaleDistance"))
        self.cityStreaks: Optional[int] = gu.int_or_none(datas.get("cityStreaks"))
        self.liveChallenges: Optional[int] = gu.int_or_none(datas.get("liveChallenges"))
        self.bullseye: Optional[int] = gu.int_or_none(datas.get("bullseye"))
        self.quizzes: Optional[int] = gu.int_or_none(datas.get("quizzes"))
