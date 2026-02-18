# Geoguessr Async - Models Documentation (English)

This documentation describes all data models available in the `geoguessr_async.models` module.

## Table of Contents

- [Base Classes](#base-classes)
- [Main Models](#main-models)
- [Statistics Models](#statistics-models)
- [Game Models](#game-models)
- [Utility Models](#utility-models)

---

## Base Classes

### GeoguessrStr

Base class for all Geoguessr models. Provides tree representation methods.

#### Methods

- `to_tree(indent=0)`: Converts the object to tree representation
- `__str__()`: String representation of the object

---

## Main Models

### GeoguessrProfile

Represents a Geoguessr user profile.

#### Main Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `nick` | `str` | User nickname |
| `createdAt` | `datetime` | Account creation date |
| `isProUser` | `bool` | Premium account status |
| `isVerified` | `bool` | Verified account |
| `id` | `str` | Unique user ID |
| `url` | `str` | Profile URL |
| `countryCode` | `Optional[str]` | Country code |
| `stats` | `Optional[GeoguessrStats]` | Player statistics |

#### Level and Progression Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `battleRoyaleLevel` | `Optional[int]` | Battle Royale level |
| `battleRoyaleDivision` | `Optional[int]` | Battle Royale division |
| `progress` | `GeoguessrLevelProgress` | XP progression |
| `competitive` | `Optional[GeoguessrCompetitive]` | Competitive statistics |

#### Account Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `isBanned` | `bool` | Banned account |
| `chatBan` | `bool` | Chat banned |
| `isBotUser` | `bool` | Bot account |

#### Methods

- `add_stats(stats: GeoguessrStats)`: Adds statistics to the profile

---

### GeoguessrStats

Represents all player statistics.

#### Ranked Team Duels Statistics

| Attribute | Type | Description |
|-----------|------|-------------|
| `rankedTeamDuelsStandard` | `GeoguessrStatsRankedTeamDuelsStandard` | Standard team duels |
| `rankedTeamDuelsNoMove` | `GeoguessrStatsRankedTeamDuelsNoMove` | No move team duels |
| `rankedTeamDuelsNmpz` | `GeoguessrStatsRankedTeamDuelsNmpz` | NMPZ team duels |
| `rankedTeamDuelsTotal` | `GeoguessrStatsRankedTeamDuelsTotal` | Total team duels |

#### Battle Royale Statistics

| Attribute | Type | Description |
|-----------|------|-------------|
| `battleRoyaleDistance` | `GeoguessrStatsBattleRoyaleDistance` | Distance stats |
| `battleRoyaleCountry` | `GeoguessrStatsBattleRoyaleCountry` | Country stats |
| `battleRoyaleMedals` | `GeoguessrStatsBattleRoyaleMedals` | Medals |

#### Competitive Statistics

| Attribute | Type | Description |
|-----------|------|-------------|
| `competitiveCityStreaks` | `GeoguessrStatsCompetitiveCityStreaks` | City streaks |
| `competitiveStreaksMedals` | `GeoguessrStatsCompetitiveStreaksMedals` | Streak medals |

#### Duels Statistics

| Attribute | Type | Description |
|-----------|------|-------------|
| `duels` | `GeoguessrStatsDuels` | Standard duels |
| `duelsNoMove` | `GeoguessrStatsDuelsNoMove` | No move duels |
| `duelsNmpz` | `GeoguessrStatsDuelsNmpz` | NMPZ duels |
| `duelsTotal` | `GeoguessrStatsDuelsTotal` | Total duels |
| `duelsMedals` | `GeoguessrStatsDuelsMedals` | Duel medals |

#### Unranked Duels Statistics

| Attribute | Type | Description |
|-----------|------|-------------|
| `unrankedDuels` | `GeoguessrStatsUnrankedDuels` | Unranked duels |
| `unrankedDuelsNoMove` | `GeoguessrStatsUnrankedDuelsNoMove` | Unranked no move duels |
| `unrankedDuelsNmpz` | `GeoguessrStatsUnrankedDuelsNmpz` | Unranked NMPZ duels |
| `unrankedDuelsTotal` | `GeoguessrStatsUnrankedDuelsTotal` | Total unranked duels |

#### Progression and XP

| Attribute | Type | Description |
|-----------|------|-------------|
| `lifeTimeXpProgression` | `GeoguessrStatsLifeTimeXpProgression` | Lifetime XP progression |
| `totalMedals` | `GeoguessrStatsTotalMedals` | Total medals |
| `teamDuels` | `GeoguessrStatsTeamDuels` | Team duels |
| `teamDuelsQuickplay` | `GeoguessrStatsTeamDuelsQuickplay` | Quickplay team duels |
| `party` | `GeoguessrStatsParty` | Party statistics |

---

### GeoguessrUserELO

Represents a user's ELO rankings.

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `divisionNumber` | `int` | Division number |
| `divisionName` | `str` | Division name |
| `rating` | `int` | ELO ranking |
| `tier` | `str` | Tier level |
| `gameModeRatingsStandardduels` | `int` | Standard duels ELO |
| `gameModeRatingsNmpzduels` | `int` | NMPZ duels ELO |
| `gameModeRatingsNomoveduels` | `int` | No move duels ELO |

---

### GeoguessrChallenge

Represents a Geoguessr challenge.

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `token` | `str` | Unique challenge token |
| `mapSlug` | `str` | Map identifier |
| `roundCount` | `int` | Number of rounds |
| `timeLimit` | `int` | Time limit (seconds) |
| `forbidMoving` | `bool` | Forbids movement |
| `forbidZooming` | `bool` | Forbids zooming |
| `forbidRotating` | `bool` | Forbids rotation |
| `numberOfParticipants` | `Optional[int]` | Number of participants |
| `gameMode` | `str` | Game mode |
| `challengeType` | `int` | Challenge type |
| `locationOrder` | `int` | Location order |

---

### GeoguessrMap

Represents a Geoguessr map.

#### Main Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | `str` | Unique map ID |
| `name` | `str` | Map name |
| `slug` | `str` | Map slug |
| `description` | `Optional[str]` | Description |
| `url` | `str` | Map URL |
| `playUrl` | `str` | Play URL |
| `published` | `bool` | Publication status |
| `banned` | `bool` | Banned map |
| `coordinatesCount` | `Optional[str]` | Number of coordinates |
| `creator` | `Optional[GeoguessrProfile]` | Map creator |

#### Game Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `difficulty` | `str` | Difficulty |
| `difficultyLevel` | `int` | Difficulty level |
| `averageScore` | `Optional[int]` | Average score |
| `numFinishedGames` | `Optional[int]` | Number of finished games |
| `likes` | `int` | Number of likes |
| `deleted` | `bool` | Deleted map |
| `free` | `bool` | Free map |
| `inExplorerMode` | `bool` | Explorer mode |
| `maxErrorDistance` | `int` | Max error distance |
| `locationSelectionMode` | `int` | Location selection mode |
| `tags` | `list` | Tags |
| `collaborators` | `Any` | Collaborators |

#### Date Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `createdAt` | `datetime` | Creation date |
| `updatedAt` | `datetime` | Update date |

---

### GeoguessrDuel

Represents a Geoguessr duel.

#### Main Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `gameId` | `Optional[str]` | Unique game ID |
| `teams` | `list` | List of teams |
| `rounds` | `list` | List of rounds |
| `currentRoundNumber` | `Optional[int]` | Current round |
| `status` | `Optional[str]` | Game status |
| `version` | `Optional[int]` | Game version |

#### Game Options

| Attribute | Type | Description |
|-----------|------|-------------|
| `optionsInitialhealth` | `Optional[int]` | Initial health |
| `optionsRoundtime` | `Optional[int]` | Time per round |
| `optionsMaxroundtime` | `Optional[int]` | Max round time |
| `optionsMaxnumberofrounds` | `Optional[int]` | Max number of rounds |
| `optionsMovementoptionsForbidmoving` | `Optional[bool]` | Forbid movement |
| `optionsMovementoptionsForbidzooming` | `Optional[bool]` | Forbid zoom |
| `optionsMovementoptionsForbidrotating` | `Optional[bool]` | Forbid rotation |

---

## Game Models

### GeoguessrChallengeResult

Represents a challenge result.

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `player` | `GeoguessrScorePlayerInfo` | Player information |
| `type` | `Optional[str]` | Game type |
| `mode` | `Optional[str]` | Game mode |
| `state` | `Optional[str]` | Game state |
| `roundCount` | `Optional[int]` | Number of rounds |
| `map` | `Optional[str]` | Played map |
| `rounds` | `list[GeoguessrChallengeRound]` | Played rounds |
| `playerTotalScore` | `GeoguessrChallengePlayerTotalResult` | Total score |

### GeoguessrChallengeRound

Represents a challenge round.

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `number` | `int` | Round number |
| `lat` | `float` | Latitude |
| `long` | `float` | Longitude |
| `panoId` | `Optional[str]` | Panorama ID |
| `heading` | `float` | Heading |
| `pitch` | `float` | Pitch |
| `zoom` | `float` | Zoom level |
| `startTime` | `datetime` | Start time |

### GeoguessrPlayerGuesses

Represents a player's guesses.

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `number` | `int` | Round number |
| `lat` | `float` | Guessed latitude |
| `long` | `float` | Guessed longitude |
| `timedOut` | `bool` | Timed out |
| `timedOutWithGuess` | `bool` | Timed out with guess |
| `skippedRound` | `bool` | Skipped round |
| `roundScore` | `GeoguessrScore` | Round score |
| `roundScoreInPercentage` | `int` | Score in percentage |
| `roundScoreInPoints` | `int` | Score in points |
| `distance` | `GeoguessrDistance` | Distance |
| `distanceInMeters` | `float` | Distance in meters |
| `stepsCount` | `int` | Number of steps |
| `time` | `GeoguessrTime` | Time |

---

## Utility Models

### GeoguessrScore

Represents a score.

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `amount` | `float` | Score amount |
| `unit` | `Optional[str]` | Score unit |
| `percentage` | `Optional[float]` | Percentage |

### GeoguessrDistance

Represents distance measurements.

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `meters` | `float` | Distance in meters |
| `kilometers` | `float` | Distance in kilometers |
| `miles` | `float` | Distance in miles |

### GeoguessrTime

Represents time measurements.

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `seconds` | `Optional[float]` | Time in seconds |
| `minutes` | `Optional[float]` | Time in minutes |
| `hours` | `Optional[float]` | Time in hours |

### GeoguessrActivities

Represents a user's activities.

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `entries` | `list` | List of activity entries |

---

## Support Models

### Progression and Level Classes

| Class | Description |
|-------|-------------|
| `GeoguessrLevel` | Level information |
| `GeoguessrXpTitle` | XP title |
| `GeoguessrCompetitionMedals` | Competition medals |
| `GeoguessrPin` | Profile pin |
| `GeoguessrDivision` | Competitive division |
| `GeoguessrCompetitive` | Competitive statistics (deprecated) |

#### Level Class Attributes

| Class | Main Attributes |
|-------|-----------------|
| `GeoguessrLevel` | `level: int`, `xpStart: int` |
| `GeoguessrXpTitle` | `id: int`, `tierId: int`, `minimumLevel: int`, `name: str` |
| `GeoguessrScorePlayerInfo` | `isLeader: bool`, `id: str`, `nick: str`, `isVerified: bool` |
| `GeoguessrGameBounds` | `minLat: float`, `minLng: float`, `maxLat: float`, `maxLng: float` |
| `GeoguessMapAvatar` | `background: str`, `decoration: str`, `ground: str`, `landscape: str` |

### Detailed Statistics Classes

Each game mode has its own statistics class with common attributes:

| Common Attribute | Type | Description |
|-------------------|------|-------------|
| `numGamesPlayed` | `int` | Number of games played |
| `numWins` | `int` | Number of wins |
| `winRatio` | `float` | Win ratio |
| `avgPosition` | `float` | Average position |
| `avgGuessDistance` | `float` | Average guess distance |
| `numGuesses` | `int` | Number of guesses |
| `numFlawlessWins` | `int` | Flawless wins |

### Medal Classes

| Class | Description |
|-------|-------------|
| `GeoguessrStatsBattleRoyaleMedals` | Battle Royale medals |
| `GeoguessrStatsCompetitiveStreaksMedals` | Competitive streak medals |
| `GeoguessrStatsDuelsMedals` | Duel medals |
| `GeoguessrStatsTotalMedals` | Total medals |

Each medal class contains:
- `medalCountGold`: Number of gold medals
- `medalCountSilver`: Number of silver medals  
- `medalCountBronze`: Number of bronze medals

### Progression Classes

| Class | Description | Main Attributes |
|-------|-------------|-----------------|
| `GeoguessrStatsLifeTimeXpProgression` | Lifetime XP progression | `xp: int` |
| `GeoguessrStatsTeamDuels` | Team duels | `numGamesPlayed: int`, `numWins: int`, `winRatio: float` |
| `GeoguessrStatsTeamDuelsQuickplay` | Quickplay team duels | `numGamesPlayed: int`, `numWins: int` |
| `GeoguessrStatsParty` | Party statistics | `total: int`, `duels: int`, `teamDuels: int`, etc. |

---

## Usage

### Import

```python
from geoguessr_async.models import (
    GeoguessrProfile,
    GeoguessrStats,
    GeoguessrChallenge,
    GeoguessrMap,
    GeoguessrDuel
)
```

### Creating Instances

Models are typically created from API data:

```python
# User profile
profile_data = await api.get_user_data()
profile = GeoguessrProfile(profile_data)

# Statistics
stats_data = await api.get_user_stats()
stats = GeoguessrStats(stats_data)

# Challenge
challenge_data = await api.get_challenge_info()
challenge = GeoguessrChallenge(challenge_data)
```

### Representation

All models inherit from `GeoguessrStr` and can be displayed:

```python
print(profile)  # Tree display
print(profile.to_tree(2))  # With custom indentation
```

---

## Notes

- Essential attributes are now typed as non-optional (`str`, `int`, `float`, `bool`, `datetime`)
- Attributes that can actually be missing from the API remain `Optional[T]`
- Missing data is gracefully handled with `None` values via `geo_utils` utilities
- Dates are automatically converted to `datetime` objects
- Classes use `geo_utils` utilities for safe type conversion

## GeoguessrDuelData Classes

### GeoguessrDuelData
Represents complete Geoguessr duel data with all game information, teams, rounds, and replays.

**Attributes:**
- `gameId` (str): Unique game identifier
- `context` (Any): Game context
- `teams` (list[GeoguessrDuelTeam]): List of teams (blue/red)
- `rounds` (list[GeoguessrDuelRound]): List of duel rounds
- `totalRoundCount` (int): Total number of rounds
- `status` (str): Game status
- `version` (int): Game version
- `options` (GeoguessrDuelOptions): Duel configuration options
- `initialHealth` (int): Initial health points
- `maxNumberOfRounds` (int): Maximum number of rounds
- `result` (GeoguessrDuelResult): Final duel result
- `gameServerNodeId` (str): Game server node ID
- `tournamentId` (str): Tournament ID
- `playersId` (list[str]): List of player IDs
- `replays` (dict[str, list[GeoguessrDuelReplay]]): Player replays by round

**Methods:**
- `set_replays(session)`: Asynchronously retrieves replays

### GeoguessrDuelTeam
Represents a team in a duel.

**Attributes:**
- `id` (str): Team identifier
- `name` (str): Team name (e.g., "Blue", "Red")
- `healthAtEnd` (int): Health points at the end
- `players` (list[GeoguessrDuelPlayer]): Team players
- `roundResults` (list[GeoguessrDuelTeamRoundResult]): Round results
- `isMultiplierActive` (bool): If multiplier is active
- `multiplierAtEnd` (float): Multiplier at the end

### GeoguessrDuelPlayer
Represents a player in a duel.

**Attributes:**
- `playerId` (str): Player identifier
- `guesses` (list[GeoguessrDuelPlayerGuess]): Player's guesses
- `rating` (int): Player rating
- `countryCode` (str): Player's country code
- `progressChange` (GeoguessrDuelProgressChange): Player's progression
- `helpRequested` (bool): If help was requested
- `isSteam` (bool): If Steam player

### GeoguessrDuelPlayerGuess
Represents a player's guess with Big Number parsing.

**Attributes:**
- `score` (float): Score obtained (with Big Number parsing)
- `distanceInKm` (float): Distance in km (with Big Number parsing)
- `timeInMs` (int): Time in milliseconds
- `guessPoint` (GeoguessrDuelCoordinate): Guess coordinates
- `locationPoint` (GeoguessrDuelCoordinate): Real coordinates

### GeoguessrDuelProgressChange
Represents a player's complete progression.

**Attributes:**
- `xpAtStart` (GeoguessrDuelXpProgression): XP at start
- `xpAtEnd` (GeoguessrDuelXpProgression): XP at end
- `awardedXp` (GeoguessrDuelAwardedXp): Awarded XP
- `medal` (str): Medal obtained
- `competitiveProgress` (Any): Competitive progression
- `rankedSystemProgress` (GeoguessrDuelRankedSystemProgress): Ranked system progression
- `rankedTeamDuelsProgress` (Any): Ranked team duels progression
- `quickplayDuelsProgress` (Any): Quickplay duels progression

### GeoguessrDuelReplay
Represents a player replay with all movements and actions.

**Attributes:**
- `datas` (list[GeoguessrDuelReplayStep]): List of replay steps

**Types (Enum):**
- `PANOPOSITION`: Position in panorama
- `PANOPOV`: Panorama point of view
- `PANOZOOM`: Panorama zoom
- `MAPZOOM`: Map zoom
- `MAPPOSITION`: Position on map
- `GUESSWITHLATLNG`: Guess with coordinates
- `PINPOSITION`: Pin position
- `TIMER`: Timer
- `MAPDISPLAY`: Map display

### GeoguessrDuelReplayStep
Represents an individual replay step.

**Attributes:**
- `time` (datetime): Action timestamp
- `type` (GeoguessrDuelReplay.Type): Action type
- `payload` (Union[...]): Type-specific action data

### Payload Classes
- `GeoguessrDuelReplayPanoPositionPayload`: Panorama position (lat, lng, panoId)
- `GeoguessrDuelReplayPanoPovPayload`: Panorama point of view (heading, pitch, zoom)
- `GeoguessrDuelReplayPanoZoomPayload`: Panorama zoom (zoom)
- `GeoguessrDuelReplayMapZoomPayload`: Map zoom (zoom)
- `GeoguessrDuelReplayMapPositionPayload`: Map position (lat, lng)
- `GeoguessrDuelReplayGuessWithLatLngPayload`: Guess (lat, lng)
- `GeoguessrDuelReplayPinPositionPayload`: Pin position (lat, lng)
- `GeoguessrDuelReplayTimerPayload`: Timer (time)
- `GeoguessrDuelReplayMapDisplayPayload`: Map display (isActive, isSticky, size)

### Other Duel Classes
- `GeoguessrDuelTeamRoundResult`: Round result for a team
- `GeoguessrDuelRound`: Round information
- `GeoguessrDuelPanorama`: Panorama data
- `GeoguessrDuelXpProgression`: XP progression
- `GeoguessrDuelAwardedXp`: Awarded XP
- `GeoguessrDuelXpAward`: Individual XP reward
- `GeoguessrDuelRankedSystemProgress`: Ranked system progression
- `GeoguessrDuelOptions`: Duel options
- `GeoguessrDuelMap`: Duel map
- `GeoguessrDuelMapBounds`: Map bounds
- `GeoguessrDuelCoordinate`: Geographic coordinates
- `GeoguessrDuelGameContext`: Game context
- `GeoguessrDuelResult`: Final result

### Special Features
- **Big Number Parsing**: Automatic handling of `{"value": "66.11n", "type": "Big Number"}` format
- **Asynchronous Replays**: Automatic replay retrieval with `set_replays()`
- **Enhanced Tree**: Dictionary support in `to_tree()` for structured display
- **Strong Types**: Comprehensive type usage for better robustness
