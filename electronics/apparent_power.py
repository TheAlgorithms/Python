import cmath
import math


def gorunen_guc(
    gerilim: float, akim: float, gerilim_acisi: float, akim_acisi: float
) -> complex:
    """
    Tek fazlı AC devresinde görünen gücü hesaplayın.

    Referans: https://en.wikipedia.org/wiki/AC_power#Apparent_power

    >>> gorunen_guc(100, 5, 0, 0)
    (500+0j)
    >>> gorunen_guc(100, 5, 90, 0)
    (3.061616997868383e-14+500j)
    >>> gorunen_guc(100, 5, -45, -60)
    (-129.40952255126027-482.9629131445341j)
    >>> gorunen_guc(200, 10, -30, -90)
    (-999.9999999999998-1732.0508075688776j)
    """
    # Açıları dereceden radyana çevir
    gerilim_acisi_rad = math.radians(gerilim_acisi)
    akim_acisi_rad = math.radians(akim_acisi)

    # Gerilim ve akımı dikdörtgen forma çevir
    gerilim_dikdortgen = cmath.rect(gerilim, gerilim_acisi_rad)
    akim_dikdortgen = cmath.rect(akim, akim_acisi_rad)

    # Görünen gücü hesapla
    return gerilim_dikdortgen * akim_dikdortgen


if __name__ == "__main__":
    import doctest

    doctest.testmod()
