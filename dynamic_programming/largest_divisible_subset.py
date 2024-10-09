from __future__ import annotations


def en_buyuk_bolen_alt_kume(elemanlar: list[int]) -> list[int]:
    """
    Verilen dizideki en büyük alt kümeyi bulma algoritması, öyle ki alt kümedeki herhangi iki eleman
    x ve y için, ya x y'yi böler ya da y x'i böler.
    >>> en_buyuk_bolen_alt_kume([1, 16, 7, 8, 4])
    [16, 8, 4, 1]
    >>> en_buyuk_bolen_alt_kume([1, 2, 3])
    [2, 1]
    >>> en_buyuk_bolen_alt_kume([-1, -2, -3])
    [-3]
    >>> en_buyuk_bolen_alt_kume([1, 2, 4, 8])
    [8, 4, 2, 1]
    >>> en_buyuk_bolen_alt_kume((1, 2, 4, 8))
    [8, 4, 2, 1]
    >>> en_buyuk_bolen_alt_kume([1, 1, 1])
    [1, 1, 1]
    >>> en_buyuk_bolen_alt_kume([0, 0, 0])
    [0, 0, 0]
    >>> en_buyuk_bolen_alt_kume([-1, -1, -1])
    [-1, -1, -1]
    >>> en_buyuk_bolen_alt_kume([])
    []
    """
    # Diziyi artan sırayla sıralayın çünkü dizinin sırası önemli değil, sadece bir alt küme seçmemiz gerekiyor.
    elemanlar = sorted(elemanlar)

    eleman_sayisi = len(elemanlar)

    # Memo'yu 1'lerle ve hash'i artan sayılarla başlatın
    memo = [1] * eleman_sayisi
    hash_dizisi = list(range(eleman_sayisi))

    # Dizi boyunca yineleyin
    for i, eleman in enumerate(elemanlar):
        for onceki_indeks in range(i):
            if ((elemanlar[onceki_indeks] != 0 and eleman % elemanlar[onceki_indeks]) == 0) and (
                (1 + memo[onceki_indeks]) > memo[i]
            ):
                memo[i] = 1 + memo[onceki_indeks]
                hash_dizisi[i] = onceki_indeks

    cevap = -1
    son_indeks = -1

    # Maksimum uzunluğu ve karşılık gelen indeksini bulun
    for i, memo_eleman in enumerate(memo):
        if memo_eleman > cevap:
            cevap = memo_eleman
            son_indeks = i

    # Bölünebilir alt kümeyi yeniden oluşturun
    if son_indeks == -1:
        return []
    sonuc = [elemanlar[son_indeks]]
    while hash_dizisi[son_indeks] != son_indeks:
        son_indeks = hash_dizisi[son_indeks]
        sonuc.append(elemanlar[son_indeks])

    return sonuc


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    elemanlar = [1, 16, 7, 8, 4]
    print(
        f"{elemanlar} dizisinin en uzun bölünebilir alt kümesi {en_buyuk_bolen_alt_kume(elemanlar)}."
    )
