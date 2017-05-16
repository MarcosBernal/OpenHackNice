import json
import random
from tweepy.streaming import StreamListener
from sfCreateTicket import create_sf_ticket


class MyListener(StreamListener):
    def __init__(self, file_name, manager):
        super(MyListener, self).__init__()
        self.file_name = file_name
        self.manager = manager

    def on_data(self, data):
        try:
            with open(self.file_name, 'a') as f:
                f.write(data)
                tweet = json.loads(data.decode('utf-8'))
                print("Received new tweet", tweet['text'], tweet['user'])
                self.manager.analyse_new_tweet(tweet)
                print("Analyzed new tweet")
                return True
        except BaseException as e:
            print("Error on_data: " % str(e))
            return True

    def on_error(self, status_code):
        if status_code == 420:
            print("Reached limit of tweets", status_code)
            # returning False in on_data s the stream
            return False
        else:
            print("Unknown error", status_code)
            # returning False in on_data s the stream
            return False


class MyManager:
    def __init__(self, api):
        self.api = api

    def analyse_new_tweet(self, tweet):
        text = tweet['text']
        user = tweet['user']['screen_name']

        if tweet['geo'] is None or tweet['geo']['coordinates'] is None:
            position = [18, 15]
        #    new_tweet = "Thanks @" + user + ", please add position and image for investigating the issue. ID:" + str(random.randint(00000, 99999))
        #    self.post_tweet(new_tweet)

        else:
            position = self.get_position(tweet)

        image = None

        if 'entities' in tweet and 'media' in tweet['entities']:
            for media_metadata in tweet['entities']['media']:
                image = media_metadata['media_url_https']
                print "There is image in " + str(image)

        new_tweet = "Thanks @"+user+" for the feedback. From lat:" + str(position[0]) +" lon:"+ str(position[1]) +" Generating Public ID:" + str(random.randint(00000, 99999))
        self.post_tweet(new_tweet)
        self.trigger_new_case(user, text, position[0], position[1], image)

    def post_tweet(self, tweet):
        if len(tweet) < 140:
            self.api.update_status(status=tweet)

    def trigger_new_case(self, user, text, lat, lon, image):
        create_sf_ticket(user, text, lat, lon)
        print "Created new Ticket!"

    def checking_possible_spam(self):
        pass

    def get_position(self, tweet):
        if tweet['geo'] is not None:
            return tweet['geo']['coordinates']
        else:
            return None