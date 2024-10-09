# İkili kaydırmalar hakkında bilgi:
# https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types
# https://www.interviewcake.com/concept/java/bit-shift


def mantiksal_sola_kaydir(sayi: int, kaydirma_miktari: int) -> str:
    """
    2 pozitif tam sayı alır.
    'sayi', 'kaydirma_miktari' kadar mantıksal olarak sola kaydırılacak tam sayıdır.
    Yani (sayi << kaydirma_miktari)
    Kaydırılmış ikili gösterimi döner.

    >>> mantiksal_sola_kaydir(0, 1)
    '0b0'
    >>> mantiksal_sola_kaydir(1, 1)
    '0b10'
    >>> mantiksal_sola_kaydir(1, 5)
    '0b100000'
    >>> mantiksal_sola_kaydir(17, 2)
    '0b1000100'
    >>> mantiksal_sola_kaydir(1983, 4)
    '0b111101111110000'
    >>> mantiksal_sola_kaydir(1, -1)
    Traceback (most recent call last):
        ...
    ValueError: her iki girdi de pozitif tam sayılar olmalıdır
    """
    if sayi < 0 or kaydirma_miktari < 0:
        raise ValueError("her iki girdi de pozitif tam sayılar olmalıdır")

    ikili_sayi = str(bin(sayi))
    ikili_sayi += "0" * kaydirma_miktari
    return ikili_sayi


def mantiksal_saga_kaydir(sayi: int, kaydirma_miktari: int) -> str:
    """
    2 pozitif tam sayı alır.
    'sayi', 'kaydirma_miktari' kadar mantıksal olarak sağa kaydırılacak tam sayıdır.
    Yani (sayi >>> kaydirma_miktari)
    Kaydırılmış ikili gösterimi döner.

    >>> mantiksal_saga_kaydir(0, 1)
    '0b0'
    >>> mantiksal_saga_kaydir(1, 1)
    '0b0'
    >>> mantiksal_saga_kaydir(1, 5)
    '0b0'
    >>> mantiksal_saga_kaydir(17, 2)
    '0b100'
    >>> mantiksal_saga_kaydir(1983, 4)
    '0b1111011'
    >>> mantiksal_saga_kaydir(1, -1)
    Traceback (most recent call last):
        ...
    ValueError: her iki girdi de pozitif tam sayılar olmalıdır
    """
    if sayi < 0 or kaydirma_miktari < 0:
        raise ValueError("her iki girdi de pozitif tam sayılar olmalıdır")

    ikili_sayi = str(bin(sayi))[2:]
    if kaydirma_miktari >= len(ikili_sayi):
        return "0b0"
    kaydirilmis_ikili_sayi = ikili_sayi[: len(ikili_sayi) - kaydirma_miktari]
    return "0b" + kaydirilmis_ikili_sayi


def aritmetik_saga_kaydir(sayi: int, kaydirma_miktari: int) -> str:
    """
    2 tam sayı alır.
    'sayi', 'kaydirma_miktari' kadar aritmetik olarak sağa kaydırılacak tam sayıdır.
    Yani (sayi >> kaydirma_miktari)
    Kaydırılmış ikili gösterimi döner.

    >>> aritmetik_saga_kaydir(0, 1)
    '0b0'
    >>> aritmetik_saga_kaydir(1, 1)
    '0b0'
    >>> aritmetik_saga_kaydir(-1, 1)
    '0b1'
    >>> aritmetik_saga_kaydir(17, 2)
    '0b100'
    >>> aritmetik_saga_kaydir(-17, 2)
    '0b111011'
    >>> aritmetik_saga_kaydir(-1983, 4)
    '0b111110000100'
    """
    if sayi >= 0:  # Pozitif sayının ikili gösterimini al
        ikili_sayi = "0" + str(bin(sayi)).strip("-")[2:]
    else:  # Negatif sayının ikili (2'nin tamamlayanı) gösterimini al
        ikili_sayi_uzunlugu = len(bin(sayi)[3:])  # Sayının 2'nin tamamlayanı bulun
        ikili_sayi = bin(abs(sayi) - (1 << ikili_sayi_uzunlugu))[3:]
        ikili_sayi = (
            "1" + "0" * (ikili_sayi_uzunlugu - len(ikili_sayi)) + ikili_sayi
        )

    if kaydirma_miktari >= len(ikili_sayi):
        return "0b" + ikili_sayi[0] * len(ikili_sayi)
    return (
        "0b"
        + ikili_sayi[0] * kaydirma_miktari
        + ikili_sayi[: len(ikili_sayi) - kaydirma_miktari]
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
