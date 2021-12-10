'''
@author: Souvik Das
Institute: University at Buffalo
'''

import os
import pysolr
import requests
import json

# https://tecadmin.net/install-apache-solr-on-ubuntu/


CORE_NAME = "FINAL"
AWS_IP = "localhost"


# [CAUTION] :: Run this script once, i.e. during core creation


def delete_core(core=CORE_NAME):
    print(os.system('sudo su - solr -c "/opt/solr/bin/solr delete -c {core}"'.format(core=core)))


def create_core(core=CORE_NAME):
    print(os.system(
        'sudo su - solr -c "/opt/solr/bin/solr create -c {core} -n data_driven_schema_configs"'.format(
            core=core)))


class Indexer:
    def __init__(self):
        self.solr_url = f'http://{AWS_IP}:8983/solr/'
        self.connection = pysolr.Solr(self.solr_url + CORE_NAME, always_commit=True, timeout=5000000)

    def do_initial_setup(self):
        delete_core()
        create_core()

    def create_documents(self, docs):
        print(self.connection.add(docs))

    def add_fields(self):
        data = {
            "add-field": [
                {
                    "name": "poi_name",
                    "type": "string",
                    "multiValued": False,
                    "indexed":True,
                    "stored":True
                },
                {
                    "name": "poi_id",
                    "type": "plong",
                    "multiValued": False
                }, 
                {
                    "name": "verified",
                    "type": "boolean",
                    "multiValued": False
                },
                {
                    "name": "country",
                    "type": "string",
                    "multiValued": False,
                    "indexed": True,
                    "stored": True
                },
                {
                    "name": "replied_to_tweet_id",
                    "type": "plong",
                    "multiValued": False
                },
                {
                    "name": "replied_to_user_id",
                    "type": "plong",
                    "multiValued": False
                }, 
                {
                    "name": "reply_text",
                    "type": "text_general",
                    "multiValued": False
                },
                {
                    "name": "tweet_text",
                    "type": "text_general",
                    "multiValued": False,
                    "indexed":True,
                    "stored":True
                },
                {
                    "name": "tweet_lang",
                    "type": "string",
                    "multiValued": False,
                    "indexed":True,
                    "stored":True
                },
                {
                    "name": "text_en",
                    "type": "text_en",
                    "multiValued": False
                },
                {
                    "name": "text_es",
                    "type": "text_es",
                    "multiValued": False
                },
                {
                    "name": "text_hi",
                    "type": "text_hi",
                    "multiValued": False
                },
                {
                    "name": "hashtags",
                    "type": "string",
                    "multiValued": True
                }, 
                {
                    "name": "mentions",
                    "type": "string",
                    "multiValued": True
                },
                {
                    "name": "tweet_urls",
                    "type": "string",
                    "multiValued": True
                },
                {
                    "name": "tweet_emoticons",
                    "type": "string",
                    "multiValued": True
                },
                {
                    "name": "tweet_date",
                    "type": "pdate",
                    "multiValued": False
                },
                {
                    "name": "geolocation",
                    "type": "string",
                    "multiValued": False
                },
                {
                    "name": "Clean_text",
                    "type": "text_general",
                    "multiValued": False
                },
                {
                    "name": "Polarity",
                    "type": "pdouble",
                    "multiValued": False
                },
                {
                    "name": "a",
                    "type": "pdouble",
                    "multiValued": False
                },
                {
                    "name": "b",
                    "type": "pdouble",
                    "multiValued": False
                },
                {
                    "name": "c",
                    "type": "pdouble",
                    "multiValued": False
                },
                {
                    "name": "d",
                    "type": "pdouble",
                    "multiValued": False
                },
                {
                    "name": "e",
                    "type": "pdouble",
                    "multiValued": False
                },
                {
                    "name": "f",
                    "type": "pdouble",
                    "multiValued": False
                },
                {
                    "name": "g",
                    "type": "pdouble",
                    "multiValued": False
                },
                {
                    "name": "h",
                    "type": "pdouble",
                    "multiValued": False
                },
                {
                    "name": "i",
                    "type": "pdouble",
                    "multiValued": False
                },
                {
                    "name": "j",
                    "type": "pdouble",
                    "multiValued": False
                },
                {
                    "name": "k",
                    "type": "pdouble",
                    "multiValued": False
                },
                {
                    "name": "l",
                    "type": "pdouble",
                    "multiValued": False
                },
                {
                    "name": "m",
                    "type": "pdouble",
                    "multiValued": False
                },
                {
                    "name": "n",
                    "type": "pdouble",
                    "multiValued": False
                },
                {
                    "name": "o",
                    "type": "pdouble",
                    "multiValued": False
                },
                {
                    "name": "dominant_topic",
                    "type": "pdouble",
                    "multiValued": False
                }
            ]
        }

        print(requests.post(self.solr_url + CORE_NAME + "/schema", json=data).json())


if __name__ == "__main__":
    i = Indexer()
#     i.do_initial_setup()
#     i.add_fields()
    
    print("English tweets indexing..")
    f = open("cleaned_english_tweets_topic_modeled.json")
    doo = json.load(f)
    i.create_documents(doo)
    f.close()
    
    print("hindi tweets indexing..")
    
    f1 = open("cleaned_hindi_converted_tweets_topic_modeled.json")
    doo1 = json.load(f1)
    i.create_documents(doo1)
    f1.close()
    
    print("spanish tweets indexing..")
    f2 = open("cleaned_spanish_tweets_topic_modeled.json")
    doo2 = json.load(f2)
    i.create_documents(doo2)
    f2.close()
    print("indexing complete")
    
    

