import datetime
from typing import Any, Optional

import geoguessr_async.geo_utils as gu


class GeoguessrStats:
    def __init__(self, datas: dict) -> None:
        datas = gu.flatten_dict(datas)
        self.battleRoyaleRankRank: int = datas.get("battleRoyaleRankRank")
        self.battleRoyaleRankRating: int = datas.get("battleRoyaleRankRating")
        self.battleRoyaleRankGamesleftbeforeranked: int = datas.get("battleRoyaleRankGamesleftbeforeranked")
        self.battleRoyaleRankDivisionId: int = datas.get("battleRoyaleRankDivisionId")
        self.battleRoyaleRankDivisionDivisionid: int = datas.get("battleRoyaleRankDivisionDivisionid")
        self.battleRoyaleRankDivisionTierid: int = datas.get("battleRoyaleRankDivisionTierid")
        self.battleRoyaleRankDivisionName: str = datas.get("battleRoyaleRankDivisionName")
        self.battleRoyaleRankDivisionMinimumrank: int = datas.get("battleRoyaleRankDivisionMinimumrank")
        self.battleRoyaleDistanceNumgamesplayed: int = datas.get("battleRoyaleDistanceNumgamesplayed")
        self.battleRoyaleDistanceAvgposition: float = datas.get("battleRoyaleDistanceAvgposition")
        self.battleRoyaleDistanceNumwins: int = datas.get("battleRoyaleDistanceNumwins")
        self.battleRoyaleDistanceWinratio: float = datas.get("battleRoyaleDistanceWinratio")
        self.battleRoyaleDistanceAvgguessdistance: float = datas.get("battleRoyaleDistanceAvgguessdistance")
        self.battleRoyaleDistanceNumguesses: int = datas.get("battleRoyaleDistanceNumguesses")
        self.battleRoyaleCountryNumgamesplayed: int = datas.get("battleRoyaleCountryNumgamesplayed")
        self.battleRoyaleCountryAvgposition: float = datas.get("battleRoyaleCountryAvgposition")
        self.battleRoyaleCountryNumwins: int = datas.get("battleRoyaleCountryNumwins")
        self.battleRoyaleCountryWinratio: float = datas.get("battleRoyaleCountryWinratio")
        self.battleRoyaleCountryNumguesses: int = datas.get("battleRoyaleCountryNumguesses")
        self.battleRoyaleCountryAvgcorrectguesses: float = datas.get("battleRoyaleCountryAvgcorrectguesses")
        self.battleRoyaleMedalsMedalcountgold: int = datas.get("battleRoyaleMedalsMedalcountgold")
        self.battleRoyaleMedalsMedalcountsilver: int = datas.get("battleRoyaleMedalsMedalcountsilver")
        self.battleRoyaleMedalsMedalcountbronze: int = datas.get("battleRoyaleMedalsMedalcountbronze")
        self.competitiveCityStreaksNumgamesplayed: int = datas.get("competitiveCityStreaksNumgamesplayed")
        self.competitiveCityStreaksAvgposition: float = datas.get("competitiveCityStreaksAvgposition")
        self.competitiveCityStreaksNumwins: int = datas.get("competitiveCityStreaksNumwins")
        self.competitiveCityStreaksWinratio: float = datas.get("competitiveCityStreaksWinratio")
        self.competitiveCityStreaksNumguesses: int = datas.get("competitiveCityStreaksNumguesses")
        self.competitiveCityStreaksAvgcorrectguesses: float = datas.get("competitiveCityStreaksAvgcorrectguesses")
        self.competitiveStreaksRankRank: int = datas.get("competitiveStreaksRankRank")
        self.competitiveStreaksRankRating: int = datas.get("competitiveStreaksRankRating")
        self.competitiveStreaksRankGamesleftbeforeranked: int = datas.get("competitiveStreaksRankGamesleftbeforeranked")
        self.competitiveStreaksRankDivisionId: int = datas.get("competitiveStreaksRankDivisionId")
        self.competitiveStreaksRankDivisionDivisionid: int = datas.get("competitiveStreaksRankDivisionDivisionid")
        self.competitiveStreaksRankDivisionTierid: int = datas.get("competitiveStreaksRankDivisionTierid")
        self.competitiveStreaksRankDivisionName: str = datas.get("competitiveStreaksRankDivisionName")
        self.competitiveStreaksRankDivisionMinimumrank: int = datas.get("competitiveStreaksRankDivisionMinimumrank")
        self.competitiveStreaksMedalsMedalcountgold: int = datas.get("competitiveStreaksMedalsMedalcountgold")
        self.competitiveStreaksMedalsMedalcountsilver: int = datas.get("competitiveStreaksMedalsMedalcountsilver")
        self.competitiveStreaksMedalsMedalcountbronze: int = datas.get("competitiveStreaksMedalsMedalcountbronze")
        self.duelsNumgamesplayed: int = datas.get("duelsNumgamesplayed")
        self.duelsAvgposition: float = datas.get("duelsAvgposition")
        self.duelsNumwins: int = datas.get("duelsNumwins")
        self.duelsWinratio: float = datas.get("duelsWinratio")
        self.duelsAvgguessdistance: float = datas.get("duelsAvgguessdistance")
        self.duelsNumguesses: int = datas.get("duelsNumguesses")
        self.duelsNumflawlesswins: int = datas.get("duelsNumflawlesswins")
        self.duelsRankRank: int = datas.get("duelsRankRank")
        self.duelsRankRating: int = datas.get("duelsRankRating")
        self.duelsRankGamesleftbeforeranked: int = datas.get("duelsRankGamesleftbeforeranked")
        self.duelsRankDivisionId: int = datas.get("duelsRankDivisionId")
        self.duelsRankDivisionDivisionid: int = datas.get("duelsRankDivisionDivisionid")
        self.duelsRankDivisionTierid: int = datas.get("duelsRankDivisionTierid")
        self.duelsRankDivisionName: str = datas.get("duelsRankDivisionName")
        self.duelsRankDivisionMinimumrank: int = datas.get("duelsRankDivisionMinimumrank")
        self.duelsMedalsMedalcountgold: int = datas.get("duelsMedalsMedalcountgold")
        self.duelsMedalsMedalcountsilver: int = datas.get("duelsMedalsMedalcountsilver")
        self.duelsMedalsMedalcountbronze: int = datas.get("duelsMedalsMedalcountbronze")
        self.lifeTimeXpProgressionXp: int = datas.get("lifeTimeXpProgressionXp")
        self.lifeTimeXpProgressionCurrentlevelLevel: int = datas.get("lifeTimeXpProgressionCurrentlevelLevel")
        self.lifeTimeXpProgressionCurrentlevelXpstart: int = datas.get("lifeTimeXpProgressionCurrentlevelXpstart")
        self.lifeTimeXpProgressionNextlevelLevel: int = datas.get("lifeTimeXpProgressionNextlevelLevel")
        self.lifeTimeXpProgressionNextlevelXpstart: int = datas.get("lifeTimeXpProgressionNextlevelXpstart")
        self.lifeTimeXpProgressionCurrenttitleId: int = datas.get("lifeTimeXpProgressionCurrenttitleId")
        self.lifeTimeXpProgressionCurrenttitleTierid: int = datas.get("lifeTimeXpProgressionCurrenttitleTierid")
        self.lifeTimeXpProgressionCurrenttitleMinimumlevel: int = datas.get("lifeTimeXpProgressionCurrenttitleMinimumlevel")
        self.lifeTimeXpProgressionCurrenttitleName: str = datas.get("lifeTimeXpProgressionCurrenttitleName")
        self.totalMedalsMedalcountgold: int = datas.get("totalMedalsMedalcountgold")
        self.totalMedalsMedalcountsilver: int = datas.get("totalMedalsMedalcountsilver")
        self.totalMedalsMedalcountbronze: int = datas.get("totalMedalsMedalcountbronze")
        self.teamDuelsNumgamesplayed: int = datas.get("teamDuelsNumgamesplayed")
        self.teamDuelsNumwins: int = datas.get("teamDuelsNumwins")
        self.teamDuelsWinratio: float = datas.get("teamDuelsWinratio")
        self.perfectRounds: int = datas.get("perfectRounds")

    def __repr__(self) -> str:
        return "\n".join([f"{k} : {v}" for k, v in vars(self).items()])


class GeoguessrProfile:
    def __init__(self, datas: dict) -> None:
        datas = gu.flatten_dict(datas)
        self.nick: str = datas.get("nick")
        self.created: str = datas.get("created")
        self.isProUser: bool = datas.get("isProUser")
        self.type: str = datas.get("type")
        self.consumedTrial: bool = datas.get("consumedTrial")
        self.isVerified: bool = datas.get("isVerified")
        self.pinUrl: str = datas.get("pinUrl")
        self.pinAnchor: str = datas.get("pinAnchor")
        self.pinIsdefault: bool = datas.get("pinIsdefault")
        self.fullBodyPin: Optional[Any] = datas.get("fullBodyPin")
        self.color: int = datas.get("color")
        self.url: str = datas.get("url")
        self.id: str = datas.get("id")
        self.countryCode: str = datas.get("countryCode")
        self.brLevel: int = datas.get("brLevel")
        self.brDivision: int = datas.get("brDivision")
        self.brStreak: int = datas.get("brStreak")
        self.streakProgress: Optional[Any] = datas.get("streakProgress")
        self.explorerProgress: Optional[Any] = datas.get("explorerProgress")
        self.dailyChallengeProgress: int = datas.get("dailyChallengeProgress")
        self.progressXp: int = datas.get("progressXp")
        self.progressLevel: int = datas.get("progressLevel")
        self.progressLevelxp: int = datas.get("progressLevelxp")
        self.progressNextlevel: int = datas.get("progressNextlevel")
        self.progressNextlevelxp: int = datas.get("progressNextlevelxp")
        self.progressTitleId: int = datas.get("progressTitleId")
        self.progressTitleTierid: int = datas.get("progressTitleTierid")
        self.progressBrrankRating: int = datas.get("progressBrrankRating")
        self.progressBrrankRank: int = datas.get("progressBrrankRank")
        self.progressBrrankGamesleftbeforeranked: int = datas.get("progressBrrankGamesleftbeforeranked")
        self.progressBrrankDivisionId: int = datas.get("progressBrrankDivisionId")
        self.progressBrrankDivisionDivisionid: int = datas.get("progressBrrankDivisionDivisionid")
        self.progressBrrankDivisionTierid: int = datas.get("progressBrrankDivisionTierid")
        self.progressCsrankRating: int = datas.get("progressCsrankRating")
        self.progressCsrankRank: int = datas.get("progressCsrankRank")
        self.progressCsrankGamesleftbeforeranked: int = datas.get("progressCsrankGamesleftbeforeranked")
        self.progressCsrankDivisionId: int = datas.get("progressCsrankDivisionId")
        self.progressCsrankDivisionDivisionid: int = datas.get("progressCsrankDivisionDivisionid")
        self.progressCsrankDivisionTierid: int = datas.get("progressCsrankDivisionTierid")
        self.progressDuelsrankRating: int = datas.get("progressDuelsrankRating")
        self.progressDuelsrankRank: int = datas.get("progressDuelsrankRank")
        self.progressDuelsrankGamesleftbeforeranked: int = datas.get("progressDuelsrankGamesleftbeforeranked")
        self.progressDuelsrankDivisionId: int = datas.get("progressDuelsrankDivisionId")
        self.progressDuelsrankDivisionDivisionid: int = datas.get("progressDuelsrankDivisionDivisionid")
        self.progressDuelsrankDivisionTierid: int = datas.get("progressDuelsrankDivisionTierid")
        self.progressCompetitionmedalsBronze: int = datas.get("progressCompetitionmedalsBronze")
        self.progressCompetitionmedalsSilver: int = datas.get("progressCompetitionmedalsSilver")
        self.progressCompetitionmedalsGold: int = datas.get("progressCompetitionmedalsGold")
        self.progressCompetitionmedalsPlatinum: int = datas.get("progressCompetitionmedalsPlatinum")
        self.competitiveElo: int = datas.get("competitiveElo")
        self.competitiveRating: int = datas.get("competitiveRating")
        self.competitiveLastratingchange: int = datas.get("competitiveLastratingchange")
        self.competitiveDivisionType: int = datas.get("competitiveDivisionType")
        self.competitiveDivisionStartrating: int = datas.get("competitiveDivisionStartrating")
        self.competitiveDivisionEndrating: int = datas.get("competitiveDivisionEndrating")
        self.lastNameChange: str = datas.get("lastNameChange")
        self.isBanned: bool = datas.get("isBanned")
        self.nameChangeAvailableAt: Optional[datetime.datetime] = datas.get("nameChangeAvailableAt")
        self.avatarFullbodypath: Optional[str] = datas.get("avatarFullbodypath")
        self.isBotUser: bool = datas.get("isBotUser")
        self.suspendedUntil: Optional[datetime.datetime] = datas.get("suspendedUntil")
        self.wallet: int = datas.get("wallet")
        self.Flair: int = datas.get("flair")
        self.isCreator: bool = datas.get("isCreator")
        self.stats: Optional[GeoguessrStats] = None

    def add_stats(self, stats: GeoguessrStats) -> None:
        self.stats = stats

    def __repr__(self) -> str:
        return "\n".join([f"{k} : {v}" for k, v in vars(self).items()])


class GeoguessrChallenge:
    def __init__(self, datas: dict) -> None:
        datas = gu.flatten_dict(datas)
        self.challengeToken: str = datas.get("challengeToken")
        self.challengeMapslug: str = datas.get("challengeMapslug")
        self.challengeRoundcount: int = datas.get("challengeRoundcount")
        self.challengeTimelimit: int = datas.get("challengeTimelimit")
        self.challengeForbidmoving: bool = datas.get("challengeForbidmoving")
        self.challengeForbidzooming: bool = datas.get("challengeForbidzooming")
        self.challengeForbidrotating: bool = datas.get("challengeForbidrotating")
        self.challengeNumberofparticipants: int = datas.get("challengeNumberofparticipants")
        self.challengeGamemode: str = datas.get("challengeGamemode")
        self.challengeChallengetype: int = datas.get("challengeChallengetype")
        self.challengeStreaktype: str = datas.get("challengeStreaktype")
        self.challengeStr_timelimit: str = datas.get("challengeStr_timelimit")
        self.mapId: str = datas.get("mapId")
        self.creatorNick: str = datas.get("creatorNick")
        self.creatorId: str = datas.get("creatorId")
        self.mode: str = datas.get("mode")

    def __repr__(self) -> str:
        return "\n".join([f"{k} : {v}" for k, v in vars(self).items()])


class GeoguessrScore:
    def __init__(self, datas: dict) -> None:
        datas = gu.flatten_dict(datas)
        self.gameToken: str = datas.get("gameToken")
        self.playerName: str = datas.get("playerName")
        self.userId: str = datas.get("userId")
        self.totalScore: int = datas.get("totalScore")
        self.isLeader: bool = datas.get("isLeader")
        self.pinUrl: str = datas.get("pinUrl")
        self.gameType: str = datas.get("gameType")
        self.gameMode: str = datas.get("gameMode")
        self.gameState: str = datas.get("gameState")
        self.gameRoundcount: int = datas.get("gameRoundcount")
        self.gameStreaktype: str = datas.get("gameStreaktype")
        self.gameMap: str = datas.get("gameMap")
        self.gameMapname: str = datas.get("gameMapname")
        self.gamePanoramaprovider: int = datas.get("gamePanoramaprovider")
        self.gameBoundsMinLat: float = datas.get("gameBoundsMinLat")
        self.gameBoundsMinLng: float = datas.get("gameBoundsMinLng")
        self.gameBoundsMaxLat: float = datas.get("gameBoundsMaxLat")
        self.gameBoundsMaxLng: float = datas.get("gameBoundsMaxLng")
        self.gameRound: int = datas.get("gameRound")
        self.gameRoundsLats: list[float] = [
            round["lat"] for round in datas.get("gameRounds") if round != None
        ]
        self.gameRoundsLngs: list[float] = [
            round["lng"] for round in datas.get("gameRounds") if round != None
        ]
        self.gameRoundsPanoIds: list[str] = [
            round["panoId"] for round in datas.get("gameRounds") if round != None
        ]
        self.gameRoundsHeadings: list[float] = [
            round["heading"] for round in datas.get("gameRounds") if round != None
        ]
        self.gameRoundsPitches: list[float] = [
            round["pitch"] for round in datas.get("gameRounds") if round != None
        ]
        self.gameRoundsZoomes: list[float] = [
            round["zoom"] for round in datas.get("gameRounds") if round != None
        ]
        self.gameRoundsStreakLocationCodes: list[str] = [
            round["streakLocationCode"] for round in datas.get("gameRounds") if round != None
        ]
        self.gameRoundsStartTime: list[datetime.datetime] = [
            round["startTime"] for round in datas.get("gameRounds") if round != None
        ]
        self.gamePlayerTotalscoreAmount: str = datas.get("gamePlayerTotalscoreAmount")
        self.gamePlayerTotalscoreUnit: str = datas.get("gamePlayerTotalscoreUnit")
        self.gamePlayerTotalscorePercentage: float = datas.get("gamePlayerTotalscorePercentage")
        self.gamePlayerTotalDistanceMetersAmount: str = datas.get("gamePlayerTotaldistanceMetersAmount")
        self.gamePlayerTotalDistanceMetersUnit: str = datas.get("gamePlayerTotaldistanceMetersUnit")
        self.gamePlayerTotalDistanceMilesAmount: str = datas.get("gamePlayerTotaldistanceMilesAmount")
        self.gamePlayerTotalDistanceMilesUnit: str = datas.get("gamePlayerTotaldistanceMilesUnit")
        self.gamePlayerTotalDistanceInMeters: float = datas.get("gamePlayerTotaldistanceinmeters")
        self.gamePlayerTotaltime: int = datas.get("gamePlayerTotaltime")
        self.gamePlayerTotalstreak: int = datas.get("gamePlayerTotalstreak")
        self.gamePlayerGuessesLats: list[float] = [
            guess["lat"] for guess in datas.get("gamePlayerGuesses") if guess != None
        ]
        self.gamePlayerGuessesLngs: list[float] = [
            guess["lng"] for guess in datas.get("gamePlayerGuesses") if guess != None
        ]
        self.gamePlayerGuessesTimedOut: list[bool] = [
            guess["timedOut"] for guess in datas.get("gamePlayerGuesses") if guess != None
        ]
        self.gamePlayerGuessesTimedOutWithGuess: list[bool] = [
            guess["timedOutWithGuess"] for guess in datas.get("gamePlayerGuesses") if guess != None
        ]
        self.gamePlayerGuessesSkippedRound: list[bool] = [
            guess["skippedRound"] for guess in datas.get("gamePlayerGuesses") if guess != None
        ]
        self.gamePlayerGuessesRoundScoreInPercentage: list[float] = [
            guess["roundScoreInPercentage"] for guess in datas.get("gamePlayerGuesses") if guess != None
        ]
        self.gamePlayerGuessesRoundScoreInPoints: list[int] = [
            guess["roundScoreInPoints"] for guess in datas.get("gamePlayerGuesses") if guess != None
        ]
        self.gamePlayerGuessesDistanceInMeters: list[float] = [
            guess["distanceInMeters"] for guess in datas.get("gamePlayerGuesses") if guess != None
        ]
        self.gamePlayerGuessesStreakLocationCode: list[str] = [
            guess["streakLocationCode"] for guess in datas.get("gamePlayerGuesses") if guess != None
        ]
        self.gamePlayerGuessesTime: list[int] = [
            guess["time"] for guess in datas.get("gamePlayerGuesses") if guess != None
        ]
        self.gamePlayerId: str = datas.get("gamePlayerId")
        self.gamePlayerNick: str = datas.get("gamePlayerNick")
        self.gameProgresschangeAwardedXp: int = datas.get("gameProgresschangeAwardedxpTotalawardedxp")

    def __repr__(self) -> str:
        return "\n".join([f"{k} : {v}" for k, v in vars(self).items()])


class GeoguessrMap:
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
        self.boundsMinLat: float = datas.get("boundsMinLat")
        self.boundsMinLng: float = datas.get("boundsMinLng")
        self.boundsMaxLat: float = datas.get("boundsMaxLat")
        self.boundsMaxLng: float = datas.get("boundsMaxLng")
        self.customCoordinates: Optional[Any] = datas.get("customCoordinates")
        self.coordinateCount: int = datas.get("coordinateCount")
        self.regions: Optional[Any] = datas.get("regions")
        self.creatorNick: str = datas.get("creatorNick")
        self.creatorId: str = datas.get("creatorId")
        self.createdAt: str = datas.get("createdAt")
        self.updatedAt: str = datas.get("updatedAt")
        self.numFinishedGames: int = datas.get("numFinishedGames")
        self.likedByUser: Optional[Any] = datas.get("likedByUser")
        self.averageScore: int = datas.get("averageScore")
        self.avatarBackground: str = datas.get("avatarBackground")
        self.avatarDecoration: str = datas.get("avatarDecoration")
        self.avatarGround: str = datas.get("avatarGround")
        self.avatarLandscape: str = datas.get("avatarLandscape")
        self.difficulty: str = datas.get("difficulty")
        self.difficultyLevel: int = datas.get("difficultyLevel")
        self.highscore: Optional[Any] = datas.get("highscore")
        self.isUserMap: bool = datas.get("isUserMap")
        self.highlighted: bool = datas.get("highlighted")
        self.free: bool = datas.get("free")
        self.panoramaProvider: str = datas.get("panoramaProvider")
        self.inExplorerMode: bool = datas.get("inExplorerMode")
        self.maxErrorDistance: int = datas.get("maxErrorDistance")
        self.likes: int = datas.get("likes")
        self.locationSelectionMode: int = datas.get("locationSelectionMode")

    def __repr__(self) -> str:
        return "\n".join([f"{k} : {v}" for k, v in vars(self).items()])

class GeoguessrDuel:
    def __init__(self, datas) -> None:
        datas = gu.flatten_dict(datas)
        self.gameId: str = datas.get("gameId")
        self.teams: list = datas.get("teams")
        self.rounds: list = datas.get("rounds")
        self.currentRoundNumber: int = datas.get("currentRoundNumber")
        self.status: str = datas.get("status")
        self.version: int = datas.get("version")
        self.optionsInitialhealth: int = datas.get("optionsInitialhealth")
        self.optionsRoundtime: int = datas.get("optionsRoundtime")
        self.optionsMaxroundtime: int = datas.get("optionsMaxroundtime")
        self.optionsMaxnumberofrounds: int = datas.get("optionsMaxnumberofrounds")
        self.optionsHealingrounds: list = datas.get("optionsHealingrounds")
        self.optionsMovementoptionsForbidmoving: bool = datas.get("optionsMovementoptionsForbidmoving")
        self.optionsMovementoptionsForbidzooming: bool = datas.get("optionsMovementoptionsForbidzooming")
        self.optionsMovementoptionsForbidrotating: bool = datas.get("optionsMovementoptionsForbidrotating")
        self.optionsMapslug: str = datas.get("optionsMapslug")
        self.optionsIsrated: bool = datas.get("optionsIsrated")
        self.optionsMapName: str = datas.get("optionsMapName")
        self.optionsMapSlug: str = datas.get("optionsMapSlug")
        self.optionsMapBoundsMinLat: float = datas.get("optionsMapBoundsMinLat")
        self.optionsMapBoundsMinLng: float = datas.get("optionsMapBoundsMinLng")
        self.optionsMapBoundsMaxLat: float = datas.get("optionsMapBoundsMaxLat")
        self.optionsMapBoundsMaxLng: float = datas.get("optionsMapBoundsMaxLng")
        self.optionsMapMaxerrordistance: int = datas.get("optionsMapMaxerrordistance")
        self.optionsDuelroundoptions: list = datas.get("optionsDuelroundoptions")
        self.optionsRoundswithoutdamagemultiplier: int = datas.get("optionsRoundswithoutdamagemultiplier")
        self.optionsDisablemultipliers: bool = datas.get("optionsDisablemultipliers")
        self.optionsMultiplierincrement: int = datas.get("optionsMultiplierincrement")
        self.optionsDisablehealing: bool = datas.get("optionsDisablehealing")
        self.optionsIsteamduels: bool = datas.get("optionsIsteamduels")
        self.optionsGamecontextType: str = datas.get("optionsGamecontextType")
        self.optionsGamecontextId: str = datas.get("optionsGamecontextId")
        self.optionsManuallystartrounds: bool = datas.get("optionsManuallystartrounds")
        self.optionsFlashbackrounds: list = datas.get("optionsFlashbackrounds")
        self.movementOptionsForbidmoving: bool = datas.get("movementOptionsForbidmoving")
        self.movementOptionsForbidzooming: bool = datas.get("movementOptionsForbidzooming")
        self.movementOptionsForbidrotating: bool = datas.get("movementOptionsForbidrotating")
        self.mapBoundsMinLat: float = datas.get("mapBoundsMinLat")
        self.mapBoundsMinLng: float = datas.get("mapBoundsMinLng")
        self.mapBoundsMaxLat: float = datas.get("mapBoundsMaxLat")
        self.mapBoundsMaxLng: float = datas.get("mapBoundsMaxLng")
        self.initialHealth: int = datas.get("initialHealth")
        self.maxNumberOfRounds: int = datas.get("maxNumberOfRounds")
        self.resultIsdraw: bool = datas.get("resultIsdraw")
        self.resultWinningteamid: str = datas.get("resultWinningteamid")
        self.resultWinnerstyle: str = datas.get("resultWinnerstyle")
    
    def __repr__(self) -> str:
        return "\n".join([f"{k} : {v}" for k, v in vars(self).items()])
    
class GeoguessrActivities:
    def __init__(self, entries) -> None:
        self.entries = entries
        
    def __repr__(self) -> str:
        return "\n".join([f"{k} : {v}" for k, v in vars(self).items()])