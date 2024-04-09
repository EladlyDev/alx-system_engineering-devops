#!/usr/bin/python3
""" Contains the subs function """
import requests


def number_of_subscribers(subreddit):
    """  queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ubuntu:Python"}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.ok:
        subs = r.json().get('data').get('subscribers')
        return subs if subs else 0
    return 0
