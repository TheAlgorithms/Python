# imports
import requests, json
# beautifulsoup4
from bs4 import BeautifulSoup

def searchDisplay(username):
    # base url for the data
    url = 'https://www.instagram.com/{}/'.format(username)
    try:
        req = requests.get(url).content
        soup=BeautifulSoup(req,"html.parser")
        row=soup.find_all('script')
        details=str(row[3]).strip("<script type=></")[22:].strip()
        account=json.loads(details)
        try:
            if len(account['description'])<1:
                account['description']=""
        except:
            account['description']=""
        print("Name : ",account['name'],'\t',"Username : ",account['alternateName'],
              '\t',"Followers : ",account['mainEntityofPage']['interactionStatistic']['userInteractionCount'],'\n',
              "Bio : ",account['description'])
    except:
        print('Not found or no internet connection')

if __name__ == "__main__":
    while True:
        username = input("Enter a username:").strip()
        if username:
            searchDisplay(username)
        else:
            break
