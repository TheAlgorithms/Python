""" This file provides a function which will take
a product name as input from the user,and fetch the necessary
information about that kind of products from Amazon like the product
title,link to that product,price of the product,the ratings of
the product and the discount available on the product
in the form of a csv file,this will help the users by improving searchability
and navigability and find the right product easily and in a short period of time,
it will also be beneficial for performing better analysis on products"""


import itertools as it

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


def get_product_info(
    product="laptop",
):  # function that will take the product as input and return the product details as output in the form of a csv file,if no input is given,it will fetch the details of laptop by default
    url = (
        f"https://www.amazon.in/laptop/s?k={product}"  # generation of search query url
    )
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36",
        "Accept-Language": "en-US, en;q=0.5",
    }  # header that will indicate to the destination server that the request is coming from a genuine human being and not a bot
    page = requests.get(url, headers=header)
    page_content = page.text
    soup = bs(page_content)
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
    ):  # for loop to parse through each entry and store them in the dataframe along with try....except block for handling exceptions that may arise
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
                discount = ""
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
    data.to_csv(
        f"Amazon Product Data({product}).csv"
    )  # writing the data to the csv file
    return data
