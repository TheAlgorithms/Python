# https://en.wikipedia.org/wiki/Circular_convolution

"""
Dairesel konvolüsyon, döngüsel konvolüsyon olarak da bilinir,
aynı döneme sahip iki periyodik fonksiyonun konvolüsyonunun özel bir durumudur. Periyodik konvolüsyon,
örneğin, ayrık zamanlı Fourier dönüşümü (DTFT) bağlamında ortaya çıkar.
Özellikle, iki ayrık dizinin çarpımının DTFT'si, bireysel dizilerin DTFT'lerinin periyodik konvolüsyonudur.
Ve her DTFT, sürekli bir Fourier dönüşüm fonksiyonunun periyodik bir toplamıdır.

Kaynak: https://en.wikipedia.org/wiki/Circular_convolution
"""

import doctest
from collections import deque

import numpy as np


class DaireselKonvolusyon:
    """
    Bu sınıf birinci ve ikinci sinyali saklar ve dairesel konvolüsyonu gerçekleştirir
    """

    def __init__(self) -> None:
        """
        Birinci sinyal ve ikinci sinyal 1-D dizi olarak saklanır
        """

        self.birinci_sinyal = [2, 1, 2, -1]
        self.ikinci_sinyal = [1, 2, 3, 4]

    def dairesel_konvolusyon(self) -> list[float]:
        """
        Bu fonksiyon birinci ve ikinci sinyalin dairesel konvolüsyonunu
        matris yöntemi kullanarak gerçekleştirir

        Kullanım:
        >>> konvolusyon = DaireselKonvolusyon()
        >>> konvolusyon.dairesel_konvolusyon()
        [10.0, 10.0, 6.0, 14.0]

        >>> konvolusyon.birinci_sinyal = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6]
        >>> konvolusyon.ikinci_sinyal = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5]
        >>> konvolusyon.dairesel_konvolusyon()
        [5.2, 6.0, 6.48, 6.64, 6.48, 6.0, 5.2, 4.08]

        >>> konvolusyon.birinci_sinyal = [-1, 1, 2, -2]
        >>> konvolusyon.ikinci_sinyal = [0.5, 1, -1, 2, 0.75]
        >>> konvolusyon.dairesel_konvolusyon()
        [6.25, -3.0, 1.5, -2.0, -2.75]

        >>> konvolusyon.birinci_sinyal = [1, -1, 2, 3, -1]
        >>> konvolusyon.ikinci_sinyal = [1, 2, 3]
        >>> konvolusyon.dairesel_konvolusyon()
        [8.0, -2.0, 3.0, 4.0, 11.0]

        """

        birinci_sinyal_uzunluk = len(self.birinci_sinyal)
        ikinci_sinyal_uzunluk = len(self.ikinci_sinyal)

        max_uzunluk = max(birinci_sinyal_uzunluk, ikinci_sinyal_uzunluk)

        # max_uzunluk x max_uzunluk boyutunda sıfır matrisi oluştur
        matris = [[0] * max_uzunluk for i in range(max_uzunluk)]

        # daha küçük sinyali sıfırlarla doldurarak her iki sinyali de aynı uzunlukta yapar
        if birinci_sinyal_uzunluk < ikinci_sinyal_uzunluk:
            self.birinci_sinyal += [0] * (max_uzunluk - birinci_sinyal_uzunluk)
        elif birinci_sinyal_uzunluk > ikinci_sinyal_uzunluk:
            self.ikinci_sinyal += [0] * (max_uzunluk - ikinci_sinyal_uzunluk)

        """
        Matris aşağıdaki şekilde doldurulur, 'x' sinyalinin uzunluğu 4 varsayılırsa
        [
            [x[0], x[3], x[2], x[1]],
            [x[1], x[0], x[3], x[2]],
            [x[2], x[1], x[0], x[3]],
            [x[3], x[2], x[1], x[0]]
        ]
        """
        for i in range(max_uzunluk):
            döndürülmüş_sinyal = deque(self.ikinci_sinyal)
            döndürülmüş_sinyal.rotate(i)
            for j, eleman in enumerate(döndürülmüş_sinyal):
                matris[i][j] += eleman

        # matrisi birinci sinyal ile çarp
        son_sinyal = np.matmul(np.transpose(matris), np.transpose(self.birinci_sinyal))

        # iki ondalık basamağa yuvarlama
        return [float(round(i, 2)) for i in son_sinyal]


if __name__ == "__main__":
    doctest.testmod()
