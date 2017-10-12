import tweepy
from tweepy import OAuthHandler


# Marcos Twitter
consumer_key = NOT_DEFINED
consumer_secret = NOT_DEFINED
access_token = NOT_DEFINED
access_secret = NOT_DEFINED

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)