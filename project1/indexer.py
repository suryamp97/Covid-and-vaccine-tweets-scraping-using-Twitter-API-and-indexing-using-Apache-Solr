'''
@author: Souvik Das
Institute: University at Buffalo
'''

import os
import pysolr
import requests

# https://tecadmin.net/install-apache-solr-on-ubuntu/


CORE_NAME = "IRF21P1"
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
                    "multiValued": False
                },
                {
                    "name": "poi_id",
                    "type": "string",
                    "multiValued": False
                }, {
                    "name": "verified",
                    "type": "string",
                    "multiValued": False
                },
                {
                    "name": "country",
                    "type": "pint",
                    "multiValued": False
                },
                {
                    "name": "id",
                    "type": "plongs",
                    "multiValued": True
                },
                {
                    "name": "replied_to_tweet_id",
                    "type": "string",
                    "multiValued": False
                },
                {
                    "name": "replied_to_user_id",
                    "type": "string",
                    "multiValued": False
                }, 
                {
                    "name": "reply_text",
                    "type": "string",
                    "multiValued": False
                },
                {
                    "name": "tweet_text",
                    "type": "pint",
                    "multiValued": False
                },
                {
                    "name": "tweet_lang",
                    "type": "plongs",
                    "multiValued": True
                },
                {
                    "name": "text_xx",
                    "type": "string",
                    "multiValued": False
                },
                {
                    "name": "hashtags",
                    "type": "string",
                    "multiValued": False
                }, 
                {
                    "name": "mentions",
                    "type": "string",
                    "multiValued": False
                },
                {
                    "name": "tweet_urls",
                    "type": "pint",
                    "multiValued": False
                },
                {
                    "name": "tweet_emoticons",
                    "type": "plongs",
                    "multiValued": True
                },
                {
                    "name": "tweet_date",
                    "type": "string",
                    "multiValued": False
                },
                {
                    "name": "geolocation",
                    "type": "pint",
                    "multiValued": False
                }
            ]
        }

        print(requests.post(self.solr_url + CORE_NAME + "/schema", json=data).json())


if __name__ == "__main__":
    i = Indexer()
    i.do_initial_setup()
    i.add_fields()
