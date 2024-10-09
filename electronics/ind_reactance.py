# https://tr.wikipedia.org/wiki/Elektriksel_reaktans#Endüktif_reaktans
from __future__ import annotations

from math import pi


def end_reaktans(
    endüktans: float, frekans: float, reaktans: float
) -> dict[str, float]:
    """
    İki verilen elektriksel özelliktenden endüktif reaktans, frekans veya endüktansı hesaplayın
    ve sıfır değeri bir Python sözlüğünde isim/değer çifti olarak döndürün.

    Parametreler
    ------------
    endüktans : Henriler biriminde float

    frekans : Hertz biriminde float

    reaktans : Ohm biriminde float

    >>> end_reaktans(-35e-6, 1e3, 0)
    Traceback (most recent call last):
        ...
    ValueError: Endüktans negatif olamaz

    >>> end_reaktans(35e-6, -1e3, 0)
    Traceback (most recent call last):
        ...
    ValueError: Frekans negatif olamaz

    >>> end_reaktans(35e-6, 0, -1)
    Traceback (most recent call last):
        ...
    ValueError: Endüktif reaktans negatif olamaz

    >>> end_reaktans(0, 10e3, 50)
    {'endüktans': 0.0007957747154594767}

    >>> end_reaktans(35e-3, 0, 50)
    {'frekans': 227.36420441699332}

    >>> end_reaktans(35e-6, 1e3, 0)
    {'reaktans': 0.2199114857512855}

    """

    if (endüktans, frekans, reaktans).count(0) != 1:
        raise ValueError("Bir ve yalnızca bir argüman 0 olmalıdır")
    if endüktans < 0:
        raise ValueError("Endüktans negatif olamaz")
    if frekans < 0:
        raise ValueError("Frekans negatif olamaz")
    if reaktans < 0:
        raise ValueError("Endüktif reaktans negatif olamaz")
    if endüktans == 0:
        return {"endüktans": reaktans / (2 * pi * frekans)}
    elif frekans == 0:
        return {"frekans": reaktans / (2 * pi * endüktans)}
    elif reaktans == 0:
        return {"reaktans": 2 * pi * frekans * endüktans}
    else:
        raise ValueError("Tam olarak bir argüman 0 olmalıdır")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
