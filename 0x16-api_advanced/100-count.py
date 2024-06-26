#!/usr/bin/python3
"""
Reddit API recursive query to count words in titles of hot articles.
"""

import requests

def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively query Reddit API, parse titles of hot articles, and count keywords.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return
    
    data = response.json().get('data')
    if not data:
        return
    
    for child in data.get('children', []):
        title = child['data']['title'].lower()
        for word in word_list:
            word_lower = word.lower()
            word_count[word_lower] = word_count.get(word_lower, 0) + title.split().count(word_lower)
    
    after = data.get('after')
    if after:
        count_words(subreddit, word_list, after, word_count)
    else:
        sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_count:
            if count > 0:
                print(f"{word}: {count}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])

