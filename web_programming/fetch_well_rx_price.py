"""

Scrape the price and pharmacy name for a prescription drug from rx site
after providing the drug name and zipcode.

"""

import httpx
from bs4 import BeautifulSoup

BASE_URL = "https://www.wellrx.com/prescriptions/{}/{}/?freshSearch=true"


def fetch_pharmacy_and_price_list(drug_name: str, zip_code: str) -> list | None:
    """[summary]

    This function will take input of drug name and zipcode,
    then request to the BASE_URL site.
    Get the page data and scrape it to generate the
    list of the lowest prices for the prescription drug.

    Args:
        drug_name (str): [Drug name]
        zip_code(str): [Zip code]

    Returns:
        list: [List of pharmacy name and price]

    >>> print(fetch_pharmacy_and_price_list(None, None))
    None
    >>> print(fetch_pharmacy_and_price_list(None, 30303))
    None
    >>> print(fetch_pharmacy_and_price_list("eliquis", None))
    None
    """

    try:
        # Has user provided both inputs?
        if not drug_name or not zip_code:
            return None

        request_url = BASE_URL.format(drug_name, zip_code)
        response = httpx.get(request_url, timeout=10).raise_for_status()

        # Scrape the data using bs4
        soup = BeautifulSoup(response.text, "html.parser")

        # This list will store the name and price.
        pharmacy_price_list = []

        # Fetch all the grids that contain the items.
        grid_list = soup.find_all("div", {"class": "grid-x pharmCard"})
        if grid_list and len(grid_list) > 0:
            for grid in grid_list:
                # Get the pharmacy price.
                pharmacy_name = grid.find("p", {"class": "list-title"}).text

                # Get the price of the drug.
                price = grid.find("span", {"p", "price price-large"}).text

                pharmacy_price_list.append(
                    {
                        "pharmacy_name": pharmacy_name,
                        "price": price,
                    }
                )

        return pharmacy_price_list

    except (httpx.HTTPError, ValueError):
        return None


if __name__ == "__main__":
    # Enter a drug name and a zip code
    drug_name = input("Enter drug name: ").strip()
    zip_code = input("Enter zip code: ").strip()

    pharmacy_price_list: list | None = fetch_pharmacy_and_price_list(
        drug_name, zip_code
    )

    if pharmacy_price_list:
        print(f"\nSearch results for {drug_name} at location {zip_code}:")
        for pharmacy_price in pharmacy_price_list:
            name = pharmacy_price["pharmacy_name"]
            price = pharmacy_price["price"]

            print(f"Pharmacy: {name} Price: {price}")
    else:
        print(f"No results found for {drug_name}")
