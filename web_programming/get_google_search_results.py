import urllib.parse

import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

BASE_URL = "https://www.google.com"


def parse_results(query: str = "") -> list:
    """ "Reads google search result page for the given query and
    stores all the results in with title, link and descriptions
    in a list.
    Args:
        query (str): The search term provided by the user.
    Returns:
        list: list with search results

    >>> len(parse_results("python")) != None
    True
    >>> len(parse_results("")) == 0
    True
    """
    query = urllib.parse.quote_plus(query)
    url = "https://www.google.com/search?q=" + query
    response = None
    try:
        session = HTMLSession()
        response = session.get(url)

    except requests.exceptions.RequestException:
        return []

    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".IsZvec"
    results = response.html.find(css_identifier_result)
    soup = BeautifulSoup(response.html.html, "html.parser")
    stat_table = soup.find("table")
    if stat_table is None:
        return []
    table_data = stat_table.select("td a")
    next_page = []

    for item in table_data:
        next_page.append(item.attrs["href"])

    output = []

    for result in results:

        item = {
            "title": result.find(css_identifier_title, first=True).text,
            "link": result.find(css_identifier_link, first=True).attrs["href"],
            "text": result.find(css_identifier_text, first=True).text,
        }

        output.append(item)

    for next_page_link in next_page:
        new_link = BASE_URL + next_page_link
        try:
            session = HTMLSession()
            response = session.get(new_link)

        except requests.exceptions.RequestException:
            continue
        results = response.html.find(css_identifier_result)
        for result in results:

            item = {
                "title": result.find(css_identifier_title, first=True).text,
                "link": result.find(css_identifier_link, first=True).attrs["href"],
                "text": result.find(css_identifier_text, first=True).text,
            }

            output.append(item)
    return output


def write_google_search_results(query: str = "", filename: str = "") -> str:
    """Writes the Google search result page for the given query into a local file.
    Args:
        query: The search term provided by the user.
        filename: The name of the file into which the search results should be
            saved.

    Returns:
        str: The name of the file into which the search results were saved.

    >>> write_google_search_results("python", "test") != None
    True
    >>> write_google_search_results("", "tet.html") != None
    True
    >>> write_google_search_results("python", "") != None
    True
    >>> write_google_search_results("", "") != None
    True
    """
    if filename == "":
        filename = query + "-query.txt"
    elif not filename.endswith(".txt"):
        filename = filename + ".txt"
    response = parse_results(query)
    with open(filename, "w") as f:
        for item in response:
            f.write(f"Title: {item['title']}\n")
            f.write(f"Link: {item['link']}\n")
            f.write(f"Text: {item['text']}\n\n")

    return filename


if __name__ == "__main__":
    query = input("Enter query: ") or "potato"
    filename = input("Enter optional filename: ")
    print(f"Searching Google for {query} ....")
    filename = write_google_search_results(query, filename)
    print(f"File saved into {filename}")
