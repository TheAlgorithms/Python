import sys
import webbrowser

from bs4 import BeautifulSoup
import requests

# fake_useragent is needed for so that this script is not viewed as a bot
from fake_useragent import UserAgent  # noqa: F401

user_agent = {
    "UserAgent": (
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) "
        "Gecko/20100101 Firefox/69.0"
    )
}
print("Googling.....")
url = "https://www.google.com/search?q=" + " ".join(sys.argv[1:])
res = requests.get(url, headers=user_agent)
# res.raise_for_status()
with open("project1a.html", "wb") as out_file:  # only for knowing the class
    for data in res.iter_content(10000):
        out_file.write(data)
soup = BeautifulSoup(res.text, "lxml")
links = list(soup.select(".eZt8xd"))[:5]

print(len(links))
for link in links:
    webbrowser.open(f"http://google.com{links.get('href')}")
