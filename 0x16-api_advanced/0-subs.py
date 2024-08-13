#!/usr/bin/python3

""" get subs in reddit"""

import requests


def number_of_subscribers(subreddit):
	headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
	response = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit), headers=headers, allow_redirects=False)
	
	if response.status_code == 404:
		return 0
	results = response.json().get("data")
	
	return results.get("subscribers")

