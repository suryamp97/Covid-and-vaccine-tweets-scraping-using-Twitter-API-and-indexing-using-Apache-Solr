'''
@author: Souvik Das
Institute: University at Buffalo
'''

import demoji, re, datetime
import preprocessor


# demoji.download_codes()


class TWPreprocessor:
    @classmethod
    def preprocess(cls, tweet, context):
        '''
        Do tweet pre-processing before indexing, make sure all the field data types are in the format as asked in the project doc.
        :param tweet:
        :return: dict
        '''
        tw = {}
        lang = tweet["lang"]
        country=""
        reply_text=""
        if lang=="en":
            country="USA"
            #clean_text = re.sub(r"(http|https|www|@|#)\S+", " ", tweet["text"])
            tw["text_en"]=_text_cleaner(tweet["text"])
            reply_text = tw["text_en"]
        if lang=="es":
            country="MEXICO"
            #clean_text = re.sub(r"(http|https|www|@|#)\S+", " ", tweet["text"])
            tw["text_es"]=_text_cleaner(tweet["text"])
            reply_text = tw["text_es"]
        if lang=="hi":
            country="INDIA"
            #clean_text = re.sub(r"(http|https|www|@|#)\S+", " ", tweet["text"])
            tw["text_hi"]=_text_cleaner(tweet["text"])
            reply_text = tw["text_hi"]
        
        # mandatory fields
        tw["id"]            = tweet["id"]
        tw["country"]       = country
        tw["tweet_lang"]    = tweet["lang"]
        tw["tweet_text"]    = tweet["text"]
        tw["tweet_date"]    = str(_get_tweet_date(tweet["created_at"]))
        tw["verified"]      = tweet["user"]["verified"]
        
        if context == "poi":
            tw["poi_id"]        = tweet["user"]["id"]
            tw["poi_name"]      = tweet["user"]["screen_name"]
            
        if context == "reply":
            tw["replied_to_tweet_id"] = tweet["in_reply_to_status_id"]
            tw["replied_to_user_id"]  = tweet["in_reply_to_user_id"]
            tw["reply_text"]          = reply_text
        
        tw["hashtags"]          = _get_entities(tweet,'hashtags')
        tw["mentions"]          = _get_entities(tweet,'mentions')
        tw["tweet_urls"]        = _get_entities(tweet,'urls')
        #tw["tweet_emoticons"]   = _get_entities(tweet,'symbols')                    
                            
        return tw


def _get_entities(tweet, type=None):
    result = []
    if type == 'hashtags':
        hashtags = tweet['entities']['hashtags']

        for hashtag in hashtags:
            result.append(hashtag['text'])
    elif type == 'mentions':
        mentions = tweet['entities']['user_mentions']

        for mention in mentions:
            result.append(mention['screen_name'])
    elif type == 'urls':
        urls = tweet['entities']['urls']

        for url in urls:
            result.append(url['url'])
                      

    return result


def _text_cleaner(text):
    
    emoticons_happy = list([
        ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
        ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
        '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
        'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
        '<3'
    ])
    emoticons_sad = list([
        ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
        ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
        ':c', ':{', '>:\\', ';('
    ])
    all_emoticons = emoticons_happy + emoticons_sad

    emojis = list(demoji.findall(text).keys())
    clean_text = demoji.replace(text, '')

    for emo in all_emoticons:
        if (emo in clean_text):
            clean_text = clean_text.replace(emo, '')
            emojis.append(emo)
    

    
    #removing punctuations
    punc = "!()-[]{};:'\"\,<>./?$%^&*_~"
    for p in punc:
        if (p in clean_text):
            clean_text =  clean_text.replace(p,'')
        
    
    
    
    # preprocessor.set_options(preprocessor.OPT.EMOJI, preprocessor.OPT.SMILEY)
    # emojis= preprocessor.parse(text)
    

    return clean_text


def _get_tweet_date(tweet_date):
    return _hour_rounder(datetime.datetime.strptime(tweet_date, '%a %b %d %H:%M:%S +0000 %Y'))


def _hour_rounder(t):
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour)
            + datetime.timedelta(hours=t.minute // 30))
