from __future__ import annotations

ELEKTRON_YÜKÜ = 1.6021e-19  # birimler = C


def elektrik_iletkenliği(
    iletkenlik: float,
    elektron_konsantrasyonu: float,
    hareketlilik: float,
) -> tuple[str, float]:
    """
    Bu fonksiyon üç şeyden birini hesaplayabilir -
    1. İletkenlik
    2. Elektron Konsantrasyonu
    3. Elektron Hareketliliği
    Bu, sağlanan diğer iki değerden hesaplanır
    Örnekler -
    >>> elektrik_iletkenliği(iletkenlik=25, elektron_konsantrasyonu=100, hareketlilik=0)
    ('hareketlilik', 1.5604519068722301e+18)
    >>> elektrik_iletkenliği(iletkenlik=0, elektron_konsantrasyonu=1600, hareketlilik=200)
    ('iletkenlik', 5.12672e-14)
    >>> elektrik_iletkenliği(iletkenlik=1000, elektron_konsantrasyonu=0, hareketlilik=1200)
    ('elektron_konsantrasyonu', 5.201506356240767e+18)
    """
    if (iletkenlik, elektron_konsantrasyonu, hareketlilik).count(0) != 1:
        raise ValueError("2 değerden fazla veya az değer sağlayamazsınız")
    elif iletkenlik < 0:
        raise ValueError("İletkenlik negatif olamaz")
    elif elektron_konsantrasyonu < 0:
        raise ValueError("Elektron konsantrasyonu negatif olamaz")
    elif hareketlilik < 0:
        raise ValueError("Hareketlilik negatif olamaz")
    elif iletkenlik == 0:
        return (
            "iletkenlik",
            hareketlilik * elektron_konsantrasyonu * ELEKTRON_YÜKÜ,
        )
    elif elektron_konsantrasyonu == 0:
        return (
            "elektron_konsantrasyonu",
            iletkenlik / (hareketlilik * ELEKTRON_YÜKÜ),
        )
    else:
        return (
            "hareketlilik",
            iletkenlik / (elektron_konsantrasyonu * ELEKTRON_YÜKÜ),
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
