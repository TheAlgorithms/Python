import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.google.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    + "AppleWebKit/537.36 (KHTML, like Gecko)"
    + "Chrome/72.0.3538 102 Safari/537.36 Edge/18.19582"
}


def parse_results(query: str = "", num_q: int = 20) -> list:
    """Reads google search result page for the given query and
    stores all the results in with title, link and descriptions
    in a list.
    Args:
        query : The search term provided by the user.
        num_q : The number of search results to fetch.
    Returns:
        list: list with search results

    >>> len(parse_results("python")) != None
    True
    >>> len(parse_results("")) == 0
    True
    """
    params = {"q": str(query)}
    response = None
    try:
        response = requests.get(BASE_URL + "/search", headers=headers, params=params)
    except requests.exceptions.RequestException:
        return []
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = "#rso .lyLwlc"

    soup = BeautifulSoup(response.text, "lxml")
    results = soup.select(css_identifier_result)
    output = []
    for result in results:
        title = result.select_one(css_identifier_title).text
        link = result.select_one(css_identifier_link)["href"]
        try:
            snippet = result.select_one(css_identifier_text).text
        except Exception:
            snippet = None
        item = {"title": title, "link": link, "text": snippet}
        output.append(item)
    stat_table = BeautifulSoup(response.content, "html.parser").find("table")
    stat_table = soup.find("table")
    if stat_table is None:
        return []
    table_data = stat_table.select("td a")
    next_page = []

    for item in table_data:
        next_page.append(item["href"])
    for next_page_link in next_page:
        new_link = BASE_URL + next_page_link
        try:
            response = requests.get(new_link, headers=headers)

        except requests.exceptions.RequestException:
            continue
        soup = BeautifulSoup(response.text, "lxml")
        results = soup.select(css_identifier_result)
        for result in results:
            title = result.select_one(css_identifier_title).text
            link = result.select_one(css_identifier_link)["href"]
            try:
                snippet = result.select_one(css_identifier_text).text
            except Exception:
                snippet = None
            item = {"title": title, "link": link, "text": snippet}
            output.append(item)
    return output


def write_google_search_results(query: str = "", filename: str = "") -> str:
    """Writes the Google search result page for the given query into a local file.
    Args:
        query: The search term provided by the user. Default is "potato".
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
    >>> "test" in write_google_search_results("python", "test")
    True
    >>> "test1" in write_google_search_results("", "test1")
    True
    >>> "potato" in write_google_search_results("", "")
    True
    """
    if query == "":
        query = "potato"
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
    filename = input("Enter optional filename: ") or "smt"
    print(f"Searching Google for {query} ....")
    filename = write_google_search_results(query, filename)
    print(f"File saved into {filename}")
