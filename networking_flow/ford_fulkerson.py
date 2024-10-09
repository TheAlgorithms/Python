"""
Ford-Fulkerson Algoritması Maksimum Akış Problemi için
* https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm

Açıklama:
    (1) Başlangıç akışını 0 olarak ayarlayın.
    (2) Kaynaktan hedefe giden artırıcı yolu seçin ve bu yolu akışa ekleyin.

    Yazar: K. Umut Araz
"""

graf = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0],
]


def genis_ilk_arama(graf: list, kaynak: int, hedef: int, ebeveynler: list) -> bool:
    """
    Bu fonksiyon, henüz ziyaret edilmemiş bir düğüm varsa True döner.

    Argümanlar:
        graf: Grafın komşuluk matrisini temsil eder.
        kaynak: Başlangıç düğümü.
        hedef: Hedef düğümü.
        ebeveynler: Düğümlerin ebeveynlerini saklayan liste.

    Dönüş:
        Eğer henüz ziyaret edilmemiş bir düğüm varsa True döner.

    >>> genis_ilk_arama(graf, 0, 5, [-1, -1, -1, -1, -1, -1])
    True
    >>> genis_ilk_arama(graf, 0, 6, [-1, -1, -1, -1, -1, -1])
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    """
    ziyaret_edilen = [False] * len(graf)  # Tüm düğümleri ziyaret edilmemiş olarak işaretle
    kuyruk = []  # Genişlik öncelikli arama kuyruğu

    # Kaynak düğüm kuyruğa eklenir
    kuyruk.append(kaynak)
    ziyaret_edilen[kaynak] = True

    while kuyruk:
        u = kuyruk.pop(0)  # Ön düğümü çıkar
        # u'nun tüm komşu düğümlerini gez
        for ind, node in enumerate(graf[u]):
            if not ziyaret_edilen[ind] and node > 0:
                kuyruk.append(ind)
                ziyaret_edilen[ind] = True
                ebeveynler[ind] = u
    return ziyaret_edilen[hedef]


def ford_fulkerson(graf: list, kaynak: int, hedef: int) -> int:
    """
    Bu fonksiyon, verilen grafikte kaynak ile hedef arasındaki maksimum akışı döner.

    DİKKAT: Bu fonksiyon verilen grafi değiştirir.

    Organiser: K. Umut Araz

    Argümanlar:
        graf: Grafın komşuluk matrisini temsil eder.
        kaynak: Başlangıç düğümü.
        hedef: Hedef düğümü.

    Dönüş:
        Maksimum akış miktarını döner.

    >>> test_graf = [
    ...     [0, 16, 13, 0, 0, 0],
    ...     [0, 0, 10, 12, 0, 0],
    ...     [0, 4, 0, 0, 14, 0],
    ...     [0, 0, 9, 0, 0, 20],
    ...     [0, 0, 0, 7, 0, 4],
    ...     [0, 0, 0, 0, 0, 0],
    ... ]
    >>> ford_fulkerson(test_graf, 0, 5)
    23
    """
    # Ebeveyn dizisi genişlik öncelikli arama ile doldurulur ve yolu saklar
    ebeveyn = [-1] * len(graf)
    maksimum_akış = 0

    # Kaynaktan hedefe bir yol olduğu sürece
    while genis_ilk_arama(graf, kaynak, hedef, ebeveyn):
        yol_akışı = float('inf')  # Sonsuz değer
        s = hedef

        while s != kaynak:
            # Seçilen yoldaki minimum değeri bul
            yol_akışı = min(yol_akışı, graf[ebeveyn[s]][s])
            s = ebeveyn[s]

        maksimum_akış += yol_akışı
        v = hedef

        while v != kaynak:
            u = ebeveyn[v]
            graf[u][v] -= yol_akışı
            graf[v][u] += yol_akışı
            v = ebeveyn[v]

    return maksimum_akış


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{ford_fulkerson(graf, kaynak=0, hedef=5) = }")
