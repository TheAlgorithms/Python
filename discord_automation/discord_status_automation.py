import requests,time,json



headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': 'ENTER YOUR TOKEN',
    }

request = requests.Session()

def task():
    while True:
        
        response = requests.get("https://zenquotes.io/api/random").json()
        json_data =json.dumps(response)
        json_data =json.loads(json_data)
        quote = json_data [0] ['q'] + "-" + json_data [0] ['a']
        setting = {
                    'status': "idle",
                    'theme'	: "dark",
                    "custom_status": {"text": quote,},
                    }
            
        
        request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
        print(quote)
        
        time.sleep(15)
    

try:
    task()
except Exception as e:
    print(e)
    

