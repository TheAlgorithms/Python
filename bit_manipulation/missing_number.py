def eksik_sayi_bul(nums: list[int]) -> int:
    """
    Ardışık tamsayılar listesindeki eksik sayıyı bulur.

    Args:
        nums: Bir tamsayı listesi.

    Returns:
        Eksik sayı.

    Örnek:
        >>> eksik_sayi_bul([0, 1, 3, 4])
        2
        >>> eksik_sayi_bul([4, 3, 1, 0])
        2
        >>> eksik_sayi_bul([-4, -3, -1, 0])
        -2
        >>> eksik_sayi_bul([-2, 2, 1, 3, 0])
        -1
        >>> eksik_sayi_bul([1, 3, 4, 5, 6])
        2
        >>> eksik_sayi_bul([6, 5, 4, 2, 1])
        3
        >>> eksik_sayi_bul([6, 1, 5, 3, 4])
        2
    """
    düşük = min(nums)
    yüksek = max(nums)
    eksik_sayi = yüksek

    for i in range(düşük, yüksek):
        eksik_sayi ^= i ^ nums[i - düşük]

    return eksik_sayi


if __name__ == "__main__":
    import doctest

    doctest.testmod()
