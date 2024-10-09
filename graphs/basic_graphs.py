from collections import deque


def _input(mesaj):
    return input(mesaj).strip().split(" ")

# Produced by K. Umut Araz


def ağırlıksız_yönlü_grafiği_başlat(düğüm_sayısı: int, kenar_sayısı: int) -> dict[int, list[int]]:
    grafik: dict[int, list[int]] = {}
    for i in range(düğüm_sayısı):
        grafik[i + 1] = []

    for e in range(kenar_sayısı):
        x, y = (int(i) for i in _input(f"Kenar {e + 1}: <düğüm1> <düğüm2> "))
        grafik[x].append(y)
    return grafik


def ağırlıksız_yönsüz_grafiği_başlat(düğüm_sayısı: int, kenar_sayısı: int) -> dict[int, list[int]]:
    grafik: dict[int, list[int]] = {}
    for i in range(düğüm_sayısı):
        grafik[i + 1] = []

    for e in range(kenar_sayısı):
        x, y = (int(i) for i in _input(f"Kenar {e + 1}: <düğüm1> <düğüm2> "))
        grafik[x].append(y)
        grafik[y].append(x)
    return grafik


def ağırlıklı_yönsüz_grafiği_başlat(düğüm_sayısı: int, kenar_sayısı: int) -> dict[int, list[tuple[int, int]]]:
    grafik: dict[int, list[tuple[int, int]]] = {}
    for i in range(düğüm_sayısı):
        grafik[i + 1] = []

    for e in range(kenar_sayısı):
        x, y, w = (int(i) for i in _input(f"Kenar {e + 1}: <düğüm1> <düğüm2> <ağırlık> "))
        grafik[x].append((y, w))
        grafik[y].append((x, w))
    return grafik


if __name__ == "__main__":
    n, m = (int(i) for i in _input("Düğüm ve kenar sayısı: "))

    grafik_seçimi = int(
        _input(
            "1 veya 2 veya 3'e basın \n"
            "1. Ağırlıksız yönlü \n"
            "2. Ağırlıksız yönsüz \n"
            "3. Ağırlıklı yönsüz \n"
        )[0]
    )

    g = {
        1: ağırlıksız_yönlü_grafiği_başlat,
        2: ağırlıksız_yönsüz_grafiği_başlat,
        3: ağırlıklı_yönsüz_grafiği_başlat,
    }[grafik_seçimi](n, m)


"""
--------------------------------------------------------------------------------
    Derinlik Öncelikli Arama (DFS).
        Args :  G - Kenarların Sözlüğü
                s - Başlangıç Düğümü
        Vars :  vis - Ziyaret edilen düğümlerin kümesi
                S - Geçiş Yığını
--------------------------------------------------------------------------------
"""


def dfs(g, s):
    vis, _s = {s}, [s]
    print(s)
    while _s:
        flag = 0
        for i in g[_s[-1]]:
            if i not in vis:
                _s.append(i)
                vis.add(i)
                flag = 1
                print(i)
                break
        if not flag:
            _s.pop()


"""
--------------------------------------------------------------------------------
    Genişlik Öncelikli Arama (BFS).
        Args :  G - Kenarların Sözlüğü
                s - Başlangıç Düğümü
        Vars :  vis - Ziyaret edilen düğümlerin kümesi
                Q - Geçiş Kuyruğu
--------------------------------------------------------------------------------
"""


def bfs(g, s):
    vis, q = {s}, deque([s])
    print(s)
    while q:
        u = q.popleft()
        for v in g[u]:
            if v not in vis:
                vis.add(v)
                q.append(v)
                print(v)


"""
--------------------------------------------------------------------------------
    Dijkstra'nın en kısa yol algoritması
        Args :  G - Kenarların Sözlüğü
                s - Başlangıç Düğümü
        Vars :  dist - s'den her düğüme en kısa mesafeyi saklayan sözlük
                known - Bilinen düğümlerin kümesi
                path - Yoldaki önceki düğüm
--------------------------------------------------------------------------------
"""


def dijkstra(g, s):
    dist, known, path = {s: 0}, set(), {s: 0}
    while True:
        if len(known) == len(g) - 1:
            break
        mini = 100000
        for i in dist:
            if i not in known and dist[i] < mini:
                mini = dist[i]
                u = i
        known.add(u)
        for v in g[u]:
            if v[0] not in known and dist[u] + v[1] < dist.get(v[0], 100000):
                dist[v[0]] = dist[u] + v[1]
                path[v[0]] = u
    for i in dist:
        if i != s:
            print(dist[i])


"""
--------------------------------------------------------------------------------
    Topolojik Sıralama
--------------------------------------------------------------------------------
"""


def topolojik_sıralama(g, ind=None, q=None):
    if q is None:
        q = [1]
    if ind is None:
        ind = [0] * (len(g) + 1)  # 0. İndeks göz ardı edilir
        for u in g:
            for v in g[u]:
                ind[v] += 1
        q = deque()
        for i in g:
            if ind[i] == 0:
                q.append(i)
    if len(q) == 0:
        return
    v = q.popleft()
    print(v)
    for w in g[v]:
        ind[w] -= 1
        if ind[w] == 0:
            q.append(w)
    topolojik_sıralama(g, ind, q)


"""
--------------------------------------------------------------------------------
    Komşuluk Matrisi Okuma
--------------------------------------------------------------------------------
"""


def komşuluk_matrisi():
    r"""
    Komşuluk Matrisi Okuma

    Parametreler:
        Yok

    Dönüş:
        tuple: Kenarların listesi ve kenar sayısını içeren bir tuple

    Örnek:
    >>> # 3 düğüm için kullanıcı girdisini simüle et
    >>> input_data = "4\n0 1 0 1\n1 0 1 0\n0 1 0 1\n1 0 1 0\n"
    >>> import sys,io
    >>> original_input = sys.stdin
    >>> sys.stdin = io.StringIO(input_data)  # Test için stdin'i yönlendir
    >>> komşuluk_matrisi()
    ([(0, 1, 0, 1), (1, 0, 1, 0), (0, 1, 0, 1), (1, 0, 1, 0)], 4)
    >>> sys.stdin = original_input  # Orijinal stdin'i geri yükle
    """
    n = int(input().strip())
    a = []
    for _ in range(n):
        a.append(tuple(map(int, input().strip().split())))
    return a, n


"""
--------------------------------------------------------------------------------
    Floyd Warshall algoritması
        Args :  G - Kenarların Sözlüğü
                s - Başlangıç Düğümü
        Vars :  dist - s'den her düğüme en kısa mesafeyi saklayan sözlük
                known - Bilinen düğümlerin kümesi
                path - Yoldaki önceki düğüm

--------------------------------------------------------------------------------
"""


def floyd_warshall(a_and_n):
    (a, n) = a_and_n
    dist = list(a)
    path = [[0] * n for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][k] = k
    print(dist)


"""
--------------------------------------------------------------------------------
    Prim'in Minimum Spanning Tree (MST) Algoritması
        Args :  G - Kenarların Sözlüğü
                s - Başlangıç Düğümü
        Vars :  dist - s'den en yakın düğüme en kısa mesafeyi saklayan sözlük
                known - Bilinen düğümlerin kümesi
                path - Yoldaki önceki düğüm
--------------------------------------------------------------------------------
"""


def prim(g, s):
    dist, known, path = {s: 0}, set(), {s: 0}
    while True:
        if len(known) == len(g) - 1:
            break
        mini = 100000
        for i in dist:
            if i not in known and dist[i] < mini:
                mini = dist[i]
                u = i
        known.add(u)
        for v in g[u]:
            if v[0] not in known and v[1] < dist.get(v[0], 100000):
                dist[v[0]] = v[1]
                path[v[0]] = u
    return dist


"""
--------------------------------------------------------------------------------
    Kenar Listesi Kabul Etme
        Vars :  n - Düğüm sayısı
                m - Kenar sayısı
        Dönüş : l - Kenar listesi
                n - Düğüm sayısı
--------------------------------------------------------------------------------
"""


def kenar_listesi():
    r"""
    Kullanıcıdan kenarları ve kenar sayısını alın

    Parametreler:
        Yok

    Dönüş:
        tuple: Kenarların listesi ve kenar sayısını içeren bir tuple

    Örnek:
    >>> # 3 kenar ve 4 düğüm için kullanıcı girdisini simüle et: (1, 2), (2, 3), (3, 4)
    >>> input_data = "4 3\n1 2\n2 3\n3 4\n"
    >>> import sys,io
    >>> original_input = sys.stdin
    >>> sys.stdin = io.StringIO(input_data)  # Test için stdin'i yönlendir
    >>> kenar_listesi()
    ([(1, 2), (2, 3), (3, 4)], 4)
    >>> sys.stdin = original_input  # Orijinal stdin'i geri yükle
    """
    n, m = tuple(map(int, input().split(" ")))
    kenarlar = []
    for _ in range(m):
        kenarlar.append(tuple(map(int, input().split(" "))))
    return kenarlar, n


"""
--------------------------------------------------------------------------------
    Kruskal'ın Minimum Spanning Tree (MST) Algoritması
        Args :  E - Kenar listesi
                n - Düğüm sayısı
        Vars :  s - Başlangıçta benzersiz ayrık kümeler olarak tüm düğümlerin kümesi
--------------------------------------------------------------------------------
"""


def kruskal(e_and_n):
    """
    Kenarları mesafeye göre sırala
    """
    (e, n) = e_and_n
    e.sort(reverse=True, key=lambda x: x[2])
    s = [{i} for i in range(1, n + 1)]
    while True:
        if len(s) == 1:
            break
        print(s)
        x = e.pop()
        for i in range(len(s)):
            if x[0] in s[i]:
                break
        for j in range(len(s)):
            if x[1] in s[j]:
                if i == j:
                    break
                s[j].update(s[i])
                s.pop(i)
                break


def izole_düğümleri_bul(graf):
    """
    Grafikteki izole düğümleri bulun

    Parametreler:
    graf (dict): Bir grafiği temsil eden sözlük.

    Dönüş:
    list: İzole düğümlerin listesi.

    Örnekler:
    >>> graf1 = {1: [2, 3], 2: [1, 3], 3: [1, 2], 4: []}
    >>> izole_düğümleri_bul(graf1)
    [4]

    >>> graf2 = {'A': ['B', 'C'], 'B': ['A'], 'C': ['A'], 'D': []}
    >>> izole_düğümleri_bul(graf2)
    ['D']

    >>> graf3 = {'X': [], 'Y': [], 'Z': []}
    >>> izole_düğümleri_bul(graf3)
    ['X', 'Y', 'Z']

    >>> graf4 = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
    >>> izole_düğümleri_bul(graf4)
    []

    >>> graf5 = {}
    >>> izole_düğümleri_bul(graf5)
    []
    """
    izole = []
    for düğüm in graf:
        if not graf[düğüm]:
            izole.append(düğüm)
    return izole
