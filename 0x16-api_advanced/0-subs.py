#!/usr/bin/python3

""" get subs in reddit"""

import requests


def number_of_subscribers(subreddit):
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0'}
	response = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit), headers=headers)
	
	if response.status_code != 200:
		return 0

	try:
		results = response.json()
		return results.get("data", {}).get("subscribers", 0)
	except ValueError:
		return 0 
