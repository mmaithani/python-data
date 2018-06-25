# Q.3- Using Tweepy library try to extract tweets 
# from Twitter.

#    ----------------------all key are wrong--------------

import tweepy

consumer_key_mohit ="FBtXscjgS4mcYdCgDQEyThpPbm"
consumer_secret_mohit ="zxcXXa4mMIaGd0NVfh9kQyNuLdkIV3VEVVIqZCdEiUW6hq2tTNm"
access_token_mohit= "3228687524-GZdECSsgj1f5qs0I0zBfkjWAZO8cqodNbbOGPhYm"
access_secret_mohit = "aH7u68bvTTeeMUEHmnTx9nZpGDRfyawEb4kvcqUXlcYkGm"
auth=tweepy.OAuthHandler(consumer_key_mohit,consumer_secret_mohit)
auth.set_access_token(access_token_mohit,access_secret_mohit)
api=tweepy.API(auth)

hastag="#"+input("enter the hastag you want to find:")
num=int(input("enter the number of text you want tp fetch:"))

tweets=api.search(hastag,lang="en",count=num,tweet_mode="extended")

for tweet in tweets:
	print(".....................")
	print(tweet.full_text)
	print(".....................")
