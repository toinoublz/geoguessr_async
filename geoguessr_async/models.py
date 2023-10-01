import datetime
from typing import Any, Optional

import geoguessr_async.geo_utils as gu


class GeoguessrStats:
    def __init__(self, datas: dict) -> None:
        datas = gu.flatten_dict(datas)
        self.battleRoyaleRankRank: int = datas["battleRoyaleRankRank"]
        self.battleRoyaleRankRating: int = datas["battleRoyaleRankRating"]
        self.battleRoyaleRankGamesleftbeforeranked: int = datas[
            "battleRoyaleRankGamesleftbeforeranked"
        ]
        self.battleRoyaleRankDivisionId: int = datas["battleRoyaleRankDivisionId"]
        self.battleRoyaleRankDivisionDivisionid: int = datas[
            "battleRoyaleRankDivisionDivisionid"
        ]
        self.battleRoyaleRankDivisionTierid: int = datas[
            "battleRoyaleRankDivisionTierid"
        ]
        self.battleRoyaleRankDivisionName: str = datas["battleRoyaleRankDivisionName"]
        self.battleRoyaleRankDivisionMinimumrank: int = datas[
            "battleRoyaleRankDivisionMinimumrank"
        ]
        self.battleRoyaleDistanceNumgamesplayed: int = datas[
            "battleRoyaleDistanceNumgamesplayed"
        ]
        self.battleRoyaleDistanceAvgposition: float = datas[
            "battleRoyaleDistanceAvgposition"
        ]
        self.battleRoyaleDistanceNumwins: int = datas["battleRoyaleDistanceNumwins"]
        self.battleRoyaleDistanceWinratio: float = datas["battleRoyaleDistanceWinratio"]
        self.battleRoyaleDistanceAvgguessdistance: float = datas[
            "battleRoyaleDistanceAvgguessdistance"
        ]
        self.battleRoyaleDistanceNumguesses: int = datas[
            "battleRoyaleDistanceNumguesses"
        ]
        self.battleRoyaleDistanceStreak: int = datas["battleRoyaleDistanceStreak"]
        self.battleRoyaleCountryNumgamesplayed: int = datas[
            "battleRoyaleCountryNumgamesplayed"
        ]
        self.battleRoyaleCountryAvgposition: float = datas[
            "battleRoyaleCountryAvgposition"
        ]
        self.battleRoyaleCountryNumwins: int = datas["battleRoyaleCountryNumwins"]
        self.battleRoyaleCountryWinratio: float = datas["battleRoyaleCountryWinratio"]
        self.battleRoyaleCountryNumguesses: int = datas["battleRoyaleCountryNumguesses"]
        self.battleRoyaleCountryAvgcorrectguesses: float = datas[
            "battleRoyaleCountryAvgcorrectguesses"
        ]
        self.battleRoyaleCountryStreak: int = datas["battleRoyaleCountryStreak"]
        self.battleRoyaleMedalsMedalcountgold: int = datas[
            "battleRoyaleMedalsMedalcountgold"
        ]
        self.battleRoyaleMedalsMedalcountsilver: int = datas[
            "battleRoyaleMedalsMedalcountsilver"
        ]
        self.battleRoyaleMedalsMedalcountbronze: int = datas[
            "battleRoyaleMedalsMedalcountbronze"
        ]
        self.competitiveCityStreaksNumgamesplayed: int = datas[
            "competitiveCityStreaksNumgamesplayed"
        ]
        self.competitiveCityStreaksAvgposition: float = datas[
            "competitiveCityStreaksAvgposition"
        ]
        self.competitiveCityStreaksNumwins: int = datas["competitiveCityStreaksNumwins"]
        self.competitiveCityStreaksWinratio: float = datas[
            "competitiveCityStreaksWinratio"
        ]
        self.competitiveCityStreaksNumguesses: int = datas[
            "competitiveCityStreaksNumguesses"
        ]
        self.competitiveCityStreaksAvgcorrectguesses: float = datas[
            "competitiveCityStreaksAvgcorrectguesses"
        ]
        self.competitiveCityStreaksStreak: int = datas["competitiveCityStreaksStreak"]
        self.competitiveStreaksRankRank: int = datas["competitiveStreaksRankRank"]
        self.competitiveStreaksRankRating: int = datas["competitiveStreaksRankRating"]
        self.competitiveStreaksRankGamesleftbeforeranked: int = datas[
            "competitiveStreaksRankGamesleftbeforeranked"
        ]
        self.competitiveStreaksRankDivisionId: int = datas[
            "competitiveStreaksRankDivisionId"
        ]
        self.competitiveStreaksRankDivisionDivisionid: int = datas[
            "competitiveStreaksRankDivisionDivisionid"
        ]
        self.competitiveStreaksRankDivisionTierid: int = datas[
            "competitiveStreaksRankDivisionTierid"
        ]
        self.competitiveStreaksRankDivisionName: str = datas[
            "competitiveStreaksRankDivisionName"
        ]
        self.competitiveStreaksRankDivisionMinimumrank: int = datas[
            "competitiveStreaksRankDivisionMinimumrank"
        ]
        self.competitiveStreaksMedalsMedalcountgold: int = datas[
            "competitiveStreaksMedalsMedalcountgold"
        ]
        self.competitiveStreaksMedalsMedalcountsilver: int = datas[
            "competitiveStreaksMedalsMedalcountsilver"
        ]
        self.competitiveStreaksMedalsMedalcountbronze: int = datas[
            "competitiveStreaksMedalsMedalcountbronze"
        ]
        self.duelsNumgamesplayed: int = datas["duelsNumgamesplayed"]
        self.duelsAvgposition: float = datas["duelsAvgposition"]
        self.duelsNumwins: int = datas["duelsNumwins"]
        self.duelsWinratio: float = datas["duelsWinratio"]
        self.duelsAvgguessdistance: float = datas["duelsAvgguessdistance"]
        self.duelsNumguesses: int = datas["duelsNumguesses"]
        self.duelsNumflawlesswins: int = datas["duelsNumflawlesswins"]
        self.duelsStreak: int = datas["duelsStreak"]
        self.duelsRankRank: int = datas["duelsRankRank"]
        self.duelsRankRating: int = datas["duelsRankRating"]
        self.duelsRankGamesleftbeforeranked: int = datas[
            "duelsRankGamesleftbeforeranked"
        ]
        self.duelsRankDivisionId: int = datas["duelsRankDivisionId"]
        self.duelsRankDivisionDivisionid: int = datas["duelsRankDivisionDivisionid"]
        self.duelsRankDivisionTierid: int = datas["duelsRankDivisionTierid"]
        self.duelsRankDivisionName: str = datas["duelsRankDivisionName"]
        self.duelsRankDivisionMinimumrank: int = datas["duelsRankDivisionMinimumrank"]
        self.duelsMedalsMedalcountgold: int = datas["duelsMedalsMedalcountgold"]
        self.duelsMedalsMedalcountsilver: int = datas["duelsMedalsMedalcountsilver"]
        self.duelsMedalsMedalcountbronze: int = datas["duelsMedalsMedalcountbronze"]
        self.lifeTimeXpProgressionXp: int = datas["lifeTimeXpProgressionXp"]
        self.lifeTimeXpProgressionCurrentlevelLevel: int = datas[
            "lifeTimeXpProgressionCurrentlevelLevel"
        ]
        self.lifeTimeXpProgressionCurrentlevelXpstart: int = datas[
            "lifeTimeXpProgressionCurrentlevelXpstart"
        ]
        self.lifeTimeXpProgressionNextlevelLevel: int = datas[
            "lifeTimeXpProgressionNextlevelLevel"
        ]
        self.lifeTimeXpProgressionNextlevelXpstart: int = datas[
            "lifeTimeXpProgressionNextlevelXpstart"
        ]
        self.lifeTimeXpProgressionCurrenttitleId: int = datas[
            "lifeTimeXpProgressionCurrenttitleId"
        ]
        self.lifeTimeXpProgressionCurrenttitleTierid: int = datas[
            "lifeTimeXpProgressionCurrenttitleTierid"
        ]
        self.lifeTimeXpProgressionCurrenttitleMinimumlevel: int = datas[
            "lifeTimeXpProgressionCurrenttitleMinimumlevel"
        ]
        self.lifeTimeXpProgressionCurrenttitleName: str = datas[
            "lifeTimeXpProgressionCurrenttitleName"
        ]
        self.totalMedalsMedalcountgold: int = datas["totalMedalsMedalcountgold"]
        self.totalMedalsMedalcountsilver: int = datas["totalMedalsMedalcountsilver"]
        self.totalMedalsMedalcountbronze: int = datas["totalMedalsMedalcountbronze"]
        self.teamDuelsNumgamesplayed: int = datas["teamDuelsNumgamesplayed"]
        self.teamDuelsNumwins: int = datas["teamDuelsNumwins"]
        self.teamDuelsWinratio: float = datas["teamDuelsWinratio"]
        self.perfectRounds: int = datas["perfectRounds"]

    def __repr__(self) -> str:
        return "\n".join([f"{k} : {v}" for k, v in vars(self).items()])


class GeoguessrProfile:
    def __init__(self, datas: dict) -> None:
        datas = gu.flatten_dict(datas)
        self.nick: str = datas["nick"]
        self.created: str = datas["created"]
        self.isProUser: bool = datas["isProUser"]
        self.type: str = datas["type"]
        self.consumedTrial: bool = datas["consumedTrial"]
        self.isVerified: bool = datas["isVerified"]
        self.pinUrl: str = datas["pinUrl"]
        self.pinAnchor: str = datas["pinAnchor"]
        self.pinIsdefault: bool = datas["pinIsdefault"]
        self.fullBodyPin: Optional[Any] = datas["fullBodyPin"]
        self.color: int = datas["color"]
        self.url: str = datas["url"]
        self.id: str = datas["id"]
        self.countryCode: str = datas["countryCode"]
        self.onboardingTutorialtoken: Optional[str] = datas["onboardingTutorialtoken"]
        self.onboardingTutorialstate: str = datas["onboardingTutorialstate"]
        self.brLevel: int = datas["brLevel"]
        self.brDivision: int = datas["brDivision"]
        self.brStreak: int = datas["brStreak"]
        self.streakProgress: Optional[Any] = datas["streakProgress"]
        self.explorerProgress: Optional[Any] = datas["explorerProgress"]
        self.dailyChallengeProgress: int = datas["dailyChallengeProgress"]
        self.progressXp: int = datas["progressXp"]
        self.progressLevel: int = datas["progressLevel"]
        self.progressLevelxp: int = datas["progressLevelxp"]
        self.progressNextlevel: int = datas["progressNextlevel"]
        self.progressNextlevelxp: int = datas["progressNextlevelxp"]
        self.progressTitleId: int = datas["progressTitleId"]
        self.progressTitleTierid: int = datas["progressTitleTierid"]
        self.progressBrrankRating: int = datas["progressBrrankRating"]
        self.progressBrrankRank: int = datas["progressBrrankRank"]
        self.progressBrrankGamesleftbeforeranked: int = datas[
            "progressBrrankGamesleftbeforeranked"
        ]
        self.progressBrrankDivisionId: int = datas["progressBrrankDivisionId"]
        self.progressBrrankDivisionDivisionid: int = datas[
            "progressBrrankDivisionDivisionid"
        ]
        self.progressBrrankDivisionTierid: int = datas["progressBrrankDivisionTierid"]
        self.progressCsrankRating: int = datas["progressCsrankRating"]
        self.progressCsrankRank: int = datas["progressCsrankRank"]
        self.progressCsrankGamesleftbeforeranked: int = datas[
            "progressCsrankGamesleftbeforeranked"
        ]
        self.progressCsrankDivisionId: int = datas["progressCsrankDivisionId"]
        self.progressCsrankDivisionDivisionid: int = datas[
            "progressCsrankDivisionDivisionid"
        ]
        self.progressCsrankDivisionTierid: int = datas["progressCsrankDivisionTierid"]
        self.progressDuelsrankRating: int = datas["progressDuelsrankRating"]
        self.progressDuelsrankRank: int = datas["progressDuelsrankRank"]
        self.progressDuelsrankGamesleftbeforeranked: int = datas[
            "progressDuelsrankGamesleftbeforeranked"
        ]
        self.progressDuelsrankDivisionId: int = datas["progressDuelsrankDivisionId"]
        self.progressDuelsrankDivisionDivisionid: int = datas[
            "progressDuelsrankDivisionDivisionid"
        ]
        self.progressDuelsrankDivisionTierid: int = datas[
            "progressDuelsrankDivisionTierid"
        ]
        self.progressCompetitionmedalsBronze: int = datas[
            "progressCompetitionmedalsBronze"
        ]
        self.progressCompetitionmedalsSilver: int = datas[
            "progressCompetitionmedalsSilver"
        ]
        self.progressCompetitionmedalsGold: int = datas["progressCompetitionmedalsGold"]
        self.progressCompetitionmedalsPlatinum: int = datas[
            "progressCompetitionmedalsPlatinum"
        ]
        self.progressStreaksBrcountries: int = datas["progressStreaksBrcountries"]
        self.progressStreaksBrdistance: int = datas["progressStreaksBrdistance"]
        self.progressStreaksCscities: int = datas["progressStreaksCscities"]
        self.progressStreaksDuels: int = datas["progressStreaksDuels"]
        self.competitiveElo: int = datas["competitiveElo"]
        self.competitiveRating: int = datas["competitiveRating"]
        self.competitiveLastratingchange: int = datas["competitiveLastratingchange"]
        self.competitiveDivisionType: int = datas["competitiveDivisionType"]
        self.competitiveDivisionStartrating: int = datas[
            "competitiveDivisionStartrating"
        ]
        self.competitiveDivisionEndrating: int = datas["competitiveDivisionEndrating"]
        self.lastNameChange: str = datas["lastNameChange"]
        self.isBanned: bool = datas["isBanned"]
        self.nameChangeAvailableAt: Optional[datetime.datetime] = datas[
            "nameChangeAvailableAt"
        ]
        self.avatarFullbodypath: Optional[str] = datas["avatarFullbodypath"]
        self.isBotUser: bool = datas["isBotUser"]
        self.suspendedUntil: Optional[datetime.datetime] = datas["suspendedUntil"]
        self.walletCoins: int = datas["walletCoins"]
        self.Flair: int = datas["flair"]
        self.stats: Optional[GeoguessrStats] = None

    def add_stats(self, stats: GeoguessrStats) -> None:
        self.stats = stats

    def __repr__(self) -> str:
        return "\n".join([f"{k} : {v}" for k, v in vars(self).items()])


class GeoguessrChallenge:
    def __init__(self, datas: dict) -> None:
        datas = gu.flatten_dict(datas)
        self.challengeToken: str = datas["challengeToken"]
        self.challengeMapslug: str = datas["challengeMapslug"]
        self.challengeRoundcount: int = datas["challengeRoundcount"]
        self.challengeTimelimit: int = datas["challengeTimelimit"]
        self.challengeForbidmoving: bool = datas["challengeForbidmoving"]
        self.challengeForbidzooming: bool = datas["challengeForbidzooming"]
        self.challengeForbidrotating: bool = datas["challengeForbidrotating"]
        self.challengeNumberofparticipants: int = datas["challengeNumberofparticipants"]
        self.challengeGamemode: str = datas["challengeGamemode"]
        self.challengeChallengetype: int = datas["challengeChallengetype"]
        self.challengeStreaktype: str = datas["challengeStreaktype"]
        self.challengeStr_timelimit: str = datas["challengeStr_timelimit"]
        self.mapId: str = datas["mapId"]
        self.creatorNick: str = datas["creatorNick"]
        self.creatorId: str = datas["creatorId"]
        self.mode: str = datas["mode"]

    def __repr__(self) -> str:
        return "\n".join([f"{k} : {v}" for k, v in vars(self).items()])


class GeoguessrScore:
    def __init__(self, datas: dict) -> None:
        datas = gu.flatten_dict(datas)
        self.gameToken: str = datas["gameToken"]
        self.playerName: str = datas["playerName"]
        self.userId: str = datas["userId"]
        self.totalScore: int = datas["totalScore"]
        self.isLeader: bool = datas["isLeader"]
        self.pinUrl: str = datas["pinUrl"]
        self.gameType: str = datas["gameType"]
        self.gameMode: str = datas["gameMode"]
        self.gameState: str = datas["gameState"]
        self.gameRoundcount: int = datas["gameRoundcount"]
        self.gameStreaktype: str = datas["gameStreaktype"]
        self.gameMap: str = datas["gameMap"]
        self.gameMapname: str = datas["gameMapname"]
        self.gamePanoramaprovider: int = datas["gamePanoramaprovider"]
        self.gameBoundsMinLat: float = datas["gameBoundsMinLat"]
        self.gameBoundsMinLng: float = datas["gameBoundsMinLng"]
        self.gameBoundsMaxLat: float = datas["gameBoundsMaxLat"]
        self.gameBoundsMaxLng: float = datas["gameBoundsMaxLng"]
        self.gameRound: int = datas["gameRound"]
        self.gameRoundsLats: list[float] = [
            round["lat"] for round in datas["gameRounds"]
        ]
        self.gameRoundsLngs: list[float] = [
            round["lng"] for round in datas["gameRounds"]
        ]
        self.gameRoundsPanoIds: list[str] = [
            round["panoId"] for round in datas["gameRounds"]
        ]
        self.gameRoundsHeadings: list[float] = [
            round["heading"] for round in datas["gameRounds"]
        ]
        self.gameRoundsPitches: list[float] = [
            round["pitch"] for round in datas["gameRounds"]
        ]
        self.gameRoundsZoomes: list[float] = [
            round["zoom"] for round in datas["gameRounds"]
        ]
        self.gameRoundsStreakLocationCodes: list[str] = [
            round["streakLocationCode"] for round in datas["gameRounds"]
        ]
        self.gameRoundsStartTime: list[datetime.datetime] = [
            round["startTime"] for round in datas["gameRounds"]
        ]
        self.gamePlayerTotalscoreAmount: str = datas["gamePlayerTotalscoreAmount"]
        self.gamePlayerTotalscoreUnit: str = datas["gamePlayerTotalscoreUnit"]
        self.gamePlayerTotalscorePercentage: float = datas[
            "gamePlayerTotalscorePercentage"
        ]
        self.gamePlayerTotalDistanceMetersAmount: str = datas[
            "gamePlayerTotaldistanceMetersAmount"
        ]
        self.gamePlayerTotalDistanceMetersUnit: str = datas[
            "gamePlayerTotaldistanceMetersUnit"
        ]
        self.gamePlayerTotalDistanceMilesAmount: str = datas[
            "gamePlayerTotaldistanceMilesAmount"
        ]
        self.gamePlayerTotalDistanceMilesUnit: str = datas[
            "gamePlayerTotaldistanceMilesUnit"
        ]
        self.gamePlayerTotalDistanceInMeters: float = datas[
            "gamePlayerTotaldistanceinmeters"
        ]
        self.gamePlayerTotaltime: int = datas["gamePlayerTotaltime"]
        self.gamePlayerTotalstreak: int = datas["gamePlayerTotalstreak"]
        self.gamePlayerGuessesLats: list[float] = [
            guess["lat"] for guess in datas["gamePlayerGuesses"]
        ]
        self.gamePlayerGuessesLngs: list[float] = [
            guess["lng"] for guess in datas["gamePlayerGuesses"]
        ]
        self.gamePlayerGuessesTimedOut: list[bool] = [
            guess["timedOut"] for guess in datas["gamePlayerGuesses"]
        ]
        self.gamePlayerGuessesTimedOutWithGuess: list[bool] = [
            guess["timedOutWithGuess"] for guess in datas["gamePlayerGuesses"]
        ]
        self.gamePlayerGuessesSkippedRound: list[bool] = [
            guess["skippedRound"] for guess in datas["gamePlayerGuesses"]
        ]
        self.gamePlayerGuessesRoundScoreInPercentage: list[float] = [
            guess["roundScoreInPercentage"] for guess in datas["gamePlayerGuesses"]
        ]
        self.gamePlayerGuessesRoundScoreInPoints: list[int] = [
            guess["roundScoreInPoints"] for guess in datas["gamePlayerGuesses"]
        ]
        self.gamePlayerGuessesDistanceInMeters: list[float] = [
            guess["distanceInMeters"] for guess in datas["gamePlayerGuesses"]
        ]
        self.gamePlayerGuessesStreakLocationCode: list[str] = [
            guess["streakLocationCode"] for guess in datas["gamePlayerGuesses"]
        ]
        self.gamePlayerGuessesTime: list[int] = [
            guess["time"] for guess in datas["gamePlayerGuesses"]
        ]
        self.gamePlayerId: str = datas["gamePlayerId"]
        self.gamePlayerNick: str = datas["gamePlayerNick"]
        self.gameProgresschangeAwardedXp: int = datas[
            "gameProgresschangeAwardedxpTotalawardedxp"
        ]

    def __repr__(self) -> str:
        return "\n".join([f"{k} : {v}" for k, v in vars(self).items()])


class GeoguessrMap:
    def __init__(self, datas: dict) -> None:
        datas = gu.flatten_dict(datas)
        self.id: str = datas["id"]
        self.name: str = datas["name"]
        self.slug: str = datas["slug"]
        self.description: Optional[str] = datas["description"]
        self.url: str = datas["url"]
        self.playUrl: str = datas["playUrl"]
        self.published: bool = datas["published"]
        self.banned: bool = datas["banned"]
        self.imagesBackgroundlarge: Optional[Any] = datas["imagesBackgroundlarge"]
        self.imagesIncomplete: bool = datas["imagesIncomplete"]
        self.boundsMinLat: float = datas["boundsMinLat"]
        self.boundsMinLng: float = datas["boundsMinLng"]
        self.boundsMaxLat: float = datas["boundsMaxLat"]
        self.boundsMaxLng: float = datas["boundsMaxLng"]
        self.customCoordinates: Optional[Any] = datas["customCoordinates"]
        self.coordinateCount: int = datas["coordinateCount"]
        self.regions: Optional[Any] = datas["regions"]
        self.creatorNick: str = datas["creatorNick"]
        self.creatorId: str = datas["creatorId"]
        self.createdAt: str = datas["createdAt"]
        self.updatedAt: str = datas["updatedAt"]
        self.numFinishedGames: int = datas["numFinishedGames"]
        self.likedByUser: Optional[Any] = datas["likedByUser"]
        self.averageScore: int = datas["averageScore"]
        self.avatarBackground: str = datas["avatarBackground"]
        self.avatarDecoration: str = datas["avatarDecoration"]
        self.avatarGround: str = datas["avatarGround"]
        self.avatarLandscape: str = datas["avatarLandscape"]
        self.difficulty: str = datas["difficulty"]
        self.difficultyLevel: int = datas["difficultyLevel"]
        self.highscore: Optional[Any] = datas["highscore"]
        self.isUserMap: bool = datas["isUserMap"]
        self.highlighted: bool = datas["highlighted"]
        self.free: bool = datas["free"]
        self.panoramaProvider: str = datas["panoramaProvider"]
        self.inExplorerMode: bool = datas["inExplorerMode"]
        self.maxErrorDistance: int = datas["maxErrorDistance"]
        self.likes: int = datas["likes"]
        self.locationSelectionMode: int = datas["locationSelectionMode"]

    def __repr__(self) -> str:
        return "\n".join([f"{k} : {v}" for k, v in vars(self).items()])
