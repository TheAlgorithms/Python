"""

Bir reçeteli ilacın fiyatını ve eczane adını rx sitesinden
ilaç adı ve posta kodu sağladıktan sonra kazıyın.

"""

from urllib.error import HTTPError

from bs4 import BeautifulSoup
from requests import exceptions, get

BASE_URL = "https://www.wellrx.com/prescriptions/{0}/{1}/?freshSearch=true"


def fetch_pharmacy_and_price_list(drug_name: str, zip_code: str) -> list | None:
    """[özet]

    Bu fonksiyon ilaç adı ve posta kodu girdisini alacak,
    ardından BASE_URL sitesine istek gönderecek.
    Sayfa verilerini al ve kazıyarak
    reçeteli ilaç için en düşük fiyatların listesini oluşturun.

    Args:
        drug_name (str): [İlaç adı]
        zip_code(str): [Posta kodu]

    Returns:
        list: [Eczane adı ve fiyat listesi]

    >>> fetch_pharmacy_and_price_list(None, None)

    >>> fetch_pharmacy_and_price_list(None, 30303)

    >>> fetch_pharmacy_and_price_list("eliquis", None)

    """

    try:
        # Kullanıcı her iki girdiyi de sağladı mı?
        if not drug_name or not zip_code:
            return None

        request_url = BASE_URL.format(drug_name, zip_code)
        response = get(request_url, timeout=10)

        # Yanıt tamam mı?
        response.raise_for_status()

        # Verileri bs4 kullanarak kazıyın
        soup = BeautifulSoup(response.text, "html.parser")

        # Bu liste adı ve fiyatı saklayacak.
        pharmacy_price_list = []

        # Öğeleri içeren tüm ızgaraları alın.
        grid_list = soup.find_all("div", {"class": "grid-x pharmCard"})
        if grid_list and len(grid_list) > 0:
            for grid in grid_list:
                # Eczane fiyatını alın.
                pharmacy_name = grid.find("p", {"class": "list-title"}).text

                # İlacın fiyatını alın.
                price = grid.find("span", {"class": "price price-large"}).text

                pharmacy_price_list.append(
                    {
                        "pharmacy_name": pharmacy_name,
                        "price": price,
                    }
                )

        return pharmacy_price_list

    except (HTTPError, exceptions.RequestException, ValueError):
        return None


if __name__ == "__main__":
    # Bir ilaç adı ve posta kodu girin
    drug_name = input("İlaç adı girin: ").strip()
    zip_code = input("Posta kodu girin: ").strip()

    pharmacy_price_list: list | None = fetch_pharmacy_and_price_list(
        drug_name, zip_code
    )

    if pharmacy_price_list:
        print(f"\n{zip_code} konumunda {drug_name} için arama sonuçları:")
        for pharmacy_price in pharmacy_price_list:
            name = pharmacy_price["pharmacy_name"]
            price = pharmacy_price["price"]

            print(f"Eczane: {name} Fiyat: {price}")
    else:
        print(f"{drug_name} için sonuç bulunamadı")
