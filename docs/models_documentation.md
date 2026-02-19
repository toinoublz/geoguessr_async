# Geoguessr Async - Models Documentation

Cette documentation décrit tous les modèles de données disponibles dans le module `geoguessr_async.models`.

## Table des matières

- [Classes de Base](#classes-de-base)
- [Modèles Principaux](#modèles-principaux)
- [Modèles de Statistiques](#modèles-de-statistiques)
- [Modèles de Jeu](#modèles-de-jeu)
- [Modèles Utilitaires](#modèles-utilitaires)

---

## Classes de Base

### GeoguessrStr

Classe de base pour tous les modèles Geoguessr. Fournit des méthodes de représentation en arborescence.

#### Méthodes

- `to_tree(indent=0)`: Convertit l'objet en représentation arborescente
- `__str__()`: Représentation string de l'objet

---

## Modèles Principaux

### GeoguessrProfile

Représente le profil d'un utilisateur Geoguessr.

#### Attributs principaux

| Attribut | Type | Description |
|----------|------|-------------|
| `nick` | `str` | Pseudonyme de l'utilisateur |
| `createdAt` | `datetime` | Date de création du compte |
| `isProUser` | `bool` | Statut compte premium |
| `isVerified` | `bool` | Compte vérifié |
| `id` | `str` | ID unique de l'utilisateur |
| `url` | `str` | URL du profil |
| `countryCode` | `Optional[str]` | Code pays |
| `stats` | `Optional[GeoguessrStats]` | Statistiques du joueur |

#### Attributs de niveau et progression

| Attribut | Type | Description |
|----------|------|-------------|
| `battleRoyaleLevel` | `Optional[int]` | Niveau Battle Royale |
| `battleRoyaleDivision` | `Optional[int]` | Division Battle Royale |
| `progress` | `GeoguessrLevelProgress` | Progression XP |
| `competitive` | `Optional[GeoguessrCompetitive]` | Statistiques compétitives |

#### Attributs de compte

| Attribut | Type | Description |
|----------|------|-------------|
| `isBanned` | `bool` | Compte banni |
| `chatBan` | `bool` | Banni du chat |
| `isBotUser` | `bool` | Compte bot |

#### Méthodes

- `add_stats(stats: GeoguessrStats)`: Ajoute les statistiques au profil

---

### GeoguessrStats

Représente l'ensemble des statistiques d'un joueur.

#### Statistiques Ranked Team Duels

| Attribut | Type | Description |
|----------|------|-------------|
| `rankedTeamDuelsStandard` | `GeoguessrStatsRankedTeamDuelsStandard` | Duels standard en équipe |
| `rankedTeamDuelsNoMove` | `GeoguessrStatsRankedTeamDuelsNoMove` | Duels sans mouvement en équipe |
| `rankedTeamDuelsNmpz` | `GeoguessrStatsRankedTeamDuelsNmpz` | Duels NMPZ en équipe |
| `rankedTeamDuelsTotal` | `GeoguessrStatsRankedTeamDuelsTotal` | Total duels en équipe |

#### Statistiques Battle Royale

| Attribut | Type | Description |
|----------|------|-------------|
| `battleRoyaleDistance` | `GeoguessrStatsBattleRoyaleDistance` | Stats distance |
| `battleRoyaleCountry` | `GeoguessrStatsBattleRoyaleCountry` | Stats pays |
| `battleRoyaleMedals` | `GeoguessrStatsBattleRoyaleMedals` | Médailles |

#### Statistiques Compétitives

| Attribut | Type | Description |
|----------|------|-------------|
| `competitiveCityStreaks` | `GeoguessrStatsCompetitiveCityStreaks` | Streaks villes |
| `competitiveStreaksMedals` | `GeoguessrStatsCompetitiveStreaksMedals` | Médailles streaks |

#### Statistiques Duels

| Attribut | Type | Description |
|----------|------|-------------|
| `duels` | `GeoguessrStatsDuels` | Duels standard |
| `duelsNoMove` | `GeoguessrStatsDuelsNoMove` | Duels sans mouvement |
| `duelsNmpz` | `GeoguessrStatsDuelsNmpz` | Duels NMPZ |
| `duelsTotal` | `GeoguessrStatsDuelsTotal` | Total duels |
| `duelsMedals` | `GeoguessrStatsDuelsMedals` | Médailles duels |

#### Statistiques Unranked Duels

| Attribut | Type | Description |
|----------|------|-------------|
| `unrankedDuels` | `GeoguessrStatsUnrankedDuels` | Duels non classés |
| `unrankedDuelsNoMove` | `GeoguessrStatsUnrankedDuelsNoMove` | Duels non classés sans mouvement |
| `unrankedDuelsNmpz` | `GeoguessrStatsUnrankedDuelsNmpz` | Duels non classés NMPZ |
| `unrankedDuelsTotal` | `GeoguessrStatsUnrankedDuelsTotal` | Total duels non classés |

#### Progression et XP

| Attribut | Type | Description |
|----------|------|-------------|
| `lifeTimeXpProgression` | `GeoguessrStatsLifeTimeXpProgression` | Progression XP vie entière |
| `totalMedals` | `GeoguessrStatsTotalMedals` | Total médailles |
| `teamDuels` | `GeoguessrStatsTeamDuels` | Duels équipe |
| `teamDuelsQuickplay` | `GeoguessrStatsTeamDuelsQuickplay` | Duels équipe rapide |
| `party` | `GeoguessrStatsParty` | Statistiques party |

---

### GeoguessrUserELO

Représente les classements ELO d'un utilisateur.

#### Attributs

| Attribut | Type | Description |
|----------|------|-------------|
| `divisionNumber` | `int` | Numéro de division |
| `divisionName` | `str` | Nom de la division |
| `rating` | `int` | Classement ELO |
| `tier` | `str` | Niveau (tier) |
| `gameModeRatingsStandardduels` | `int` | ELO duels standard |
| `gameModeRatingsNmpzduels` | `int` | ELO duels NMPZ |
| `gameModeRatingsNomoveduels` | `int` | ELO duels sans mouvement |

---

### GeoguessrChallenge

Représente un défi Geoguessr.

#### Attributs

| Attribut | Type | Description |
|----------|------|-------------|
| `token` | `str` | Token unique du défi |
| `mapSlug` | `str` | Identifiant de la carte |
| `roundCount` | `int` | Nombre de manches |
| `timeLimit` | `int` | Limite de temps (secondes) |
| `forbidMoving` | `bool` | Interdit le mouvement |
| `forbidZooming` | `bool` | Interdit le zoom |
| `forbidRotating` | `bool` | Interdit la rotation |
| `numberOfParticipants` | `Optional[int]` | Nombre de participants |
| `gameMode` | `str` | Mode de jeu |
| `challengeType` | `int` | Type de défi |
| `locationOrder` | `int` | Ordre des localisations |

---

### GeoguessrMap

Représente une carte Geoguessr.

#### Attributs principaux

| Attribut | Type | Description |
|----------|------|-------------|
| `id` | `str` | ID unique de la carte |
| `name` | `str` | Nom de la carte |
| `slug` | `str` | Slug de la carte |
| `description` | `Optional[str]` | Description |
| `url` | `str` | URL de la carte |
| `playUrl` | `str` | URL de jeu |
| `published` | `bool` | Statut publication |
| `banned` | `bool` | Carte bannie |
| `coordinatesCount` | `Optional[str]` | Nombre de coordonnées |
| `creator` | `Optional[GeoguessrProfile]` | Créateur de la carte |

#### Attributs de jeu

| Attribut | Type | Description |
|----------|------|-------------|
| `difficulty` | `str` | Difficulté |
| `difficultyLevel` | `int` | Niveau de difficulté |
| `averageScore` | `Optional[int]` | Score moyen |
| `numFinishedGames` | `Optional[int]` | Nombre de parties terminées |
| `likes` | `int` | Nombre de likes |
| `deleted` | `bool` | Carte supprimée |
| `free` | `bool` | Carte gratuite |
| `inExplorerMode` | `bool` | Mode exploration |
| `maxErrorDistance` | `int` | Distance d'erreur max |
| `locationSelectionMode` | `int` | Mode sélection localisation |
| `tags` | `list` | Étiquettes |
| `collaborators` | `Any` | Collaborateurs |

#### Attributs de dates

| Attribut | Type | Description |
|----------|------|-------------|
| `createdAt` | `datetime` | Date de création |
| `updatedAt` | `datetime` | Date de mise à jour |

---

### GeoguessrDuel

Représente un duel Geoguessr.

#### Attributs principaux

| Attribut | Type | Description |
|----------|------|-------------|
| `gameId` | `Optional[str]` | ID unique du jeu |
| `teams` | `list` | Liste des équipes |
| `rounds` | `list` | Liste des manches |
| `currentRoundNumber` | `Optional[int]` | Manche actuelle |
| `status` | `Optional[str]` | Statut du jeu |
| `version` | `Optional[int]` | Version du jeu |

#### Options de jeu

| Attribut | Type | Description |
|----------|------|-------------|
| `optionsInitialhealth` | `Optional[int]` | Santé initiale |
| `optionsRoundtime` | `Optional[int]` | Temps par manche |
| `optionsMaxroundtime` | `Optional[int]` | Temps max manche |
| `optionsMaxnumberofrounds` | `Optional[int]` | Nombre max de manches |
| `optionsMovementoptionsForbidmoving` | `Optional[bool]` | Interdit mouvement |
| `optionsMovementoptionsForbidzooming` | `Optional[bool]` | Interdit zoom |
| `optionsMovementoptionsForbidrotating` | `Optional[bool]` | Interdit rotation |

---

## Modèles de Jeu

### GeoguessrChallengeResult

Représente le résultat d'un défi.

#### Attributs

| Attribut | Type | Description |
|----------|------|-------------|
| `player` | `GeoguessrScorePlayerInfo` | Informations joueur |
| `type` | `Optional[str]` | Type de jeu |
| `mode` | `Optional[str]` | Mode de jeu |
| `state` | `Optional[str]` | État du jeu |
| `roundCount` | `Optional[int]` | Nombre de manches |
| `map` | `Optional[str]` | Carte jouée |
| `rounds` | `list[GeoguessrChallengeRound]` | Manches jouées |
| `playerTotalScore` | `GeoguessrChallengePlayerTotalResult` | Score total |

### GeoguessrChallengeRound

Représente une manche de défi.

#### Attributs

| Attribut | Type | Description |
|----------|------|-------------|
| `number` | `int` | Numéro de la manche |
| `lat` | `float` | Latitude |
| `long` | `float` | Longitude |
| `panoId` | `Optional[str]` | ID panorama |
| `heading` | `float` | Orientation |
| `pitch` | `float` | Inclinaison |
| `zoom` | `float` | Niveau de zoom |
| `startTime` | `datetime` | Heure de début |

### GeoguessrPlayerGuesses

Représente les suppositions d'un joueur.

#### Attributs

| Attribut | Type | Description |
|----------|------|-------------|
| `number` | `int` | Numéro de la manche |
| `lat` | `float` | Latitude supposée |
| `long` | `float` | Longitude supposée |
| `timedOut` | `bool` | Temps écoulé |
| `timedOutWithGuess` | `bool` | Temps écoulé avec supposition |
| `skippedRound` | `bool` | Manche sautée |
| `roundScore` | `GeoguessrScore` | Score de la manche |
| `roundScoreInPercentage` | `int` | Score en pourcentage |
| `roundScoreInPoints` | `int` | Score en points |
| `distance` | `GeoguessrDistance` | Distance |
| `distanceInMeters` | `float` | Distance en mètres |
| `stepsCount` | `int` | Nombre de pas |
| `time` | `GeoguessrTime` | Temps |

---

## Modèles Utilitaires

### GeoguessrScore

Représente un score.

#### Attributs

| Attribut | Type | Description |
|----------|------|-------------|
| `amount` | `float` | Montant du score |
| `unit` | `Optional[str]` | Unité du score |
| `percentage` | `Optional[float]` | Pourcentage |

### GeoguessrDistance

Représente des mesures de distance.

#### Attributs

| Attribut | Type | Description |
|----------|------|-------------|
| `meters` | `float` | Distance en mètres |
| `kilometers` | `float` | Distance en kilomètres |
| `miles` | `float` | Distance en miles |

### GeoguessrTime

Représente des mesures de temps.

#### Attributs

| Attribut | Type | Description |
|----------|------|-------------|
| `seconds` | `Optional[float]` | Temps en secondes |
| `minutes` | `Optional[float]` | Temps en minutes |
| `hours` | `Optional[float]` | Temps en heures |

### GeoguessrActivities

Représente les activités d'un utilisateur.

#### Attributs

| Attribut | Type | Description |
|----------|------|-------------|
| `entries` | `list` | Liste des entrées d'activité |

---

## Modèles de Support

### Classes de progression et niveau

| Classe | Description |
|--------|-------------|
| `GeoguessrLevel` | Informations de niveau |
| `GeoguessrXpTitle` | Titre XP |
| `GeoguessrCompetitionMedals` | Médailles de compétition |
| `GeoguessrPin` | Épingle de profil |
| `GeoguessrDivision` | Division compétitive |
| `GeoguessrCompetitive` | Statistiques compétitives (déprécié) |

#### Attributs des classes de niveau

| Classe | Attributs principaux |
|--------|-------------------|
| `GeoguessrLevel` | `level: int`, `xpStart: int` |
| `GeoguessrXpTitle` | `id: int`, `tierId: int`, `minimumLevel: int`, `name: str` |
| `GeoguessrScorePlayerInfo` | `isLeader: bool`, `id: str`, `nick: str`, `isVerified: bool` |
| `GeoguessrGameBounds` | `minLat: float`, `minLng: float`, `maxLat: float`, `maxLng: float` |
| `GeoguessMapAvatar` | `background: str`, `decoration: str`, `ground: str`, `landscape: str` |

### Classes de statistiques détaillées

Chaque mode de jeu possède sa propre classe de statistiques avec les attributs communs :

| Attribut commun | Type | Description |
|-----------------|------|-------------|
| `numGamesPlayed` | `int` | Nombre de parties jouées |
| `numWins` | `int` | Nombre de victoires |
| `winRatio` | `float` | Ratio de victoires |
| `avgPosition` | `float` | Position moyenne |
| `avgGuessDistance` | `float` | Distance moyenne de supposition |
| `numGuesses` | `int` | Nombre de suppositions |
| `numFlawlessWins` | `int` | Victoires parfaites |

### Classes de médailles

| Classe | Description |
|--------|-------------|
| `GeoguessrStatsBattleRoyaleMedals` | Médailles Battle Royale |
| `GeoguessrStatsCompetitiveStreaksMedals` | Médailles streaks compétitifs |
| `GeoguessrStatsDuelsMedals` | Médailles duels |
| `GeoguessrStatsTotalMedals` | Total des médailles |

Chaque classe de médailles contient :
- `medalCountGold`: Nombre de médailles d'or
- `medalCountSilver`: Nombre de médailles d'argent  
- `medalCountBronze`: Nombre de médailles de bronze

### Classes de progression

| Classe | Description | Attributs principaux |
|--------|-------------|-------------------|
| `GeoguessrStatsLifeTimeXpProgression` | Progression XP vie entière | `xp: int` |
| `GeoguessrStatsTeamDuels` | Duels équipe | `numGamesPlayed: int`, `numWins: int`, `winRatio: float` |
| `GeoguessrStatsTeamDuelsQuickplay` | Duels équipe rapide | `numGamesPlayed: int`, `numWins: int` |
| `GeoguessrStatsParty` | Statistiques party | `total: int`, `duels: int`, `teamDuels: int`, etc. |

---

## Utilisation

### Importation

```python
from geoguessr_async.models import (
    GeoguessrProfile,
    GeoguessrStats,
    GeoguessrChallenge,
    GeoguessrMap,
    GeoguessrDuel
)
```

### Création d'instances

Les modèles sont généralement créés à partir des données de l'API :

```python
# Profil utilisateur
profile_data = await api.get_user_data()
profile = GeoguessrProfile(profile_data)

# Statistiques
stats_data = await api.get_user_stats()
stats = GeoguessrStats(stats_data)

# Défi
challenge_data = await api.get_challenge_info()
challenge = GeoguessrChallenge(challenge_data)
```

### Représentation

Tous les modèles héritent de `GeoguessrStr` et peuvent être affichés :

```python
print(profile)  # Affichage en arborescence
print(profile.to_tree(2))  # Avec indentation personnalisée
```

---

## Notes

- Les attributs essentiels sont maintenant typés comme non-optionnels (`str`, `int`, `float`, `bool`, `datetime`)
- Les attributs qui peuvent réellement être absents de l'API restent `Optional[T]`
- Les données manquantes sont gérées gracieusement avec des valeurs `None` via les utilitaires `geo_utils`
- Les dates sont automatiquement converties en objets `datetime`
- Les classes utilisent les utilitaires de `geo_utils` pour la conversion sécurisée des types

## GeoguessrDuelData Classes

### GeoguessrDuelData
Représente les données complètes d'un duel Geoguessr avec toutes les informations de jeu, équipes, manches, et replays.

**Attributs :**
- `gameId` (str): Identifiant unique du jeu
- `context` (Any): Contexte du jeu
- `teams` (list[GeoguessrDuelTeam]): Liste des équipes (bleue/rouge)
- `rounds` (list[GeoguessrDuelRound]): Liste des manches du duel
- `totalRoundCount` (int): Nombre total de manches
- `status` (str): Statut du jeu
- `version` (int): Version du jeu
- `options` (GeoguessrDuelOptions): Options de configuration du duel
- `initialHealth` (int): Points de vie initiaux
- `maxNumberOfRounds` (int): Nombre maximum de manches
- `result` (GeoguessrDuelResult): Résultat final du duel
- `gameServerNodeId` (str): ID du serveur de jeu
- `tournamentId` (str): ID du tournoi
- `playersId` (list[str]): Liste des IDs des joueurs
- `replays` (dict[str, list[GeoguessrDuelReplay]]): Replays des joueurs par manche

**Méthodes :**
- `set_replays(session)`: Récupère les replays de manière asynchrone

### GeoguessrDuelTeam
Représente une équipe dans un duel.

**Attributs :**
- `id` (str): Identifiant de l'équipe
- `name` (str): Nom de l'équipe (ex: "Blue", "Red")
- `healthAtEnd` (int): Points de vie à la fin
- `players` (list[GeoguessrDuelPlayer]): Joueurs de l'équipe
- `roundResults` (list[GeoguessrDuelTeamRoundResult]): Résultats par manche
- `isMultiplierActive` (bool): Si le multiplicateur est actif
- `multiplierAtEnd` (float): Multiplicateur à la fin

### GeoguessrDuelPlayer
Représente un joueur dans un duel.

**Attributs :**
- `playerId` (str): Identifiant du joueur
- `guesses` (list[GeoguessrDuelPlayerGuess]): Suppositions du joueur
- `rating` (int): Rating du joueur
- `countryCode` (str): Code pays du joueur
- `progressChange` (GeoguessrDuelProgressChange): Progression du joueur
- `helpRequested` (bool): Si aide demandée
- `isSteam` (bool): Si joueur Steam

### GeoguessrDuelPlayerGuess
Représente une supposition de joueur avec parsing des Big Numbers.

**Attributs :**
- `score` (float): Score obtenu (avec parsing Big Number)
- `distanceInKm` (float): Distance en km (avec parsing Big Number)
- `timeInMs` (int): Temps en millisecondes
- `guessPoint` (GeoguessrDuelCoordinate): Coordonnées de la supposition
- `locationPoint` (GeoguessrDuelCoordinate): Coordonnées réelles

### GeoguessrDuelProgressChange
Représente la progression complète d'un joueur.

**Attributs :**
- `xpAtStart` (GeoguessrDuelXpProgression): XP au début
- `xpAtEnd` (GeoguessrDuelXpProgression): XP à la fin
- `awardedXp` (GeoguessrDuelAwardedXp): XP awardés
- `medal` (str): Médaille obtenue
- `competitiveProgress` (Any): Progression compétitive
- `rankedSystemProgress` (GeoguessrDuelRankedSystemProgress): Progression classée
- `rankedTeamDuelsProgress` (Any): Progression duels en équipe
- `quickplayDuelsProgress` (Any): Progression duels rapides

### GeoguessrDuelReplay
Représente un replay de joueur avec tous les mouvements et actions.

**Attributs :**
- `datas` (list[GeoguessrDuelReplayStep]): Liste des étapes du replay

**Types (Enum) :**
- `PANOPOSITION`: Position dans le panorama
- `PANOPOV`: Point de vue du panorama
- `PANOZOOM`: Zoom du panorama
- `MAPZOOM`: Zoom de la carte
- `MAPPOSITION`: Position sur la carte
- `GUESSWITHLATLNG`: Supposition avec coordonnées
- `PINPOSITION`: Position de l'épingle
- `TIMER`: Timer
- `MAPDISPLAY`: Affichage de la carte

### GeoguessrDuelReplayStep
Représente une étape individuelle d'un replay.

**Attributs :**
- `time` (datetime): Timestamp de l'action
- `type` (GeoguessrDuelReplay.Type): Type d'action
- `payload` (Union[...]): Données spécifiques au type d'action

### Classes de Payload
- `GeoguessrDuelReplayPanoPositionPayload`: Position panorama (lat, lng, panoId)
- `GeoguessrDuelReplayPanoPovPayload`: Point de vue panorama (heading, pitch, zoom)
- `GeoguessrDuelReplayPanoZoomPayload`: Zoom panorama (zoom)
- `GeoguessrDuelReplayMapZoomPayload`: Zoom carte (zoom)
- `GeoguessrDuelReplayMapPositionPayload`: Position carte (lat, lng)
- `GeoguessrDuelReplayGuessWithLatLngPayload`: Supposition (lat, lng)
- `GeoguessrDuelReplayPinPositionPayload`: Position épingle (lat, lng)
- `GeoguessrDuelReplayTimerPayload`: Timer (time)
- `GeoguessrDuelReplayMapDisplayPayload`: Affichage carte (isActive, isSticky, size)

### Autres classes de duel
- `GeoguessrDuelTeamRoundResult`: Résultat d'une manche pour une équipe
- `GeoguessrDuelRound`: Informations sur une manche
- `GeoguessrDuelPanorama`: Données du panorama
- `GeoguessrDuelXpProgression`: Progression XP
- `GeoguessrDuelAwardedXp`: XP awardés
- `GeoguessrDuelXpAward`: Récompense XP individuelle
- `GeoguessrDuelRankedSystemProgress`: Progression système classé
- `GeoguessrDuelOptions`: Options du duel
- `GeoguessrDuelMap`: Carte du duel
- `GeoguessrDuelMapBounds`: Limites de la carte
- `GeoguessrDuelCoordinate`: Coordonnées géographiques
- `GeoguessrDuelGameContext`: Contexte de jeu
- `GeoguessrDuelResult`: Résultat final

### Fonctionnalités spéciales
- **Parsing des Big Numbers**: Gestion automatique du format `{"value": "66.11n", "type": "Big Number"}`
- **Replays asynchrones**: Récupération automatique des replays avec `set_replays()`
- **Arborescence améliorée**: Support des dictionnaires dans `to_tree()` pour un affichage structuré
- **Types forts**: Utilisation exhaustive des types pour une meilleure robustesse
