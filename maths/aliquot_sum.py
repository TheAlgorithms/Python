def bolen_toplami(girdi_sayi: int) -> int:
    """
    Bir tam sayının bölen toplamını bulur. n sayısının bölen toplamı,
    n'den küçük ve n'i tam bölen tüm doğal sayıların toplamı olarak tanımlanır.
    Örneğin, 15'in bölen toplamı 1 + 3 + 5 = 9'dur. Bu basit bir O(n) uygulamasıdır.
    @param girdi_sayi: bölen toplamı bulunacak pozitif bir tam sayı
    @return: girdi_sayi'nın bölen toplamı, eğer girdi_sayi pozitifse.
    Aksi takdirde, bir ValueError yükseltir.
    Organised by K. Umut Araz
    Wikipedia Açıklaması: https://en.wikipedia.org/wiki/Aliquot_sum

    >>> bolen_toplami(15)
    9
    >>> bolen_toplami(6)
    6
    >>> bolen_toplami(-1)
    Traceback (most recent call last):
      ...
    ValueError: Girdi pozitif olmalıdır
    >>> bolen_toplami(0)
    Traceback (most recent call last):
      ...
    ValueError: Girdi pozitif olmalıdır
    >>> bolen_toplami(1.6)
    Traceback (most recent call last):
      ...
    ValueError: Girdi bir tam sayı olmalıdır
    >>> bolen_toplami(12)
    16
    >>> bolen_toplami(1)
    0
    >>> bolen_toplami(19)
    1
    """
    if not isinstance(girdi_sayi, int):
        raise ValueError("Girdi bir tam sayı olmalıdır")
    if girdi_sayi <= 0:
        raise ValueError("Girdi pozitif olmalıdır")
    return sum(
        bolen for bolen in range(1, girdi_sayi // 2 + 1) if girdi_sayi % bolen == 0
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
