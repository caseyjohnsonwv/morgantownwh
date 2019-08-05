import time, twitter, os
from email.utils import parsedate
from datetime import date


#load environment variables
try:
	ACCESS_TOKEN_KEY = str(os.environ['ACCESS_TOKEN_KEY'])
	ACCESS_TOKEN_SECRET = str(os.environ['ACCESS_TOKEN_SECRET'])
	BOT_TWITTER_ID = int(os.environ['BOT_TWITTER_ID'])
	CONSUMER_KEY = str(os.environ['CONSUMER_KEY'])
	CONSUMER_SECRET = str(os.environ['CONSUMER_SECRET'])
	ENV_NAME = str(os.environ['ENV_NAME'])
	PERSONAL_TWITTER_ID = int(os.environ['PERSONAL_TWITTER_ID'])
except Exception as ex:
	print("Failed to load environment variables.")


#authenticate to Twitter API
try:
	api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token_key=ACCESS_TOKEN_KEY, access_token_secret=ACCESS_TOKEN_SECRET)
except Exception as ex:
	print("Failed to authenticate to Twitter.")
	exit()


#post update to @MorgantownWH on Twitter
def main():
	print("Creating tweet.")
	tweet = 'No.'

	print("Creating analytics DM.")
	try:
		bot_account = api.GetUser(user_id=BOT_TWITTER_ID)
		last_tweet = api.GetUserTimeline(user_id=BOT_TWITTER_ID, count=1)[0]
		data = [
			bot_account.followers_count,
			date(*list(parsedate(last_tweet.created_at))[:3]),
			last_tweet.retweet_count,
			last_tweet.favorite_count,
		]
		msg = """
Followers: {}
---
Last Tweet:
Date: {}
RTs: {}
Likes: {}
		""".format(*data)
	except Exception as ex:
		print("Failed to create analytics DM.")
		print(ex)

	if 'prod' in ENV_NAME.lower():
		print("Posting update to Twitter.")
		try:
			api.PostUpdate(tweet)
		except Exception as ex:
			print("Failed to post update to Twitter.")
			print(ex)
			exit()

		print("Sending analytics DM.")
		try:
			api.PostDirectMessage(msg, user_id=PERSONAL_TWITTER_ID)
		except Exception as ex:
			print("Failed to send analytics DM.")
			print(ex)
	else:
		print(tweet)
		print(msg)


if __name__ == "__main__":
	main()
