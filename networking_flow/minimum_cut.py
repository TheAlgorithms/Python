# Ford-Fulkerson algoritmasında minimum kesim.

test_graf = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0],
]

# Organiser: K. Umut Araz

def bfs(graf, kaynak, hedef, ebeveyn):
    # Ziyaret edilmemiş bir düğüm varsa True döner.
    ziyaret_edilen = [False] * len(graf)
    kuyruk = [kaynak]
    ziyaret_edilen[kaynak] = True

    while kuyruk:
        u = kuyruk.pop(0)
        for ind in range(len(graf[u])):
            if not ziyaret_edilen[ind] and graf[u][ind] > 0:
                kuyruk.append(ind)
                ziyaret_edilen[ind] = True
                ebeveyn[ind] = u

    return ziyaret_edilen[hedef]

def min_kesim(graf, kaynak, hedef):
    """Bu dizi BFS ile doldurulur ve yolu saklar.
    >>> min_kesim(test_graf, kaynak=0, hedef=5)
    [(1, 3), (4, 3), (4, 5)]
    """
    ebeveyn = [-1] * len(graf)
    maksimum_akış = 0
    sonuç = []
    geçici = [i[:] for i in graf]  # Orijinal kesimi kaydet, kopyala.
    
    while bfs(graf, kaynak, hedef, ebeveyn):
        yol_akışı = float("Inf")
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

    for i in range(len(graf)):
        for j in range(len(graf[0])):
            if graf[i][j] == 0 and geçici[i][j] > 0:
                sonuç.append((i, j))

    return sonuç

if __name__ == "__main__":
    print(min_kesim(test_graf, kaynak=0, hedef=5))
