from twitter_auth import auth, api
import tweepy
from twitter_streamer import MyListener, MyManager
from multiprocessing import Process


def twitter_streaming():
    manager = MyManager(api)
    twitter_stream = tweepy.Stream(auth, MyListener("python.json", manager))
    twitter_stream.filter(track=['@RHIME_OpenHack'])


def f(name):
    print 'hello', name


if __name__ == '__main__':
    p_hello = Process(target=f, args=('bob',))
    p_twitter = Process(target=twitter_streaming)

    p_twitter.start()
    p_hello.start()

    p_twitter.join()
    p_hello.join()