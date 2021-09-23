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
        c=0
        for tweet in tweepy.Cursor(self.api.user_timeline, screen_name=screen_name, count=2500).items(2500):    
            tj=tweet._json
            txt = tj["text"]
            if txt.startswith('RT @'):
                c=c+1
                if c<200:
                    tweets.append(tj)
            else :
                tweets.append(tj)
        return tweets

    def get_tweets_by_lang_and_keyword(self,keyword):
        '''
        Use search api to fetch keywords and language related tweets, use tweepy Cursor.
        :return: List
        '''
        tweets = []
        c=0
        for tweet in tweepy.Cursor(self.api.search,q=keyword, count=7500).items(7500):  
            tj=tweet._json
            verified = tj["user"]["verified"]
            txt = tj["text"]
            if not verified:
                if txt.startswith('RT @'):
                    c=c+1
                    if c<1000:
                        tweets.append(tj)
                else :
                    tweets.append(tj)
        return tweets

    def get_replies(self,pois,keywords):
        '''
        Get replies for a particular tweet_id, use max_id and since_id.
        For more info: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/guides/working-with-timelines
        :return: List
        '''
        keys = []
        for i in range(25):
            keys.append(keywords[i]['name'])

        tweets = []
        c=0
        poi_twids = []
        for i in range(len(pois)):
            sc_name = pois[i]['screen_name']
            for tweet in tweepy.Cursor(self.api.user_timeline, screen_name=sc_name, count=3000).items(3000):    
                tj=tweet._json
                txt = tj["text"]
                if any(k in txt for k in keys):
                    if txt.startswith('RT @'):
                        c=c+1
                        if c<2:
                            poi_twids.append(tj['id'])
                    else :
                        poi_twids.append(tj['id'])
            print(sc_name,i+1," complete")                
        
        print()
        print(poi_twids)
        print()
        print("covid tweets",len(poi_twids))
        

        
#         for idd in poi_twids:
#             lim=0
#             for tweet in tweepy.Cursor(self.api.search,q='to:{}'.format(screen_name),since_id= idd,count=1000).items(1000): 
#                 if lim>9 :
#                     break
#                 tj = tweet._json
#                 txt = tj["text"]                
#                 repts = tj["in_reply_to_status_id"] 

#                 if repts == idd:
#                     if txt.startswith('RT @'):
#                         c=c+1
#                         if c<5:
#                             tweets.append(tj)
#                             lim=lim+1
#                             #print(tj)
#                     else :
#                         tweets.append(tj)
#                         lim=lim+1
#                         #print(tj)
#             print(idd," ",len(tweets))     
                 
#         print("tot: ",len(tweets))
        return tweets
