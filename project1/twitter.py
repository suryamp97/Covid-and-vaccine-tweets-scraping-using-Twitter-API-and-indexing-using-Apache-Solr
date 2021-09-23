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

    def get_replies(self,screen_name,keywords):
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
        poi_twids = [1438971071282257924, 1438563415757410307, 1437454033283866625, 1437116297192648717, 1435996498853040139, 1432373798699941890, 1430907893423894535, 1430603385825280007, 1429096019925606402, 1428363652340477968, 1427342394530451458, 1426261270718652420, 1423346832730738691, 1423013621181857799, 1422623525723152385, 1422286839457665031, 1419743573805699081, 1418257319411032067, 1418224314122395648, 1417148748577353728, 1415754050184912897, 1412861988850573323, 1412063726166056961, 1410629364727926784, 1409891919984054276, 1408527349709148165, 1405964538319708160, 1405616673588142082, 1404905743275507715, 1404091188978798592, 1403434469474832386, 1402366081910575106, 1400104926508851202, 1399803015683575809, 1396137541125001220, 1395778918737580033, 1395446727415459840, 1394705853714939913, 1394307001933500422, 1393332518838054912, 1389973312101564422, 1389239331961950213, 1388193956815638529, 1387816462744793090, 1387128173318574089, 1385279752907407368, 1384951586628251649, 1383438876778270729, 1380252596036894726, 1379483036979490824, 1379483029794607113, 1379483025763880981, 1379448862050508804, 1379448851094966278, 1378022168152391685, 1376986594104778763, 1376640364694605829, 1375522706280620032, 1375490492780150787, 1375132200295874562, 1374768479891550208, 1374740296278364163, 1372982726438092808, 1372276711065329664, 1371510056043343887, 1370471658834829317, 1369790740667265034, 1369033951587823630, 1367958119125508096, 1367537631664500737, 1367521495942053898, 1367498118200242177, 1365344161793253379, 1365034594114957312, 1362450565108797441, 1362087472436502528, 1361756230633590790, 1361729617548165124, 1361710729448067074, 1359961170510295040, 1358902150827560966, 1358874240758525954, 1357436953768116239, 1357391293786304516, 1356286566377926656, 1354887272517263365, 1354574425476243461, 1354519807673171968, 1353848055850741760, 1352028219063603202, 1350142392695988231, 1349058081225912321, 1348755323725688835, 1347619157450379269, 1346856597717446656, 1346225903039295488, 1345070785891885057, 1344769057720070144, 1344741626430816256, 1344432389834092544, 1344342593245765632, 1342943527555264515, 1341864731741724679, 1341840679354454023, 1341503792987205633, 1341503791514959873, 1339681787799334921, 1339614850155220994, 1339239149715517451, 1337453870474276867, 1335352003141230593, 1334541672747847681, 1334290759533596673, 1334265594846334978, 1333848431006191619, 1333501150482620416, 1332793900168310785, 1331689190396989447, 1331680319448223746, 1331660763979780098, 1331301578993786884, 1329529999771246593, 1329505975557087232, 1329468488688275458, 1329075541140332549, 1327371914004766720, 1326984370842906625, 1322280374911848454, 1321829320411799554, 1316789703081943042, 1314276126886330369, 1314269397121409027, 1313932608808517633, 1308781940842082304]
#         for tweet in tweepy.Cursor(self.api.user_timeline, screen_name=screen_name, count=3000).items(3000):    
#             tj=tweet._json
#             txt = tj["text"]
#             if any(k in txt for k in keys):
#                 if txt.startswith('RT @'):
#                     c=c+1
#                     if c<2:
#                         poi_twids.append(tj['id'])
#                 else :
#                     poi_twids.append(tj['id'])
        
#         print(poi_twids)
        print("covid tweets",len(poi_twids),screen_name)


        
        for idd in poi_twids:
            lim=0
            for tweet in tweepy.Cursor(self.api.search,q='to:{}'.format(screen_name),since_id= idd).items(500): 
                if lim>9 :
                    break
                tj = tweet._json
                txt = tj["text"]                
                repts = tj["in_reply_to_status_id"] 

                if int(repts) == idd:
                    if txt.startswith('RT @'):
                        c=c+1
                        if c<5:
                            tweets.append(tj)
                            lim=lim+1
                            #print(tj)
                    else :
                        tweets.append(tj)
                        lim=lim+1
                        #print(tj)
            print(idd," ",len(tweets))     
                 
        print("tot: ",len(tweets))
        return tweets
