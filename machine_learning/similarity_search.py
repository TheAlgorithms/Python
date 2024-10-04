"""
Benzerlik Araması : https://en.wikipedia.org/wiki/Similarity_search
Benzerlik araması, doğal dil işleme alanında kullanılan, en yakın vektörü bulmak için
bir arama algoritmasıdır.
Bu algoritmada, öklid mesafesi ile mesafeyi hesaplar ve her vektör için iki veri içeren bir liste döndürür:
    1. en yakın vektör
    2. vektör ile en yakın vektör arasındaki mesafe (float)
"""

from __future__ import annotations

import math

import numpy as np
from numpy.linalg import norm


def oklid(input_a: np.ndarray, input_b: np.ndarray) -> float:
    """
    İki veri arasındaki öklid mesafesini hesaplar.
    :param input_a: İlk vektörün ndarray'i.
    :param input_b: İkinci vektörün ndarray'i.
    :return: input_a ve input_b'nin Öklid mesafesi. math.sqrt() kullanılarak,
             sonuç float olacaktır.

    >>> oklid(np.array([0]), np.array([1]))
    1.0
    >>> oklid(np.array([0, 1]), np.array([1, 1]))
    1.0
    >>> oklid(np.array([0, 0, 0]), np.array([0, 0, 1]))
    1.0
    """
    return math.sqrt(sum(pow(a - b, 2) for a, b in zip(input_a, input_b)))


def benzerlik_arama(
    veri_seti: np.ndarray, deger_dizisi: np.ndarray
) -> list[list[list[float] | float]]:
    """
    :param veri_seti: Vektörleri içeren set. ndarray olmalıdır.
    :param deger_dizisi: veri_setinden en yakın vektörü bilmek istediğimiz vektör/vektörler.
    :return: Sonuç, bir liste içerecek
            1. en yakın vektör
            2. vektörden mesafe

    >>> veri_seti = np.array([[0], [1], [2]])
    >>> deger_dizisi = np.array([[0]])
    >>> benzerlik_arama(veri_seti, deger_dizisi)
    [[[0], 0.0]]

    >>> veri_seti = np.array([[0, 0], [1, 1], [2, 2]])
    >>> deger_dizisi = np.array([[0, 1]])
    >>> benzerlik_arama(veri_seti, deger_dizisi)
    [[[0, 0], 1.0]]

    >>> veri_seti = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
    >>> deger_dizisi = np.array([[0, 0, 1]])
    >>> benzerlik_arama(veri_seti, deger_dizisi)
    [[[0, 0, 0], 1.0]]

    >>> veri_seti = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
    >>> deger_dizisi = np.array([[0, 0, 0], [0, 0, 1]])
    >>> benzerlik_arama(veri_seti, deger_dizisi)
    [[[0, 0, 0], 0.0], [[0, 0, 0], 1.0]]

    Bu hatalar meydana gelebilir:

    1. Eğer boyutlar farklıysa.
    Örneğin, veri_seti 2d diziye ve deger_dizisi 1d diziye sahipse:
    >>> veri_seti = np.array([[1]])
    >>> deger_dizisi = np.array([1])
    >>> benzerlik_arama(veri_seti, deger_dizisi)
    Traceback (most recent call last):
        ...
    ValueError: Yanlış giriş verilerinin boyutları... veri_seti : 2, deger_dizisi : 1

    2. Eğer verilerin şekilleri farklıysa.
    Örneğin, veri_seti (3, 2) şekline ve deger_dizisi (2, 3) şekline sahipse.
    İki dizinin aynı şekillerde olmasını bekliyoruz, bu yüzden bu yanlış.
    >>> veri_seti = np.array([[0, 0], [1, 1], [2, 2]])
    >>> deger_dizisi = np.array([[0, 0, 0], [0, 0, 1]])
    >>> benzerlik_arama(veri_seti, deger_dizisi)
    Traceback (most recent call last):
        ...
    ValueError: Yanlış giriş verilerinin şekli... veri_seti : 2, deger_dizisi : 3

    3. Eğer veri türleri farklıysa.
    Karşılaştırmaya çalışırken, aynı türleri bekliyoruz, bu yüzden aynı olmalılar.
    Eğer değilse, hatalarla karşılaşılacaktır.
    >>> veri_seti = np.array([[0, 0], [1, 1], [2, 2]], dtype=np.float32)
    >>> deger_dizisi = np.array([[0, 0], [0, 1]], dtype=np.int32)
    >>> benzerlik_arama(veri_seti, deger_dizisi)  # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    TypeError: Giriş verileri farklı veri türlerine sahip...
    veri_seti : float32, deger_dizisi : int32
    """

    if veri_seti.ndim != deger_dizisi.ndim:
        msg = (
            "Yanlış giriş verilerinin boyutları... "
            f"veri_seti : {veri_seti.ndim}, deger_dizisi : {deger_dizisi.ndim}"
        )
        raise ValueError(msg)

    try:
        if veri_seti.shape[1] != deger_dizisi.shape[1]:
            msg = (
                "Yanlış giriş verilerinin şekli... "
                f"veri_seti : {veri_seti.shape[1]}, deger_dizisi : {deger_dizisi.shape[1]}"
            )
            raise ValueError(msg)
    except IndexError:
        if veri_seti.ndim != deger_dizisi.ndim:
            raise TypeError("Yanlış şekil")

    if veri_seti.dtype != deger_dizisi.dtype:
        msg = (
            "Giriş verileri farklı veri türlerine sahip... "
            f"veri_seti : {veri_seti.dtype}, deger_dizisi : {deger_dizisi.dtype}"
        )
        raise TypeError(msg)

    cevap = []

    for deger in deger_dizisi:
        mesafe = oklid(deger, veri_seti[0])
        vektor = veri_seti[0].tolist()

        for veri_seti_degeri in veri_seti[1:]:
            gecici_mesafe = oklid(deger, veri_seti_degeri)

            if mesafe > gecici_mesafe:
                mesafe = gecici_mesafe
                vektor = veri_seti_degeri.tolist()

        cevap.append([vektor, mesafe])

    return cevap


def kosin_benzerligi(input_a: np.ndarray, input_b: np.ndarray) -> float:
    """
    İki veri arasındaki kosinüs benzerliğini hesaplar.
    :param input_a: İlk vektörün ndarray'i.
    :param input_b: İkinci vektörün ndarray'i.
    :return: input_a ve input_b'nin Kosinüs benzerliği. math.sqrt() kullanılarak,
             sonuç float olacaktır.

    >>> kosin_benzerligi(np.array([1]), np.array([1]))
    1.0
    >>> kosin_benzerligi(np.array([1, 2]), np.array([6, 32]))
    0.9615239476408232
    """
    return float(np.dot(input_a, input_b) / (norm(input_a) * norm(input_b)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
