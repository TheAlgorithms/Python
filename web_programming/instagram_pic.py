import requests
from bs4 import BeautifulSoup
import datetime


def DownloadSingleFile(URL):
    print("Downloading image...")
    req = requests.get(URL)
    soup = BeautifulSoup(req.content, "html.parser")
    metaTag = soup.find_all("meta", {"property": "og:image"})
    imgURL = metaTag[0]["content"]
    r = requests.get(imgURL)
    fileName = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + ".jpg"
    with open(fileName, "wb") as fp:
        fp.write(r.content)
    print("Done. Image saved to disk as " + fileName)


if __name__ == "__main__":
    url = input("Enter image url: ")
    DownloadSingleFile(url)
