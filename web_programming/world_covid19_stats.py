def world_covid19_stats(
    url: str = "https://www.worldometers.info/coronavirus/",
) -> dict:
    """
    Return a dict of current worldwide COVID-19 statistics.

    Example:
        >>> stats = world_covid19_stats()
        >>> isinstance(stats, dict)
        True
        >>> len(stats) > 0  # Check that we got some statistics
        True
        >>> 'Total Cases' in stats.keys()  # Ensure 'Total Cases' is one of the keys
        True

    Raises:
        Exception: If the request fails or the number of keys and values does not match.
    """
    response = requests.get(url, timeout=10)
    if response.status_code != 200:
        raise Exception(
            f"Failed to fetch data from {url}, status code: {response.status_code}"
        )

    soup = BeautifulSoup(response.text, "html.parser")
    keys = [h1.get_text(strip=True) for h1 in soup.find_all("h1")]
    values = [
        div.get_text(strip=True)
        for div in soup.find_all("div", class_="maincounter-number")
    ]

    keys += [
        span.get_text(strip=True)
        for span in soup.find_all("span", class_="panel-title")
    ]
    values += [
        div.get_text(strip=True)
        for div in soup.find_all("div", class_="number-table-main")
    ]

    if len(keys) != len(values):
        raise ValueError("The number of keys and values extracted does not match.")

    return {key: value for key, value in zip(keys, values)}
