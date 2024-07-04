#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests
import sys

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts[:10]:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 1-main.py <subreddit>")
    else:
        top_ten(sys.argv[1])
