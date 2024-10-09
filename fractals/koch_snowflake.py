"""
Açıklama
    Koch kar tanesi, bir fraktal eğridir ve tanımlanan ilk fraktallardan biridir.
    Koch kar tanesi, aşamalı olarak oluşturulabilir. İlk aşama bir eşkenar üçgendir
    ve her ardışık aşama, önceki aşamanın her bir kenarına dışa doğru bükülmeler
    ekleyerek, daha küçük eşkenar üçgenler oluşturarak oluşur.
    Bu, her bir çizgi için şu adımlarla gerçekleştirilebilir:
        1. Çizgi segmentini eşit uzunlukta üç segmente bölün.
        2. 1. adımdaki orta segmenti taban olarak alan ve dışa doğru işaret eden
        bir eşkenar üçgen çizin.
        3. 2. adımdaki üçgenin tabanı olan çizgi segmentini kaldırın.
    (açıklama https://en.wikipedia.org/wiki/Koch_snowflake adresinden uyarlanmıştır)
    (daha ayrıntılı bir açıklama ve Processing dilinde bir uygulama için bkz.
    https://natureofcode.com/book/chapter-8-fractals/#84-the-koch-curve-and-the-arraylist-technique)

Gereksinimler (pip):
    - matplotlib
    - numpy
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

# Koch kar tanesinin başlangıç üçgeni
VEKTÖR_1 = np.array([0, 0])
VEKTÖR_2 = np.array([0.5, 0.8660254])
VEKTÖR_3 = np.array([1, 0])
BAŞLANGIÇ_VEKTÖRLERİ = [VEKTÖR_1, VEKTÖR_2, VEKTÖR_3, VEKTÖR_1]

# Sadece Koch eğrisi için yorum satırını kaldırın
# BAŞLANGIÇ_VEKTÖRLERİ = [VEKTÖR_1, VEKTÖR_3]


def yineleme(başlangıç_vektörleri: list[np.ndarray], adımlar: int) -> list[np.ndarray]:
    """
    "adımlar" argümanıyla belirlenen yineleme sayısını gerçekleştirin.
    Yüksek değerlerle (5'in üzerinde) dikkatli olun, çünkü hesaplama süresi
    üstel olarak artar.
    >>> yineleme([np.array([0, 0]), np.array([1, 0])], 1)
    [array([0, 0]), array([0.33333333, 0.        ]), array([0.5       , \
0.28867513]), array([0.66666667, 0.        ]), array([1, 0])]
    """
    vektörler = başlangıç_vektörleri
    for _ in range(adımlar):
        vektörler = yineleme_adımı(vektörler)
    return vektörler


def yineleme_adımı(vektörler: list[np.ndarray]) -> list[np.ndarray]:
    """
    Her bir bitişik vektör çiftini döngüye sokar. İki bitişik vektör arasındaki
    her çizgi, orijinal iki vektör arasına 3 ek vektör eklenerek 4 segmente
    bölünür. Ortadaki vektör, 60 derece döndürülerek dışa doğru bükülür.
    >>> yineleme_adımı([np.array([0, 0]), np.array([1, 0])])
    [array([0, 0]), array([0.33333333, 0.        ]), array([0.5       , \
0.28867513]), array([0.66666667, 0.        ]), array([1, 0])]
    """
    yeni_vektörler = []
    for i, başlangıç_vektörü in enumerate(vektörler[:-1]):
        bitiş_vektörü = vektörler[i + 1]
        yeni_vektörler.append(başlangıç_vektörü)
        fark_vektörü = bitiş_vektörü - başlangıç_vektörü
        yeni_vektörler.append(başlangıç_vektörü + fark_vektörü / 3)
        yeni_vektörler.append(
            başlangıç_vektörü + fark_vektörü / 3 + döndür(fark_vektörü / 3, 60)
        )
        yeni_vektörler.append(başlangıç_vektörü + fark_vektörü * 2 / 3)
    yeni_vektörler.append(vektörler[-1])
    return yeni_vektörler


def döndür(vektör: np.ndarray, açı_derece: float) -> np.ndarray:
    """
    Bir 2D vektörün standart döndürme matrisi ile döndürülmesi
    (bkz. https://en.wikipedia.org/wiki/Rotation_matrix)
    >>> döndür(np.array([1, 0]), 60)
    array([0.5      , 0.8660254])
    >>> döndür(np.array([1, 0]), 90)
    array([6.123234e-17, 1.000000e+00])
    """
    theta = np.radians(açı_derece)
    c, s = np.cos(theta), np.sin(theta)
    döndürme_matrisi = np.array(((c, -s), (s, c)))
    return np.dot(döndürme_matrisi, vektör)


def çiz(vektörler: list[np.ndarray]) -> None:
    """
    Vektörleri matplotlib.pyplot kullanarak çizmek için yardımcı işlev
    Bu işlevin bir dönüş değeri olmadığından herhangi bir doctest uygulanmadı
    """
    # Grafiğin gerilmesini önleyin
    eksenler = plt.gca()
    eksenler.set_aspect("equal")

    # matplotlib.pyplot.plot, girdi olarak tüm x-koordinatlarının bir listesini
    # ve tüm y-koordinatlarının bir listesini alır, bu da vektör listesinden
    # zip() kullanılarak oluşturulur
    x_koordinatları, y_koordinatları = zip(*vektörler)
    plt.plot(x_koordinatları, y_koordinatları)
    plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    işlenmiş_vektörler = yineleme(BAŞLANGIÇ_VEKTÖRLERİ, 5)
    çiz(işlenmiş_vektörler)
