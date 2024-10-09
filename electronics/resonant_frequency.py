# https://en.wikipedia.org/wiki/LC_circuit

"""Bir LC devresi, rezonans devresi, tank devresi veya ayarlı devre olarak da adlandırılır,
bir indüktör (L harfi ile temsil edilir) ve bir kapasitörden (C harfi ile temsil edilir)
oluşan bir elektrik devresidir. Devre, bir elektrik rezonatörü olarak işlev görebilir,
bir akort çatalının elektriksel analoğu olarak, devrenin rezonans frekansında salınan enerjiyi depolar.
Kaynak: https://en.wikipedia.org/wiki/LC_circuit
"""

from __future__ import annotations

from math import pi, sqrt


def rezonans_frekansı(indüktans: float, kapasitans: float) -> tuple:
    """
    Bu fonksiyon, verilen indüktans ve kapasitans değerleri için LC devresinin
    rezonans frekansını hesaplayabilir.

    Aşağıda örnekler verilmiştir:
    >>> rezonans_frekansı(indüktans=10, kapasitans=5)
    ('Rezonans frekansı', 0.022507907903927652)
    >>> rezonans_frekansı(indüktans=0, kapasitans=5)
    Traceback (most recent call last):
      ...
    ValueError: İndüktans 0 veya negatif olamaz
    >>> rezonans_frekansı(indüktans=10, kapasitans=0)
    Traceback (most recent call last):
      ...
    ValueError: Kapasitans 0 veya negatif olamaz
    """

    if indüktans <= 0:
        raise ValueError("İndüktans 0 veya negatif olamaz")

    elif kapasitans <= 0:
        raise ValueError("Kapasitans 0 veya negatif olamaz")

    else:
        return (
            "Rezonans frekansı",
            float(1 / (2 * pi * (sqrt(indüktans * kapasitans)))),
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
