"""
Hızlı seçim algoritmasının Python uygulaması. Bu algoritma, bir listenin sıralandığında hangi indekste hangi değerin bulunacağını hesaplamak için etkilidir, liste sıralı olmasa bile.
https://en.wikipedia.org/wiki/Quickselect

Organiser: K. Umut Araz
"""

import random


def _partition(data: list, pivot) -> tuple:
    """
    Veriyi, pivot ile ilişkili olarak daha küçük, eşit ve daha büyük listelere üç yönlü olarak ayırır.
    :param data: Sıralanacak veri (bir liste)
    :param pivot: Veriyi ayırmak için kullanılan değer
    :return: Üç liste: daha küçük, eşit ve daha büyük
    """
    kucuk, esit, buyuk = [], [], []
    for eleman in data:
        if eleman < pivot:
            kucuk.append(eleman)
        elif eleman > pivot:
            buyuk.append(eleman)
        else:
            esit.append(eleman)
    return kucuk, esit, buyuk


def quick_select(ogeler: list, indeks: int):
    """
    >>> quick_select([2, 4, 5, 7, 899, 54, 32], 5)
    54
    >>> quick_select([2, 4, 5, 7, 899, 54, 32], 1)
    4
    >>> quick_select([5, 4, 3, 2], 2)
    4
    >>> quick_select([3, 5, 7, 10, 2, 12], 3)
    7
    """
    # indeks = medyanı bulmaya çalışırken len(ogeler) // 2
    #   (ogeler sıralandığında indeksin değeri)

    # geçersiz giriş
    if indeks >= len(ogeler) or indeks < 0:
        return None

    pivot = ogeler[random.randint(0, len(ogeler) - 1)]
    sayac = 0
    kucuk, esit, buyuk = _partition(ogeler, pivot)
    sayac = len(esit)
    m = len(kucuk)

    # indeks pivot
    if m <= indeks < m + sayac:
        return pivot
    # daha küçükte olmalı
    elif m > indeks:
        return quick_select(kucuk, indeks)
    # daha büyükte olmalı
    else:
        return quick_select(buyuk, indeks - (m + sayac))
