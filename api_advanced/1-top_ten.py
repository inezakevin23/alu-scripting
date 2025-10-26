#!/usr/bin/python3
"""Print the titles of the first 10Hot Posts"""
import requests


def top_ten(subreddit):
    """The top ten titles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyAPI/0.0.1"}
    params = {"limit": 10}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code == 200:
        json_data = response.json()
        for i in range(10):
            print(
                    json_data.get('data')
                    .get('children')[i]
                    .get('data')
                    .get('title')
                )
    else:
        print(None)
