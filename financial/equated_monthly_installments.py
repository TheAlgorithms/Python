"""
Aylık amortisman tutarını hesaplama programı, verilen
- Alınan anapara
- Yıllık faiz oranı
- Krediyi geri ödemek için yıl sayısı

Wikipedia Referansı: https://en.wikipedia.org/wiki/Equated_monthly_installment
"""


def esit_aylik_taksitler(
    anapara: float, yillik_faiz_orani: float, geri_odeme_yili: int
) -> float:
    """
    Aylık amortisman tutarı formülü:
    A = p * r * (1 + r)^n / ((1 + r)^n - 1)
    burada p anapara, r aylık faiz oranı
    ve n ödeme sayısıdır

    >>> esit_aylik_taksitler(25000, 0.12, 3)
    830.3577453212793
    >>> esit_aylik_taksitler(25000, 0.12, 10)
    358.67737100646826
    >>> esit_aylik_taksitler(0, 0.12, 3)
    Traceback (most recent call last):
        ...
    Exception: Alınan anapara > 0 olmalıdır
    >>> esit_aylik_taksitler(25000, -1, 3)
    Traceback (most recent call last):
        ...
    Exception: Faiz oranı >= 0 olmalıdır
    >>> esit_aylik_taksitler(25000, 0.12, 0)
    Traceback (most recent call last):
        ...
    Exception: Geri ödeme yılı 0'dan büyük bir tamsayı olmalıdır
    """
    if anapara <= 0:
        raise Exception("Alınan anapara > 0 olmalıdır")
    if yillik_faiz_orani < 0:
        raise Exception("Faiz oranı >= 0 olmalıdır")
    if geri_odeme_yili <= 0 or not isinstance(geri_odeme_yili, int):
        raise Exception("Geri ödeme yılı 0'dan büyük bir tamsayı olmalıdır")

    # Yıllık faiz oranı aylık oranı elde etmek için 12'ye bölünür
    aylik_faiz_orani = yillik_faiz_orani / 12

    # Geri ödeme yılı, ödeme sayısını elde etmek için 12 ile çarpılır çünkü ödeme aylıktır
    odeme_sayisi = geri_odeme_yili * 12

    return (
        anapara
        * aylik_faiz_orani
        * (1 + aylik_faiz_orani) ** odeme_sayisi
        / ((1 + aylik_faiz_orani) ** odeme_sayisi - 1)
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
