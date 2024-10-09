"""
Referans: https://www.investopedia.com/terms/p/presentvalue.asp

Yıllık nakit akışlarının bugünkü değerini hesaplayan bir algoritma...
1. İskonto oranı (ondalık olarak, yüzde değil)
2. Nakit akışlarının bir dizisi, nakit akışının indeksi ilgili yılı temsil eder

Not: Bu algoritma, nakit akışlarının belirtilen yılın sonunda ödendiğini varsayar
"""


def bugunku_deger(iskonto_orani: float, nakit_akislari: list[float]) -> float:
    """
    >>> bugunku_deger(0.13, [10, 20.70, -293, 297])
    4.69
    >>> bugunku_deger(0.07, [-109129.39, 30923.23, 15098.93, 29734.39])
    -42739.63
    >>> bugunku_deger(0.07, [109129.39, 30923.23, 15098.93, 29734.39])
    175519.15
    >>> bugunku_deger(-1, [109129.39, 30923.23, 15098.93, 29734.39])
    Traceback (most recent call last):
        ...
    ValueError: İskonto oranı negatif olamaz
    >>> bugunku_deger(0.03, [])
    Traceback (most recent call last):
        ...
    ValueError: Nakit akışları listesi boş olamaz
    """
    if iskonto_orani < 0:
        raise ValueError("İskonto oranı negatif olamaz")
    if not nakit_akislari:
        raise ValueError("Nakit akışları listesi boş olamaz")
    bugunku_deger = sum(
        nakit_akisi / ((1 + iskonto_orani) ** i) for i, nakit_akisi in enumerate(nakit_akislari)
    )
    return round(bugunku_deger, ndigits=2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
