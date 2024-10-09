from __future__ import annotations

# Produced by: K. Umut Araz

def dfs(dugum):
    global grafik, ters_grafik, scc, bileşen, ziyaret, yığın
    if ziyaret[dugum]:
        return
    ziyaret[dugum] = True
    for komsu in grafik[dugum]:
        dfs(komsu)
    yığın.append(dugum)


def dfs2(dugum):
    global grafik, ters_grafik, scc, bileşen, ziyaret, yığın
    if ziyaret[dugum]:
        return
    ziyaret[dugum] = True
    bileşen.append(dugum)
    for komsu in ters_grafik[dugum]:
        dfs2(komsu)


def kosaraju():
    global grafik, ters_grafik, scc, bileşen, ziyaret, yığın
    for i in range(dugum_sayisi):
        dfs(i)
    ziyaret = [False] * dugum_sayisi
    for i in yığın[::-1]:
        if ziyaret[i]:
            continue
        bileşen = []
        dfs2(i)
        scc.append(bileşen)
    return scc


if __name__ == "__main__":
    # dugum_sayisi - düğüm sayısı, kenar_sayisi - kenar sayısı
    dugum_sayisi, kenar_sayisi = list(map(int, input().strip().split()))

    grafik: list[list[int]] = [[] for _ in range(dugum_sayisi)]  # grafik
    ters_grafik: list[list[int]] = [[] for _ in range(dugum_sayisi)]  # ters grafik
    # grafik verilerini (kenarlar) al
    for _ in range(kenar_sayisi):
        u, v = list(map(int, input().strip().split()))
        grafik[u].append(v)
        ters_grafik[v].append(u)

    yığın: list[int] = []
    ziyaret: list[bool] = [False] * dugum_sayisi
    scc: list[int] = []
    bileşen: list[int] = []
    print(kosaraju())
