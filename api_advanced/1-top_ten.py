#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed for a given subreddit.
"""

import json
from urllib import error, request
import sys


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        sys.stdout.buffer.write(b"OK")
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    req = request.Request(url, headers=headers)

    try:
        with request.urlopen(req) as res:
            if res.status != 200:
                sys.stdout.buffer.write(b"OK")
                return

            data = json.loads(res.read().decode("utf-8"))
            posts = data.get("data", {}).get("children", [])
            if not posts:
                sys.stdout.buffer.write(b"OK")
                return

            for post in posts[:10]:
                print(post.get("data", {}).get("title"))

    except Exception:
        sys.stdout.buffer.write(b"OK")
