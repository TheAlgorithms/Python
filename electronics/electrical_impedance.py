"""Elektrik empedansı, bir devrenin bir voltaj uygulandığında bir akıma karşı
gösterdiği direncin ölçüsüdür. Empedans, direnç kavramını alternatif akım (AC) devrelerine genişletir.
Kaynak: https://en.wikipedia.org/wiki/Electrical_impedance
"""

from __future__ import annotations

from math import pow, sqrt


def elektrik_empedansi(
    direnç: float, reaktans: float, empedans: float
) -> dict[str, float]:
    """
    Elektrik Empedansı formülünü, direnç, reaktans ve empedans gibi verilen herhangi iki elektriksel değer üzerinde uygulayın
    ve ardından sıfır değeri olan adı/değer çiftini bir Python sözlüğünde döndürün.

    >>> elektrik_empedansi(3,4,0)
    {'empedans': 5.0}
    >>> elektrik_empedansi(0,4,5)
    {'direnç': 3.0}
    >>> elektrik_empedansi(3,0,5)
    {'reaktans': 4.0}
    >>> elektrik_empedansi(3,4,5)
    Traceback (most recent call last):
      ...
    ValueError: Bir ve yalnızca bir argüman 0 olmalıdır
    """
    if (direnç, reaktans, empedans).count(0) != 1:
        raise ValueError("Bir ve yalnızca bir argüman 0 olmalıdır")
    if direnç == 0:
        return {"direnç": sqrt(pow(empedans, 2) - pow(reaktans, 2))}
    elif reaktans == 0:
        return {"reaktans": sqrt(pow(empedans, 2) - pow(direnç, 2))}
    elif empedans == 0:
        return {"empedans": sqrt(pow(direnç, 2) + pow(reaktans, 2))}
    else:
        raise ValueError("Tam olarak bir argüman 0 olmalıdır")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
