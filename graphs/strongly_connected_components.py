"""
https://tr.wikipedia.org/wiki/Güçlü_bağlantılı_bileşen

Yönlendirilmiş grafikte güçlü bağlantılı bileşenleri bulma

Produced By K. Umut Araz

"""

test_graf_1 = {0: [2, 3], 1: [0], 2: [1], 3: [4], 4: []}

test_graf_2 = {0: [1, 2, 3], 1: [2], 2: [0], 3: [4], 4: [5], 5: [3]}


def topolojik_sıralama(
    graf: dict[int, list[int]], düğüm: int, ziyaret_edildi: list[bool]
) -> list[int]:
    """
    Derinlemesine arama kullanarak grafiği sırala
    Bu aşamada graf giriş ile aynıdır
    >>> topolojik_sıralama(test_graf_1, 0, 5 * [False])
    [1, 2, 4, 3, 0]
    >>> topolojik_sıralama(test_graf_2, 0, 6 * [False])
    [2, 1, 5, 4, 3, 0]
    """

    ziyaret_edildi[düğüm] = True
    sıra = []

    for komşu in graf[düğüm]:
        if not ziyaret_edildi[komşu]:
            sıra += topolojik_sıralama(graf, komşu, ziyaret_edildi)

    sıra.append(düğüm)

    return sıra


def bileşenleri_bul(
    ters_graf: dict[int, list[int]], düğüm: int, ziyaret_edildi: list[bool]
) -> list[int]:
    """
    Derinlemesine arama kullanarak güçlü bağlantılı
    düğümleri bul. Şimdi graf ters çevrilmiştir
    >>> bileşenleri_bul({0: [1], 1: [2], 2: [0]}, 0, 5 * [False])
    [0, 1, 2]
    >>> bileşenleri_bul({0: [2], 1: [0], 2: [0, 1]}, 0, 6 * [False])
    [0, 2, 1]
    """

    ziyaret_edildi[düğüm] = True
    bileşen = [düğüm]

    for komşu in ters_graf[düğüm]:
        if not ziyaret_edildi[komşu]:
            bileşen += bileşenleri_bul(ters_graf, komşu, ziyaret_edildi)

    return bileşen


def güçlü_bağlantılı_bileşenler(graf: dict[int, list[int]]) -> list[list[int]]:
    """
    Bu fonksiyon grafı parametre olarak alır
    ve ardından güçlü bağlantılı bileşenlerin listesini döndürür
    >>> güçlü_bağlantılı_bileşenler(test_graf_1)
    [[0, 1, 2], [3], [4]]
    >>> güçlü_bağlantılı_bileşenler(test_graf_2)
    [[0, 2, 1], [3, 5, 4]]
    """

    ziyaret_edildi = len(graf) * [False]
    ters_graf: dict[int, list[int]] = {düğüm: [] for düğüm in range(len(graf))}

    for düğüm, komşular in graf.items():
        for komşu in komşular:
            ters_graf[komşu].append(düğüm)

    sıra = []
    for i, ziyaret in enumerate(ziyaret_edildi):
        if not ziyaret:
            sıra += topolojik_sıralama(graf, i, ziyaret_edildi)

    bileşenler_listesi = []
    ziyaret_edildi = len(graf) * [False]

    for i in range(len(graf)):
        düğüm = sıra[len(graf) - i - 1]
        if not ziyaret_edildi[düğüm]:
            bileşen = bileşenleri_bul(ters_graf, düğüm, ziyaret_edildi)
            bileşenler_listesi.append(bileşen)

    return bileşenler_listesi
