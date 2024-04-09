#!/usr/bin/python3
""" 3. Count it! """
import requests


def count_words(subreddit, word_list, next='', found={}):
    """ prints the titles of all the hot posts listed
    for a given subreddit. (recursive) """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 next)
    headers = {"User-Agent": "ubuntu:Python"}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if not r.ok:
        return

    try:
        data = r.json().get('data')
        post = data.get('children')[0].get('data')
        words = post.get('title').lower().split(' ')
        for word in word_list:
            word = word.lower()
            if word in words:
                if word in found:
                    found[word] += 1
                else:
                    found[word] = 0
        next = data.get('after')
        if next:
            count_words(subreddit, word_list, next=next, found=found)
        else:
            found = dict(sorted(found.items(), key=lambda item:
                                (-item[1], item[0])))
            for k, v in found.items():
                if v > 0:
                    print('{}: {}'.format(k, v))
    except Exception as e:
        pass
