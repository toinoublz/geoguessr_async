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
| `nick` | `Optional[str]` | Pseudonyme de l'utilisateur |
| `created` | `datetime` | Date de création du compte |
| `isProUser` | `Optional[bool]` | Statut compte premium |
| `isVerified` | `Optional[bool]` | Compte vérifié |
| `id` | `Optional[str]` | ID unique de l'utilisateur |
| `countryCode` | `Optional[str]` | Code pays |
| `stats` | `Optional[GeoguessrStats]` | Statistiques du joueur |

#### Attributs de niveau et progression

| Attribut | Type | Description |
|----------|------|-------------|
| `battleRoyaleLevel` | `Optional[int]` | Niveau Battle Royale |
| `battleRoyaleDivision` | `Optional[int]` | Division Battle Royale |
| `progress` | `GeoguessrLevelProgress` | Progression XP |
| `competitive` | `GeoguessrCompetitive` | Statistiques compétitives |

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
| `divisionNumber` | `Optional[int]` | Numéro de division |
| `divisionName` | `Optional[str]` | Nom de la division |
| `rating` | `Optional[int]` | Classement ELO |
| `tier` | `Optional[str]` | Niveau (tier) |
| `gameModeRatingsStandardduels` | `Optional[int]` | ELO duels standard |
| `gameModeRatingsNmpzduels` | `Optional[int]` | ELO duels NMPZ |
| `gameModeRatingsNomoveduels` | `Optional[int]` | ELO duels sans mouvement |

---

### GeoguessrChallenge

Représente un défi Geoguessr.

#### Attributs

| Attribut | Type | Description |
|----------|------|-------------|
| `token` | `Optional[str]` | Token unique du défi |
| `mapSlug` | `Optional[str]` | Identifiant de la carte |
| `roundCount` | `Optional[int]` | Nombre de manches |
| `timeLimit` | `Optional[int]` | Limite de temps (secondes) |
| `forbidMoving` | `Optional[bool]` | Interdit le mouvement |
| `forbidZooming` | `Optional[bool]` | Interdit le zoom |
| `forbidRotating` | `Optional[bool]` | Interdit la rotation |
| `numberOfParticipants` | `Optional[int]` | Nombre de participants |
| `gameMode` | `Optional[str]` | Mode de jeu |

---

### GeoguessrMap

Représente une carte Geoguessr.

#### Attributs principaux

| Attribut | Type | Description |
|----------|------|-------------|
| `id` | `Optional[str]` | ID unique de la carte |
| `name` | `Optional[str]` | Nom de la carte |
| `slug` | `Optional[str]` | Slug de la carte |
| `description` | `Optional[str]` | Description |
| `published` | `Optional[bool]` | Statut publication |
| `banned` | `Optional[bool]` | Carte bannie |
| `coordinatesCount` | `Optional[str]` | Nombre de coordonnées |
| `creator` | `Optional[GeoguessrProfile]` | Créateur de la carte |

#### Attributs de jeu

| Attribut | Type | Description |
|----------|------|-------------|
| `difficulty` | `Optional[str]` | Difficulté |
| `difficultyLevel` | `Optional[int]` | Niveau de difficulté |
| `averageScore` | `Optional[int]` | Score moyen |
| `numFinishedGames` | `Optional[int]` | Nombre de parties terminées |
| `likes` | `Optional[int]` | Nombre de likes |

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
| `number` | `Optional[int]` | Numéro de la manche |
| `lat` | `Optional[float]` | Latitude |
| `long` | `Optional[float]` | Longitude |
| `panoId` | `Optional[str]` | ID panorama |
| `heading` | `Optional[float]` | Orientation |
| `pitch` | `Optional[float]` | Inclinaison |
| `zoom` | `Optional[float]` | Niveau de zoom |
| `startTime` | `datetime` | Heure de début |

### GeoguessrPlayerGuesses

Représente les suppositions d'un joueur.

#### Attributs

| Attribut | Type | Description |
|----------|------|-------------|
| `number` | `Optional[int]` | Numéro de la manche |
| `lat` | `Optional[float]` | Latitude supposée |
| `long` | `Optional[float]` | Longitude supposée |
| `timedOut` | `Optional[bool]` | Temps écoulé |
| `timedOutWithGuess` | `Optional[bool]` | Temps écoulé avec supposition |
| `skippedRound` | `Optional[bool]` | Manche sautée |
| `roundScore` | `GeoguessrScore` | Score de la manche |
| `distance` | `GeoguessrDistance` | Distance |
| `time` | `GeoguessrTime` | Temps |

---

## Modèles Utilitaires

### GeoguessrScore

Représente un score.

#### Attributs

| Attribut | Type | Description |
|----------|------|-------------|
| `amount` | `Optional[float]` | Montant du score |
| `unit` | `Optional[str]` | Unité du score |
| `percentage` | `Optional[float]` | Pourcentage |

### GeoguessrDistance

Représente des mesures de distance.

#### Attributs

| Attribut | Type | Description |
|----------|------|-------------|
| `meters` | `Optional[float]` | Distance en mètres |
| `kilometers` | `Optional[float]` | Distance en kilomètres |
| `miles` | `Optional[float]` | Distance en miles |

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
| `GeoguessrLevelProgress` | Progression de niveau XP |
| `GeoguessrLevel` | Informations de niveau |
| `GeoguessrXpTitle` | Titre XP |
| `GeoguessrCompetitionMedals` | Médailles de compétition |
| `GeoguessrPin` | Épingle de profil |
| `GeoguessrDivision` | Division compétitive |
| `GeoguessrCompetitive` | Statistiques compétitives (déprécié) |

### Classes de statistiques détaillées

Chaque mode de jeu possède sa propre classe de statistiques avec les attributs communs :

| Attribut commun | Type | Description |
|-----------------|------|-------------|
| `numGamesPlayed` | `Optional[int]` | Nombre de parties jouées |
| `numWins` | `Optional[int]` | Nombre de victoires |
| `winRatio` | `Optional[float]` | Ratio de victoires |
| `avgPosition` | `Optional[float]` | Position moyenne |
| `avgGuessDistance` | `Optional[float]` | Distance moyenne de supposition |
| `numGuesses` | `Optional[int]` | Nombre de suppositions |
| `numFlawlessWins` | `Optional[int]` | Victoires parfaites |

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

- Tous les attributs sont optionnels (`Optional[T]`) car les données de l'API peuvent varier
- Les classes utilisent les utilitaires de `geo_utils` pour la conversion sécurisée des types
- Les dates sont automatiquement converties en objets `datetime`
- Les données manquantes sont gérées gracieusement avec des valeurs `None`
