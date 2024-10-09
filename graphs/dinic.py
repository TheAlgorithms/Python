INF = float("inf")


class Dinic:
    def __init__(self, n):
        self.seviye = [0] * n
        self.ptr = [0] * n
        self.kuyruk = [0] * n
        self.komsuluk_listesi = [[] for _ in range(n)]

    """
    Burada kenarlarımızı şu parametrelerle ekleyeceğiz:
    kaynağa en yakın düğüm, hedefe en yakın düğüm ve bu kenar üzerinden akış kapasitesi...
    """

    def kenar_ekle(self, a, b, c, rkap=0):
        self.komsuluk_listesi[a].append([b, len(self.komsuluk_listesi[b]), c, 0])
        self.komsuluk_listesi[b].append([a, len(self.komsuluk_listesi[a]) - 1, rkap, 0])

    # Bu, max_akışta kullanılacak örnek bir derinlik öncelikli aramadır
    def derinlik_oncelikli_arama(self, dugum, hedef, akış):
        if dugum == hedef or not akış:
            return akış

        for i in range(self.ptr[dugum], len(self.komsuluk_listesi[dugum])):
            e = self.komsuluk_listesi[dugum][i]
            if self.seviye[e[0]] == self.seviye[dugum] + 1:
                p = self.derinlik_oncelikli_arama(e[0], hedef, min(akış, e[2] - e[3]))
                if p:
                    self.komsuluk_listesi[dugum][i][3] += p
                    self.komsuluk_listesi[e[0]][e[1]][3] -= p
                    return p
            self.ptr[dugum] = self.ptr[dugum] + 1
        return 0

    # Burada hedefe ulaşan akışı hesaplıyoruz
    def max_akış(self, kaynak, hedef):
        akış, self.kuyruk[0] = 0, kaynak
        for l in range(31):  # l = 30 rastgele veri için daha hızlı olabilir  # noqa: E741
            while True:
                self.seviye, self.ptr = [0] * len(self.kuyruk), [0] * len(self.kuyruk)
                qi, qe, self.seviye[kaynak] = 0, 1, 1
                while qi < qe and not self.seviye[hedef]:
                    v = self.kuyruk[qi]
                    qi += 1
                    for e in self.komsuluk_listesi[v]:
                        if not self.seviye[e[0]] and (e[2] - e[3]) >> (30 - l):
                            self.kuyruk[qe] = e[0]
                            qe += 1
                            self.seviye[e[0]] = self.seviye[v] + 1

                p = self.derinlik_oncelikli_arama(kaynak, hedef, INF)
                while p:
                    akış += p
                    p = self.derinlik_oncelikli_arama(kaynak, hedef, INF)

                if not self.seviye[hedef]:
                    break

        return akış


# Kullanım örneği

"""
Bu bir iki parçalı grafik olacak, bu nedenle kaynağa yakın düğümler (4)
ve hedefe yakın düğümler (4) vardır
"""
# Burada 10 düğümlü bir grafik oluşturuyoruz (kaynak ve hedef dahil)
grafik = Dinic(10)
kaynak = 0
hedef = 9
"""
Şimdi kaynağa yakın düğümleri kenar kapasitesi 1 olan kaynak ile ekliyoruz
(kaynak -> kaynak düğümleri)
"""
for dugum in range(1, 5):
    grafik.kenar_ekle(kaynak, dugum, 1)
"""
Aynı şeyi hedefe yakın düğümler için de yapacağız, ancak düğümden hedefe
(hedef düğümleri -> hedef)
"""
for dugum in range(5, 9):
    grafik.kenar_ekle(dugum, hedef, 1)
"""
Son olarak, hedefe yakın düğümleri kaynağa yakın düğümlere ekliyoruz.
(kaynak düğümleri -> hedef düğümleri)
"""
for dugum in range(1, 5):
    grafik.kenar_ekle(dugum, dugum + 4, 1)

# Şimdi kaynak -> hedef arasındaki maksimum akışı öğrenebiliriz
print(grafik.max_akış(kaynak, hedef))
