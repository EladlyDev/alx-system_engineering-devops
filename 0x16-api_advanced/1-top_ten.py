#!/usr/bin/python3
""" 1. Top Ten """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed
    for a given subreddit. """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=9'.format(subreddit)
    headers = {"User-Agent": "ubuntu:Python"}

    r = requests.get(url, headers=headers, allow_redirects=False)

    top = None
    try:
        top = r.json().get('data').get('children')
        for post in top:
            print(post.get('data').get('title'))
    except Exception as e:
        print(None)
