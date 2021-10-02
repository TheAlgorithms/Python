import requests
from fake_useragent import UserAgent


def get_google_search_results(query: str = "potato") -> str:
    """Return a Google search result page for the given query.

    Args:
        query: The search term provided by the user. Defaults to "potato".

    >>> "hacktober" in get_google_search_results("hacktober")
    True
    >>> "potato" in get_google_search_results()
    True
    """
    url = f"https://www.google.com/search?q={query or 'potato'}"
    return requests.get(url, headers={"User-Agent": UserAgent().random}).text


def write_google_search_results(query: str = "", filename: str = "") -> str:
    """Stores a Google search result page for the given query into a local file.
    Args:
        query: The search term provided by the user.
        filename: The name of the file into which the search results should be
            saved.
    """
    filename = filename or query + "-query.html"
    if not filename.endswith(".html"):
        filename += ".html"

    with open(filename, "w") as out_file:
        out_file.write(get_google_search_results(query))
    return filename  # Just so the caller knows the filename.


if __name__ == "__main__":
    query = input("Enter query: ") or "potato"
    filename = input("Enter optional filename: ")
    print(f"Searching Google for {query} ....")
    filename = write_google_search_results(query, filename)
    print(f"File saved into {filename}")
