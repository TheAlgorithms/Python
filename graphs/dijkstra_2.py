def mesafeleri_yazdir(mesafeler, v):
    print("\nDüğüm Mesafesi")
    for i in range(v):
        if mesafeler[i] != float("inf"):
            print(i, "\t", int(mesafeler[i]), end="\t")
        else:
            print(i, "\t", "SONSUZ", end="\t")
        print()


def min_mesafe(mesafeler, ziyaret_edilen, v):
    min_deger = float("inf")
    min_indis = -1
    for i in range(v):
        if (not ziyaret_edilen[i]) and mesafeler[i] < min_deger:
            min_indis = i
            min_deger = mesafeler[i]
    return min_indis


def dijkstra(graf, v, kaynak):
    mesafeler = [float("inf") for _ in range(v)]
    ziyaret_edilen = [False for _ in range(v)]
    mesafeler[kaynak] = 0.0

    for _ in range(v - 1):
        u = min_mesafe(mesafeler, ziyaret_edilen, v)
        ziyaret_edilen[u] = True

        for i in range(v):
            if (
                (not ziyaret_edilen[i])
                and graf[u][i] != float("inf")
                and mesafeler[u] + graf[u][i] < mesafeler[i]
            ):
                mesafeler[i] = mesafeler[u] + graf[u][i]

    mesafeleri_yazdir(mesafeler, v)


if __name__ == "__main__":
    V = int(input("Düğüm sayısını girin: ").strip())
    E = int(input("Kenar sayısını girin: ").strip())

    graf = [[float("inf") for i in range(V)] for j in range(V)]

    for i in range(V):
        graf[i][i] = 0.0

    for i in range(E):
        print("\nKenar ", i + 1)
        kaynak = int(input("Kaynak düğümü girin:").strip())
        hedef = int(input("Hedef düğümü girin:").strip())
        agirlik = float(input("Ağırlığı girin:").strip())
        graf[kaynak][hedef] = agirlik

    kaynak_düğüm = int(input("\nEn kısa yolun kaynağını girin:").strip())
    dijkstra(graf, V, kaynak_düğüm)
