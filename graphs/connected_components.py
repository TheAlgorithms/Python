"""
https://en.wikipedia.org/wiki/Component_(graph_theory)

Grafikte bağlı bileşenleri bulma

"""

test_graf_1 = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1], 4: [5, 6], 5: [4, 6], 6: [4, 5]}

test_graf_2 = {0: [1, 2, 3], 1: [0, 3], 2: [0], 3: [0, 1], 4: [], 5: []}


def dfs(graf: dict, dugum: int, ziyaret_edildi: list) -> list:
    """
    Derinlik öncelikli arama kullanarak başlangıç düğümü ile aynı bileşende olan tüm düğümleri bul
    >>> dfs(test_graf_1, 0, 5 * [False])
    [0, 1, 3, 2]
    >>> dfs(test_graf_2, 0, 6 * [False])
    [0, 1, 3, 2]
    """

    ziyaret_edildi[dugum] = True
    bagli_dugumler = []

    for komsu in graf[dugum]:
        if not ziyaret_edildi[komsu]:
            bagli_dugumler += dfs(graf, komsu, ziyaret_edildi)

    return [dugum, *bagli_dugumler]


def bagli_bilesenler(graf: dict) -> list:
    """
    Bu fonksiyon grafı parametre olarak alır ve bağlı bileşenlerin listesini döner
    >>> bagli_bilesenler(test_graf_1)
    [[0, 1, 3, 2], [4, 5, 6]]
    >>> bagli_bilesenler(test_graf_2)
    [[0, 1, 3, 2], [4], [5]]
    """

    graf_boyutu = len(graf)
    ziyaret_edildi = graf_boyutu * [False]
    bilesenler_listesi = []

    for i in range(graf_boyutu):
        if not ziyaret_edildi[i]:
            i_bagli = dfs(graf, i, ziyaret_edildi)
            bilesenler_listesi.append(i_bagli)

    return bilesenler_listesi


if __name__ == "__main__":
    import doctest

    doctest.testmod()
