# Knapsack problemini çözmek için naif özyinelemeli yönteme bir bakış


"""
Bir bakkalın her biri farklı ağırlıklara ve farklı karlara sahip buğday çuvalları vardır.
ör.
eşya_sayısı 4
kar 5 4 8 6
ağırlık 1 2 4 5
maks_ağırlık 5
Kısıtlamalar:
maks_ağırlık > 0
kar[i] >= 0
ağırlık[i] >= 0
Taşınabilecek maksimum ağırlık verildiğinde bakkalın elde edebileceği maksimum karı hesaplayın.
"""


def knapsack(
    ağırlıklar: list, değerler: list, eşya_sayısı: int, maks_ağırlık: int, indeks: int
) -> int:
    """
    Fonksiyon açıklaması aşağıdaki gibidir-
    :param ağırlıklar: Ağırlıkların bir listesini alın
    :param değerler: Ağırlıklara karşılık gelen karların bir listesini alın
    :param eşya_sayısı: Seçilebilecek eşya sayısı
    :param maks_ağırlık: Taşınabilecek maksimum ağırlık
    :param indeks: baktığımız eleman
    :return: Beklenen maksimum kazanç
    >>> knapsack([1, 2, 4, 5], [5, 4, 8, 6], 4, 5, 0)
    13
    >>> knapsack([3 ,4 , 5], [10, 9 , 8], 3, 25, 0)
    27
    """
    if indeks == eşya_sayısı:
        return 0
    cevap1 = 0
    cevap2 = 0
    cevap1 = knapsack(ağırlıklar, değerler, eşya_sayısı, maks_ağırlık, indeks + 1)
    if ağırlıklar[indeks] <= maks_ağırlık:
        cevap2 = değerler[indeks] + knapsack(
            ağırlıklar, değerler, eşya_sayısı, maks_ağırlık - ağırlıklar[indeks], indeks + 1
        )
    return max(cevap1, cevap2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
