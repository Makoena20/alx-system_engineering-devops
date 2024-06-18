#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, after='', word_count={}):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data')
    if data is None:
        return

    titles = [post.get('data').get('title') for post in data.get('children')]
    for title in titles:
        for word in title.split():
            word_lower = word.lower()
            if word_lower in word_list:
                if word_lower in word_count:
                    word_count[word_lower] += 1
                else:
                    word_count[word_lower] = 1

    after = data.get('after')
    if after is None:
        if not word_count:
            return
        sorted_counts = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
        for word, count in sorted_counts:
            print(f'{word}: {count}')
    else:
        count_words(subreddit, word_list, after, word_count)

# Test the function with a main script
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x.lower() for x in sys.argv[2].split()])

