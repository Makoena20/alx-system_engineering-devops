#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests
import sys  # Import sys module for command-line argument access


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise exception for bad responses
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts[:10]:
                print(post['data']['title'])
        else:
            print("Subreddit not found or no posts available.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as val_err:
        print(f"Value error occurred: {val_err}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-main.py <subreddit>")
        sys.exit(1)
    
    subreddit = sys.argv[1]
    top_ten(subreddit)
