# https://en.m.wikipedia.org/wiki/Electric_power
from __future__ import annotations

from typing import NamedTuple


class Sonuç(NamedTuple):
    ad: str
    değer: float


def elektrik_gücü(gerilim: float, akım: float, güç: float) -> tuple:
    """
    Bu fonksiyon elektrik sisteminin temel değeri olan üç şeyden birini (gerilim, akım, güç) hesaplayabilir.
    örnekler aşağıdadır:
    >>> elektrik_gücü(gerilim=0, akım=2, güç=5)
    Sonuç(ad='gerilim', değer=2.5)
    >>> elektrik_gücü(gerilim=2, akım=2, güç=0)
    Sonuç(ad='güç', değer=4.0)
    >>> elektrik_gücü(gerilim=-2, akım=3, güç=0)
    Sonuç(ad='güç', değer=6.0)
    >>> elektrik_gücü(gerilim=2, akım=4, güç=2)
    Traceback (most recent call last):
        ...
    ValueError: Sadece bir argüman 0 olmalıdır
    >>> elektrik_gücü(gerilim=0, akım=0, güç=2)
    Traceback (most recent call last):
        ...
    ValueError: Sadece bir argüman 0 olmalıdır
    >>> elektrik_gücü(gerilim=0, akım=2, güç=-4)
    Traceback (most recent call last):
        ...
    ValueError: Güç herhangi bir elektrik/elektronik sistemde negatif olamaz
    >>> elektrik_gücü(gerilim=2.2, akım=2.2, güç=0)
    Sonuç(ad='güç', değer=4.84)
    """
    if (gerilim, akım, güç).count(0) != 1:
        raise ValueError("Sadece bir argüman 0 olmalıdır")
    elif güç < 0:
        raise ValueError(
            "Güç herhangi bir elektrik/elektronik sistemde negatif olamaz"
        )
    elif gerilim == 0:
        return Sonuç("gerilim", güç / akım)
    elif akım == 0:
        return Sonuç("akım", güç / gerilim)
    elif güç == 0:
        return Sonuç("güç", float(round(abs(gerilim * akım), 2)))
    else:
        raise ValueError("Tam olarak bir argüman 0 olmalıdır")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
