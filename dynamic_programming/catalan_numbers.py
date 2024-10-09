"""
0'dan n'ye kadar olan tüm Catalan sayılarını yazdırın, n kullanıcı girdisidir.

 * Catalan sayıları, kombinatorikte birçok sayma probleminde ortaya çıkan
 * pozitif tam sayıların bir dizisidir [1]. Bu tür problemler şunları içerir [2]:
 * - 2n uzunluğundaki Dyck kelimelerinin sayısı
 * - n çift parantez ile iyi biçimlendirilmiş ifadelerin sayısı
 *   (örneğin, `()()` geçerlidir ancak `())(` geçerli değildir)
 * - n + 1 faktörün tamamen parantezlenebileceği farklı yolların sayısı
 *   (örneğin, n = 2 için, C(n) = 2 ve (ab)c ve a(bc) parantezlemenin iki geçerli yoludur.
 * - n + 1 yapraklı tam ikili ağaçların sayısı

 * Bir Catalan sayısı, bu algoritmada kullanacağımız aşağıdaki yinelemeli ilişkiyi sağlar [1].
 * C(0) = C(1) = 1
 * C(n) = sum(C(i).C(n-i-1)), i = 0'dan n-1'e kadar

 * Ayrıca, n'inci Catalan sayısı aşağıdaki kapalı formül kullanılarak hesaplanabilir [1]:
 * C(n) = (1 / (n + 1)) * (2n choose n)

 * Kaynaklar:
 *  [1] https://brilliant.org/wiki/catalan-numbers/
 *  [2] https://en.wikipedia.org/wiki/Catalan_number
"""


def catalan_sayilari(ust_sinir: int) -> "list[int]":
    """
    0'dan `ust_sinir`a kadar olan Catalan sayı dizisini içeren bir liste döndürür.

    >>> catalan_sayilari(5)
    [1, 1, 2, 5, 14, 42]
    >>> catalan_sayilari(2)
    [1, 1, 2]
    >>> catalan_sayilari(-1)
    Traceback (most recent call last):
    ValueError: Catalan dizisi için sınır ≥ 0 olmalıdır
    """
    if ust_sinir < 0:
        raise ValueError("Catalan dizisi için sınır ≥ 0 olmalıdır")

    catalan_listesi = [0] * (ust_sinir + 1)

    # Temel durum: C(0) = C(1) = 1
    catalan_listesi[0] = 1
    if ust_sinir > 0:
        catalan_listesi[1] = 1

    # Yinelemeli ilişki: C(i) = sum(C(j).C(i-j-1)), j = 0'dan i'ye kadar
    for i in range(2, ust_sinir + 1):
        for j in range(i):
            catalan_listesi[i] += catalan_listesi[j] * catalan_listesi[i - j - 1]

    return catalan_listesi


if __name__ == "__main__":
    print("\n********* Dinamik Programlama Kullanarak Catalan Sayıları ************\n")
    print("\n*** Çıkmak için herhangi bir zamanda -1 girin ***")
    print("\nCatalan sayı dizisi için üst sınırı girin (≥ 0): ", end="")
    try:
        while True:
            N = int(input().strip())
            if N < 0:
                print("\n********* Hoşçakalın!! ************")
                break
            else:
                print(f"0'dan {N}'ye kadar olan Catalan sayıları:")
                print(catalan_sayilari(N))
                print("Dizi için başka bir üst sınır deneyin: ", end="")
    except (NameError, ValueError):
        print("\n********* Geçersiz giriş, hoşçakalın! ************\n")

    import doctest

    doctest.testmod()
