#!/usr/bin/python3
"""Treats hot articles' titles.
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """arses the title of all hot articles, and prints a sorted count
    of given keywords (case-insensitive, delimited by spaces).
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
                title = post["data"]["title"].lower()
                for word in word_list:
                    word_lower = word.lower()
                    if title.count(word_lower):
                        if word_lower in counts:
                            counts[word_lower] += title.count(word_lower)
                        else:
                            counts[word_lower] = title.count(word_lower)

            after = data["data"]["after"]
            if after is not None:
                return count_words(subreddit, word_list, after, counts)
            else:
                sorted_counts = sorted(
                    counts.items(), key=lambda x: (-x[1], x[0])
                    )
                for word, count in sorted_counts:
                    print("{}: {}".format(word, count))
        else:
            return
    else:
        return
