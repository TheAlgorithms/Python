from __future__ import annotations

import math
from dataclasses import dataclass, field
from types import NoneType
from typing import Self

# Produced By K. Umut Araz

# Temel sınıflar


@dataclass
class Açı:
    """
    Derece cinsinden bir açı (ölçü birimi)

    >>> Açı()
    Açı(derece=90)
    >>> Açı(45.5)
    Açı(derece=45.5)
    >>> Açı(-1)
    Traceback (most recent call last):
        ...
    TypeError: derece 0 ile 360 arasında bir sayısal değer olmalıdır.
    >>> Açı(361)
    Traceback (most recent call last):
        ...
    TypeError: derece 0 ile 360 arasında bir sayısal değer olmalıdır.
    """

    derece: float = 90

    def __post_init__(self) -> None:
        if not isinstance(self.derece, (int, float)) or not 0 <= self.derece <= 360:
            raise TypeError("derece 0 ile 360 arasında bir sayısal değer olmalıdır.")


@dataclass
class Kenar:
    """
    İki boyutlu bir şeklin kenarı, örneğin çokgen vb.
    bitişik_kenarlar: mevcut kenara bitişik olan kenarların listesi
    açı: her bitişik kenar arasındaki açı derece cinsinden
    uzunluk: mevcut kenarın uzunluğu metre cinsinden

    >>> Kenar(5)
    Kenar(uzunluk=5, açı=Açı(derece=90), sonraki_kenar=None)
    >>> Kenar(5, Açı(45.6))
    Kenar(uzunluk=5, açı=Açı(derece=45.6), sonraki_kenar=None)
    >>> Kenar(5, Açı(45.6), Kenar(1, Açı(2)))  # doctest: +ELLIPSIS
    Kenar(uzunluk=5, açı=Açı(derece=45.6), sonraki_kenar=Kenar(uzunluk=1, açı=Açı(d...
    """

    uzunluk: float
    açı: Açı = field(default_factory=Açı)
    sonraki_kenar: Kenar | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.uzunluk, (int, float)) or self.uzunluk <= 0:
            raise TypeError("uzunluk pozitif bir sayısal değer olmalıdır.")
        if not isinstance(self.açı, Açı):
            raise TypeError("açı bir Açı nesnesi olmalıdır.")
        if not isinstance(self.sonraki_kenar, (Kenar, NoneType)):
            raise TypeError("sonraki_kenar bir Kenar veya None olmalıdır.")


@dataclass
class Elips:
    """
    2D yüzeyde geometrik bir elips

    >>> Elips(5, 10)
    Elips(büyük_yarıçap=5, küçük_yarıçap=10)
    >>> Elips(5, 10) is Elips(5, 10)
    False
    >>> Elips(5, 10) == Elips(5, 10)
    True
    """

    büyük_yarıçap: float
    küçük_yarıçap: float

    @property
    def alan(self) -> float:
        """
        >>> Elips(5, 10).alan
        157.07963267948966
        """
        return math.pi * self.büyük_yarıçap * self.küçük_yarıçap

    @property
    def çevre(self) -> float:
        """
        >>> Elips(5, 10).çevre
        47.12388980384689
        """
        return math.pi * (self.büyük_yarıçap + self.küçük_yarıçap)


class Daire(Elips):
    """
    2D yüzeyde geometrik bir daire

    >>> Daire(5)
    Daire(yarıçap=5)
    >>> Daire(5) is Daire(5)
    False
    >>> Daire(5) == Daire(5)
    True
    >>> Daire(5).alan
    78.53981633974483
    >>> Daire(5).çevre
    31.41592653589793
    """

    def __init__(self, yarıçap: float) -> None:
        super().__init__(yarıçap, yarıçap)
        self.yarıçap = yarıçap

    def __repr__(self) -> str:
        return f"Daire(yarıçap={self.yarıçap})"

    @property
    def çap(self) -> float:
        """
        >>> Daire(5).çap
        10
        """
        return self.yarıçap * 2

    def max_parçalar(self, kesim_sayısı: float) -> float:
        """
        Dairenin 'kesim_sayısı' kadar kesildiğinde maksimum kaç parçaya bölünebileceğini döndür.

        >>> daire = Daire(5)
        >>> daire.max_parçalar(0)
        1.0
        >>> daire.max_parçalar(7)
        29.0
        >>> daire.max_parçalar(54)
        1486.0
        >>> daire.max_parçalar(22.5)
        265.375
        >>> daire.max_parçalar(-222)
        Traceback (most recent call last):
            ...
        TypeError: kesim_sayısı pozitif bir sayısal değer olmalıdır.
        >>> daire.max_parçalar("-222")
        Traceback (most recent call last):
            ...
        TypeError: kesim_sayısı pozitif bir sayısal değer olmalıdır.
        """
        if not isinstance(kesim_sayısı, (int, float)) or kesim_sayısı < 0:
            raise TypeError("kesim_sayısı pozitif bir sayısal değer olmalıdır.")
        return (kesim_sayısı + 2 + kesim_sayısı**2) * 0.5


@dataclass
class Çokgen:
    """
    2D yüzeyde bir çokgeni temsil eden soyut bir sınıf.

    >>> Çokgen()
    Çokgen(kenarlar=[])
    """

    kenarlar: list[Kenar] = field(default_factory=list)

    def kenar_ekle(self, kenar: Kenar) -> Self:
        """
        >>> Çokgen().kenar_ekle(Kenar(5))
        Çokgen(kenarlar=[Kenar(uzunluk=5, açı=Açı(derece=90), sonraki_kenar=None)])
        """
        self.kenarlar.append(kenar)
        return self

    def kenar_al(self, index: int) -> Kenar:
        """
        >>> Çokgen().kenar_al(0)
        Traceback (most recent call last):
            ...
        IndexError: list index out of range
        >>> Çokgen().kenar_ekle(Kenar(5)).kenar_al(-1)
        Kenar(uzunluk=5, açı=Açı(derece=90), sonraki_kenar=None)
        """
        return self.kenarlar[index]

    def kenar_ayarla(self, index: int, kenar: Kenar) -> Self:
        """
        >>> Çokgen().kenar_ayarla(0, Kenar(5))
        Traceback (most recent call last):
            ...
        IndexError: list assignment index out of range
        >>> Çokgen().kenar_ekle(Kenar(5)).kenar_ayarla(0, Kenar(10))
        Çokgen(kenarlar=[Kenar(uzunluk=10, açı=Açı(derece=90), sonraki_kenar=None)])
        """
        self.kenarlar[index] = kenar
        return self


class Dikdörtgen(Çokgen):
    """
    2D yüzeyde geometrik bir dikdörtgen.

    >>> dikdörtgen_bir = Dikdörtgen(5, 10)
    >>> dikdörtgen_bir.çevre()
    30
    >>> dikdörtgen_bir.alan()
    50
    """

    def __init__(self, kısa_kenar_uzunluğu: float, uzun_kenar_uzunluğu: float) -> None:
        super().__init__()
        self.kısa_kenar_uzunluğu = kısa_kenar_uzunluğu
        self.uzun_kenar_uzunluğu = uzun_kenar_uzunluğu
        self.post_init()

    def post_init(self) -> None:
        """
        >>> Dikdörtgen(5, 10)  # doctest: +NORMALIZE_WHITESPACE
        Dikdörtgen(kenarlar=[Kenar(uzunluk=5, açı=Açı(derece=90), sonraki_kenar=None),
        Kenar(uzunluk=10, açı=Açı(derece=90), sonraki_kenar=None)])
        """
        self.kısa_kenar = Kenar(self.kısa_kenar_uzunluğu)
        self.uzun_kenar = Kenar(self.uzun_kenar_uzunluğu)
        super().kenar_ekle(self.kısa_kenar)
        super().kenar_ekle(self.uzun_kenar)

    def çevre(self) -> float:
        return (self.kısa_kenar.uzunluk + self.uzun_kenar.uzunluk) * 2

    def alan(self) -> float:
        return self.kısa_kenar.uzunluk * self.uzun_kenar.uzunluk


@dataclass
class Kare(Dikdörtgen):
    """
    2D yüzeyde geometrik bir kareyi temsil eden bir yapı
    >>> kare_bir = Kare(5)
    >>> kare_bir.çevre()
    20
    >>> kare_bir.alan()
    25
    """

    def __init__(self, kenar_uzunluğu: float) -> None:
        super().__init__(kenar_uzunluğu, kenar_uzunluğu)

    def çevre(self) -> float:
        return super().çevre()

    def alan(self) -> float:
        return super().alan()


if __name__ == "__main__":
    __import__("doctest").testmod()
