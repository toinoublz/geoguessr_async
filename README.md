This is a Geoguessr API client written in Python. It allows you to interact with the Geoguessr API, such as getting information about users, challenges, maps, and scores.

To install the package, run the following command:

```
pip install geoguessr-async
```

Once the package is installed, you can create a client object by passing your NCFA cookie to the constructor:

```
from geoguessr_async import Geoguessr

client = Geoguessr("your_ncf_a_cookie")
```

You can then use the client object to get information about users, challenges, maps, and scores. For example, to get information about yourself, you can use the following code:

```
user = client.get_user_infos("your_user_id")
```

The `user` object will contain information such as your username, country, and number of games played.

To get information about a challenge, you can use the following code:

```
challenge = client.get_challenge_infos("https://geoguessr.com/challenge/xxxx")
```

The `challenge` object will contain information such as the challenge name, description, and time limit.

To get information about a map, you can use the following code:

```
map = client.get_map_infos("https://geoguessr.com/maps/xxxx")
```

The `map` object will contain information such as the map name, size, and location.

To get information about a score, you can use the following code:

```
score = client.get_score_infos("https://geoguessr.com/challenge/xxxx/xxxx")
```

The `score` object will contain information such as the player's name, score, and time.

I hope you find this package useful! Please let me know if you have any questions or feedback.