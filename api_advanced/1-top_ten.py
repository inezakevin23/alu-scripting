#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {"User-Agent":  "ALUStudent/1.0"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print("None", end="")
        return

    data = response.json().get("data")
    if not data or "children" not in data:
        print("None", end="")
        return

    for post in data.get("children", []):
        title = post.get("data", {}).get("title")
        if title:
            print(title)
