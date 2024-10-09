"""
Produced by K. Umut Araz

https://en.wikipedia.org/wiki/Fuzzy_set
"""

from __future__ import annotations

from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np


@dataclass
class BulanıkKüme:
    """
    Üçgen bulanık kümeleri temsil etmek ve manipüle etmek için bir sınıf.
    Nitelikler:
        isim: Bulanık kümenin adı veya etiketi.
        sol_sınır: Bulanık kümenin sol sınırı.
        tepe: Bulanık kümenin tepe (merkez) değeri.
        sağ_sınır: Bulanık kümenin sağ sınırı.
    Metotlar:
        üyelik(x): Bir girdinin 'x' bulanık kümedeki üyelik değerini hesapla.
        birleşim(diger): Bu bulanık kümenin başka bir bulanık küme ile birleşimini hesapla.
        kesişim(diger): Bu bulanık kümenin başka bir bulanık küme ile kesişimini hesapla.
        tamamlayıcı(): Bu bulanık kümenin tamamlayıcısını (negasyonunu) hesapla.
        çiz(): Bulanık kümenin üyelik fonksiyonunu çiz.

    >>> sheru = BulanıkKüme("Sheru", 0.4, 1, 0.6)
    >>> sheru
    BulanıkKüme(isim='Sheru', sol_sınır=0.4, tepe=1, sağ_sınır=0.6)
    >>> str(sheru)
    'Sheru: [0.4, 1, 0.6]'

    >>> siya = BulanıkKüme("Siya", 0.5, 1, 0.7)
    >>> siya
    BulanıkKüme(isim='Siya', sol_sınır=0.5, tepe=1, sağ_sınır=0.7)

    # Tamamlayıcı İşlemi
    >>> sheru.tamamlayıcı()
    BulanıkKüme(isim='¬Sheru', sol_sınır=0.4, tepe=0.6, sağ_sınır=0)
    >>> siya.tamamlayıcı()  # doctest: +NORMALIZE_WHITESPACE
    BulanıkKüme(isim='¬Siya', sol_sınır=0.30000000000000004, tepe=0.5,
     sağ_sınır=0)

    # Kesişim İşlemi
    >>> siya.kesişim(sheru)
    BulanıkKüme(isim='Siya ∩ Sheru', sol_sınır=0.5, tepe=0.6, sağ_sınır=1.0)

    # Üyelik İşlemi
    >>> sheru.üyelik(0.5)
    0.16666666666666663
    >>> sheru.üyelik(0.6)
    0.0

    # Birleşim İşlemleri
    >>> siya.birleşim(sheru)
    BulanıkKüme(isim='Siya U Sheru', sol_sınır=0.4, tepe=0.7, sağ_sınır=1.0)
    """

    isim: str
    sol_sınır: float
    tepe: float
    sağ_sınır: float

    def __str__(self) -> str:
        """
        >>> BulanıkKüme("bulanık_küme", 0.1, 0.2, 0.3)
        BulanıkKüme(isim='bulanık_küme', sol_sınır=0.1, tepe=0.2, sağ_sınır=0.3)
        """
        return (
            f"{self.isim}: [{self.sol_sınır}, {self.tepe}, {self.sağ_sınır}]"
        )

    def tamamlayıcı(self) -> BulanıkKüme:
        """
        Bu bulanık kümenin tamamlayıcısını (negasyonunu) hesapla.
        Döndürür:
            BulanıkKüme: Tamamlayıcıyı temsil eden yeni bir bulanık küme.

        >>> BulanıkKüme("bulanık_küme", 0.1, 0.2, 0.3).tamamlayıcı()
        BulanıkKüme(isim='¬bulanık_küme', sol_sınır=0.7, tepe=0.9, sağ_sınır=0.8)
        """
        return BulanıkKüme(
            f"¬{self.isim}",
            1 - self.sağ_sınır,
            1 - self.sol_sınır,
            1 - self.tepe,
        )

    def kesişim(self, diger) -> BulanıkKüme:
        """
        Bu bulanık kümenin başka bir bulanık küme ile kesişimini hesapla.
        Argümanlar:
            diger: Kesişim yapılacak başka bir bulanık küme.
        Döndürür:
            Kesişimi temsil eden yeni bir bulanık küme.

        >>> BulanıkKüme("a", 0.1, 0.2, 0.3).kesişim(BulanıkKüme("b", 0.4, 0.5, 0.6))
        BulanıkKüme(isim='a ∩ b', sol_sınır=0.4, tepe=0.3, sağ_sınır=0.35)
        """
        return BulanıkKüme(
            f"{self.isim} ∩ {diger.isim}",
            max(self.sol_sınır, diger.sol_sınır),
            min(self.sağ_sınır, diger.sağ_sınır),
            (self.tepe + diger.tepe) / 2,
        )

    def üyelik(self, x: float) -> float:
        """
        Bir girdinin 'x' bulanık kümedeki üyelik değerini hesapla.
        Döndürür:
            'x'in bulanık kümedeki üyelik değeri.

        >>> a = BulanıkKüme("a", 0.1, 0.2, 0.3)
        >>> a.üyelik(0.09)
        0.0
        >>> a.üyelik(0.1)
        0.0
        >>> a.üyelik(0.11)
        0.09999999999999995
        >>> a.üyelik(0.4)
        0.0
        >>> BulanıkKüme("A", 0, 0.5, 1).üyelik(0.1)
        0.2
        >>> BulanıkKüme("B", 0.2, 0.7, 1).üyelik(0.6)
        0.8
        """
        if x <= self.sol_sınır or x >= self.sağ_sınır:
            return 0.0
        elif self.sol_sınır < x <= self.tepe:
            return (x - self.sol_sınır) / (self.tepe - self.sol_sınır)
        elif self.tepe < x < self.sağ_sınır:
            return (self.sağ_sınır - x) / (self.sağ_sınır - self.tepe)
        msg = f"Bulanık küme için geçersiz değer {x}: {self}"
        raise ValueError(msg)

    def birleşim(self, diger) -> BulanıkKüme:
        """
        Bu bulanık kümenin başka bir bulanık küme ile birleşimini hesapla.
        Argümanlar:
            diger (BulanıkKüme): Birleşim yapılacak başka bir bulanık küme.
        Döndürür:
            Birleşimi temsil eden yeni bir bulanık küme.

        >>> BulanıkKüme("a", 0.1, 0.2, 0.3).birleşim(BulanıkKüme("b", 0.4, 0.5, 0.6))
        BulanıkKüme(isim='a U b', sol_sınır=0.1, tepe=0.6, sağ_sınır=0.35)
        """
        return BulanıkKüme(
            f"{self.isim} U {diger.isim}",
            min(self.sol_sınır, diger.sol_sınır),
            max(self.sağ_sınır, diger.sağ_sınır),
            (self.tepe + diger.tepe) / 2,
        )

    def çiz(self):
        """
        Bulanık kümenin üyelik fonksiyonunu çiz.
        """
        x = np.linspace(0, 1, 1000)
        y = [self.üyelik(xi) for xi in x]

        plt.plot(x, y, label=self.isim)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    a = BulanıkKüme("A", 0, 0.5, 1)
    b = BulanıkKüme("B", 0.2, 0.7, 1)

    a.çiz()
    b.çiz()

    plt.xlabel("x")
    plt.ylabel("Üyelik")
    plt.legend()
    plt.show()

    birleşim_ab = a.birleşim(b)
    kesişim_ab = a.kesişim(b)
    tamamlayıcı_a = a.tamamlayıcı()

    birleşim_ab.çiz()
    kesişim_ab.çiz()
    tamamlayıcı_a.çiz()

    plt.xlabel("x")
    plt.ylabel("Üyelik")
    plt.legend()
    plt.show()
