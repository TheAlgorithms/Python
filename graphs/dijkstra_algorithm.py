# Başlık: Dijkstra Algoritması ile tek kaynaklı en kısa yolun bulunması
# Yazar: Shubham Malik
# Referanslar: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

import math
import sys

# En düşük mesafeye sahip düğümü almak için düğüm kümesini saklamak amacıyla


class OncelikKuyrugu:
    # Min Heap tabanlı
    def __init__(self):
        """
        Öncelik kuyruğu sınıfı yapıcı metodu.

        Örnekler:
        >>> oncelik_kuyrugu_test = OncelikKuyrugu()
        >>> oncelik_kuyrugu_test.mevcut_boyut
        0
        >>> oncelik_kuyrugu_test.dizi
        []
        >>> oncelik_kuyrugu_test.konum
        {}
        """
        self.mevcut_boyut = 0
        self.dizi = []
        self.konum = {}  # Düğümün dizideki konumunu saklamak için

    def bos_mu(self):
        """
        Öncelik kuyruğunun boş olup olmadığını belirlemek için koşullu boolean metodu.

        Örnekler:
        >>> oncelik_kuyrugu_test = OncelikKuyrugu()
        >>> oncelik_kuyrugu_test.bos_mu()
        True
        >>> oncelik_kuyrugu_test.ekle((2, 'A'))
        >>> oncelik_kuyrugu_test.bos_mu()
        False
        """
        return self.mevcut_boyut == 0

    def min_heapify(self, idx):
        """
        Kuyruk dizisini minimum elemanın kök olacak şekilde sıralar.

        Örnekler:
        >>> oncelik_kuyrugu_test = OncelikKuyrugu()
        >>> oncelik_kuyrugu_test.mevcut_boyut = 3
        >>> oncelik_kuyrugu_test.konum = {'A': 0, 'B': 1, 'C': 2}

        >>> oncelik_kuyrugu_test.dizi = [(5, 'A'), (10, 'B'), (15, 'C')]
        >>> oncelik_kuyrugu_test.min_heapify(0)
        >>> oncelik_kuyrugu_test.dizi
        [(5, 'A'), (10, 'B'), (15, 'C')]

        >>> oncelik_kuyrugu_test.dizi = [(10, 'A'), (5, 'B'), (15, 'C')]
        >>> oncelik_kuyrugu_test.min_heapify(0)
        >>> oncelik_kuyrugu_test.dizi
        [(5, 'B'), (10, 'A'), (15, 'C')]

        >>> oncelik_kuyrugu_test.dizi = [(10, 'A'), (15, 'B'), (5, 'C')]
        >>> oncelik_kuyrugu_test.min_heapify(0)
        >>> oncelik_kuyrugu_test.dizi
        [(5, 'C'), (15, 'B'), (10, 'A')]

        >>> oncelik_kuyrugu_test.dizi = [(10, 'A'), (5, 'B')]
        >>> oncelik_kuyrugu_test.mevcut_boyut = len(oncelik_kuyrugu_test.dizi)
        >>> oncelik_kuyrugu_test.konum = {'A': 0, 'B': 1}
        >>> oncelik_kuyrugu_test.min_heapify(0)
        >>> oncelik_kuyrugu_test.dizi
        [(5, 'B'), (10, 'A')]
        """
        sol = self.sol(idx)
        sag = self.sag(idx)
        if sol < self.mevcut_boyut and self.dizi[sol][0] < self.dizi[idx][0]:
            en_kucuk = sol
        else:
            en_kucuk = idx
        if sag < self.mevcut_boyut and self.dizi[sag][0] < self.dizi[en_kucuk][0]:
            en_kucuk = sag
        if en_kucuk != idx:
            self.takas(idx, en_kucuk)
            self.min_heapify(en_kucuk)

    def ekle(self, tup):
        """
        Öncelik Kuyruğuna bir düğüm ekler.

        Örnekler:
        >>> oncelik_kuyrugu_test = OncelikKuyrugu()
        >>> oncelik_kuyrugu_test.ekle((10, 'A'))
        >>> oncelik_kuyrugu_test.dizi
        [(10, 'A')]
        >>> oncelik_kuyrugu_test.ekle((15, 'B'))
        >>> oncelik_kuyrugu_test.dizi
        [(10, 'A'), (15, 'B')]
        >>> oncelik_kuyrugu_test.ekle((5, 'C'))
        >>> oncelik_kuyrugu_test.dizi
        [(5, 'C'), (15, 'B'), (10, 'A')]
        """
        self.konum[tup[1]] = self.mevcut_boyut
        self.mevcut_boyut += 1
        self.dizi.append((sys.maxsize, tup[1]))
        self.anahtar_azalt((sys.maxsize, tup[1]), tup[0])

    def min_cikar(self):
        """
        Öncelik kuyruğunun en üstündeki minimum elemanı çıkarır ve döndürür.

        Örnekler:
        >>> oncelik_kuyrugu_test = OncelikKuyrugu()
        >>> oncelik_kuyrugu_test.dizi = [(10, 'A'), (15, 'B')]
        >>> oncelik_kuyrugu_test.mevcut_boyut = len(oncelik_kuyrugu_test.dizi)
        >>> oncelik_kuyrugu_test.konum = {'A': 0, 'B': 1}
        >>> oncelik_kuyrugu_test.ekle((5, 'C'))
        >>> oncelik_kuyrugu_test.min_cikar()
        'C'
        >>> oncelik_kuyrugu_test.dizi[0]
        (10, 'A')
        """
        min_dugum = self.dizi[0][1]
        self.dizi[0] = self.dizi[self.mevcut_boyut - 1]
        self.mevcut_boyut -= 1
        self.min_heapify(0)
        del self.konum[min_dugum]
        return min_dugum

    def sol(self, i):
        """
        Sol çocuğun indeksini döndürür

        Örnekler:
        >>> oncelik_kuyrugu_test = OncelikKuyrugu()
        >>> oncelik_kuyrugu_test.sol(0)
        1
        >>> oncelik_kuyrugu_test.sol(1)
        3
        """
        return 2 * i + 1

    def sag(self, i):
        """
        Sağ çocuğun indeksini döndürür

        Örnekler:
        >>> oncelik_kuyrugu_test = OncelikKuyrugu()
        >>> oncelik_kuyrugu_test.sag(0)
        2
        >>> oncelik_kuyrugu_test.sag(1)
        4
        """
        return 2 * i + 2

    def ebeveyn(self, i):
        """
        Ebeveynin indeksini döndürür

        Örnekler:
        >>> oncelik_kuyrugu_test = OncelikKuyrugu()
        >>> oncelik_kuyrugu_test.ebeveyn(1)
        0
        >>> oncelik_kuyrugu_test.ebeveyn(2)
        0
        >>> oncelik_kuyrugu_test.ebeveyn(4)
        1
        """
        return (i - 1) // 2

    def takas(self, i, j):
        """
        Dizideki i ve j indekslerindeki elemanları takas eder, konum{} günceller

        Örnekler:
        >>> oncelik_kuyrugu_test = OncelikKuyrugu()
        >>> oncelik_kuyrugu_test.dizi = [(10, 'A'), (15, 'B')]
        >>> oncelik_kuyrugu_test.mevcut_boyut = len(oncelik_kuyrugu_test.dizi)
        >>> oncelik_kuyrugu_test.konum = {'A': 0, 'B': 1}
        >>> oncelik_kuyrugu_test.takas(0, 1)
        >>> oncelik_kuyrugu_test.dizi
        [(15, 'B'), (10, 'A')]
        >>> oncelik_kuyrugu_test.konum
        {'A': 1, 'B': 0}
        """
        self.konum[self.dizi[i][1]] = j
        self.konum[self.dizi[j][1]] = i
        temp = self.dizi[i]
        self.dizi[i] = self.dizi[j]
        self.dizi[j] = temp

    def anahtar_azalt(self, tup, yeni_d):
        """
        Verilen bir tuple için anahtar değerini azaltır, yeni_d en fazla eski_d olduğunu varsayar.

        Örnekler:
        >>> oncelik_kuyrugu_test = OncelikKuyrugu()
        >>> oncelik_kuyrugu_test.dizi = [(10, 'A'), (15, 'B')]
        >>> oncelik_kuyrugu_test.mevcut_boyut = len(oncelik_kuyrugu_test.dizi)
        >>> oncelik_kuyrugu_test.konum = {'A': 0, 'B': 1}
        >>> oncelik_kuyrugu_test.anahtar_azalt((10, 'A'), 5)
        >>> oncelik_kuyrugu_test.dizi
        [(5, 'A'), (15, 'B')]
        """
        idx = self.konum[tup[1]]
        # yeni_d en fazla eski_d olduğunu varsayarak
        self.dizi[idx] = (yeni_d, tup[1])
        while idx > 0 and self.dizi[self.ebeveyn(idx)][0] > self.dizi[idx][0]:
            self.takas(idx, self.ebeveyn(idx))
            idx = self.ebeveyn(idx)


class Grafik:
    def __init__(self, num):
        """
        Grafik sınıfı yapıcı metodu

        Örnekler:
        >>> grafik_test = Grafik(1)
        >>> grafik_test.dugum_sayisi
        1
        >>> grafik_test.mesafe
        [0]
        >>> grafik_test.ebeveyn
        [-1]
        >>> grafik_test.komsuListesi
        {}
        """
        self.komsuListesi = {}  # Grafiği saklamak için: u -> (v,w)
        self.dugum_sayisi = num  # Grafikteki düğüm sayısı
        # Kaynak düğümden mesafeyi saklamak için
        self.mesafe = [0] * self.dugum_sayisi
        self.ebeveyn = [-1] * self.dugum_sayisi  # Yolu saklamak için

    def kenar_ekle(self, u, v, w):
        """
        u düğümünden v'ye ve v'den u'ya ağırlık w ile kenar ekler: u (w)-> v, v (w) -> u

        Örnekler:
        >>> grafik_test = Grafik(1)
        >>> grafik_test.kenar_ekle(1, 2, 1)
        >>> grafik_test.kenar_ekle(2, 3, 2)
        >>> grafik_test.komsuListesi
        {1: [(2, 1)], 2: [(1, 1), (3, 2)], 3: [(2, 2)]}
        """
        # u zaten grafikte mi kontrol et
        if u in self.komsuListesi:
            self.komsuListesi[u].append((v, w))
        else:
            self.komsuListesi[u] = [(v, w)]

        # Yönsüz grafik varsayımı
        if v in self.komsuListesi:
            self.komsuListesi[v].append((u, w))
        else:
            self.komsuListesi[v] = [(u, w)]

    def grafik_goster(self):
        """
        Grafiği göster: u -> v(w)

        Örnekler:
        >>> grafik_test = Grafik(1)
        >>> grafik_test.kenar_ekle(1, 2, 1)
        >>> grafik_test.grafik_goster()
        1 -> 2(1)
        2 -> 1(1)
        >>> grafik_test.kenar_ekle(2, 3, 2)
        >>> grafik_test.grafik_goster()
        1 -> 2(1)
        2 -> 1(1) -> 3(2)
        3 -> 2(2)
        """
        for u in self.komsuListesi:
            print(u, "->", " -> ".join(str(f"{v}({w})") for v, w in self.komsuListesi[u]))

    def dijkstra(self, src):
        """
        Dijkstra algoritması

        Örnekler:
        >>> grafik_test = Grafik(3)
        >>> grafik_test.kenar_ekle(0, 1, 2)
        >>> grafik_test.kenar_ekle(1, 2, 2)
        >>> grafik_test.dijkstra(0)
        Düğümden mesafe: 0
        Düğüm 0 mesafesi: 0
        Düğüm 1 mesafesi: 2
        Düğüm 2 mesafesi: 4
        >>> grafik_test.mesafe
        [0, 2, 4]

        >>> grafik_test = Grafik(2)
        >>> grafik_test.kenar_ekle(0, 1, 2)
        >>> grafik_test.dijkstra(0)
        Düğümden mesafe: 0
        Düğüm 0 mesafesi: 0
        Düğüm 1 mesafesi: 2
        >>> grafik_test.mesafe
        [0, 2]

        >>> grafik_test = Grafik(3)
        >>> grafik_test.kenar_ekle(0, 1, 2)
        >>> grafik_test.dijkstra(0)
        Düğümden mesafe: 0
        Düğüm 0 mesafesi: 0
        Düğüm 1 mesafesi: 2
        Düğüm 2 mesafesi: 0
        >>> grafik_test.mesafe
        [0, 2, 0]

        >>> grafik_test = Grafik(3)
        >>> grafik_test.kenar_ekle(0, 1, 2)
        >>> grafik_test.kenar_ekle(1, 2, 2)
        >>> grafik_test.kenar_ekle(0, 2, 1)
        >>> grafik_test.dijkstra(0)
        Düğümden mesafe: 0
        Düğüm 0 mesafesi: 0
        Düğüm 1 mesafesi: 2
        Düğüm 2 mesafesi: 1
        >>> grafik_test.mesafe
        [0, 2, 1]

        >>> grafik_test = Grafik(4)
        >>> grafik_test.kenar_ekle(0, 1, 4)
        >>> grafik_test.kenar_ekle(1, 2, 2)
        >>> grafik_test.kenar_ekle(2, 3, 1)
        >>> grafik_test.kenar_ekle(0, 2, 3)
        >>> grafik_test.dijkstra(0)
        Düğümden mesafe: 0
        Düğüm 0 mesafesi: 0
        Düğüm 1 mesafesi: 4
        Düğüm 2 mesafesi: 3
        Düğüm 3 mesafesi: 4
        >>> grafik_test.mesafe
        [0, 4, 3, 4]

        >>> grafik_test = Grafik(4)
        >>> grafik_test.kenar_ekle(0, 1, 4)
        >>> grafik_test.kenar_ekle(1, 2, 2)
        >>> grafik_test.kenar_ekle(2, 3, 1)
        >>> grafik_test.kenar_ekle(0, 2, 7)
        >>> grafik_test.dijkstra(0)
        Düğümden mesafe: 0
        Düğüm 0 mesafesi: 0
        Düğüm 1 mesafesi: 4
        Düğüm 2 mesafesi: 6
        Düğüm 3 mesafesi: 7
        >>> grafik_test.mesafe
        [0, 4, 6, 7]
        """
        # ebeveyn[] içindeki eski değerleri temizle
        self.ebeveyn = [-1] * self.dugum_sayisi
        # src kaynak düğüm
        self.mesafe[src] = 0
        q = OncelikKuyrugu()
        q.ekle((0, src))  # (kaynak mesafesi, düğüm)
        for u in self.komsuListesi:
            if u != src:
                self.mesafe[u] = sys.maxsize  # Sonsuz
                self.ebeveyn[u] = -1

        while not q.bos_mu():
            u = q.min_cikar()  # Kaynaktan minimum mesafeye sahip düğümü döndürür
            # u'nun tüm komşularının mesafesini güncelle ve
            # önceki mesafeleri SONSUZ ise onları Q'ya ekle
            for v, w in self.komsuListesi[u]:
                yeni_mesafe = self.mesafe[u] + w
                if self.mesafe[v] > yeni_mesafe:
                    if self.mesafe[v] == sys.maxsize:
                        q.ekle((yeni_mesafe, v))
                    else:
                        q.anahtar_azalt((self.mesafe[v], v), yeni_mesafe)
                    self.mesafe[v] = yeni_mesafe
                    self.ebeveyn[v] = u

        # Kaynaktan en kısa mesafeleri göster
        self.mesafeleri_goster(src)

    def mesafeleri_goster(self, src):
        """
        Grafikteki tüm diğer düğümlere olan mesafeleri src'den gösterir

        Örnekler:
        >>> grafik_test = Grafik(1)
        >>> grafik_test.mesafeleri_goster(0)
        Düğümden mesafe: 0
        Düğüm 0 mesafesi: 0
        """
        print(f"Düğümden mesafe: {src}")
        for u in range(self.dugum_sayisi):
            print(f"Düğüm {u} mesafesi: {self.mesafe[u]}")

    def yol_goster(self, src, dest):
        """
        src'den dest'e en kısa yolu gösterir.
        UYARI: dijkstra'yı çağırdıktan *sonra* kullanın.

        Örnekler:
        >>> grafik_test = Grafik(4)
        >>> grafik_test.kenar_ekle(0, 1, 1)
        >>> grafik_test.kenar_ekle(1, 2, 2)
        >>> grafik_test.kenar_ekle(2, 3, 3)
        >>> grafik_test.dijkstra(0)
        Düğümden mesafe: 0
        Düğüm 0 mesafesi: 0
        Düğüm 1 mesafesi: 1
        Düğüm 2 mesafesi: 3
        Düğüm 3 mesafesi: 6
        >>> grafik_test.yol_goster(0, 3)  # doctest: +NORMALIZE_WHITESPACE
        ---- 0'dan 3'e ulaşmak için yol ----
        0 -> 1 -> 2 -> 3
        Yolun toplam maliyeti:  6
        """
        yol = []
        maliyet = 0
        temp = dest
        # dest'den src'ye geri izleme
        while self.ebeveyn[temp] != -1:
            yol.append(temp)
            if temp != src:
                for v, w in self.komsuListesi[temp]:
                    if v == self.ebeveyn[temp]:
                        maliyet += w
                        break
            temp = self.ebeveyn[temp]
        yol.append(src)
        yol.reverse()

        print(f"---- {src}'den {dest}'e ulaşmak için yol ----")
        for u in yol:
            print(f"{u}", end=" ")
            if u != dest:
                print("-> ", end="")

        print("\nYolun toplam maliyeti: ", maliyet)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    grafik = Grafik(9)
    grafik.kenar_ekle(0, 1, 4)
    grafik.kenar_ekle(0, 7, 8)
    grafik.kenar_ekle(1, 2, 8)
    grafik.kenar_ekle(1, 7, 11)
    grafik.kenar_ekle(2, 3, 7)
    grafik.kenar_ekle(2, 8, 2)
    grafik.kenar_ekle(2, 5, 4)
    grafik.kenar_ekle(3, 4, 9)
    grafik.kenar_ekle(3, 5, 14)
    grafik.kenar_ekle(4, 5, 10)
    grafik.kenar_ekle(5, 6, 2)
    grafik.kenar_ekle(6, 7, 1)
    grafik.kenar_ekle(6, 8, 6)
    grafik.kenar_ekle(7, 8, 7)
    grafik.grafik_goster()
    grafik.dijkstra(0)
    grafik.yol_goster(0, 4)

# OUTPUT
# 0 -> 1(4) -> 7(8)
# 1 -> 0(4) -> 2(8) -> 7(11)
# 7 -> 0(8) -> 1(11) -> 6(1) -> 8(7)
# 2 -> 1(8) -> 3(7) -> 8(2) -> 5(4)
# 3 -> 2(7) -> 4(9) -> 5(14)
# 8 -> 2(2) -> 6(6) -> 7(7)
# 5 -> 2(4) -> 3(14) -> 4(10) -> 6(2)
# 4 -> 3(9) -> 5(10)
# 6 -> 5(2) -> 7(1) -> 8(6)
# Düğümden mesafe: 0
# Düğüm 0 mesafesi: 0
# Düğüm 1 mesafesi: 4
# Düğüm 2 mesafesi: 12
# Düğüm 3 mesafesi: 19
# Düğüm 4 mesafesi: 21
# Düğüm 5 mesafesi: 11
# Düğüm 6 mesafesi: 9
# Düğüm 7 mesafesi: 8
# Düğüm 8 mesafesi: 14
# ---- 0'dan 4'e ulaşmak için yol ----
# 0 -> 7 -> 6 -> 5 -> 4
# Yolun toplam maliyeti:  21
