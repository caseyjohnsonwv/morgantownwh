import time, twitter, os

try:
	consumer_key = os.environ['CONSUMER_KEY']
	consumer_secret = os.environ['CONSUMER_SECRET']
	access_token_key = os.environ['ACCESS_TOKEN_KEY']
	access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
except Exception as ex:
	print("Failed to load credentials.")

try:
	api = twitter.Api(	consumer_key = "WmJlz4YogcfCFHf78G45JmQ4W",
						consumer_secret = "2IEun9ZcYnBhwF30di4X3PxnAh8gA76KrauT1Tst0HGdOwrlN9",
						access_token_key = "1108033076167364608-F7pygEJqqu50bESbG7Pjw60z1gjHf6",
						access_token_secret = "ZhoUJbggGsu1F06pTgc7vPaZ3C7LEq2GMvSBhkYKfrMHV")
except Exception as ex:
	print("Failed to authenticate to Twitter.")

try:
	api.PostUpdate('No.')
except Exception as ex:
	print("Failed to post update to Twitter.")
