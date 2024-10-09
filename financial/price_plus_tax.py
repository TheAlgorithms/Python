"""
Bir mal veya hizmetin fiyatını ve vergi oranını vererek vergi dahil fiyatını hesaplar.
"""


def vergi_dahil_fiyat(fiyat: float, vergi_orani: float) -> float:
    """
    >>> vergi_dahil_fiyat(100, 0.25)
    125.0
    >>> vergi_dahil_fiyat(125.50, 0.05)
    131.775
    """
    return fiyat * (1 + vergi_orani)


if __name__ == "__main__":
    print(f"{vergi_dahil_fiyat(100, 0.25) = }")
    print(f"{vergi_dahil_fiyat(125.50, 0.05) = }")
