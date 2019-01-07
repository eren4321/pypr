import tweepy
import datetime
from pymongo import MongoClient


class Bot:

    def __init__(self):
        self.CONSUMER_KEY = "YrP8jnprZn1ouxFB57GBItrW6e"
        self.CONSUMER_KEY_SECRET = "RyiJvk7re05fPYh3LxXNUUmfY4qn8fW6Jza4cNWxGc1DkdBPBIe"
        self.ACCESS_TOKEN = "840827114387562496-zLew76EvM4w99TMGTqI3eX00zOPXdvbe"
        self.ACCESS_TOKEN_SECRET = "dapuxS6sG3r26dZpsfTzeC6uYeJ8jaqDbuc5pjjtr3PkNe"
        self.api = self.authenticate()
        self.user_list = []

    def authenticate(self):
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_KEY_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)

        try:
            api.verify_credentials()
        except Exception as e:
            print(e)
            print('Bot baglanamadi, key ve tokenları kontrol ediniz')
        else:
            print('Bot basarılı bir sekilde baglandı')
            return api

    def kanald(self, max_tweets=100):

        try:
            conn = MongoClient()
            print("Connected successfully!!!")
        except:
            print("Could not connect to MongoDB")

        conn = MongoClient("mongodb://localhost:27017/")
        db = conn.mydatabase
        collection = db.kanald
        searched_tweets = []
        last_id = -1
        max_tweets = max_tweets
        conf = db.settings.find_one({"name": "kanald"})
        print(conf["last_id"])
        last = conf["last_id"]
        tmm = conf["tm"]
        print(tmm)
        while len(searched_tweets) < max_tweets:
            count = max_tweets - len(searched_tweets)
            a = last
            try:
                new_tweets = self.api.search(
                    q="#kanald -filter:retweets",
                    count=count,
                    lang='tr',
                    # since_id=a,
                    max_id=str(last_id - 1),
                    tweet_mode='extended'

                )

                if not new_tweets:
                    break
                searched_tweets.extend(new_tweets)
                last_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                print('Error', str(e))
                break

        for tweet in reversed(searched_tweets):
            db.kanald.update({}, {
                "$set": {
                    'tweet': tweet.full_text,
                    'retweet': int(tweet.retweet_count),
                    'favorite': int(tweet.favorite_count),
                    'created': tweet.created_at,
                    "tarih": datetime.datetime.utcnow(),
                    "username": tweet.user.name,
                    "description": tweet.user.description,
                    "friends_count": tweet.user.friends_count,
                    "followers_count": tweet.user.followers_count,
                    "id": tweet.id

                }})

    def __init__(self):
        self.CONSUMER_KEY = "YrP8jnprZn1ouxFB57GBItrW6"
        self.CONSUMER_KEY_SECRET = "RyiJvk7re05fPYh3LxXNUUmfY4qn8fW6Jza4cNWxGc1DkdBPBI"
        self.ACCESS_TOKEN = "840827114387562496-zLew76EvM4w99TMGTqI3eX00zOPXdvb"
        self.ACCESS_TOKEN_SECRET = "dapuxS6sG3r26dZpsfTzeC6uYeJ8jaqDbuc5pjjtr3PkN"
        self.api = self.authenticate()
        self.user_list = []

    def authenticate(self):
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_KEY_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)

        try:
            api.verify_credentials()
        except Exception as e:
            print(e)
            print('Bot baglanamadi, key ve tokenları kontrol ediniz')
        else:
            print('Bot basarılı bir sekilde baglandı')
            return api

    def hurriyet(self, max_tweets=100):

        try:
            conn = MongoClient()
            print("Connected successfully!!!")
        except:
            print("Could not connect to MongoDB")

        conn = MongoClient("mongodb://localhost:27017/")
        db = conn.mydatabase
        collection = db.hurriyet
        searched_tweets = []
        last_id = -1
        max_tweets = max_tweets
        conf = db.settings.find_one({"name": "hurriyet"})
        print(conf["last_id"])
        last = str(conf["last_id"])
        tmm = conf["tm"]
        print(tmm)
        while len(searched_tweets) < max_tweets:
            count = max_tweets - len(searched_tweets)
            try:
                new_tweets = self.api.search(
                    q="#hürriyet -filter:retweets",
                    count=count,
                    lang='tr',
                    # since_id=last,
                    max_id=str(last_id - 1),
                    tweet_mode='extended'

                )

                if not new_tweets:
                    break
                searched_tweets.extend(new_tweets)
                last_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                print('Error', str(e))
                break

        for tweet in reversed(searched_tweets):
            db.hurriyet.update({}, {
                "$set": {
                    'tweet': tweet.full_text,
                    'retweet': int(tweet.retweet_count),
                    'favorite': int(tweet.favorite_count),
                    'created': tweet.created_at,
                    "tarih": datetime.datetime.utcnow(),
                    "username": tweet.user.name,
                    "description": tweet.user.description,
                    "friends_count": tweet.user.friends_count,
                    "followers_count": tweet.user.followers_count,
                    "id": tweet.id

                }})

    def __init__(self):
        self.CONSUMER_KEY = "YrP8jnprZn1ouxFB57GBItrW6"
        self.CONSUMER_KEY_SECRET = "RyiJvk7re05fPYh3LxXNUUmfY4qn8fW6Jza4cNWxGc1DkdBPBI"
        self.ACCESS_TOKEN = "840827114387562496-zLew76EvM4w99TMGTqI3eX00zOPXdvb"
        self.ACCESS_TOKEN_SECRET = "dapuxS6sG3r26dZpsfTzeC6uYeJ8jaqDbuc5pjjtr3PkN"
        self.api = self.authenticate()
        self.user_list = []

    def authenticate(self):
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_KEY_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)

        try:
            api.verify_credentials()
        except Exception as e:
            print(e)
            print('Bot baglanamadi, key ve tokenları kontrol ediniz')
        else:
            print('Bot basarili bir sekilde baglandi')
            return api

    def cnn(self, max_tweets=100):

        try:
            conn = MongoClient()
            print("Connected successfully!!!")
        except:
            print("Could not connect to MongoDB")

        conn = MongoClient("mongodb://localhost:27017/")
        db = conn.mydatabase
        collection = db.cnn
        searched_tweets = []
        last_id = -1
        max_tweets = max_tweets

        while len(searched_tweets) < max_tweets:
            count = max_tweets - len(searched_tweets)
            try:
                new_tweets = self.api.search(
                    q="#cnn -filter:retweets",
                    count=count,
                    lang='tr',
                    max_id=str(last_id - 1),
                    tweet_mode='extended'

                )

                if not new_tweets:
                    break
                searched_tweets.extend(new_tweets)
                last_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                print('Error', str(e))
                break

        for tweet in reversed(searched_tweets):
            db.cnn.update({}, {
                "$set": {
                    'tweet': tweet.full_text,
                    'retweet': int(tweet.retweet_count),
                    'favorite': int(tweet.favorite_count),
                    'created': tweet.created_at,
                    "tarih": datetime.datetime.utcnow(),
                    "username": tweet.user.name,
                    "description": tweet.user.description,
                    "friends_count": tweet.user.friends_count,
                    "followers_count": tweet.user.followers_count,
                    "id": tweet.id

                }})

    def __init__(self):
        self.CONSUMER_KEY = "YrP8jnprZn1ouxFB57GBItrW6"
        self.CONSUMER_KEY_SECRET = "RyiJvk7re05fPYh3LxXNUUmfY4qn8fW6Jza4cNWxGc1DkdBPBI"
        self.ACCESS_TOKEN = "840827114387562496-zLew76EvM4w99TMGTqI3eX00zOPXdvb"
        self.ACCESS_TOKEN_SECRET = "dapuxS6sG3r26dZpsfTzeC6uYeJ8jaqDbuc5pjjtr3PkN"
        self.api = self.authenticate()
        self.user_list = []

    def authenticate(self):
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_KEY_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)

        try:
            api.verify_credentials()
        except Exception as e:
            print(e)
            print('Bot baglanamadi, key ve tokenları kontrol ediniz')
        else:
            print('Bot basarılı bir sekilde baglandı')
            return api

    def milliyet(self, max_tweets=100):

        try:
            conn = MongoClient()
            print("Connected successfully!!!")
        except:
            print("Could not connect to MongoDB")

        conn = MongoClient("mongodb://localhost:27017/")
        db = conn.mydatabase
        collection = db.milliyet
        searched_tweets = []
        last_id = -1
        max_tweets = max_tweets
        conf = db.settings.find_one({"name": "milliyet"})
        print(conf["last_id"])
        last = str(conf["last_id"])
        tmm = conf["tm"]
        print(tmm)
        while len(searched_tweets) < max_tweets:
            count = max_tweets - len(searched_tweets)
            try:
                new_tweets = self.api.search(
                    q="#milliyet -filter:retweets",
                    count=count,
                    lang='tr',
                    # since_id=last,
                    max_id=str(last_id - 1),
                    tweet_mode='extended'

                )

                if not new_tweets:
                    break
                searched_tweets.extend(new_tweets)
                last_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                print('Error', str(e))
                break

            for tweet in reversed(searched_tweets):
                        db.milliyet.upsert({}, {
                            "$set": {
                                'tweet': tweet.full_text,
                                'retweet': int(tweet.retweet_count),
                                'favorite': int(tweet.favorite_count),
                                'created': tweet.created_at,
                                "tarih": datetime.datetime.utcnow(),
                                "username": tweet.user.name,
                                "description": tweet.user.description,
                                "friends_count": tweet.user.friends_count,
                                "followers_count": tweet.user.followers_count,
                                "id": tweet.id

                            }})


a = Bot()
a.milliyet()
a.cnn()
a.hurriyet()
a.kanald()
