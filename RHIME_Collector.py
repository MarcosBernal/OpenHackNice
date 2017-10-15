from twitter_streamer import TwitterStream
from multiprocessing import Process


def twitter_streaming():
    twitter_stream = TwitterStream(storing_filename="python.json")
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