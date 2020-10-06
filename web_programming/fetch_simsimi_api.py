import requests
import json

_SIMSIMI_API = "https://wsapi.simsimi.com/190410/talk"
_SIMSIMI_API_KEY = "<Simsimi Api Key>"
_SIMSIMI_LANG = "<Bot Language>"

def bot_simsimi(question):
    headers = {"Content-Type": "application/json","x-api-key": "'+_SIMSIMI_API_KEY+'"}
    data = '{"utext":"'+question+'","lang": "'+_SIMSIMI_LANG+'"}'
    response = requests.post(_SIMSIMI_API, headers=headers, data=data)
    response_json = response.json()
    simsimi_answer = response_json['atext']
    print(simsimi_answer)

if __name__ == "main":
    bot_simsimi("<YOUR QUESTION>")
