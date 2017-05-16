import tweepy
from tweepy import OAuthHandler


# Marcos Twitter
consumer_key = X
consumer_secret = X
access_token = X
access_secret = X

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)