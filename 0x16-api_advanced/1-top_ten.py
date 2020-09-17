#!/usr/bin/python3
"""
queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    top ten
    """
    get = requests.get(url, headers=headers, allow_redirects=False)
    headers = {'User-Agent': 'its_me'}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    if get.status_code == 404:
        print('None')
    else:
        print(post.get('data', {}).get('title', ''))
