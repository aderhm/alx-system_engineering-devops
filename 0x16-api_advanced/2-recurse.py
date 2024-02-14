#!/usr/bin/python3
"""Returns the hotest titles recursively.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """This is a recursive function and it returns the hotest titles.
    """
    if after is None:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, after
            )

    header = {"User-Agent": "API Advanced/0.1"}

    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if "data" in data and "children" in data["data"]:
            for post in data["data"]["children"]:
                hot_list.append(post["data"]["title"])

            after = data["data"]["after"]
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    else:
        return None
