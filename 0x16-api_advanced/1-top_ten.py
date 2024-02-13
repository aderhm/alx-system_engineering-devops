#!/usr/bin/python3
"""Prints top 10 hot posts"""
import requests


def top_ten(subreddit):
    """Prints the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {
        "User-Agent": "API Advanced)"
    }
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data")
        for child in results.get("children"):
            print(child.get("data").get("title"))
    else:
        print("None")
