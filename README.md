This is a Geoguessr API client written in Python. It allows you to interact with the Geoguessr API, such as getting information about users, challenges, maps, and scores.

To install the package, run the following command:

```
pip install geoguessr-async
```

Once the package is installed, you can create a client object by passing your NCFA cookie to the constructor:

```
from geoguessr_async import Geoguessr

client = Geoguessr("your_ncfa_cookie")
```

You can then use the client object to get information about users, challenges, maps, and scores. For example, to get information about an user with his ID, you can use the following code:

```
user = client.get_user_infos(userId)
```

The `Profile` object will contain information such as your username, country, and number of games played.

To get information about a challenge, you can use the following code:

```
challenge = client.get_challenge_infos("https://geoguessr.com/challenge/xxxx")
```

The `Challenge` object will contain information such as the challenge name, description, and time limit.

To get information about a map, you can use the following code:

```
map = client.get_map_infos("https://geoguessr.com/maps/xxxx")
```

The `Map` object will contain information such as the map name, size, and location.

To get information about a score, you can use the following code:

```
score = client.get_challenge_score("https://geoguessr.com/challenge/xxxx")
```

The `Score` object will contain information such as the player's name, score, and time.

I hope you find this package useful! Please let me know if you have any questions or feedback.