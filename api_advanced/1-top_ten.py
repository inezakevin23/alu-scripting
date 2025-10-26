#!/usr/bin/python3
"""Print the titles of the first 10 Hot Posts"""
import requests
import sys

def top_ten(subreddit):
    """The top ten titles"""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = f"https://reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        for post in json_data.get('data', {}).get('children', [])[:10]:
            print(post.get('data', {}).get('title'))
    else:
        sys.stdout.write("ok")
