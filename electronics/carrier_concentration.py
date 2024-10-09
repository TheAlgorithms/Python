# https://en.wikipedia.org/wiki/Charge_carrier_density
# https://www.pveducation.org/pvcdrom/pn-junctions/equilibrium-carrier-concentration
# http://www.ece.utep.edu/courses/ee3329/ee3329/Studyguide/ToC/Fundamentals/Carriers/concentrations.html

from __future__ import annotations


def tasiyici_konsantrasyonu(
    elektron_kons: float,
    delik_kons: float,
    iç_kons: float,
) -> tuple:
    """
    Bu fonksiyon üç değerden herhangi birini hesaplayabilir -
    1. Elektron Konsantrasyonu
    2. Delik Konsantrasyonu
    3. İçsel Konsantrasyon
    diğer ikisi verildiğinde.
    Örnekler -
    >>> tasiyici_konsantrasyonu(elektron_kons=25, delik_kons=100, iç_kons=0)
    ('iç_kons', 50.0)
    >>> tasiyici_konsantrasyonu(elektron_kons=0, delik_kons=1600, iç_kons=200)
    ('elektron_kons', 25.0)
    >>> tasiyici_konsantrasyonu(elektron_kons=1000, delik_kons=0, iç_kons=1200)
    ('delik_kons', 1440.0)
    >>> tasiyici_konsantrasyonu(elektron_kons=1000, delik_kons=400, iç_kons=1200)
    Traceback (most recent call last):
        ...
    ValueError: 2 değerden fazla veya az değer veremezsiniz
    >>> tasiyici_konsantrasyonu(elektron_kons=-1000, delik_kons=0, iç_kons=1200)
    Traceback (most recent call last):
        ...
    ValueError: Bir yarı iletkende elektron konsantrasyonu negatif olamaz
    >>> tasiyici_konsantrasyonu(elektron_kons=0, delik_kons=-400, iç_kons=1200)
    Traceback (most recent call last):
        ...
    ValueError: Bir yarı iletkende delik konsantrasyonu negatif olamaz
    >>> tasiyici_konsantrasyonu(elektron_kons=0, delik_kons=400, iç_kons=-1200)
    Traceback (most recent call last):
        ...
    ValueError: Bir yarı iletkende içsel konsantrasyon negatif olamaz
    """
    if (elektron_kons, delik_kons, iç_kons).count(0) != 1:
        raise ValueError("2 değerden fazla veya az değer veremezsiniz")
    elif elektron_kons < 0:
        raise ValueError("Bir yarı iletkende elektron konsantrasyonu negatif olamaz")
    elif delik_kons < 0:
        raise ValueError("Bir yarı iletkende delik konsantrasyonu negatif olamaz")
    elif iç_kons < 0:
        raise ValueError("Bir yarı iletkende içsel konsantrasyon negatif olamaz")
    elif elektron_kons == 0:
        return (
            "elektron_kons",
            iç_kons**2 / delik_kons,
        )
    elif delik_kons == 0:
        return (
            "delik_kons",
            iç_kons**2 / elektron_kons,
        )
    elif iç_kons == 0:
        return (
            "iç_kons",
            (elektron_kons * delik_kons) ** 0.5,
        )
    else:
        return (-1, -1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
