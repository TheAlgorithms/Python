"""
Bu, arama alanını 3 parçaya bölen ve hedef değeri dizinin veya listenin özelliğine (genellikle monoton özellik) dayanarak bulan bir böl ve fethet algoritması türüdür.

Zaman Karmaşıklığı  : O(log3 N)
Alan Karmaşıklığı   : O(1)
"""

from __future__ import annotations

# Bu fonksiyon için hassasiyet ayarıdır ve değiştirilebilir.
# Kullanıcıların bu sayıyı 10 veya daha büyük tutmaları önerilir.
hassasiyet = 10


# Arama alanı küçüldükten sonra gerçekleştirilecek doğrusal arama.


def dogrusal_arama(sol: int, sag: int, dizi: list[int], hedef: int) -> int:
    """Listede doğrusal arama yapar. Eleman bulunamazsa -1 döner.

    Parametreler
    ----------
    sol : int
        Sol indeks sınırı.
    sag : int
        Sağ indeks sınırı.
    dizi : List[int]
        Arama yapılacak elemanların listesi.
    hedef : int
        Aranan eleman.

    Dönüş
    -------
    int
        Aranan elemanın indeksi.

    Örnekler
    --------
    >>> dogrusal_arama(0, 4, [4, 5, 6, 7], 7)
    3
    >>> dogrusal_arama(0, 3, [4, 5, 6, 7], 7)
    -1
    >>> dogrusal_arama(0, 2, [-18, 2], -18)
    0
    >>> dogrusal_arama(0, 1, [5], 5)
    0
    >>> dogrusal_arama(0, 3, ['a', 'c', 'd'], 'c')
    1
    >>> dogrusal_arama(0, 3, [.1, .4 , -.1], .1)
    0
    >>> dogrusal_arama(0, 3, [.1, .4 , -.1], -.1)
    2
    """
    for i in range(sol, sag):
        if dizi[i] == hedef:
            return i
    return -1


def iteratif_ternary_arama(dizi: list[int], hedef: int) -> int:
    """Ternary arama algoritmasının iteratif yöntemi.
    >>> test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    >>> iteratif_ternary_arama(test_list, 3)
    -1
    >>> iteratif_ternary_arama(test_list, 13)
    4
    >>> iteratif_ternary_arama([4, 5, 6, 7], 4)
    0
    >>> iteratif_ternary_arama([4, 5, 6, 7], -10)
    -1
    >>> iteratif_ternary_arama([-18, 2], -18)
    0
    >>> iteratif_ternary_arama([5], 5)
    0
    >>> iteratif_ternary_arama(['a', 'c', 'd'], 'c')
    1
    >>> iteratif_ternary_arama(['a', 'c', 'd'], 'f')
    -1
    >>> iteratif_ternary_arama([], 1)
    -1
    >>> iteratif_ternary_arama([.1, .4 , -.1], .1)
    0
    """

    sol = 0
    sag = len(dizi)
    while sol <= sag:
        if sag - sol < hassasiyet:
            return dogrusal_arama(sol, sag, dizi, hedef)

        bir_uc = (sol + sag) // 3 + 1
        iki_uc = 2 * (sol + sag) // 3 + 1

        if dizi[bir_uc] == hedef:
            return bir_uc
        elif dizi[iki_uc] == hedef:
            return iki_uc

        elif hedef < dizi[bir_uc]:
            sag = bir_uc - 1
        elif dizi[iki_uc] < hedef:
            sol = iki_uc + 1

        else:
            sol = bir_uc + 1
            sag = iki_uc - 1
    return -1


def rekursif_ternary_arama(sol: int, sag: int, dizi: list[int], hedef: int) -> int:
    """Ternary arama algoritmasının rekursif yöntemi.

    >>> test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    >>> rekursif_ternary_arama(0, len(test_list), test_list, 3)
    -1
    >>> rekursif_ternary_arama(4, len(test_list), test_list, 42)
    8
    >>> rekursif_ternary_arama(0, 2, [4, 5, 6, 7], 4)
    0
    >>> rekursif_ternary_arama(0, 3, [4, 5, 6, 7], -10)
    -1
    >>> rekursif_ternary_arama(0, 1, [-18, 2], -18)
    0
    >>> rekursif_ternary_arama(0, 1, [5], 5)
    0
    >>> rekursif_ternary_arama(0, 2, ['a', 'c', 'd'], 'c')
    1
    >>> rekursif_ternary_arama(0, 2, ['a', 'c', 'd'], 'f')
    -1
    >>> rekursif_ternary_arama(0, 0, [], 1)
    -1
    >>> rekursif_ternary_arama(0, 3, [.1, .4 , -.1], .1)
    0
    """
    if sol < sag:
        if sag - sol < hassasiyet:
            return dogrusal_arama(sol, sag, dizi, hedef)
        bir_uc = (sol + sag) // 3 + 1
        iki_uc = 2 * (sol + sag) // 3 + 1

        if dizi[bir_uc] == hedef:
            return bir_uc
        elif dizi[iki_uc] == hedef:
            return iki_uc

        elif hedef < dizi[bir_uc]:
            return rekursif_ternary_arama(sol, bir_uc - 1, dizi, hedef)
        elif dizi[iki_uc] < hedef:
            return rekursif_ternary_arama(iki_uc + 1, sag, dizi, hedef)
        else:
            return rekursif_ternary_arama(bir_uc + 1, iki_uc - 1, dizi, hedef)
    else:
        return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    kullanici_girdisi = input("Virgülle ayrılmış sayıları girin:\n").strip()
    koleksiyon = [int(item.strip()) for item in kullanici_girdisi.split(",")]
    assert koleksiyon == sorted(koleksiyon), f"Liste sıralı olmalıdır.\n{koleksiyon}."
    hedef = int(input("Listede bulunacak sayıyı girin:\n").strip())
    sonuc1 = iteratif_ternary_arama(koleksiyon, hedef)
    sonuc2 = rekursif_ternary_arama(0, len(koleksiyon) - 1, koleksiyon, hedef)
    if sonuc2 != -1:
        print(f"İteratif arama: {hedef} pozisyonlarda bulundu: {sonuc1}")
        print(f"Rekürsif arama: {hedef} pozisyonlarda bulundu: {sonuc2}")
    else:
        print("Bulunamadı")
