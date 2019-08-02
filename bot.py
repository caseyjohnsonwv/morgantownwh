import time, twitter, os

try:
	consumer_key = str(os.environ['CONSUMER_KEY'])
	consumer_secret = str(os.environ['CONSUMER_SECRET'])
	access_token_key = str(os.environ['ACCESS_TOKEN_KEY'])
	access_token_secret = str(os.environ['ACCESS_TOKEN_SECRET'])
except Exception as ex:
	print("Failed to load credentials.")
	exit()

try:
	api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token_key=ACCESS_TOKEN_KEY, access_token_secret=ACCESS_TOKEN_SECRET)
except Exception as ex:
	print("Failed to authenticate to Twitter.")
	exit()

try:
	api.PostUpdate('No.')
except Exception as ex:
	print("Failed to post update to Twitter.")
	exit()
