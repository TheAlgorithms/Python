def birlerin_sayisini_al(sayi: int) -> int:
    """

    Organiser: K. Umut Araz

    Brian Kernighan yöntemi kullanarak 32 bitlik bir tam sayıda ayarlanmış bitlerin sayısını sayar.
    Ref - https://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetKernighan
    >>> birlerin_sayisini_al(25)
    3
    >>> birlerin_sayisini_al(37)
    3
    >>> birlerin_sayisini_al(21)
    3
    >>> birlerin_sayisini_al(58)
    4
    >>> birlerin_sayisini_al(0)
    0
    >>> birlerin_sayisini_al(256)
    1
    >>> birlerin_sayisini_al(-1)
    Traceback (most recent call last):
        ...
    ValueError: Girdi negatif olmayan bir tam sayı olmalıdır
    >>> birlerin_sayisini_al(0.8)
    Traceback (most recent call last):
        ...
    ValueError: Girdi negatif olmayan bir tam sayı olmalıdır
    >>> birlerin_sayisini_al("25")
    Traceback (most recent call last):
        ...
    ValueError: Girdi negatif olmayan bir tam sayı olmalıdır
    """
    if not isinstance(sayi, int) or sayi < 0:
        raise ValueError("Girdi negatif olmayan bir tam sayı olmalıdır")

    sayac = 0
    while sayi:
        # Bu yöntemle her bitin üzerinden geçmek yerine bir sonraki ayarlanmış biti (bir sonraki 1) buluruz
        # bu nedenle döngü 32 kez çalışmaz, yalnızca `1` sayısı kadar çalışır
        sayi &= sayi - 1
        sayac += 1
    return sayac


if __name__ == "__main__":
    import doctest

    doctest.testmod()
