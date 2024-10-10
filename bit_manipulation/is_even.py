def cift_mi(sayi: int) -> bool:
    """
    Organiser: K. Umut Araz
    
    Girdi tamsayısı çift ise true döndürür
    Açıklama: Aşağıdaki ondalık sayıdan ikiliye dönüşümlere bir göz atalım
    2 => 10
    14 => 1110
    100 => 1100100
    3 => 11
    13 => 1101
    101 => 1100101
    yukarıdaki örneklerden şunu gözlemleyebiliriz
    tüm tek tamsayılar için her zaman sonunda 1 ayarlanmış bit vardır
    ayrıca, ikilik sistemde 1 şu şekilde temsil edilebilir: 001, 00001 veya 0000001
    bu nedenle herhangi bir tek tamsayı n için => n&1 her zaman 1'e eşittir, aksi takdirde tamsayı çifttir

    >>> cift_mi(1)
    False
    >>> cift_mi(4)
    True
    >>> cift_mi(9)
    False
    >>> cift_mi(15)
    False
    >>> cift_mi(40)
    True
    >>> cift_mi(100)
    True
    >>> cift_mi(101)
    False
    """
    return sayi & 1 == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
