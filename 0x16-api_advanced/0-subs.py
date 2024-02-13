#!/usr/bin/python3
"""Returns the number of subscribers.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers of a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {'User-Agent': 'API Advanced'}

    response = requests.get(url, headers=header)
    data = response.json()

    if "data" in data and "subscribers" in data["data"]:
        return data["data"]["subscribers"]
    else:
        return 0
