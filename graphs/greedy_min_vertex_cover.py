"""
* Yazar: Manuel Di Lullo (https://github.com/manueldilullo)
* Açıklama: Minimum köşe örtüsü problemi için yaklaşık algoritma.
            Açgözlü Yaklaşım. Komşuluk listesi ile temsil edilen grafikleri kullanır.
URL: https://mathworld.wolfram.com/MinimumVertexCover.html
URL: https://cs.stackexchange.com/questions/129017/greedy-algorithm-for-vertex-cover
"""

import heapq


def acgozlu_min_kose_ortusu(grafik: dict) -> set[int]:
    """
    Minimum Köşe Örtüsü için Açgözlü Yaklaşım Algoritması
    @girdi: grafik (her köşenin bir tamsayı ile temsil edildiği bir komşuluk listesinde saklanan grafik)
    @örnek:
    >>> grafik = {0: [1, 3], 1: [0, 3], 2: [0, 3, 4], 3: [0, 1, 2], 4: [2, 3]}
    >>> acgozlu_min_kose_ortusu(grafik)
    {0, 1, 2, 4}
    """
    # düğümleri ve sıralarını saklamak için kullanılan kuyruk
    kuyruk: list[list] = []

    # her düğüm ve onun komşuluk listesini kuyruk ve düğümün sırasına ekle
    # heapq modülünü kullanarak kuyruk bir Öncelik Kuyruğu gibi doldurulacak
    # heapq bir min öncelik kuyruğu ile çalışır, bu yüzden -1*len(v) kullandım
    for anahtar, deger in grafik.items():
        # O(log(n))
        heapq.heappush(kuyruk, [-1 * len(deger), (anahtar, deger)])

    # secilen_koseler = seçilen köşelerin kümesi
    secilen_koseler = set()

    # kuyruk boş değilken ve hala kenarlar varken
    #   (kuyruk[0][0] en yüksek sıraya sahip düğümün sırasıdır)
    while kuyruk and kuyruk[0][0] != 0:
        # en yüksek sıraya sahip düğümü kuyruktan çıkar ve secilen_koseler'e ekle
        argmax = heapq.heappop(kuyruk)[1][0]
        secilen_koseler.add(argmax)

        # argmax'e bitişik tüm yayları kaldır
        for eleman in kuyruk:
            # eğer v'nin bitişik düğümü yoksa, atla
            if eleman[0] == 0:
                continue
            # eğer argmax elemandan ulaşılabiliyorsa
            # argmax'i elemanın bitişik listesinden kaldır ve sırasını güncelle
            if argmax in eleman[1][1]:
                index = eleman[1][1].index(argmax)
                del eleman[1][1][index]
                eleman[0] += 1
        # kuyruğu yeniden sırala
        heapq.heapify(kuyruk)
    return secilen_koseler


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    grafik = {0: [1, 3], 1: [0, 3], 2: [0, 3, 4], 3: [0, 1, 2], 4: [2, 3]}
    print(f"Minimum köşe örtüsü:\n{acgozlu_min_kose_ortusu(grafik)}")
