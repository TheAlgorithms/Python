
//Toot daily one Tamil word on mastodon

//daily_oneword_toot.py

from __future__ import unicode_literals
import back4app
import toot
import os

from secret_keys import *
from mastodon import Mastodon
from sys import argv

//connect to mastodon using api key
def connect():
    mastodon = Mastodon(access_token = 'GZ4dEVxYNAO3n__fEskXMPf0VMg4aQm0yURL-eJAU9Q',api_base_url = 'https://mastodon.social')
    return mastodon


if __name__ == "__main__":
    api = connect()
    mine = back4app.Back4App()

    status = mine.get_sentance()
    print(status)

    if status is not None and len(status) < 210:
        if not DEBUG:
            post_word=api.toot(status)
        #print(repr(status))
        #print(post_word)

    elif not status:
        print("Status is empty, sorry.")
    else:
        print("TOO LONG: " + status)






//back4app.py


import requests
import json
from secret_keys import *


def get_headers():
    return {
        'X-Parse-Application-Id': X_PARSE_APPLICATION_ID,
        'X-Parse-REST-API-Key': X_PARSE_REST_API_KEY,
        'Content-Type': 'application/json'
    }


def update_status(objectId):
    url = "https://parseapi.back4app.com/classes/WordCorpus/"+objectId
    payload = {'status': True}
    header = get_headers()
    response = requests.put(url, data=json.dumps(payload), headers=header)
    print(response.text)
    return response.status_code

class Back4App():
    def get_sentance(self):
        header = get_headers()
        url = "https://parseapi.back4app.com/classes/WordCorpus?where=%7B%22status%22%3Afalse%7D"
        data = requests.get(url, headers=header)
        print(data)
        json_response = data.json()
        print(json_response)
        results = json_response['results'][0]
        #for i in results['meaning']:
            #print(i)

        sentence = ("சொல் : %s \n பொருள் : %s" %
                    (results['word'], results['meaning']))
        update_status(results['objectId'])
        tags = "\n#தினமொரு #தமிழ்_சொல்"
        return sentence+tags


if __name__ == "__main__":
    print("Try running daily_one_word.py first")




//secrete_keys.py

from os import environ


# Configuration for Parse API
X_PARSE_APPLICATION_ID = 'your_account_appication_id'
X_PARSE_REST_API_KEY = 'Api_key'
DEBUG = False  # Set this to False to start Tweeting live
ODDS = 8
