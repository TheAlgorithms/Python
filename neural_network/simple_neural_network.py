"""
İleri yayılma açıklaması:
https://towardsdatascience.com/forward-propagation-in-neural-networks-simplified-math-and-code-version-bbcfef6f9250


"""

import math
import random


# Sigmoid fonksiyonu
def sigmoid_fonksiyonu(değer: float, türev: bool = False) -> float:
    """Bir float sayısının sigmoid fonksiyonunu döndürür.

    >>> sigmoid_fonksiyonu(3.5)
    0.9706877692486436
    >>> sigmoid_fonksiyonu(3.5, True)
    -8.75
    """
    if türev:
        return değer * (1 - değer)
    return 1 / (1 + math.exp(-değer))


# Başlangıç Değeri
BAŞLANGIÇ_DEĞERİ = 0.02


def ileri_yayılma(beklenen: int, yayılma_sayısı: int) -> float:
    """İleri yayılma eğitimi sonrası bulunan değeri döndürür.

    >>> sonuç = ileri_yayılma(32, 450_000)  # Önceki değer 10_000_000 idi
    >>> sonuç > 31 and sonuç < 33
    True

    >>> sonuç = ileri_yayılma(32, 1000)
    >>> sonuç > 31 and sonuç < 33
    False
    """

    # Rastgele ağırlık
    ağırlık = float(2 * (random.randint(1, 100)) - 1)

    for _ in range(yayılma_sayısı):
        # İleri yayılma
        katman_1 = sigmoid_fonksiyonu(BAŞLANGIÇ_DEĞERİ * ağırlık)
        # Ne kadar hata yaptık?
        katman_1_hata = (beklenen / 100) - katman_1
        # Hata delta
        katman_1_delta = katman_1_hata * sigmoid_fonksiyonu(katman_1, True)
        # Ağırlığı güncelle
        ağırlık += BAŞLANGIÇ_DEĞERİ * katman_1_delta

    return katman_1 * 100


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    beklenen = int(input("Beklenen değer: "))
    yayılma_sayısı = int(input("Yayılma sayısı: "))
    print(ileri_yayılma(beklenen, yayılma_sayısı))
