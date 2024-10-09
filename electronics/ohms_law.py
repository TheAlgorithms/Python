# https://en.wikipedia.org/wiki/Ohm%27s_law
from __future__ import annotations


def ohm_kanunu(gerilim: float, akım: float, direnç: float) -> dict[str, float]:
    """
    Ohm Kanunu'nu, gerilim, akım ve direnç gibi verilen herhangi iki elektriksel değer üzerinde uygulayın
    ve ardından sıfır değeri olan adı/değer çiftini bir Python sözlüğünde döndürün.

    >>> ohm_kanunu(gerilim=10, direnç=5, akım=0)
    {'akım': 2.0}
    >>> ohm_kanunu(gerilim=0, akım=0, direnç=10)
    Traceback (most recent call last):
      ...
    ValueError: Bir ve yalnızca bir argüman 0 olmalıdır
    >>> ohm_kanunu(gerilim=0, akım=1, direnç=-2)
    Traceback (most recent call last):
      ...
    ValueError: Direnç negatif olamaz
    >>> ohm_kanunu(direnç=0, gerilim=-10, akım=1)
    {'direnç': -10.0}
    >>> ohm_kanunu(gerilim=0, akım=-1.5, direnç=2)
    {'gerilim': -3.0}
    """
    if (gerilim, akım, direnç).count(0) != 1:
        raise ValueError("Bir ve yalnızca bir argüman 0 olmalıdır")
    if direnç < 0:
        raise ValueError("Direnç negatif olamaz")
    if gerilim == 0:
        return {"gerilim": float(akım * direnç)}
    elif akım == 0:
        return {"akım": gerilim / direnç}
    elif direnç == 0:
        return {"direnç": gerilim / akım}
    else:
        raise ValueError("Tam olarak bir argüman 0 olmalıdır")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
