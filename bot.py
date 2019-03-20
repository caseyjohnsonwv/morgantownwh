import time
import twitter

api = twitter.Api(	consumer_key = "WmJlz4YogcfCFHf78G45JmQ4W",
					consumer_secret = "2IEun9ZcYnBhwF30di4X3PxnAh8gA76KrauT1Tst0HGdOwrlN9",
					access_token_key = "1108033076167364608-F7pygEJqqu50bESbG7Pjw60z1gjHf6",
					access_token_secret = "ZhoUJbggGsu1F06pTgc7vPaZ3C7LEq2GMvSBhkYKfrMHV")
					
old_followers = 0
while True:
#analytics DM

	account = api.GetUser(user_id=1108033076167364608)
	rts = account.status.retweet_count
	likes = account.status.favorite_count

	followers = account.followers_count
	delta_followers = followers - old_followers

	if (delta_followers >= 0):
		df_string = "+%d" % (delta_followers)
	else:
		df_string = "-%d" % (delta_followers)

	msg = "Last Tweet Analytics:\nRTs: %d\nLikes: %d\n\nAccount Analytics:\nFollowers: %d (%s)" % (rts, likes, followers, df_string)

	api.PostDirectMessage(msg, user_id=403837992)
	old_followers = followers
#end analytics DM
	
	api.PostUpdate('No.')
	time.sleep(86400)
	
#after pushing, call 'heroku ps:scale worker=1' to init one instance