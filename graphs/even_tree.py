"""
Size bir ağaç (döngüsü olmayan basit bağlı grafik) verildi. Ağaç N düğümüne sahiptir ve 1'den N'ye kadar numaralandırılmıştır ve kökü düğüm 1'dir.

Her bir bağlı bileşenin çift sayıda düğüm içereceği bir orman elde etmek için ağaçtan çıkarabileceğiniz maksimum kenar sayısını bulun.

Kısıtlamalar
2 <= N <= 100

Not: Ağaç girişi her zaman çift sayıda düğüm içeren bileşenlere ayrılabilecek şekilde olacaktır.
"""

# pylint: disable=invalid-name
from collections import defaultdict


def dfs(baslangic: int) -> int:
    """DFS geçişi"""
    # pylint: disable=redefined-outer-name
    ret = 1
    ziyaret_edilen[baslangic] = True
    for v in agac[baslangic]:
        if v not in ziyaret_edilen:
            ret += dfs(v)
    if ret % 2 == 0:
        kesikler.append(baslangic)
    return ret


def cift_agac():
    """
    2 1
    3 1
    4 3
    5 2
    6 1
    7 2
    8 6
    9 8
    10 8
    Kenarları (1,3) ve (1,6) çıkardığımızda, istenen sonuç olan 2'yi elde edebiliriz.
    """
    dfs(1)


if __name__ == "__main__":
    n, m = 10, 9
    agac = defaultdict(list)
    ziyaret_edilen: dict[int, bool] = {}
    kesikler: list[int] = []
    kenarlar = [(2, 1), (3, 1), (4, 3), (5, 2), (6, 1), (7, 2), (8, 6), (9, 8), (10, 8)]
    for u, v in kenarlar:
        agac[u].append(v)
        agac[v].append(u)
    cift_agac()
    print(len(kesikler) - 1)
