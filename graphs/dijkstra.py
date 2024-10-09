"""
pseudo-code

DIJKSTRA(graph G, start vertex s, destination vertex d):

//tüm düğümler başlangıçta keşfedilmemiş

1 -  H = min yığın veri yapısı olarak başlat, 0 ve s ile başlat [burada 0,
     başlangıç düğümü s'den olan mesafeyi gösterir]
2 -  H boş olmadığı sürece:
3 -    H'den ilk düğümü ve maliyeti çıkar, buna U ve maliyet de
4 -    U daha önce keşfedildiyse:
5 -      while döngüsüne, satır 2'ye git //Bir düğüm keşfedildikten sonra tekrar
         işleme gerek yok
6 -    U'yu keşfedildi olarak işaretle
7 -    Eğer U, d ise:
8 -      maliyeti döndür // başlangıç düğümünden hedef düğüme toplam maliyet
9 -    her bir kenar(U, V) için: c=kenar(U,V) maliyeti // V, graph[U] içindeyse
10 -     V keşfedildiyse:
11 -       satır 9'daki bir sonraki V'ye git
12 -     toplam_maliyet = maliyet + c
13 -     (toplam_maliyet, V) H'ye ekle

Maliyeti, Dijkstra'nın s ve v düğümleri arasındaki en kısa mesafeyi bulduğu bir
mesafe olarak düşünebilirsiniz. H'nin min yığın olarak kullanılması, bir düğüm
zaten keşfedildiyse başka bir kısa yolun olmayacağını garanti eder, çünkü
heapq.heappop her zaman bir sonraki en kısa mesafeye sahip düğümü döndürecektir,
bu da yığının sadece önceki düğüm ile mevcut düğüm arasındaki mesafeyi değil,
başlangıç düğümünden hedef düğüme kadar olan tüm mesafeyi sakladığı anlamına
gelir.
"""

import heapq


def dijkstra(grafik, baslangic, hedef):
    """Başlangıç ve hedef düğümleri arasındaki en kısa yolun maliyetini döndürür.

    >>> dijkstra(G, "E", "C")
    6
    >>> dijkstra(G2, "E", "F")
    3
    >>> dijkstra(G3, "E", "F")
    3
    """

    yigin = [(0, baslangic)]  # başlangıç düğümünden maliyet, bitiş düğümü
    ziyaret_edilen = set()
    while yigin:
        (maliyet, u) = heapq.heappop(yigin)
        if u in ziyaret_edilen:
            continue
        ziyaret_edilen.add(u)
        if u == hedef:
            return maliyet
        for v, c in grafik[u]:
            if v in ziyaret_edilen:
                continue
            sonraki_maliyet = maliyet + c
            heapq.heappush(yigin, (sonraki_maliyet, v))
    return -1


G = {
    "A": [["B", 2], ["C", 5]],
    "B": [["A", 2], ["D", 3], ["E", 1], ["F", 1]],
    "C": [["A", 5], ["F", 3]],
    "D": [["B", 3]],
    "E": [["B", 4], ["F", 3]],
    "F": [["C", 3], ["E", 3]],
}

r"""
G2'nin düzeni:

E -- 1 --> B -- 1 --> C -- 1 --> D -- 1 --> F
 \                                         /\
  \                                        ||
    ----------------- 3 --------------------
"""
G2 = {
    "B": [["C", 1]],
    "C": [["D", 1]],
    "D": [["F", 1]],
    "E": [["B", 1], ["F", 3]],
    "F": [],
}

r"""
G3'ün düzeni:

E -- 1 --> B -- 1 --> C -- 1 --> D -- 1 --> F
 \                                         /\
  \                                        ||
    -------- 2 ---------> G ------- 1 ------
"""
G3 = {
    "B": [["C", 1]],
    "C": [["D", 1]],
    "D": [["F", 1]],
    "E": [["B", 1], ["G", 2]],
    "F": [],
    "G": [["F", 1]],
}

kisa_mesafe = dijkstra(G, "E", "C")
print(kisa_mesafe)  # E -- 3 --> F -- 3 --> C == 6

kisa_mesafe = dijkstra(G2, "E", "F")
print(kisa_mesafe)  # E -- 3 --> F == 3

kisa_mesafe = dijkstra(G3, "E", "F")
print(kisa_mesafe)  # E -- 2 --> G -- 1 --> F == 3

if __name__ == "__main__":
    import doctest

    doctest.testmod()
