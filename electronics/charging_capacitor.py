# kaynak - The ARRL Handbook for Radio Communications
# https://en.wikipedia.org/wiki/RC_time_constant

"""
Açıklama
-----------
Bir kondansatör bir potansiyel kaynağına (AC veya DC) bağlandığında, genel bir hızla şarj olmaya başlar,
ancak bir direnç bir kondansatörle seri olarak devreye bağlandığında, kondansatör yavaşça şarj olur,
yani normalden daha fazla zaman alır. Kondansatör şarj olurken, voltaj zamanla üstel bir fonksiyondadır.

'direnç(ohm) * kapasitans(farad)' RC zaman sabiti olarak adlandırılır ve τ (tau) olarak da temsil edilebilir.
Bu RC zaman sabitini kullanarak, bir kondansatörün şarj edilmesinin başlangıcından itibaren herhangi bir
zaman 't' deki voltajı, RC içeren üstel fonksiyon yardımıyla bulabiliriz. Hem kondansatörün şarj edilmesinde
hem de deşarj edilmesinde.
"""

from math import exp  # exp değeri = 2.718281828459…


def sarj_kondansatoru(
    kaynak_gerilimi: float,  # volt cinsinden gerilim.
    direnç: float,  # ohm cinsinden direnç.
    kapasitans: float,  # farad cinsinden kapasitans.
    zaman_saniye: float,  # kondansatörün şarj edilmesinin başlatılmasından sonraki saniye cinsinden zaman.
) -> float:
    """
    Kondansatörün şarj edilmesinin başlatılmasından sonraki herhangi bir n. saniyedeki kondansatör voltajını bulun.

    Örnekler
    --------
    >>> sarj_kondansatoru(kaynak_gerilimi=.2,direnç=.9,kapasitans=8.4,zaman_saniye=.5)
    0.013

    >>> sarj_kondansatoru(kaynak_gerilimi=2.2,direnç=3.5,kapasitans=2.4,zaman_saniye=9)
    1.446

    >>> sarj_kondansatoru(kaynak_gerilimi=15,direnç=200,kapasitans=20,zaman_saniye=2)
    0.007

    >>> sarj_kondansatoru(20, 2000, 30*pow(10,-5), 4)
    19.975

    >>> sarj_kondansatoru(kaynak_gerilimi=0,direnç=10.0,kapasitans=.30,zaman_saniye=3)
    Traceback (most recent call last):
        ...
    ValueError: Kaynak gerilimi pozitif olmalıdır.

    >>> sarj_kondansatoru(kaynak_gerilimi=20,direnç=-2000,kapasitans=30,zaman_saniye=4)
    Traceback (most recent call last):
        ...
    ValueError: Direnç pozitif olmalıdır.

    >>> sarj_kondansatoru(kaynak_gerilimi=30,direnç=1500,kapasitans=0,zaman_saniye=4)
    Traceback (most recent call last):
        ...
    ValueError: Kapasitans pozitif olmalıdır.
    """

    if kaynak_gerilimi <= 0:
        raise ValueError("Kaynak gerilimi pozitif olmalıdır.")
    if direnç <= 0:
        raise ValueError("Direnç pozitif olmalıdır.")
    if kapasitans <= 0:
        raise ValueError("Kapasitans pozitif olmalıdır.")
    return round(kaynak_gerilimi * (1 - exp(-zaman_saniye / (direnç * kapasitans))), 3)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
