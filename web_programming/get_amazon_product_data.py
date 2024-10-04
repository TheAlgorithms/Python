"""
Bu dosya, kullanıcıdan bir ürün adı girdi olarak alacak ve Amazon'dan bu ad veya kategoriye ait ürünler hakkında bilgi getirecek bir fonksiyon sağlar.
Ürün bilgileri başlık, URL, fiyat, derecelendirmeler ve mevcut indirimleri içerecektir.
"""

from itertools import zip_longest

import requests
from bs4 import BeautifulSoup
from pandas import DataFrame


def get_amazon_product_data(product: str = "laptop") -> DataFrame:
    """
    Bir ürün adı veya kategori girdi olarak al ve Amazon'dan ürün bilgilerini döndür
    başlık, URL, fiyat, derecelendirmeler ve mevcut indirimleri içerecek şekilde.
    """
    url = f"https://www.amazon.in/s?k={product}"
    header = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
            "(KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
        ),
        "Accept-Language": "en-US, en;q=0.5",
    }
    soup = BeautifulSoup(
        requests.get(url, headers=header, timeout=10).text, features="lxml"
    )
    # Sütun başlıkları ile bir Pandas veri çerçevesi başlat
    data_frame = DataFrame(
        columns=[
            "Ürün Başlığı",
            "Ürün Bağlantısı",
            "Ürünün Güncel Fiyatı",
            "Ürün Derecelendirmesi",
            "Ürünün MRP'si",
            "İndirim",
        ]
    )
    # Her girişi döngüye al ve veri çerçevesine kaydet
    for item, _ in zip_longest(
        soup.find_all(
            "div",
            attrs={"class": "s-result-item", "data-component-type": "s-search-result"},
        ),
        soup.find_all("div", attrs={"class": "a-row a-size-base a-color-base"}),
    ):
        try:
            product_title = item.h2.text
            product_link = "https://www.amazon.in/" + item.h2.a["href"]
            product_price = item.find("span", attrs={"class": "a-offscreen"}).text
            try:
                product_rating = item.find("span", attrs={"class": "a-icon-alt"}).text
            except AttributeError:
                product_rating = "Mevcut değil"
            try:
                product_mrp = (
                    "₹"
                    + item.find(
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
            continue
        data_frame.loc[str(len(data_frame.index))] = [
            product_title,
            product_link,
            product_price,
            product_rating,
            product_mrp,
            discount,
        ]
    data_frame.loc[
        data_frame["Ürünün Güncel Fiyatı"] > data_frame["Ürünün MRP'si"],
        "Ürünün MRP'si",
    ] = " "
    data_frame.loc[
        data_frame["Ürünün Güncel Fiyatı"] > data_frame["Ürünün MRP'si"],
        "İndirim",
    ] = " "
    data_frame.index += 1
    return data_frame


if __name__ == "__main__":
    product = "kulaklık"
    get_amazon_product_data(product).to_csv(f"Amazon Ürün Verileri {product}.csv")
