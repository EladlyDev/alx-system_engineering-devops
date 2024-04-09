#!/usr/bin/python3
""" 2. Recurse it! """
import requests


def recurse(subreddit, hot_list=[], next=''):
    """ prints the titles of all the hot posts listed
    for a given subreddit. (recursive) """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 next)
    headers = {"User-Agent": "ubuntu:Python"}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if not r.ok:
        return None

    try:
        top = r.json().get('data')
        hot_list.append(top.get('children')[0].get('data').get('title'))
        next = top.get('after')
        if next:
            recurse(subreddit, hot_list, next)
        return hot_list
    except Exception:
        return None
