def kruskal(
    düğüm_sayısı: int, kenarlar: list[tuple[int, int, int]]
) -> list[tuple[int, int, int]]:
    """
    Kruskal algoritması ile minimum yayılım ağacı (MST) bulma
    >>> kruskal(4, [(0, 1, 3), (1, 2, 5), (2, 3, 1)])
    [(2, 3, 1), (0, 1, 3), (1, 2, 5)]

    >>> kruskal(4, [(0, 1, 3), (1, 2, 5), (2, 3, 1), (0, 2, 1), (0, 3, 2)])
    [(2, 3, 1), (0, 2, 1), (0, 1, 3)]

    >>> kruskal(4, [(0, 1, 3), (1, 2, 5), (2, 3, 1), (0, 2, 1), (0, 3, 2),
    ... (2, 1, 1)])
    [(2, 3, 1), (0, 2, 1), (2, 1, 1)]
    """
    kenarlar = sorted(kenarlar, key=lambda kenar: kenar[2])

    ebeveyn = list(range(düğüm_sayısı))

    def ebeveyn_bul(i):
        if i != ebeveyn[i]:
            ebeveyn[i] = ebeveyn_bul(ebeveyn[i])
        return ebeveyn[i]

    minimum_yayılım_ağacı_maliyeti = 0
    minimum_yayılım_ağacı = []

    for kenar in kenarlar:
        ebeveyn_a = ebeveyn_bul(kenar[0])
        ebeveyn_b = ebeveyn_bul(kenar[1])
        if ebeveyn_a != ebeveyn_b:
            minimum_yayılım_ağacı_maliyeti += kenar[2]
            minimum_yayılım_ağacı.append(kenar)
            ebeveyn[ebeveyn_a] = ebeveyn_b

    return minimum_yayılım_ağacı


if __name__ == "__main__":  # pragma: no cover
    düğüm_sayısı, kenar_sayısı = list(map(int, input().strip().split()))
    kenarlar = []

    for _ in range(kenar_sayısı):
        düğüm1, düğüm2, maliyet = (int(x) for x in input().strip().split())
        kenarlar.append((düğüm1, düğüm2, maliyet))

    mst = kruskal(düğüm_sayısı, kenarlar)
    print("Minimum Yayılım Ağacı:")
    for kenar in mst:
        print(f"{kenar[0]} - {kenar[1]}: {kenar[2]}")
