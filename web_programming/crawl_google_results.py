import sys
import webbrowser

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

<<<<<<< HEAD
print("Googling.....")
url = "https://www.google.com/search?q=" + " ".join(sys.argv[1:])
res = requests.get(url, headers={"UserAgent": UserAgent().random})
# res.raise_for_status()
with open("project1a.html", "wb") as out_file:  # only for knowing the class
    for data in res.iter_content(10000):
        out_file.write(data)
soup = BeautifulSoup(res.text, "html.parser")
links = list(soup.select(".eZt8xd"))[:5]

print(len(link))
for I in link:
    webbrowser.open(f"http://google.com{I.get('href')}")
=======

if __name__ == "__main__":
    print("Googling.....")
    url = "https://www.google.com/search?q=" + " ".join(sys.argv[1:])
    res = requests.get(url, headers={"UserAgent": UserAgent().random})
    # res.raise_for_status()
    with open("project1a.html", "wb") as out_file:  # only for knowing the class
        for data in res.iter_content(10000):
            out_file.write(data)
    soup = BeautifulSoup(res.text, "html.parser")
    links = list(soup.select(".eZt8xd"))[:5]

    print(len(links))
    for link in links:
        webbrowser.open(f"http://google.com{link.get('href')}")
>>>>>>> bd3e78321cc6a5cfffabf49e9b304ff5f04bf0ed
