"""
Uzunluk birimlerinin dönüştürülmesi.
Mevcut Birimler: - Metre, Kilometre, Ayak, İnç, Santimetre, Yarda, Mil, Milimetre

Organiser: K. Umut Araz

KULLANIM:
-> Bu dosyayı ilgili projeye dahil edin.
-> Uzunluk birimlerinin dönüştürülmesi için length_conversion() fonksiyonunu kullanın.
-> Parametreler:
    -> value: Dönüştürmek istediğiniz birim sayısı
    -> from_type: Hangi birimden dönüştürmek istediğiniz
    -> to_type: Hangi birime dönüştürmek istediğiniz

REFERANSLAR:
-> Vikipedi referansı: https://tr.wikipedia.org/wiki/Metre
-> Vikipedi referansı: https://tr.wikipedia.org/wiki/Kilometre
-> Vikipedi referansı: https://tr.wikipedia.org/wiki/Ayak
-> Vikipedi referansı: https://tr.wikipedia.org/wiki/İnç
-> Vikipedi referansı: https://tr.wikipedia.org/wiki/Santimetre
-> Vikipedi referansı: https://tr.wikipedia.org/wiki/Yarda
-> Vikipedi referansı: https://tr.wikipedia.org/wiki/Mil
-> Vikipedi referansı: https://tr.wikipedia.org/wiki/Milimetre
"""

from typing import NamedTuple


class FromTo(NamedTuple):
    from_factor: float
    to_factor: float


TIP_DONUSUMU = {
    "milimetre": "mm",
    "santimetre": "cm",
    "metre": "m",
    "kilometre": "km",
    "inç": "in",
    "ayak": "ft",
    "yarda": "yd",
    "mil": "mi",
}

METRIK_DONUSUM = {
    "mm": FromTo(0.001, 1000),
    "cm": FromTo(0.01, 100),
    "m": FromTo(1, 1),
    "km": FromTo(1000, 0.001),
    "in": FromTo(0.0254, 39.3701),
    "ft": FromTo(0.3048, 3.28084),
    "yd": FromTo(0.9144, 1.09361),
    "mi": FromTo(1609.34, 0.000621371),
}


def uzunluk_donustur(value: float, from_type: str, to_type: str) -> float:
    """
    Uzunluk birimleri arasında dönüşüm.

    >>> uzunluk_donustur(4, "METRE", "AYAK")
    13.12336
    >>> uzunluk_donustur(4, "M", "FT")
    13.12336
    >>> uzunluk_donustur(1, "metre", "kilometre")
    0.001
    >>> uzunluk_donustur(1, "kilometre", "inç")
    39370.1
    >>> uzunluk_donustur(3, "kilometre", "mil")
    1.8641130000000001
    >>> uzunluk_donustur(2, "ayak", "metre")
    0.6096
    >>> uzunluk_donustur(4, "ayak", "yarda")
    1.333329312
    >>> uzunluk_donustur(1, "inç", "metre")
    0.0254
    >>> uzunluk_donustur(2, "inç", "mil")
    3.15656468e-05
    >>> uzunluk_donustur(2, "santimetre", "milimetre")
    20.0
    >>> uzunluk_donustur(2, "santimetre", "yarda")
    0.0218722
    >>> uzunluk_donustur(4, "yarda", "metre")
    3.6576
    >>> uzunluk_donustur(4, "yarda", "kilometre")
    0.0036576
    >>> length_conversion(3, "foot", "meter")
    0.9144000000000001
    >>> length_conversion(3, "foot", "inch")
    36.00001944
    >>> length_conversion(4, "mile", "kilometer")
    6.43736
    >>> length_conversion(2, "miles", "InChEs")
    126719.753468
    >>> length_conversion(3, "millimeter", "centimeter")
    0.3
    >>> length_conversion(3, "mm", "in")
    0.1181103
    >>> length_conversion(4, "wrongUnit", "inch")
    Traceback (most recent call last):
      ...
    ValueError: Invalid 'from_type' value: 'wrongUnit'.
    Conversion abbreviations are: mm, cm, m, km, in, ft, yd, mi
    """
    new_from = from_type.lower().rstrip("s")
    new_from = TYPE_CONVERSION.get(new_from, new_from)
    new_to = to_type.lower().rstrip("s")
    new_to = TYPE_CONVERSION.get(new_to, new_to)
    if new_from not in METRIC_CONVERSION:
        msg = (
            f"Invalid 'from_type' value: {from_type!r}.\n"
            f"Conversion abbreviations are: {', '.join(METRIC_CONVERSION)}"
        )
        raise ValueError(msg)
    if new_to not in METRIC_CONVERSION:
        msg = (
            f"Invalid 'to_type' value: {to_type!r}.\n"
            f"Conversion abbreviations are: {', '.join(METRIC_CONVERSION)}"
        )
        raise ValueError(msg)
    return (
        value
        * METRIC_CONVERSION[new_from].from_factor
        * METRIC_CONVERSION[new_to].to_factor
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
