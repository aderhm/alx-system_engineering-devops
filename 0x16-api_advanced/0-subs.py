#!/usr/bin/python3
"""Returns the number of subscribers.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers of a given subreddit
    """
    if not subreddit:
        return 0

    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {'User-Agent': 'API Advanced'}

    response = requests.get(url, headers=header).json()
    if response.status_code in range(300, 404):
        return 0
    return response.get("data", {}).get("subscribers", 0)
