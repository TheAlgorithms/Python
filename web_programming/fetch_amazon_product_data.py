""" This file provides a function which will take
a product name as input from the user,and fetch the necessary
information about that kind of products from Amazon like the product
title,link to that product,price of the product,the ratings of
the product and the discount available on the product
and return it in the form of Pandas Dataframe"""


import itertools as it

import pandas as pd
import requests
from bs4 import BeautifulSoup 


def get_product_info(
    product: str = "laptop", generate_csv: bool = False
) -> pd.DataFrame:
    # function that will take the product as input and return the
    # product details as output
    # in the form of a csv file,if no input is given,it
    # will fetch the details of laptop by default
    url = (
        f"https://www.amazon.in/laptop/s?k={product}"
        # generation of search query url
    )
    header = {
        "User-Agent": """Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36
        (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36""",
        "Accept-Language": "en-US, en;q=0.5",
    }  # header that will indicate to the destination server that the
    # request is coming from a genuine human being and not a bot
    page = requests.get(url, headers=header)
    page_content = page.text
    soup = BeautifulSoup(page_content)
    data = pd.DataFrame(
        columns=[
            "Product Title",
            "Product Link",
            "Current Price of the product",
            "Product Rating",
            "MRP of the product",
            "Discount",
        ]
    )  # initializing a pandas dataframe to store the requisite information
    for i, j in it.zip_longest(
        soup.find_all(
            "div",
            attrs={"class": "s-result-item", "data-component-type": "s-search-result"},
        ),
        soup.find_all("div", attrs={"class": "a-row a-size-base a-color-base"}),
    ):  # for loop to parse through each entry and store them in the dataframe
        # along with try....except block for handling exceptions that may arise
        try:
            product_title = i.h2.text
            product_link = "https://www.amazon.in/" + i.h2.a["href"]
            product_price = i.find("span", attrs={"class": "a-offscreen"}).text
            try:
                product_rating = i.find("span", attrs={"class": "a-icon-alt"}).text
            except AttributeError:
                product_rating = "Not available"
            try:
                product_mrp = (
                    "₹"
                    + i.find(
                        "span", attrs={"class": "a-price a-text-price"}
                    ).text.split("₹")[1]
                )
            except AttributeError:
                product_mrp = ""
            try:
                discount = float(
                    (
                        (
                            float(product_mrp.strip("₹").replace(",", ""))
                            - float(product_price.strip("₹").replace(",", ""))
                        )
                        / float(product_mrp.strip("₹").replace(",", ""))
                    )
                    * 100
                )
            except ValueError:
                discount = float("nan") 
        except AttributeError:
            pass
        data.loc[len(data.index)] = [
            product_title,
            product_link,
            product_price,
            product_rating,
            product_mrp,
            discount,
        ]
    data.loc[
        data["Current Price of the product"] > data["MRP of the product"],
        "MRP of the product",
    ] = " "
    data.loc[
        data["Current Price of the product"] > data["MRP of the product"], "Discount"
    ] = " "
    data.index += 1
    if generate_csv:
        data.to_csv(f"Amazon Product Data({product}).csv")
        # writing the data to the csv file
    return data
