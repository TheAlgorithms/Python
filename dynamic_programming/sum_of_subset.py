def alt_kume_toplami_var_mi(arr: list[int], gereken_toplam: int) -> bool:
    """
    >>> alt_kume_toplami_var_mi([2, 4, 6, 8], 5)
    False
    >>> alt_kume_toplami_var_mi([2, 4, 6, 8], 14)
    True
    """
    # Bir alt küme değeri, o alt küme toplamı oluşturulabiliyorsa 1, aksi takdirde 0 der.
    # Başlangıçta hiçbir alt küme oluşturulamaz, bu nedenle False/0
    arr_uzunluk = len(arr)
    alt_kume = [[False] * (gereken_toplam + 1) for _ in range(arr_uzunluk + 1)]

    # Her arr değeri için, hiçbir eleman alınmadan sıfır(0) toplamı oluşturulabilir
    # bu nedenle True/1
    for i in range(arr_uzunluk + 1):
        alt_kume[i][0] = True

    # Toplam sıfır değilse ve küme boşsa false
    for i in range(1, gereken_toplam + 1):
        alt_kume[0][i] = False

    for i in range(1, arr_uzunluk + 1):
        for j in range(1, gereken_toplam + 1):
            if arr[i - 1] > j:
                alt_kume[i][j] = alt_kume[i - 1][j]
            if arr[i - 1] <= j:
                alt_kume[i][j] = alt_kume[i - 1][j] or alt_kume[i - 1][j - arr[i - 1]]

    return alt_kume[arr_uzunluk][gereken_toplam]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
