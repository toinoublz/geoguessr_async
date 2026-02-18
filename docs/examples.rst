Examples
========

Here are some practical examples of using Geoguessr Async.

Getting User Statistics
-----------------------

.. code-block:: python

   import asyncio
   from geoguessr_async import Geoguessr

   async def get_user_stats():
       geo = Geoguessr("your_ncfa_token")
       
       # Get comprehensive user information
       user = await geo.get_user_infos('user_id')
       
       print(f"Nickname: {user.nick}")
       print(f"Level: {user.progress.level}")
       print(f"XP: {user.progress.xp}")
       print(f"Is Pro: {user.isProUser}")
       
       # Access detailed statistics
       if user.stats:
           print(f"Duels played: {user.stats.duelsTotal.numGamesPlayed}")
           print(f"Duels win ratio: {user.stats.duelsTotal.winRatio}")
           print(f"Average guess distance: {user.stats.duelsTotal.avgGuessDistance}km")
       
       await geo.close()

   asyncio.run(get_user_stats())

Working with Duels
------------------

.. code-block:: python

   import asyncio
   from geoguessr_async import Geoguessr

   async def analyze_duel():
       geo = Geoguessr("your_ncfa_token")
       
       # Get complete duel data with replays
       duel = await geo.get_duel_info("https://www.geoguessr.com/duel/abc123")
       
       print(f"Duel ID: {duel.gameId}")
       print(f"Status: {duel.status}")
       print(f"Number of rounds: {duel.totalRoundCount}")
       
       # Analyze teams
       for team in duel.teams:
           print(f"Team {team.name}: {team.healthAtEnd} HP")
           for player in team.players:
               print(f"  Player: {player.playerId}")
               print(f"  Rating: {player.rating}")
               print(f"  Guesses: {len(player.guesses)}")
       
       # Access replays if available
       if duel.replays:
           for player_id, player_replays in duel.replays.items():
               print(f"Player {player_id} has {len(player_replays)} replay rounds")
       
       await geo.close()

   asyncio.run(analyze_duel())

Challenge Analysis
------------------

.. code-block:: python

   import asyncio
   from geoguessr_async import Geoguessr

   async def analyze_challenge():
       geo = Geoguessr("your_ncfa_token")
       
       # Get challenge information
       challenge = await geo.get_challenge_infos("challenge_token")
       
       print(f"Challenge: {challenge.token}")
       print(f"Map: {challenge.map.name}")
       print(f"Difficulty: {challenge.map.difficulty}")
       print(f"Rounds: {challenge.roundCount}")
       print(f"Time limit: {challenge.timeLimit}s")
       
       # Play the challenge
       result = await geo.play_challenge(challenge.token)
       print(f"Final score: {result.playerTotalScore.totalScore}")
       
       # Analyze each round
       for round_data in result.rounds:
           print(f"Round {round_data.number}: {round_data.roundScore.amount} points")
           print(f"  Distance: {round_data.distance.kilometers}km")
           print(f"  Time: {round_data.time.seconds}s")
       
       await geo.close()

   asyncio.run(analyze_challenge())

Batch Processing
----------------

.. code-block:: python

   import asyncio
   from geoguessr_async import Geoguessr

   async def batch_user_analysis(user_ids):
       geo = Geoguessr("your_ncfa_token")
       
       tasks = []
       for user_id in user_ids:
           tasks.append(geo.get_user_infos(user_id))
       
       users = await asyncio.gather(*tasks)
       
       for user in users:
           print(f"{user.nick}: Level {user.progress.level}")
           if user.stats:
               print(f"  Win rate: {user.stats.duelsTotal.winRatio:.1%}")
       
       await geo.close()

   # Example usage
   user_ids = ['user1', 'user2', 'user3']
   asyncio.run(batch_user_analysis(user_ids))

Error Handling
---------------

.. code-block:: python

   import asyncio
   from geoguessr_async import Geoguessr
   from geoguessr_async.geo_errors import UserUnknown

   async def robust_example():
       geo = Geoguessr("your_ncfa_token")
       
       try:
           user = await geo.get_user_infos('nonexistent_user')
       except UserUnknown:
           print("User not found!")
       except Exception as e:
           print(f"Unexpected error: {e}")
       finally:
           await geo.close()

   asyncio.run(robust_example())
