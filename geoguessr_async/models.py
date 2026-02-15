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
        datas = gu.flatten_dict(datas)
        self.battleRoyaleRankRank: int = int(datas.get("battleRoyaleRankRank"))
        self.battleRoyaleRankRating: int = int(datas.get("battleRoyaleRankRating"))
        self.battleRoyaleRankGamesleftbeforeranked: int = int(datas.get("battleRoyaleRankGamesleftbeforeranked"))
        self.battleRoyaleRankDivisionId: int = int(datas.get("battleRoyaleRankDivisionId"))
        self.battleRoyaleRankDivisionDivisionid: int = int(datas.get("battleRoyaleRankDivisionDivisionid"))
        self.battleRoyaleRankDivisionTierid: int = int(datas.get("battleRoyaleRankDivisionTierid"))
        self.battleRoyaleRankDivisionName: str = datas.get("battleRoyaleRankDivisionName")
        self.battleRoyaleRankDivisionMinimumrank: int = int(datas.get("battleRoyaleRankDivisionMinimumrank"))
        self.battleRoyaleDistanceNumgamesplayed: int = int(datas.get("battleRoyaleDistanceNumgamesplayed"))
        self.battleRoyaleDistanceAvgposition: float = float(datas.get("battleRoyaleDistanceAvgposition"))
        self.battleRoyaleDistanceNumwins: int = int(datas.get("battleRoyaleDistanceNumwins"))
        self.battleRoyaleDistanceWinratio: float = float(datas.get("battleRoyaleDistanceWinratio"))
        self.battleRoyaleDistanceAvgguessdistance: float = float(datas.get("battleRoyaleDistanceAvgguessdistance"))
        self.battleRoyaleDistanceNumguesses: int = int(datas.get("battleRoyaleDistanceNumguesses"))
        self.battleRoyaleCountryNumgamesplayed: int = int(datas.get("battleRoyaleCountryNumgamesplayed"))
        self.battleRoyaleCountryAvgposition: float = float(datas.get("battleRoyaleCountryAvgposition"))
        self.battleRoyaleCountryNumwins: int = int(datas.get("battleRoyaleCountryNumwins"))
        self.battleRoyaleCountryWinratio: float = float(datas.get("battleRoyaleCountryWinratio"))
        self.battleRoyaleCountryNumguesses: int = int(datas.get("battleRoyaleCountryNumguesses"))
        self.battleRoyaleCountryAvgcorrectguesses: float = float(datas.get("battleRoyaleCountryAvgcorrectguesses"))
        self.battleRoyaleMedalsMedalcountgold: int = int(datas.get("battleRoyaleMedalsMedalcountgold"))
        self.battleRoyaleMedalsMedalcountsilver: int = int(datas.get("battleRoyaleMedalsMedalcountsilver"))
        self.battleRoyaleMedalsMedalcountbronze: int = int(datas.get("battleRoyaleMedalsMedalcountbronze"))
        self.competitiveCityStreaksNumgamesplayed: int = int(datas.get("competitiveCityStreaksNumgamesplayed"))
        self.competitiveCityStreaksAvgposition: float = float(datas.get("competitiveCityStreaksAvgposition"))
        self.competitiveCityStreaksNumwins: int = int(datas.get("competitiveCityStreaksNumwins"))
        self.competitiveCityStreaksWinratio: float = float(datas.get("competitiveCityStreaksWinratio"))
        self.competitiveCityStreaksNumguesses: int = int(datas.get("competitiveCityStreaksNumguesses"))
        self.competitiveCityStreaksAvgcorrectguesses: float = float(
            datas.get("competitiveCityStreaksAvgcorrectguesses")
        )
        self.competitiveStreaksRankRank: int = int(datas.get("competitiveStreaksRankRank"))
        self.competitiveStreaksRankRating: int = int(datas.get("competitiveStreaksRankRating"))
        self.competitiveStreaksRankGamesleftbeforeranked: int = int(
            datas.get("competitiveStreaksRankGamesleftbeforeranked")
        )
        self.competitiveStreaksRankDivisionId: int = int(datas.get("competitiveStreaksRankDivisionId"))
        self.competitiveStreaksRankDivisionDivisionid: int = int(datas.get("competitiveStreaksRankDivisionDivisionid"))
        self.competitiveStreaksRankDivisionTierid: int = int(datas.get("competitiveStreaksRankDivisionTierid"))
        self.competitiveStreaksRankDivisionName: str = datas.get("competitiveStreaksRankDivisionName")
        self.competitiveStreaksRankDivisionMinimumrank: int = int(
            datas.get("competitiveStreaksRankDivisionMinimumrank")
        )
        self.competitiveStreaksMedalsMedalcountgold: int = int(datas.get("competitiveStreaksMedalsMedalcountgold"))
        self.competitiveStreaksMedalsMedalcountsilver: int = int(datas.get("competitiveStreaksMedalsMedalcountsilver"))
        self.competitiveStreaksMedalsMedalcountbronze: int = int(datas.get("competitiveStreaksMedalsMedalcountbronze"))
        self.duelsNumgamesplayed: int = int(datas.get("duelsNumgamesplayed"))
        self.duelsAvgposition: float = float(datas.get("duelsAvgposition"))
        self.duelsNumwins: int = int(datas.get("duelsNumwins"))
        self.duelsWinratio: float = float(datas.get("duelsWinratio"))
        self.duelsAvgguessdistance: float = float(datas.get("duelsAvgguessdistance"))
        self.duelsNumguesses: int = int(datas.get("duelsNumguesses"))
        self.duelsNumflawlesswins: int = int(datas.get("duelsNumflawlesswins"))
        self.duelsRankRank: int = int(datas.get("duelsRankRank"))
        self.duelsRankRating: int = int(datas.get("duelsRankRating"))
        self.duelsRankGamesleftbeforeranked: int = int(datas.get("duelsRankGamesleftbeforeranked"))
        self.duelsRankDivisionId: int = int(datas.get("duelsRankDivisionId"))
        self.duelsRankDivisionDivisionid: int = int(datas.get("duelsRankDivisionDivisionid"))
        self.duelsRankDivisionTierid: int = int(datas.get("duelsRankDivisionTierid"))
        self.duelsRankDivisionName: str = datas.get("duelsRankDivisionName")
        self.duelsRankDivisionMinimumrank: int = int(datas.get("duelsRankDivisionMinimumrank"))
        self.duelsMedalsMedalcountgold: int = int(datas.get("duelsMedalsMedalcountgold"))
        self.duelsMedalsMedalcountsilver: int = int(datas.get("duelsMedalsMedalcountsilver"))
        self.duelsMedalsMedalcountbronze: int = int(datas.get("duelsMedalsMedalcountbronze"))
        self.lifeTimeXpProgressionXp: int = int(datas.get("lifeTimeXpProgressionXp"))
        self.lifeTimeXpProgressionCurrentlevelLevel: int = int(datas.get("lifeTimeXpProgressionCurrentlevelLevel"))
        self.lifeTimeXpProgressionCurrentlevelXpstart: int = int(datas.get("lifeTimeXpProgressionCurrentlevelXpstart"))
        self.lifeTimeXpProgressionNextlevelLevel: int = int(datas.get("lifeTimeXpProgressionNextlevelLevel"))
        self.lifeTimeXpProgressionNextlevelXpstart: int = int(datas.get("lifeTimeXpProgressionNextlevelXpstart"))
        self.lifeTimeXpProgressionCurrenttitleId: int = int(datas.get("lifeTimeXpProgressionCurrenttitleId"))
        self.lifeTimeXpProgressionCurrenttitleTierid: int = int(datas.get("lifeTimeXpProgressionCurrenttitleTierid"))
        self.lifeTimeXpProgressionCurrenttitleMinimumlevel: int = int(
            datas.get("lifeTimeXpProgressionCurrenttitleMinimumlevel")
        )
        self.lifeTimeXpProgressionCurrenttitleName: str = datas.get("lifeTimeXpProgressionCurrenttitleName")
        self.totalMedalsMedalcountgold: int = int(datas.get("totalMedalsMedalcountgold"))
        self.totalMedalsMedalcountsilver: int = int(datas.get("totalMedalsMedalcountsilver"))
        self.totalMedalsMedalcountbronze: int = int(datas.get("totalMedalsMedalcountbronze"))
        self.teamDuelsNumgamesplayed: int = int(datas.get("teamDuelsNumgamesplayed"))
        self.teamDuelsNumwins: int = int(datas.get("teamDuelsNumwins"))
        self.teamDuelsWinratio: float = float(datas.get("teamDuelsWinratio"))
        self.perfectRounds: int = int(datas.get("perfectRounds"))


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
        datas = gu.flatten_dict(datas)
        self.nick: str = datas.get("nick")
        self.created: str = datas.get("created")
        self.isProUser: bool = bool(datas.get("isProUser"))
        self.type: str = datas.get("type")
        self.consumedTrial: bool = bool(datas.get("consumedTrial"))
        self.isVerified: bool = bool(datas.get("isVerified"))
        self.pinUrl: str = datas.get("pinUrl")
        self.pinAnchor: str = datas.get("pinAnchor")
        self.pinIsdefault: bool = bool(datas.get("pinIsdefault"))
        self.fullBodyPin: Optional[Any] = datas.get("fullBodyPin")
        self.color: int = int(datas.get("color"))
        self.url: str = datas.get("url")
        self.id: str = datas.get("id")
        self.countryCode: str = datas.get("countryCode")
        self.brLevel: int = int(datas.get("brLevel"))
        self.brDivision: int = int(datas.get("brDivision"))
        self.brStreak: int = int(datas.get("brStreak"))
        self.streakProgress: Optional[Any] = datas.get("streakProgress")
        self.explorerProgress: Optional[Any] = datas.get("explorerProgress")
        self.dailyChallengeProgress: int = int(datas.get("dailyChallengeProgress"))
        self.progressXp: int = int(datas.get("progressXp"))
        self.progressLevel: int = int(datas.get("progressLevel"))
        self.progressLevelxp: int = int(datas.get("progressLevelxp"))
        self.progressNextlevel: int = int(datas.get("progressNextlevel"))
        self.progressNextlevelxp: int = int(datas.get("progressNextlevelxp"))
        self.progressTitleId: int = int(datas.get("progressTitleId"))
        self.progressTitleTierid: int = int(datas.get("progressTitleTierid"))
        self.progressBrrankRating: int = int(datas.get("progressBrrankRating"))
        self.progressBrrankRank: int = int(datas.get("progressBrrankRank"))
        self.progressBrrankGamesleftbeforeranked: int = int(datas.get("progressBrrankGamesleftbeforeranked"))
        self.progressBrrankDivisionId: int = int(datas.get("progressBrrankDivisionId"))
        self.progressBrrankDivisionDivisionid: int = int(datas.get("progressBrrankDivisionDivisionid"))
        self.progressBrrankDivisionTierid: int = int(datas.get("progressBrrankDivisionTierid"))
        self.progressCsrankRating: int = int(datas.get("progressCsrankRating"))
        self.progressCsrankRank: int = int(datas.get("progressCsrankRank"))
        self.progressCsrankGamesleftbeforeranked: int = int(datas.get("progressCsrankGamesleftbeforeranked"))
        self.progressCsrankDivisionId: int = int(datas.get("progressCsrankDivisionId"))
        self.progressCsrankDivisionDivisionid: int = int(datas.get("progressCsrankDivisionDivisionid"))
        self.progressCsrankDivisionTierid: int = int(datas.get("progressCsrankDivisionTierid"))
        self.progressDuelsrankRating: int = int(datas.get("progressDuelsrankRating"))
        self.progressDuelsrankRank: int = int(datas.get("progressDuelsrankRank"))
        self.progressDuelsrankGamesleftbeforeranked: int = int(datas.get("progressDuelsrankGamesleftbeforeranked"))
        self.progressDuelsrankDivisionId: int = int(datas.get("progressDuelsrankDivisionId"))
        self.progressDuelsrankDivisionDivisionid: int = int(datas.get("progressDuelsrankDivisionDivisionid"))
        self.progressDuelsrankDivisionTierid: int = int(datas.get("progressDuelsrankDivisionTierid"))
        self.progressCompetitionmedalsBronze: int = int(datas.get("progressCompetitionmedalsBronze"))
        self.progressCompetitionmedalsSilver: int = int(datas.get("progressCompetitionmedalsSilver"))
        self.progressCompetitionmedalsGold: int = int(datas.get("progressCompetitionmedalsGold"))
        self.progressCompetitionmedalsPlatinum: int = int(datas.get("progressCompetitionmedalsPlatinum"))
        self.competitiveElo: int = int(datas.get("competitiveElo"))
        self.competitiveRating: int = int(datas.get("competitiveRating"))
        self.competitiveLastratingchange: int = int(datas.get("competitiveLastratingchange"))
        self.competitiveDivisionType: int = int(datas.get("competitiveDivisionType"))
        self.competitiveDivisionStartrating: int = int(datas.get("competitiveDivisionStartrating"))
        self.competitiveDivisionEndrating: int = int(datas.get("competitiveDivisionEndrating"))
        self.lastNameChange: str = datas.get("lastNameChange")
        self.isBanned: bool = bool(datas.get("isBanned"))
        self.nameChangeAvailableAt: Optional[datetime] = datas.get("nameChangeAvailableAt")
        self.avatarFullbodypath: Optional[str] = datas.get("avatarFullbodypath")
        self.isBotUser: bool = bool(datas.get("isBotUser"))
        self.suspendedUntil: Optional[datetime] = datas.get("suspendedUntil")
        self.wallet: int = int(datas.get("wallet"))
        self.flair: int = int(datas.get("flair"))
        self.isCreator: bool = bool(datas.get("isCreator"))
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
        datas = gu.flatten_dict(datas)
        self.challengeToken: str = datas.get("challengeToken")
        self.challengeMapslug: str = datas.get("challengeMapslug")
        self.challengeRoundcount: int = int(datas.get("challengeRoundcount"))
        self.challengeTimelimit: int = int(datas.get("challengeTimelimit"))
        self.challengeForbidmoving: bool = bool(datas.get("challengeForbidmoving"))
        self.challengeForbidzooming: bool = bool(datas.get("challengeForbidzooming"))
        self.challengeForbidrotating: bool = bool(datas.get("challengeForbidrotating"))
        self.challengeNumberofparticipants: int = int(datas.get("challengeNumberofparticipants"))
        self.challengeGamemode: str = datas.get("challengeGamemode")
        self.challengeChallengetype: int = int(datas.get("challengeChallengetype"))
        self.challengeStreaktype: str = datas.get("challengeStreaktype")
        self.challengeStrTimelimit: str = datas.get("challengeStr_timelimit")
        self.mapId: str = datas.get("mapId")
        self.creatorNick: str = datas.get("creatorNick")
        self.creatorId: str = datas.get("creatorId")
        self.mode: str = datas.get("mode")


class GeoguessrRound(GeoguessrStr):
    """Represents a single round in a Geoguessr game.

    Attributes:
        number (int): Round number.
        lat (float): Latitude of the location.
        long (float): Longitude of the location.
        # ... other round attributes
    """

    def __init__(self, roundData: dict, roundNumber: int) -> None:
        """Initialize GeoguessrRound.

        Args:
            roundData (dict): Raw round data from API.
            roundNumber (int): Round number (1-based).
        """
        self.number: int = roundNumber
        self.lat: float = float(roundData.get("lat"))
        self.long: float = float(roundData.get("lng"))
        self.panoId: str = roundData.get("panoId")
        self.heading: float = float(roundData.get("heading"))
        self.pitch: float = float(roundData.get("pitch"))
        self.zoom: float = float(roundData.get("zoom"))
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
        self.amount: float = float(scoreData.get("amount"))
        self.unit: str = scoreData.get("unit")
        self.percentage: float = float(scoreData.get("percentage"))


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
        self.meters: float = float(metersDistance.get("amount")) * (1000 if metersDistance.get("unit") == "km" else 1)
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
        self.seconds: float = seconds if seconds is not None else None
        self.minutes: float = minutes if minutes is not None else None
        self.hours: float = hours if hours is not None else None
        if self.seconds is not None:
            self.minutes = self.seconds / 60
            self.hours = self.minutes / 60
        elif self.minutes is not None:
            self.seconds = self.minutes * 60
            self.hours = self.minutes / 60
        elif self.hours is not None:
            self.seconds = self.hours * 3600
            self.minutes = self.hours * 60


class GeoguessrPlayerGuesses(GeoguessrStr):
    """Represents a player's guess in a round.

    Attributes:
        number (int): Round number.
        lat (float): Guess latitude.
        long (float): Guess longitude.
        timedOut (bool): Whether player timed out.
        # ... other guess attributes
    """

    def __init__(self, guessData: dict, roundNumber: int) -> None:
        """Initialize GeoguessrPlayerGuesses.

        Args:
            guessData (dict): Raw guess data from API.
            roundNumber (int): Round number (1-based).
        """
        self.number: int = roundNumber
        self.lat: float = float(guessData.get("lat"))
        self.long: float = float(guessData.get("lng"))
        self.timedOut: bool = guessData.get("timedOut")
        self.timedOutWithGuess: bool = guessData.get("timedOutWithGuess")
        self.skippedRound: bool = guessData.get("skippedRound")
        self.roundScore: GeoguessrScore = GeoguessrScore(guessData.get("roundScore"))
        self.roundScoreInPercentage: int = guessData.get("roundScoreInPercentage")
        self.roundScoreInPoints: int = guessData.get("roundScoreInPoints")
        self.distance: GeoguessrDistance = GeoguessrDistance(guessData.get("distance"))
        self.distanceInMeters: float = guessData.get("distanceInMeters")
        self.stepsCount: int = guessData.get("stepsCount")
        self.streakLocationCode: Optional[str] = guessData.get("streakLocationCode")
        self.time: GeoguessrTime = GeoguessrTime(guessData.get("time"))


class GeoguessrGameBounds(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        self.minLat: float = float(datas.get("min", {}).get("lat"))
        self.minLng: float = float(datas.get("min", {}).get("lng"))
        self.maxLat: float = float(datas.get("max", {}).get("lat"))
        self.maxLng: float = float(datas.get("max", {}).get("lng"))


class GeoguessrLevel(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        self.level: int = int(datas.get("level"))
        self.xpStart: int = int(datas.get("xpStart"))


class GeoguessrTitle(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        self.id: int = int(datas.get("id"))
        self.tierId: int = int(datas.get("tierId"))
        self.minimumLevel: int = int(datas.get("minimumLevel"))
        self.name: str = datas.get("name")


class GeoguessrScorePlayerInfo(GeoguessrStr):
    def __init__(self, playerDatas: dict, progressionDatas: dict) -> None:
        self.isLeader: bool = playerDatas.get("isLeader")
        self.id: str = playerDatas.get("id")
        self.nick: str = playerDatas.get("nick")
        self.isVerified: bool = playerDatas.get("isVerified")
        self.flair: int = playerDatas.get("flair")
        self.countryCode: str = playerDatas.get("countryCode")
        self.pinUrl: str = playerDatas.get("pin", {}).get("url")
        self.xpBeforeChallenge: int = progressionDatas.get("xpProgressions", [{}, {}])[0].get("xp")
        self.xpAfterChallenge: int = progressionDatas.get("xpProgressions", [{}, {}])[1].get("xp")
        self.xpGained: int = self.xpAfterChallenge - self.xpBeforeChallenge
        self.levelBeforeChallenge: GeoguessrLevel = GeoguessrLevel(
            progressionDatas.get("xpProgressions", [{}, {}])[0].get("currentLevel")
        )
        self.levelAfterChallenge: GeoguessrLevel = GeoguessrLevel(
            progressionDatas.get("xpProgressions", [{}, {}])[1].get("currentLevel")
        )
        self.titleBeforeChallenge: GeoguessrTitle = GeoguessrTitle(
            progressionDatas.get("xpProgressions", [{}, {}])[0].get("currentTitle")
        )
        self.titleAfterChallenge: GeoguessrTitle = GeoguessrTitle(
            progressionDatas.get("xpProgressions", [{}, {}])[1].get("currentTitle")
        )


class GeoguessrChallengePlayerTotalResult(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        self.totalScore: GeoguessrScore = GeoguessrScore(datas.get("totalScore"))
        self.totalDistance: GeoguessrDistance = GeoguessrDistance(datas.get("totalDistance"))
        self.totalStepsCount: int = int(datas.get("totalStepsCount"))
        self.totalTime: GeoguessrTime = GeoguessrTime(seconds=datas.get("totalTime"))
        self.totalStreak: int = int(datas.get("totalStreak"))
        self.guesses: list[GeoguessrPlayerGuesses] = [
            GeoguessrPlayerGuesses(guess, i + 1) for i, guess in enumerate(datas.get("guesses")) if guess is not None
        ]


class GeoguessrChallengeResult(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        gameDatas: Optional[dict] = datas.get("game")
        if gameDatas is None:
            raise ValueError("The game key is missing in the data.")
        self.player = GeoguessrScorePlayerInfo(gameDatas.get("player"), gameDatas.get("progressChange"))
        self.type: str = gameDatas.get("type")
        self.mode: str = gameDatas.get("mode")
        self.state: str = gameDatas.get("state")
        self.roundCount: int = gameDatas.get("roundCount")
        self.streakType: str = gameDatas.get("streakType")
        self.map: str = gameDatas.get("map")
        self.mapname: str = gameDatas.get("mapName")
        self.panoramaprovider: int = gameDatas.get("panoramaprovider")
        self.bounds: GeoguessrGameBounds = GeoguessrGameBounds(gameDatas.get("bounds"))
        self.rounds: list[GeoguessrRound] = [
            GeoguessrRound(round, i + 1) for i, round in enumerate(gameDatas.get("rounds")) if round is not None
        ]
        self.playerTotalScore = GeoguessrChallengePlayerTotalResult(gameDatas.get("player"))


class GeoguessrMap(GeoguessrStr):
    def __init__(self, datas: dict) -> None:
        datas = gu.flatten_dict(datas)
        self.id: str = datas.get("id")
        self.name: str = datas.get("name")
        self.slug: str = datas.get("slug")
        self.description: Optional[str] = datas.get("description")
        self.url: str = datas.get("url")
        self.playUrl: str = datas.get("playUrl")
        self.published: bool = datas.get("published")
        self.banned: bool = datas.get("banned")
        self.imagesBackgroundlarge: Optional[Any] = datas.get("imagesBackgroundlarge")
        self.imagesIncomplete: bool = datas.get("imagesIncomplete")
        self.boundsMinLat: float = float(datas.get("boundsMinLat"))
        self.boundsMinLng: float = float(datas.get("boundsMinLng"))
        self.boundsMaxLat: float = float(datas.get("boundsMaxLat"))
        self.boundsMaxLng: float = float(datas.get("boundsMaxLng"))
        self.customCoordinates: Optional[Any] = datas.get("customCoordinates")
        self.coordinateCount: int = int(datas.get("coordinateCount"))
        self.regions: Optional[Any] = datas.get("regions")
        self.creatorNick: str = datas.get("creatorNick")
        self.creatorId: str = datas.get("creatorId")
        self.createdAt: str = datas.get("createdAt")
        self.updatedAt: str = datas.get("updatedAt")
        self.numFinishedGames: int = int(datas.get("numFinishedGames"))
        self.likedByUser: Optional[Any] = datas.get("likedByUser")
        self.averageScore: int = int(datas.get("averageScore"))
        self.avatarBackground: str = datas.get("avatarBackground")
        self.avatarDecoration: str = datas.get("avatarDecoration")
        self.avatarGround: str = datas.get("avatarGround")
        self.avatarLandscape: str = datas.get("avatarLandscape")
        self.difficulty: str = datas.get("difficulty")
        self.difficultyLevel: int = int(datas.get("difficultyLevel"))
        self.highscore: Optional[Any] = datas.get("highscore")
        self.isUserMap: bool = datas.get("isUserMap")
        self.highlighted: bool = datas.get("highlighted")
        self.free: bool = datas.get("free")
        self.panoramaProvider: str = datas.get("panoramaProvider")
        self.inExplorerMode: bool = datas.get("inExplorerMode")
        self.maxErrorDistance: int = int(datas.get("maxErrorDistance"))
        self.likes: int = int(datas.get("likes"))
        self.locationSelectionMode: int = int(datas.get("locationSelectionMode"))


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
        self.gameId: str = datas.get("gameId")
        self.teams: list = datas.get("teams")
        self.rounds: list = datas.get("rounds")
        self.currentRoundNumber: int = int(datas.get("currentRoundNumber"))
        self.status: str = datas.get("status")
        self.version: int = int(datas.get("version"))
        self.optionsInitialhealth: int = int(datas.get("optionsInitialhealth"))
        self.optionsRoundtime: int = int(datas.get("optionsRoundtime"))
        self.optionsMaxroundtime: int = int(datas.get("optionsMaxroundtime"))
        self.optionsMaxnumberofrounds: int = int(datas.get("optionsMaxnumberofrounds"))
        self.optionsHealingrounds: list = datas.get("optionsHealingrounds")
        self.optionsMovementoptionsForbidmoving: bool = bool(datas.get("optionsMovementoptionsForbidmoving"))
        self.optionsMovementoptionsForbidzooming: bool = bool(datas.get("optionsMovementoptionsForbidzooming"))
        self.optionsMovementoptionsForbidrotating: bool = bool(datas.get("optionsMovementoptionsForbidrotating"))
        self.optionsMapslug: str = datas.get("optionsMapslug")
        self.optionsIsrated: bool = bool(datas.get("optionsIsrated"))
        self.optionsMapName: str = datas.get("optionsMapName")
        self.optionsMapSlug: str = datas.get("optionsMapSlug")
        self.optionsMapBoundsMinLat: float = float(datas.get("optionsMapBoundsMinLat"))
        self.optionsMapBoundsMinLng: float = float(datas.get("optionsMapBoundsMinLng"))
        self.optionsMapBoundsMaxLat: float = float(datas.get("optionsMapBoundsMaxLat"))
        self.optionsMapBoundsMaxLng: float = float(datas.get("optionsMapBoundsMaxLng"))
        self.optionsMapMaxerrordistance: int = int(datas.get("optionsMapMaxerrordistance"))
        self.optionsDuelroundoptions: list = datas.get("optionsDuelroundoptions")
        self.optionsRoundswithoutdamagemultiplier: int = int(datas.get("optionsRoundswithoutdamagemultiplier"))
        self.optionsDisablemultipliers: bool = bool(datas.get("optionsDisablemultipliers"))
        self.optionsMultiplierincrement: int = int(datas.get("optionsMultiplierincrement"))
        self.optionsDisablehealing: bool = bool(datas.get("optionsDisablehealing"))
        self.optionsIsteamduels: bool = bool(datas.get("optionsIsteamduels"))
        self.optionsGamecontextType: str = datas.get("optionsGamecontextType")
        self.optionsGamecontextId: str = datas.get("optionsGamecontextId")
        self.optionsManuallystartrounds: bool = bool(datas.get("optionsManuallystartrounds"))
        self.optionsFlashbackrounds: list = datas.get("optionsFlashbackrounds")
        self.movementOptionsForbidmoving: bool = bool(datas.get("movementOptionsForbidmoving"))
        self.movementOptionsForbidzooming: bool = bool(datas.get("movementOptionsForbidzooming"))
        self.movementOptionsForbidrotating: bool = bool(datas.get("movementOptionsForbidrotating"))
        self.mapBoundsMinLat: float = float(datas.get("mapBoundsMinLat"))
        self.mapBoundsMinLng: float = float(datas.get("mapBoundsMinLng"))
        self.mapBoundsMaxLat: float = float(datas.get("mapBoundsMaxLat"))
        self.mapBoundsMaxLng: float = float(datas.get("mapBoundsMaxLng"))
        self.initialHealth: int = int(datas.get("initialHealth"))
        self.maxNumberOfRounds: int = int(datas.get("maxNumberOfRounds"))
        self.resultIsdraw: bool = bool(datas.get("resultIsdraw"))
        self.resultWinningteamid: str = datas.get("resultWinningteamid")
        self.resultWinnerstyle: str = datas.get("resultWinnerstyle")


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
        self.divisionNumber: int = int(datas.get("divisionNumber"))
        self.divisionName: str = datas.get("divisionName")
        self.rating: int = int(datas.get("rating"))
        self.tier: str = datas.get("tier")
        self.gameModeRatingsStandardduels: int = int(datas.get("gameModeRatingsStandardduels"))
        self.gameModeRatingsNmpzduels: int = int(datas.get("gameModeRatingsNmpzduels"))
        self.gameModeRatingsNomoveduels: int = int(datas.get("gameModeRatingsNomoveduels"))
