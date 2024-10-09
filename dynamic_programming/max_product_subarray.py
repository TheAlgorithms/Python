def max_product_subarray(sayilar: list[int]) -> int:
    """
    Verilen tamsayı listesinin `nums` bitişik alt dizisini çarparak elde edilebilecek
    maksimum çarpımı döndürür.

    Örnek:
    >>> max_product_subarray([2, 3, -2, 4])
    6
    >>> max_product_subarray((-2, 0, -1))
    0
    >>> max_product_subarray([2, 3, -2, 4, -1])
    48
    >>> max_product_subarray([-1])
    -1
    >>> max_product_subarray([0])
    0
    >>> max_product_subarray([])
    0
    >>> max_product_subarray("")
    0
    >>> max_product_subarray(None)
    0
    >>> max_product_subarray([2, 3, -2, 4.5, -1])
    Traceback (most recent call last):
        ...
    ValueError: sayilar tamsayıların bir yinelemeli olmalıdır
    >>> max_product_subarray("ABC")
    Traceback (most recent call last):
        ...
    ValueError: sayilar tamsayıların bir yinelemeli olmalıdır
    """
    if not sayilar:
        return 0

    if not isinstance(sayilar, (list, tuple)) or not all(
        isinstance(sayi, int) for sayi in sayilar
    ):
        raise ValueError("sayilar tamsayıların bir yinelemeli olmalıdır")

    su_an_max = su_an_min = max_carpim = sayilar[0]

    for i in range(1, len(sayilar)):
        # maksimum ve minimum alt dizi çarpımlarını güncelle
        sayi = sayilar[i]
        if sayi < 0:
            su_an_max, su_an_min = su_an_min, su_an_max
        su_an_max = max(sayi, su_an_max * sayi)
        su_an_min = min(sayi, su_an_min * sayi)

        # şu ana kadar bulunan maksimum çarpımı güncelle
        max_carpim = max(max_carpim, su_an_max)

    return max_carpim
