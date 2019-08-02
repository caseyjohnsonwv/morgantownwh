import time, twitter, os


#load environment variables
try:
	CONSUMER_KEY = str(os.environ['CONSUMER_KEY'])
	CONSUMER_SECRET = str(os.environ['CONSUMER_SECRET'])
	ACCESS_TOKEN_KEY = str(os.environ['ACCESS_TOKEN_KEY'])
	ACCESS_TOKEN_SECRET = str(os.environ['ACCESS_TOKEN_SECRET'])
	ENV_NAME = str(os.environ['ENV_NAME'])
except Exception as ex:
	print("Failed to load environment variables.")
	print(ex)
	exit()


#authenticate to Twitter API
try:
	api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token_key=ACCESS_TOKEN_KEY, access_token_secret=ACCESS_TOKEN_SECRET)
except Exception as ex:
	print("Failed to authenticate to Twitter.")
	print(ex)
	exit()


#post update to @MorgantownWH on Twitter
def main():
	msg = 'No.'
	if 'prod' in ENV_NAME.lower():
		try:
			api.PostUpdate(msg)
		except Exception as ex:
			print("Failed to post update to Twitter.")
			print(ex)
			exit()
	else:
		print(msg)


if __name__ == "__main__":
	main()
