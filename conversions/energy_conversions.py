"""
Enerji birimlerinin dönüştürülmesi.

Mevcut birimler: joule, kilojoule, megajoule, gigajoule,\
      watt-saniye, watt-saat, kilowatt-saat, newton-metre, kalori_nutr,\
          kilokalori_nutr, elektronvolt, britanya termal birimi, ayak-pound

KULLANIM:
-> Bu dosyayı ilgili projeye dahil edin.
-> Enerji birimlerini dönüştürmek için energy_conversion() fonksiyonunu kullanın.
-> Parametreler:
    -> from_type : Hangi türden dönüştürmek istediğiniz
    -> to_type : Hangi türe dönüştürmek istediğiniz
    -> value : Dönüştürmek istediğiniz değer

REFERANSLAR:
-> Wikipedia referansı: https://en.wikipedia.org/wiki/Units_of_energy
-> Wikipedia referansı: https://en.wikipedia.org/wiki/Joule
-> Wikipedia referansı: https://en.wikipedia.org/wiki/Kilowatt-hour
-> Wikipedia referansı: https://en.wikipedia.org/wiki/Newton-metre
-> Wikipedia referansı: https://en.wikipedia.org/wiki/Calorie
-> Wikipedia referansı: https://en.wikipedia.org/wiki/Electronvolt
-> Wikipedia referansı: https://en.wikipedia.org/wiki/British_thermal_unit
-> Wikipedia referansı: https://en.wikipedia.org/wiki/Foot-pound_(energy)
-> Birim dönüştürücü referansı: https://www.unitconverters.net/energy-converter.html
"""

ENERJI_DONUSTURMA: dict[str, float] = {
    "joule": 1.0,
    "kilojoule": 1_000,
    "megajoule": 1_000_000,
    "gigajoule": 1_000_000_000,
    "wattsecond": 1.0,
    "watthour": 3_600,
    "kilowatthour": 3_600_000,
    "newtonmeter": 1.0,
    "calorie_nutr": 4_186.8,
    "kilocalorie_nutr": 4_186_800.00,
    "electronvolt": 1.602_176_634e-19,
    "britishthermalunit_it": 1_055.055_85,
    "footpound": 1.355_818,
}


def enerji_donustur(from_type: str, to_type: str, value: float) -> float:
    """
    Enerji birimlerinin dönüştürülmesi.
    >>> enerji_donustur("joule", "joule", 1)
    1.0
    >>> enerji_donustur("joule", "kilojoule", 1)
    0.001
    >>> enerji_donustur("joule", "megajoule", 1)
    1e-06
    >>> enerji_donustur("joule", "gigajoule", 1)
    1e-09
    >>> enerji_donustur("joule", "wattsecond", 1)
    1.0
    >>> enerji_donustur("joule", "watthour", 1)
    0.0002777777777777778
    >>> enerji_donustur("joule", "kilowatthour", 1)
    2.7777777777777776e-07
    >>> enerji_donustur("joule", "newtonmeter", 1)
    1.0
    >>> enerji_donustur("joule", "calorie_nutr", 1)
    0.00023884589662749592
    >>> enerji_donustur("joule", "kilocalorie_nutr", 1)
    2.388458966274959e-07
    >>> enerji_donustur("joule", "electronvolt", 1)
    6.241509074460763e+18
    >>> enerji_donustur("joule", "britishthermalunit_it", 1)
    0.0009478171226670134
    >>> enerji_donustur("joule", "footpound", 1)
    0.7375621211696556
    >>> enerji_donustur("joule", "megajoule", 1000)
    0.001
    >>> enerji_donustur("calorie_nutr", "kilocalorie_nutr", 1000)
    1.0
    >>> enerji_donustur("kilowatthour", "joule", 10)
    36000000.0
    >>> enerji_donustur("britishthermalunit_it", "footpound", 1)
    778.1692306784539
    >>> enerji_donustur("watthour", "joule", "a") # doctest: +ELLIPSIS
    Traceback (most recent call last):
      ...
    TypeError: desteklenmeyen operand türleri: 'str' ve 'float'
    >>> enerji_donustur("wrongunit", "joule", 1) # doctest: +ELLIPSIS
    Traceback (most recent call last):
      ...
    ValueError: Hatalı 'from_type' veya 'to_type' değeri: 'wrongunit', 'joule'
    Geçerli değerler: joule, ... footpound
    >>> enerji_donustur("joule", "wrongunit", 1) # doctest: +ELLIPSIS
    Traceback (most recent call last):
      ...
    ValueError: Hatalı 'from_type' veya 'to_type' değeri: 'joule', 'wrongunit'
    Geçerli değerler: joule, ... footpound
    >>> enerji_donustur("123", "abc", 1) # doctest: +ELLIPSIS
    Traceback (most recent call last):
      ...
    ValueError: Hatalı 'from_type' veya 'to_type' değeri: '123', 'abc'
    Geçerli değerler: joule, ... footpound
    """
    if to_type not in ENERJI_DONUSTURMA or from_type not in ENERJI_DONUSTURMA:
        msg = (
            f"Hatalı 'from_type' veya 'to_type' değeri: {from_type!r}, {to_type!r}\n"
            f"Geçerli değerler: {', '.join(ENERJI_DONUSTURMA)}"
        )
        raise ValueError(msg)
    return value * ENERJI_DONUSTURMA[from_type] / ENERJI_DONUSTURMA[to_type]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
