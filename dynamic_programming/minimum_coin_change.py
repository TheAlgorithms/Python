"""
Elinizde sonsuz miktarda mevcut olan m tür madeni para var
her bir madeni paranın değeri S=[S0,... Sm-1] dizisinde verilmiştir
Verilen madeni para türlerini kullanarak n birimlik değişim yapmanın
kaç yolu olduğunu belirleyebilir misiniz?
https://www.hackerrank.com/challenges/coin-change/problem
"""


def dp_count(s, n):
    """
    >>> dp_count([1, 2, 3], 4)
    4
    >>> dp_count([1, 2, 3], 7)
    8
    >>> dp_count([2, 5, 3, 6], 10)
    5
    >>> dp_count([10], 99)
    0
    >>> dp_count([4, 5, 6], 0)
    1
    >>> dp_count([1, 2, 3], -5)
    0
    """
    if n < 0:
        return 0
    # table[i] miktarına ulaşmanın yollarının sayısını temsil eder
    tablo = [0] * (n + 1)

    # Sıfıra ulaşmanın tam olarak 1 yolu vardır (Hiç madeni para seçmezsiniz).
    tablo[0] = 1

    # Tüm madeni paraları tek tek seçin ve tablo[] değerlerini güncelleyin
    # seçilen madeni paranın değerine eşit veya daha büyük olan indekslerden sonra
    for coin_val in s:
        for j in range(coin_val, n + 1):
            tablo[j] += tablo[j - coin_val]

    return tablo[n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
