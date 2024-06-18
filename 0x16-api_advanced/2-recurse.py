#!/usr/bin/python3
"""
Recursive function to query the Reddit API and return
a list of titles of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list to store the titles of hot articles.
        after (str): The "after" parameter for pagination.

    Returns:
        list: List of titles of hot articles or None if subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data')
    if not data:
        return None

    children = data.get('children', [])
    if not children:
        return hot_list if hot_list else None

    for child in children:
        hot_list.append(child['data']['title'])

    after = data.get('after')
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)

# Sample testing code (not to be included in the actual file)
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")

