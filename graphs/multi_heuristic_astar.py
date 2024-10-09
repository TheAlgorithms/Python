import heapq
import sys
import numpy as np

TPos = tuple[int, int]

class OncelikKuyrugu:
    def __init__(self):
        self.elemanlar = []
        self.kume = set()

    def min_anahtar(self):
        if not self.bos_mu():
            return self.elemanlar[0][0]
        else:
            return float("inf")

    def bos_mu(self):
        return len(self.elemanlar) == 0

    def ekle(self, eleman, oncelik):
        if eleman not in self.kume:
            heapq.heappush(self.elemanlar, (oncelik, eleman))
            self.kume.add(eleman)
        else:
            # güncelle
            temp = []
            while self.elemanlar:
                (pri, x) = heapq.heappop(self.elemanlar)
                if x == eleman:
                    break
                temp.append((pri, x))
            temp.append((oncelik, eleman))
            for pro, xxx in temp:
                heapq.heappush(self.elemanlar, (pro, xxx))

    def eleman_sil(self, eleman):
        if eleman in self.kume:
            self.kume.remove(eleman)
            temp = []
            while self.elemanlar:
                (pro, x) = heapq.heappop(self.elemanlar)
                if x == eleman:
                    break
                temp.append((pro, x))
            for prito, yyy in temp:
                heapq.heappush(self.elemanlar, (prito, yyy))

    def en_ust_goster(self):
        return self.elemanlar[0][1]

    def al(self):
        (oncelik, eleman) = heapq.heappop(self.elemanlar)
        self.kume.remove(eleman)
        return (oncelik, eleman)

def tutarli_heuristik(p: TPos, hedef: TPos):
    # öklid mesafesi
    a = np.array(p)
    b = np.array(hedef)
    return np.linalg.norm(a - b)

def heuristik_2(p: TPos, hedef: TPos):
    # zaman değişkeni ile tam sayı bölme
    return tutarli_heuristik(p, hedef) // t

def heuristik_1(p: TPos, hedef: TPos):
    # manhattan mesafesi
    return abs(p[0] - hedef[0]) + abs(p[1] - hedef[1])

def anahtar(baslangic: TPos, i: int, hedef: TPos, g_fonksiyonu: dict[TPos, float]):
    return g_fonksiyonu[baslangic] + W1 * heuristikler[i](baslangic, hedef)

def bir_sey_yap(geri_izleme, hedef, baslangic):
    grid = np.char.chararray((n, n))
    for i in range(n):
        for j in range(n):
            grid[i][j] = "*"

    for i in range(n):
        for j in range(n):
            if (j, (n - 1) - i) in bloklar:
                grid[i][j] = "#"

    grid[0][(n - 1)] = "-"
    x = geri_izleme[hedef]
    while x != baslangic:
        (x_c, y_c) = x
        grid[(n - 1) - y_c][x_c] = "-"
        x = geri_izleme[x]
    grid[(n - 1)][0] = "-"

    for i in range(n):
        for j in range(n):
            if (i, j) == (0, n - 1):
                print(grid[i][j], end=" ")
                print("<-- Bitiş noktası", end=" ")
            else:
                print(grid[i][j], end=" ")
        print()
    print("^")
    print("Başlangıç noktası")
    print()
    print("# bir engeldir")
    print("- algoritmanın izlediği yoldur")
    print("ALGORİTMANIN İZLEDİĞİ YOL:-")
    x = geri_izleme[hedef]
    while x != baslangic:
        print(x, end=" ")
        x = geri_izleme[x]
    print(x)
    sys.exit()

def gecerli(p: TPos):
    if p[0] < 0 or p[0] > n - 1:
        return False
    return not [1] < 0 or p[1] > n - 1

def durum_genislet(
    s,
    j,
    ziyaret_edilenler,
    g_fonksiyonu,
    kapali_liste_ana,
    kapali_liste_inad,
    acik_liste,
    geri_izleme,
):
    for itera in range(n_heuristik):
        acik_liste[itera].eleman_sil(s)

    (x, y) = s
    sol = (x - 1, y)
    sag = (x + 1, y)
    yukari = (x, y + 1)
    asagi = (x, y - 1)

    for komsular in [sol, sag, yukari, asagi]:
        if komsular not in bloklar:
            if gecerli(komsular) and komsular not in ziyaret_edilenler:
                ziyaret_edilenler.add(komsular)
                geri_izleme[komsular] = -1
                g_fonksiyonu[komsular] = float("inf")

            if gecerli(komsular) and g_fonksiyonu[komsular] > g_fonksiyonu[s] + 1:
                g_fonksiyonu[komsular] = g_fonksiyonu[s] + 1
                geri_izleme[komsular] = s
                if komsular not in kapali_liste_ana:
                    acik_liste[0].ekle(komsular, anahtar(komsular, 0, hedef, g_fonksiyonu))
                    if komsular not in kapali_liste_inad:
                        for var in range(1, n_heuristik):
                            if anahtar(komsular, var, hedef, g_fonksiyonu) <= W2 * anahtar(
                                komsular, 0, hedef, g_fonksiyonu
                            ):
                                acik_liste[j].ekle(
                                    komsular, anahtar(komsular, var, hedef, g_fonksiyonu)
                                )

def ortak_zemin_olustur():
    bazi_liste = []
    for x in range(1, 5):
        for y in range(1, 6):
            bazi_liste.append((x, y))

    for x in range(15, 20):
        bazi_liste.append((x, 17))

    for x in range(10, 19):
        for y in range(1, 15):
            bazi_liste.append((x, y))

    # L bloğu
    for x in range(1, 4):
        for y in range(12, 19):
            bazi_liste.append((x, y))
    for x in range(3, 13):
        for y in range(16, 19):
            bazi_liste.append((x, y))
    return bazi_liste

heuristikler = {0: tutarli_heuristik, 1: heuristik_1, 2: heuristik_2}

bloklar_blk = [
    (0, 1),
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 1),
    (7, 1),
    (8, 1),
    (9, 1),
    (10, 1),
    (11, 1),
    (12, 1),
    (13, 1),
    (14, 1),
    (15, 1),
    (16, 1),
    (17, 1),
    (18, 1),
    (19, 1),
]
bloklar_hepsi = ortak_zemin_olustur()

bloklar = bloklar_blk
# hiper parametreler
W1 = 1
W2 = 1
n = 20
n_heuristik = 3  # bir tutarlı ve iki diğer tutarsız

# başlangıç ve bitiş noktası
baslangic = (0, 0)
hedef = (n - 1, n - 1)

t = 1

def coklu_a_yildizi(baslangic: TPos, hedef: TPos, n_heuristik: int):
    g_fonksiyonu = {baslangic: 0, hedef: float("inf")}
    geri_izleme = {baslangic: -1, hedef: -1}
    acik_liste = []
    ziyaret_edilenler = set()

    for i in range(n_heuristik):
        acik_liste.append(OncelikKuyrugu())
        acik_liste[i].ekle(baslangic, anahtar(baslangic, i, hedef, g_fonksiyonu))

    kapali_liste_ana: list[int] = []
    kapali_liste_inad: list[int] = []
    while acik_liste[0].min_anahtar() < float("inf"):
        for i in range(1, n_heuristik):
            if acik_liste[i].min_anahtar() <= W2 * acik_liste[0].min_anahtar():
                global t
                t += 1
                if g_fonksiyonu[hedef] <= acik_liste[i].min_anahtar():
                    if g_fonksiyonu[hedef] < float("inf"):
                        bir_sey_yap(geri_izleme, hedef, baslangic)
                else:
                    _, get_s = acik_liste[i].en_ust_goster()
                    ziyaret_edilenler.add(get_s)
                    durum_genislet(
                        get_s,
                        i,
                        ziyaret_edilenler,
                        g_fonksiyonu,
                        kapali_liste_ana,
                        kapali_liste_inad,
                        acik_liste,
                        geri_izleme,
                    )
                    kapali_liste_inad.append(get_s)
            elif g_fonksiyonu[hedef] <= acik_liste[0].min_anahtar():
                if g_fonksiyonu[hedef] < float("inf"):
                    bir_sey_yap(geri_izleme, hedef, baslangic)
            else:
                get_s = acik_liste[0].en_ust_goster()
                ziyaret_edilenler.add(get_s)
                durum_genislet(
                    get_s,
                    0,
                    ziyaret_edilenler,
                    g_fonksiyonu,
                    kapali_liste_ana,
                    kapali_liste_inad,
                    acik_liste,
                    geri_izleme,
                )
                kapali_liste_ana.append(get_s)
    print("Hedefe giden yol bulunamadı")
    print()
    for i in range(n - 1, -1, -1):
        for j in range(n):
            if (j, i) in bloklar:
                print("#", end=" ")
            elif (j, i) in geri_izleme:
                if (j, i) == (n - 1, n - 1):
                    print("*", end=" ")
                else:
                    print("-", end=" ")
            else:
                print("*", end=" ")
            if (j, i) == (n - 1, n - 1):
                print("<-- Bitiş noktası", end=" ")
        print()
    print("^")
    print("Başlangıç noktası")
    print()
    print("# bir engeldir")
    print("- algoritmanın izlediği yoldur")

if __name__ == "__main__":
    coklu_a_yildizi(baslangic, hedef, n_heuristik)
