# https://www.investopedia.com

from __future__ import annotations


def basit_faiz(
    anapara: float, gunluk_faiz_orani: float, odeme_gunleri: float
) -> float:
    """
    >>> basit_faiz(18000.0, 0.06, 3)
    3240.0
    >>> basit_faiz(0.5, 0.06, 3)
    0.09
    >>> basit_faiz(18000.0, 0.01, 10)
    1800.0
    >>> basit_faiz(18000.0, 0.0, 3)
    0.0
    >>> basit_faiz(5500.0, 0.01, 100)
    5500.0
    >>> basit_faiz(10000.0, -0.06, 3)
    Traceback (most recent call last):
        ...
    ValueError: gunluk_faiz_orani >= 0 olmalıdır
    >>> basit_faiz(-10000.0, 0.06, 3)
    Traceback (most recent call last):
        ...
    ValueError: anapara > 0 olmalıdır
    >>> basit_faiz(5500.0, 0.01, -5)
    Traceback (most recent call last):
        ...
    ValueError: odeme_gunleri > 0 olmalıdır
    """
    if odeme_gunleri <= 0:
        raise ValueError("odeme_gunleri > 0 olmalıdır")
    if gunluk_faiz_orani < 0:
        raise ValueError("gunluk_faiz_orani >= 0 olmalıdır")
    if anapara <= 0:
        raise ValueError("anapara > 0 olmalıdır")
    return anapara * gunluk_faiz_orani * odeme_gunleri


def bilesik_faiz(
    anapara: float,
    yillik_faiz_orani_yuzde: float,
    bileşik_donem_sayisi: float,
) -> float:
    """
    >>> bilesik_faiz(10000.0, 0.05, 3)
    1576.2500000000014
    >>> bilesik_faiz(10000.0, 0.05, 1)
    500.00000000000045
    >>> bilesik_faiz(0.5, 0.05, 3)
    0.07881250000000006
    >>> bilesik_faiz(10000.0, 0.06, -4)
    Traceback (most recent call last):
        ...
    ValueError: bileşik_donem_sayisi > 0 olmalıdır
    >>> bilesik_faiz(10000.0, -3.5, 3.0)
    Traceback (most recent call last):
        ...
    ValueError: yillik_faiz_orani_yuzde >= 0 olmalıdır
    >>> bilesik_faiz(-5500.0, 0.01, 5)
    Traceback (most recent call last):
        ...
    ValueError: anapara > 0 olmalıdır
    """
    if bileşik_donem_sayisi <= 0:
        raise ValueError("bileşik_donem_sayisi > 0 olmalıdır")
    if yillik_faiz_orani_yuzde < 0:
        raise ValueError("yillik_faiz_orani_yuzde >= 0 olmalıdır")
    if anapara <= 0:
        raise ValueError("anapara > 0 olmalıdır")

    return anapara * (
        (1 + yillik_faiz_orani_yuzde) ** bileşik_donem_sayisi
        - 1
    )


def yillik_faiz_orani(
    anapara: float,
    yillik_faiz_orani_yuzde: float,
    yil_sayisi: float,
) -> float:
    """
    >>> yillik_faiz_orani(10000.0, 0.05, 3)
    1618.223072263547
    >>> yillik_faiz_orani(10000.0, 0.05, 1)
    512.6749646744732
    >>> yillik_faiz_orani(0.5, 0.05, 3)
    0.08091115361317736
    >>> yillik_faiz_orani(10000.0, 0.06, -4)
    Traceback (most recent call last):
        ...
    ValueError: yil_sayisi > 0 olmalıdır
    >>> yillik_faiz_orani(10000.0, -3.5, 3.0)
    Traceback (most recent call last):
        ...
    ValueError: yillik_faiz_orani_yuzde >= 0 olmalıdır
    >>> yillik_faiz_orani(-5500.0, 0.01, 5)
    Traceback (most recent call last):
        ...
    ValueError: anapara > 0 olmalıdır
    """
    if yil_sayisi <= 0:
        raise ValueError("yil_sayisi > 0 olmalıdır")
    if yillik_faiz_orani_yuzde < 0:
        raise ValueError("yillik_faiz_orani_yuzde >= 0 olmalıdır")
    if anapara <= 0:
        raise ValueError("anapara > 0 olmalıdır")

    return bilesik_faiz(
        anapara, yillik_faiz_orani_yuzde / 365, yil_sayisi * 365
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
