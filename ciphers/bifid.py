#!/usr/bin/env python3

"""
Bifid Şifresi, bir mesajı şifrelemek için Polybius Kare'sini kullanır ve
bu şekilde sırrı bilmeden çözülmesini oldukça zor hale getirir.

https://www.braingle.com/brainteasers/codes/bifid.php

Organiser: K. Umut Araz
"""

import numpy as np

KARE = [
    ["a", "b", "c", "d", "e"],
    ["f", "g", "h", "i", "k"],
    ["l", "m", "n", "o", "p"],
    ["q", "r", "s", "t", "u"],
    ["v", "w", "x", "y", "z"],
]


class BifidSifresi:
    def __init__(self) -> None:
        self.KARE = np.array(KARE)

    def harf_to_sayilar(self, harf: str) -> np.ndarray:
        """
        Verilen harfi polybius karesindeki sayılarla temsil eden çift sayıyı döndürür.

        >>> np.array_equal(BifidSifresi().harf_to_sayilar('a'), [1,1])
        True

        >>> np.array_equal(BifidSifresi().harf_to_sayilar('u'), [4,5])
        True
        """
        index1, index2 = np.where(harf == self.KARE)
        indeksler = np.concatenate([index1 + 1, index2 + 1])
        return indeksler

    def sayilar_to_harf(self, index1: int, index2: int) -> str:
        """
        Polybius karesindeki [index1, index2] konumuna karşılık gelen harfi döndürür.

        >>> BifidSifresi().sayilar_to_harf(4, 5) == "u"
        True

        >>> BifidSifresi().sayilar_to_harf(1, 1) == "a"
        True
        """
        harf = self.KARE[index1 - 1, index2 - 1]
        return harf

    def kodla(self, mesaj: str) -> str:
        """
        Polybius şifresine göre mesajın şifrelenmiş versiyonunu döndürür.

        >>> BifidSifresi().kodla('testmessage') == 'qtltbdxrxlk'
        True

        >>> BifidSifresi().kodla('Test Message') == 'qtltbdxrxlk'
        True

        >>> BifidSifresi().kodla('test j') == BifidSifresi().kodla('test i')
        True
        """
        mesaj = mesaj.lower()
        mesaj = mesaj.replace(" ", "")
        mesaj = mesaj.replace("j", "i")

        ilk_adim = np.empty((2, len(mesaj)))
        for harf_index in range(len(mesaj)):
            sayilar = self.harf_to_sayilar(mesaj[harf_index])

            ilk_adim[0, harf_index] = sayilar[0]
            ilk_adim[1, harf_index] = sayilar[1]

        ikinci_adim = ilk_adim.reshape(2 * len(mesaj))
        sifreli_metin = ""
        for sayi_index in range(len(mesaj)):
            index1 = int(ikinci_adim[sayi_index * 2])
            index2 = int(ikinci_adim[(sayi_index * 2) + 1])
            harf = self.sayilar_to_harf(index1, index2)
            sifreli_metin += harf

        return sifreli_metin

    def cozul(self, mesaj: str) -> str:
        """
        Polybius şifresine göre mesajın çözülmüş versiyonunu döndürür.

        >>> BifidSifresi().cozul('qtltbdxrxlk') == 'testmessage'
        True
        """
        mesaj = mesaj.lower()
        mesaj.replace(" ", "")
        ilk_adim = np.empty(2 * len(mesaj))
        for harf_index in range(len(mesaj)):
            sayilar = self.harf_to_sayilar(mesaj[harf_index])
            ilk_adim[harf_index * 2] = sayilar[0]
            ilk_adim[harf_index * 2 + 1] = sayilar[1]

        ikinci_adim = ilk_adim.reshape((2, len(mesaj)))
        cozulmus_metin = ""
        for sayi_index in range(len(mesaj)):
            index1 = int(ikinci_adim[0, sayi_index])
            index2 = int(ikinci_adim[1, sayi_index])
            harf = self.sayilar_to_harf(index1, index2)
            cozulmus_metin += harf

        return cozulmus_metin
