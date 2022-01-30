"""

Scrape the price and pharmacy name for a prescription drug from rx site
after providing the drug name and zipcode. 

"""

import lxml

from requests import Response, get
from bs4 import BeautifulSoup


def format_price(price: str) -> float:

    """[summary]

    Remove the dollar from the string and convert it to float.

    Args:
        price (str): [price of drug in string format]

    Returns:
        float: [formatted price of drug in float]

    >>> format_price("$14")
    14.0

    >>> format_price("$15.67")
    15.67

    >>> format_price("$0.00")
    0.0

    """
    dollar_removed: str = price.replace("$", "")
    formatted_price: str = float(dollar_removed)
    return formatted_price


def fetch_pharmacy_and_price_list(drug_name: str=None, zip_code: str=None) -> list or None:

    """[summary]

    This function will take input of drug name and zipcode, then request to the BASE_URL site,
    Get the page data and scrape it to the generate the list of lowest prices for the prescription drug.

    Args:
        drug_name (str): [Drug name]
        zip_code(str): [Zip code]

    Returns:
        list: [List of pharmacy name and price]

    >>> fetch_pharmacy_and_price_list()

    >>> fetch_pharmacy_and_price_list("Eliqus")

    >>> fetch_pharmacy_and_price_list(None, 30303)

    """

    try:

        # has user provided both inputs?
        if not drug_name or not zip_code:
            return None

        request_url: str = f'https://www.wellrx.com/prescriptions/{drug_name}/{zip_code}/?freshSearch=true'
        response: Response = get(request_url)

        # Is the status code ok?
        if response.status_code == 200:

            # Scrape the data using bs4
            soup: BeautifulSoup = BeautifulSoup(response.text, "lxml")

            # This list will store the name and price.
            pharmacy_price_list: list = []

            # Fetch all the grids that contains the items.
            grid_list: list = soup.find_all("div", { "class": "grid-x pharmCard" })
            if grid_list and len(grid_list) > 0:
                for grid in grid_list:

                    # Get the pharmacy price.
                    pharmacy_name: str = grid.find("p", { "class": "list-title" }).text

                    # Get price of the drug.
                    price: str = grid.find("span", { "p", "price price-large" }).text
                    formatted_price: float = format_price(price)

                    pharmacy_price_list.append({
                        "pharmacy_name": pharmacy_name,
                        "price": formatted_price,
                    })

            return pharmacy_price_list
            
        else:
            return None

    except Exception as e:
        return None


if __name__ == "__main__":

    # Enter a drug name and a zip code
    drug_name: str = input("Enter drug Name:\n")
    zip_code: str = input("Enter zip code:\n")
    pharmacy_price_list: list = fetch_pharmacy_and_price_list(drug_name, zip_code)

    if pharmacy_price_list:
        print(f'\nSearch results for {drug_name} at location {zip_code}:')
        for pharmacy_price in pharmacy_price_list:
            print(f'Pharmacy: {pharmacy_price["pharmacy_name"]} Price: {pharmacy_price["price"]}')
    else:
        print("No results found")
