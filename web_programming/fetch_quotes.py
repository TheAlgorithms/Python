"""
Bu dosya "ZenQuotes API"den alıntılar getirir.
API anahtarı gerektirmez çünkü ücretsiz katmanı kullanır.

Daha fazla ayrıntı ve premium özellikler için ziyaret edin:
    https://zenquotes.io/
"""

import pprint

import requests

API_ENDPOINT_URL = "https://zenquotes.io/api"


def gunun_alintisi() -> list:
    return requests.get(API_ENDPOINT_URL + "/today", timeout=10).json()


def rastgele_alintilar() -> list:
    return requests.get(API_ENDPOINT_URL + "/random", timeout=10).json()


if __name__ == "__main__":
    """
    response nesnesi alıntı ile ilgili tüm bilgileri içerir
    Gerçek alıntıyı almak için response.json() nesnesine aşağıdaki gibi erişin
    response.json() bir json nesnesi listesidir
        response.json()[0]['q'] = gerçek alıntı.
        response.json()[0]['a'] = yazar adı.
        response.json()[0]['h'] = html formatında.
    """
    response = rastgele_alintilar()
    pprint.pprint(response)
