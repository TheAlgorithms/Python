"""
Bir kenar, onu kaldırdıktan sonra grafikteki bağlı bileşenlerin sayısı bir artarsa köprüdür.
Köprüler, bağlı bir ağdaki zayıf noktaları temsil eder ve güvenilir ağlar tasarlamak için kullanışlıdır.
Örneğin, kablolu bir bilgisayar ağında, bir eklem noktası kritik bilgisayarları ve bir köprü kritik kabloları veya bağlantıları gösterir.

Daha fazla ayrıntı için bu makaleye bakın:
https://www.geeksforgeeks.org/bridge-in-a-graph/
"""


def __ornek_grafik(index):
    return [
        {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1, 3, 5],
            3: [2, 4],
            4: [3],
            5: [2, 6, 8],
            6: [5, 7],
            7: [6, 8],
            8: [5, 7],
        },
        {
            0: [6],
            1: [9],
            2: [4, 5],
            3: [4],
            4: [2, 3],
            5: [2],
            6: [0, 7],
            7: [6],
            8: [],
            9: [1],
        },
        {
            0: [4],
            1: [6],
            2: [],
            3: [5, 6, 7],
            4: [0, 6],
            5: [3, 8, 9],
            6: [1, 3, 4, 7],
            7: [3, 6, 8, 9],
            8: [5, 7],
            9: [5, 7],
        },
        {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 3, 4],
            3: [0, 2, 4],
            4: [1, 2, 3],
        },
    ][index]


def kopruleri_hesapla(grafik: dict[int, list[int]]) -> list[tuple[int, int]]:
    """
    Yönsüz grafikteki köprülerin listesini döndür [(a1, b1), ..., (ak, bk)]; ai <= bi
    >>> kopruleri_hesapla(__ornek_grafik(0))
    [(3, 4), (2, 3), (2, 5)]
    >>> kopruleri_hesapla(__ornek_grafik(1))
    [(6, 7), (0, 6), (1, 9), (3, 4), (2, 4), (2, 5)]
    >>> kopruleri_hesapla(__ornek_grafik(2))
    [(1, 6), (4, 6), (0, 4)]
    >>> kopruleri_hesapla(__ornek_grafik(3))
    []
    >>> kopruleri_hesapla({})
    []
    """

    id_ = 0
    n = len(grafik)  # Grafikteki düğüm sayısı
    dusuk = [0] * n
    ziyaret_edilen = [False] * n

    def dfs(at, ebeveyn, kopruler, id_):
        ziyaret_edilen[at] = True
        dusuk[at] = id_
        id_ += 1
        for hedef in grafik[at]:
            if hedef == ebeveyn:
                pass
            elif not ziyaret_edilen[hedef]:
                dfs(hedef, at, kopruler, id_)
                dusuk[at] = min(dusuk[at], dusuk[hedef])
                if id_ <= dusuk[hedef]:
                    kopruler.append((at, hedef) if at < hedef else (hedef, at))
            else:
                # Bu kenar bir geri kenardır ve köprü olamaz
                dusuk[at] = min(dusuk[at], dusuk[hedef])

    kopruler: list[tuple[int, int]] = []
    for i in range(n):
        if not ziyaret_edilen[i]:
            dfs(i, -1, kopruler, id_)
    return kopruler


if __name__ == "__main__":
    import doctest

    doctest.testmod()
