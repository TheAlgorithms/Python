"""
Medyanların Medyanı algoritmasının Python uygulaması,
hızlı seçim (quick_select) için pivotları seçmek amacıyla
kullanılır. Bu algoritma, sıralı olmasa bile bir listenin
sıralandığında hangi indekste hangi değerin olacağını
hesaplamak için etkilidir. Herhangi bir sıralamada O(n)
zaman karmaşıklığı ile arama yapar.

Organiser: K. Umut Araz
https://en.wikipedia.org/wiki/Median_of_medians
"""


def beşin_medyanı(dizi: list) -> int:
    """
    Giriş listesinin medyanını döner.
    :param dizi: Medyanı bulunacak dizi
    :return: dizi'nin medyanı

    >>> beşin_medyanı([2, 4, 5, 7, 899])
    5
    >>> beşin_medyanı([5, 7, 899, 54, 32])
    32
    >>> beşin_medyanı([5, 4, 3, 2])
    4
    >>> beşin_medyanı([3, 5, 7, 10, 2])
    5
    """
    dizi = sorted(dizi)
    return dizi[len(dizi) // 2]


def medyanların_medyanı(dizi: list) -> int:
    """
    Giriş verilerinin medyanlarını hesaplayarak
    verileri bölmek için bir pivot döner.
    :param dizi: Kontrol edilecek veri (bir liste)
    :return: giriş dizisinin medyanı

    >>> medyanların_medyanı([2, 4, 5, 7, 899, 54, 32])
    54
    >>> medyanların_medyanı([5, 7, 899, 54, 32])
    32
    >>> medyanların_medyanı([5, 4, 3, 2])
    4
    >>> medyanların_medyanı([3, 5, 7, 10, 2, 12])
    12
    """

    if len(dizi) <= 5:
        return beşin_medyanı(dizi)
    medyanlar = []
    i = 0
    while i < len(dizi):
        if (i + 4) <= len(dizi):
            medyanlar.append(beşin_medyanı(dizi[i:].copy()))
        else:
            medyanlar.append(beşin_medyanı(dizi[i: i + 5].copy()))
        i += 5
    return medyanların_medyanı(medyanlar)


def hızlı_seçim(dizi: list, hedef: int) -> int:
    """
    Verileri pivot ile ilişkili olarak daha küçük ve daha büyük
    listelere iki yönlü olarak böler.
    :param dizi: Aranacak veri (bir liste)
    :param hedef: Aranacak sıralama
    :return: hedef sıralamadaki eleman

    >>> hızlı_seçim([2, 4, 5, 7, 899, 54, 32], 5)
    32
    >>> hızlı_seçim([2, 4, 5, 7, 899, 54, 32], 1)
    2
    >>> hızlı_seçim([5, 4, 3, 2], 2)
    3
    >>> hızlı_seçim([3, 5, 7, 10, 2, 12], 3)
    5
    """

    # Geçersiz Girdi
    if hedef > len(dizi):
        return -1

    # x, medyanların medyanı algoritması ile tahmin edilen pivot
    x = medyanların_medyanı(dizi)
    sol = []
    sağ = []
    kontrol = False
    for i in range(len(dizi)):
        if dizi[i] < x:
            sol.append(dizi[i])
        elif dizi[i] > x:
            sağ.append(dizi[i])
        elif dizi[i] == x and not kontrol:
            kontrol = True
        else:
            sağ.append(dizi[i])
    sıralama_x = len(sol) + 1
    if sıralama_x == hedef:
        cevap = x
    elif sıralama_x > hedef:
        cevap = hızlı_seçim(sol, hedef)
    elif sıralama_x < hedef:
        cevap = hızlı_seçim(sağ, hedef - sıralama_x)
    return cevap


print(beşin_medyanı([5, 4, 3, 2]))
