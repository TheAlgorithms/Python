# https://en.wikipedia.org/wiki/Coulomb%27s_law

from __future__ import annotations

COULOMBS_CONSTANT = 8.988e9  # birimler = N * m^2 * C^-2


def coulombs_yasasi(
    kuvvet: float, yük1: float, yük2: float, mesafe: float
) -> dict[str, float]:
    """
    Coulomb Yasası'nı verilen üç değere uygulayın. Bunlar kuvvet, yük1,
    yük2 veya mesafe olabilir ve ardından bir Python sözlüğünde sıfır
    değerin ad/değer çiftini döndürün.

    Coulomb Yasası, iki nokta yükü arasındaki elektrostatik çekim veya
    itme kuvvetinin büyüklüğünün, yüklerin büyüklüklerinin çarpımı ile
    doğru orantılı ve aralarındaki mesafenin karesi ile ters orantılı
    olduğunu belirtir.

    Referans
    ----------
    Coulomb (1785) "Premier mémoire sur l'électricité et le magnétisme,"
    Histoire de l'Académie Royale des Sciences, ss. 569-577.

    Parametreler
    ----------
    kuvvet : Newton cinsinden birimlere sahip float

    yük1 : Coulomb cinsinden birimlere sahip float

    yük2 : Coulomb cinsinden birimlere sahip float

    mesafe : metre cinsinden birimlere sahip float

    Dönüş
    -------
    sonuç : sıfır değerin ad/değer çiftini içeren sözlük

    >>> coulombs_yasasi(kuvvet=0, yük1=3, yük2=5, mesafe=2000)
    {'kuvvet': 33705.0}

    >>> coulombs_yasasi(kuvvet=10, yük1=3, yük2=5, mesafe=0)
    {'mesafe': 116112.01488218177}

    >>> coulombs_yasasi(kuvvet=10, yük1=0, yük2=5, mesafe=2000)
    {'yük1': 0.0008900756564307966}

    >>> coulombs_yasasi(kuvvet=0, yük1=0, yük2=5, mesafe=2000)
    Traceback (most recent call last):
      ...
    ValueError: Sadece bir argüman 0 olmalıdır

    >>> coulombs_yasasi(kuvvet=0, yük1=3, yük2=5, mesafe=-2000)
    Traceback (most recent call last):
      ...
    ValueError: Mesafe negatif olamaz

    """

    yük_çarpımı = abs(yük1 * yük2)

    if (kuvvet, yük1, yük2, mesafe).count(0) != 1:
        raise ValueError("Sadece bir argüman 0 olmalıdır")
    if mesafe < 0:
        raise ValueError("Mesafe negatif olamaz")
    if kuvvet == 0:
        kuvvet = COULOMBS_CONSTANT * yük_çarpımı / (mesafe**2)
        return {"kuvvet": kuvvet}
    elif yük1 == 0:
        yük1 = abs(kuvvet) * (mesafe**2) / (COULOMBS_CONSTANT * yük2)
        return {"yük1": yük1}
    elif yük2 == 0:
        yük2 = abs(kuvvet) * (mesafe**2) / (COULOMBS_CONSTANT * yük1)
        return {"yük2": yük2}
    elif mesafe == 0:
        mesafe = (COULOMBS_CONSTANT * yük_çarpımı / abs(kuvvet)) ** 0.5
        return {"mesafe": mesafe}
    raise ValueError("Tam olarak bir argüman 0 olmalıdır")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
