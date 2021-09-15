'''
@author: Souvik Das
Institute: University at Buffalo
'''

import tweepy


class Twitter:
    def __init__(self):
        self.auth = tweepy.OAuthHandler("AC7WkBbTptQM1F9vPvaWMnPu0", "6Kv4MuuLHX3FvB0PxNLZaa1ajyIIrnGqVQriBvmYzGD8u2fD3O")
        self.auth.set_access_token("1433835629763338242-SMviK8BJ5FcBnrrYBj9CMWIoDRX8Uu", "8hcho5OJ03WadpgMjfEgvUhzX3sOJ3DNWoIvOAyqc0sdc")
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def _meet_basic_tweet_requirements(self):
        '''
        Add basic tweet requirements logic, like language, country, covid type etc.
        :return: boolean
        '''
        raise NotImplementedError

    def get_tweets_by_poi_screen_name(self, screen_name):
        
        '''
        Use user_timeline api to fetch POI related tweets, some postprocessing may be required.
        :return: List
        '''
        tweets = []
        for tweet in tweepy.Cursor(api.user_timeline, screen_name=screen_name, count=10):
            tweet.append(tweet._json)

        return tweets

    def get_tweets_by_lang_and_keyword(self):
        '''
        Use search api to fetch keywords and language related tweets, use tweepy Cursor.
        :return: List
        '''
        raise NotImplementedError

    def get_replies(self):
        '''
        Get replies for a particular tweet_id, use max_id and since_id.
        For more info: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/guides/working-with-timelines
        :return: List
        '''
        raise NotImplementedError
