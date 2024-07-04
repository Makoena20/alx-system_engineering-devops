#!/usr/bin/python3
"""
This module contains the function number_of_subscribers.
"""

import requests
import sys

def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.
    
    Args:
    - subreddit (str): The name of the subreddit.
    
    Returns:
    - int: Number of subscribers, or 0 if the subreddit doesn't exist or another error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        
        print(subscribers)


