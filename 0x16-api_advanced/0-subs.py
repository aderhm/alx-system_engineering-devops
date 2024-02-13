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

    response = requests.get(url, headers=header, allow_redirects=False).json()

    return response.get("data", {}).get("subscribers", 0)
