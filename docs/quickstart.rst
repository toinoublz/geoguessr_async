Quick Start
===========

Basic Usage
-----------

Here's a simple example of how to use Geoguessr Async:

.. code-block:: python

   import asyncio
   from geoguessr_async import Geoguessr

   async def main():
       # Initialize the client
       geo = Geoguessr("your_ncfa_token_here")
       
       # Get user information
       user_info = await geo.get_user_infos('user_id')
       print(f"User: {user_info.nick}")
       
       # Get duel information
       duel_info = await geo.get_duel_info("duel_url")
       print(f"Duel status: {duel_info.status}")
       
       # Don't forget to close the session
       await geo.close()

   if __name__ == "__main__":
       asyncio.run(main())

Authentication
--------------

Geoguessr Async uses NCFA tokens for authentication. You can obtain your token:

1. Log into Geoguessr
2. Open browser developer tools
3. Look for cookies named `ncfa`
4. Copy the token value

Working with Models
-------------------

All data is returned as structured model objects:

.. code-block:: python

   # User profile with all statistics
   profile = await geo.get_user_infos('user_id')
   print(profile.stats.duels.numGamesPlayed)
   
   # Challenge information
   challenge = await geo.get_challenge_infos('challenge_token')
   print(f"Map: {challenge.map.name}")
   
   # Duel data with replays
   duel = await geo.get_duel_info('duel_url')
   for player_id, replays in duel.replays.items():
       print(f"Player {player_id} has {len(replays)} replays")
