import requests
from fake_useragent import UserAgent


def get_google_search_results(query="potato", filename="") -> str:
    """Reads google search result page for the given query and
    stores it in a file.

    Args:
        query: The search term provided by the user. Defaults
        to "potato".
        filename (str, optional): The name of the file to be saved with the
        search results. Defaults to "".
    >>> get_google_search_results ("hacktober", "hacktober") != None
    True
    >>> get_google_search_results ("hacktober","") != None
    True
    >>> get_google_search_results ("", "hacktober") != None
    True
    >>> get_google_search_results ("", "") != None
    True

    """
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
    return filename


if __name__ == "__main__":
    query = input("Enter query: ")
    filename = input("Enter filename: ")
    print(f"Searching Google for {query} ....")
    filename = get_google_search_results(query, filename)
    print(f"File saved as {filename}")
