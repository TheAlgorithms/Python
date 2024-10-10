#!/usr/bin/env python3

"""
Polybius Kare, harfleri sayılara çeviren bir tablodur.

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


class PolybiusSifreleme:
    def __init__(self) -> None:
        self.KARE = np.array(KARE)

    def harfi_sayilara_cevir(self, harf: str) -> np.ndarray:
        """
        Verilen harfi polybius karesindeki sayılarla temsil eden çift sayıyı döndürür.
        >>> np.array_equal(PolybiusSifreleme().harfi_sayilara_cevir('a'), [1,1])
        True

        >>> np.array_equal(PolybiusSifreleme().harfi_sayilara_cevir('u'), [4,5])
        True
        """
        index1, index2 = np.where(harf == self.KARE)
        indeksler = np.concatenate([index1 + 1, index2 + 1])
        return indeksler

    def sayilardan_harf_cevir(self, index1: int, index2: int) -> str:
        """
        Polybius karesindeki [index1, index2] konumuna karşılık gelen harfi döndürür.

        >>> PolybiusSifreleme().sayilardan_harf_cevir(4, 5) == "u"
        True

        >>> PolybiusSifreleme().sayilardan_harf_cevir(1, 1) == "a"
        True
        """
        return self.KARE[index1 - 1, index2 - 1]

    def encode(self, mesaj: str) -> str:
        """
        Polybius şifrelemesine göre mesajın kodlanmış halini döndürür.

        >>> PolybiusSifreleme().encode("test message") == "44154344 32154343112215"
        True

        >>> PolybiusSifreleme().encode("Test Message") == "44154344 32154343112215"
        True
        """
        mesaj = mesaj.lower()
        mesaj = mesaj.replace("j", "i")

        kodlanmis_masaj = ""
        for harf_index in range(len(mesaj)):
            if mesaj[harf_index] != " ":
                sayilar = self.harfi_sayilara_cevir(mesaj[harf_index])
                kodlanmis_masaj += str(sayilar[0]) + str(sayilar[1])
            else:
                kodlanmis_masaj += " "

        return kodlanmis_masaj

    def decode(self, mesaj: str) -> str:
        """
        Polybius şifrelemesine göre mesajın çözülmüş halini döndürür.

        >>> PolybiusSifreleme().decode("44154344 32154343112215") == "test message"
        True

        >>> PolybiusSifreleme().decode("4415434432154343112215") == "testmessage"
        True
        """
        mesaj = mesaj.replace(" ", "  ")
        cozulmus_masaj = ""
        for sayi_index in range(int(len(mesaj) / 2)):
            if mesaj[sayi_index * 2] != " ":
                index1 = mesaj[sayi_index * 2]
                index2 = mesaj[sayi_index * 2 + 1]

                harf = self.sayilardan_harf_cevir(int(index1), int(index2))
                cozulmus_masaj += harf
            else:
                cozulmus_masaj += " "

        return cozulmus_masaj
