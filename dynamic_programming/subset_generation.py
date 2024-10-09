def alt_kume_kombinasyonlari(elemanlar: list[int], n: int) -> list:
    """
    Verilen bir listeden n elemanlı kombinasyonları dinamik programlama kullanarak hesaplar.
    Args:
        elemanlar: Kombinasyonların oluşturulacağı elemanların listesi.
        n: Her kombinasyondaki eleman sayısı.
    Returns:
        Her biri n elemanlı bir kombinasyonu temsil eden bir demet listesi.
        >>> alt_kume_kombinasyonlari(elemanlar=[10, 20, 30, 40], n=2)
        [(10, 20), (10, 30), (10, 40), (20, 30), (20, 40), (30, 40)]
        >>> alt_kume_kombinasyonlari(elemanlar=[1, 2, 3], n=1)
        [(1,), (2,), (3,)]
        >>> alt_kume_kombinasyonlari(elemanlar=[1, 2, 3], n=3)
        [(1, 2, 3)]
        >>> alt_kume_kombinasyonlari(elemanlar=[42], n=1)
        [(42,)]
        >>> alt_kume_kombinasyonlari(elemanlar=[6, 7, 8, 9], n=4)
        [(6, 7, 8, 9)]
        >>> alt_kume_kombinasyonlari(elemanlar=[10, 20, 30, 40, 50], n=0)
        [()]
        >>> alt_kume_kombinasyonlari(elemanlar=[1, 2, 3, 4], n=2)
        [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
        >>> alt_kume_kombinasyonlari(elemanlar=[1, 'elma', 3.14], n=2)
        [(1, 'elma'), (1, 3.14), ('elma', 3.14)]
        >>> alt_kume_kombinasyonlari(elemanlar=['tek'], n=0)
        [()]
        >>> alt_kume_kombinasyonlari(elemanlar=[], n=9)
        []
        >>> from itertools import combinations
        >>> all(alt_kume_kombinasyonlari(items, n) == list(combinations(items, n))
        ...     for items, n in (
        ...         ([10, 20, 30, 40], 2), ([1, 2, 3], 1), ([1, 2, 3], 3), ([42], 1),
        ...         ([6, 7, 8, 9], 4), ([10, 20, 30, 40, 50], 1), ([1, 2, 3, 4], 2),
        ...         ([1, 'elma', 3.14], 2), (['tek'], 0), ([], 9)))
        True
    """
    r = len(elemanlar)
    if n > r:
        return []

    dp: list[list[tuple]] = [[] for _ in range(r + 1)]

    dp[0].append(())

    for i in range(1, r + 1):
        for j in range(i, 0, -1):
            for onceki_kombinasyon in dp[j - 1]:
                dp[j].append((*onceki_kombinasyon, elemanlar[i - 1]))

    try:
        return sorted(dp[n])
    except TypeError:
        return dp[n]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{alt_kume_kombinasyonlari(elemanlar=[10, 20, 30, 40], n=2) = }")
