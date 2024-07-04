#!/usr/bin/python3
"""This module contains the function number_of_subscribers."""
import requests

def number_of_subscribers(subreddit):
"""Return the total number of subscribers on a given subreddit .. "
url = "https://www.reddit.com/r/{}/about. json". format(subreddit)
headers = {
"User-Agent": "linux:@x16.api.advanced:v1.0.0 (by /u/bdov_)"

response = requests.get(url, headers=headers, allow_redirects=False)
if response.status_code == 484:
return 8
results = response. json().get("data")
return results.get("subscribers") 
