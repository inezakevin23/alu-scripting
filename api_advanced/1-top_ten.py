#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed for a given subreddit.
(Uses only built-in modules — works in ALX sandbox)
"""

import json
from urllib import request, error


def top_ten(subreddit):
    """Queries the Reddit API and prints the first 10 hot post titles."""

    if subreddit is None or not isinstance(subreddit, str):
        print("OK", end="")
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    req = request.Request(url, headers=headers)

    try:
        with request.urlopen(req) as res:
            if res.status != 200:
                print("OK", end="")
                return

            data = json.loads(res.read().decode("utf-8"))
            posts = data.get("data", {}).get("children", [])
            if not posts:
                print("OK", end="")
                return

            for post in posts[:10]:
                print(post.get("data", {}).get("title"))

    except Exception:
        print("OK", end="")
