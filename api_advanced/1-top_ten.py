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
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyAPI/0.0.1"}
    params = {"limit": 10}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data")
    if not data or "children" not in data:
        print(None)
        return

    posts = data.get("children")
    if not posts:
        print(None)
        return

    for post in posts:
        title = post.get("data", {}).get("title")
        if title:
            print(title)
