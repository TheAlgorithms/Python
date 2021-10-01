import sys
import webbrowser

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def crawl_and_store_google_search_result(query = "potato", filename=""):
    """This function will crawl google search result for the given query and store it in a file.

    Args:
        query (str, optional): The search term provided by the user. Defaults to "potato".
        filename (str, optional): The name of the file to be saved with the search results. Defaults to "".
    """
    if filename == "" :
        filename = query+"-query.html"
    elif not filename.endswith(".html"):
        filename = filename+".html"

    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    url = 'https://www.google.com/search?q=' + query
    response = requests.get(url, headers=headers)
    with open(filename, "wb") as out_file:  # only for knowing the class
        for data in response.iter_content(10000):
            out_file.write(data)
    print(f"File saved in {filename}")

if __name__ == "__main__":
    print("Googling.....")
    crawl_and_store_google_search_result(sys.argv[1]) 
 