import requests 
import time

username = input("Enter your username here:")

def wrapper(fetch):
  def timing():
      start = time.time()
      fetch()
      end = time.time()
      print(f"Total execution time: {end-start:.4f}")
  return timing

@wrapper
def fetch():
  api = f"https://api.github.com/users/{username}"
  res = requests.get(api)

  if res.status_code != 200:
      print("Error fetching data")
      return

  else:
    data = res.json()
    print(f"Username : {username}")
    print(f"Name: {data.get('name','N/A')}" )
    print(f"Bio: {data.get('bio',None)}")
    print(f"Public Repos: {data.get('public_repos',None)}")
    print(f"Followers: {data.get('followers',None)}")
    print(f"Following: {data.get('following',None)}")
    print(f"Profile Link: {data.get('url',None)}")

fetch()