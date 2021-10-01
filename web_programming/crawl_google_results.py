import sys
import requests
from fake_useragent import UserAgent


def crawl_and_store_google_search_result(query="potato", filename=""):
    """Crawl google search result for the given query and
    store it in a file.

    Args:
        query: The search term provided by the user. Defaults
        to "potato".
        filename (str, optional): The name of the file to be saved with the
        search results. Defaults to "".
    >>> crawl_and_store_google_search_result ("hacktober", "hacktober")
    File saved in hacktober.html
    >>> crawl_and_store_google_search_result ("hacktober", "hacktober.html")
    File saved in hacktober.html
    >>> crawl_and_store_google_search_result ("hacktober")
    File saved in hacktober-query.html
    """
    print(f"Searching Google for {query} ....")
    if filename == "":
        filename = query + "-query.html"
    elif not filename.endswith(".html"):
        filename = filename + ".html"

    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    url = "https://www.google.com/search?q=" + query
    response = requests.get(url, headers=headers)
    with open(filename, "wb") as out_file:  # only for knowing the class
        for data in response.iter_content(10000):
            out_file.write(data)
    print(f"File saved as {filename}")


if __name__ == "__main__":
    crawl_and_store_google_search_result(sys.argv[1])
