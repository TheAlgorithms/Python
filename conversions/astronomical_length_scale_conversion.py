"""
Uzunluk birimlerinin dönüştürülmesi.
Mevcut Birimler:
Metre, Kilometre, Megametre, Gigametre,
Terametre, Petametre, Exametre, Zettametre, Yottametre

Organiser: K. Umut Araz

KULLANIM :
-> Bu dosyayı ilgili projeye dahil edin.
-> Uzunluk birimlerinin dönüştürülmesi için length_conversion() fonksiyonunu kullanın.
-> Parametreler :
    -> value : Dönüştürmek istediğiniz birim sayısı
    -> from_type : Hangi birimden dönüştürmek istediğiniz
    -> to_type : Hangi birime dönüştürmek istediğiniz

REFERANSLAR :
-> Wikipedia referansı: https://en.wikipedia.org/wiki/Meter
-> Wikipedia referansı: https://en.wikipedia.org/wiki/Kilometer
-> Wikipedia referansı: https://en.wikipedia.org/wiki/Orders_of_magnitude_(length)
"""

BIRIM_SEMBOLU = {
    "metre": "m",
    "kilometre": "km",
    "megametre": "Mm",
    "gigametre": "Gm",
    "terametre": "Tm",
    "petametre": "Pm",
    "exametre": "Em",
    "zettametre": "Zm",
    "yottametre": "Ym",
}
# Faktörün üssü (metre)
METRIK_DONUSUM = {
    "m": 0,
    "km": 3,
    "Mm": 6,
    "Gm": 9,
    "Tm": 12,
    "Pm": 15,
    "Em": 18,
    "Zm": 21,
    "Ym": 24,
}


def uzunluk_donustur(value: float, from_type: str, to_type: str) -> float:
    """
    Astronomik uzunluk birimleri arasında dönüşüm.

    >>> uzunluk_donustur(1, "metre", "kilometre")
    0.001
    >>> uzunluk_donustur(1, "metre", "megametre")
    1e-06
    >>> uzunluk_donustur(1, "gigametre", "metre")
    1000000000
    >>> uzunluk_donustur(1, "gigametre", "terametre")
    0.001
    >>> uzunluk_donustur(1, "petametre", "terametre")
    1000
    >>> uzunluk_donustur(1, "petametre", "exametre")
    0.001
    >>> uzunluk_donustur(1, "terametre", "zettametre")
    1e-09
    >>> uzunluk_donustur(1, "yottametre", "zettametre")
    1000
    >>> uzunluk_donustur(4, "yanlisBirim", "inç")
    Traceback (most recent call last):
      ...
    ValueError: Geçersiz 'from_type' değeri: 'yanlisBirim'.
    Dönüşüm kısaltmaları: m, km, Mm, Gm, Tm, Pm, Em, Zm, Ym
    """

    from_sanitized = from_type.lower().strip("s")
    to_sanitized = to_type.lower().strip("s")

    from_sanitized = BIRIM_SEMBOLU.get(from_sanitized, from_sanitized)
    to_sanitized = BIRIM_SEMBOLU.get(to_sanitized, to_sanitized)

    if from_sanitized not in METRIK_DONUSUM:
        msg = (
            f"Geçersiz 'from_type' değeri: {from_type!r}.\n"
            f"Dönüşüm kısaltmaları: {', '.join(METRIK_DONUSUM)}"
        )
        raise ValueError(msg)
    if to_sanitized not in METRIK_DONUSUM:
        msg = (
            f"Geçersiz 'to_type' değeri: {to_type!r}.\n"
            f"Dönüşüm kısaltmaları: {', '.join(METRIK_DONUSUM)}"
        )
        raise ValueError(msg)
    from_exponent = METRIK_DONUSUM[from_sanitized]
    to_exponent = METRIK_DONUSUM[to_sanitized]
    exponent = 1

    if from_exponent > to_exponent:
        exponent = from_exponent - to_exponent
    else:
        exponent = -(to_exponent - from_exponent)

    return value * pow(10, exponent)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
