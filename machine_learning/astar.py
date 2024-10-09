"""
A* algoritması, optimal çözümleri verimli bir şekilde hesaplamak için uniform-cost arama ve saf heuristic arama özelliklerini birleştirir.

A* algoritması, bir düğümle ilişkili maliyetin f(n) = g(n) + h(n) olduğu en iyi ilk arama algoritmasıdır. Burada g(n), başlangıç durumundan düğüm n'ye kadar olan yolun maliyeti ve h(n), düğüm n'den bir hedefe kadar olan yolun heuristic tahminidir.

A* algoritması, düzenli bir grafik arama algoritmasına bir heuristic ekler, esasen her adımda daha optimal bir karar verilmesi için önceden plan yapar. Bu nedenle, A* beyinli bir algoritma olarak bilinir.

https://tr.wikipedia.org/wiki/A*_arama_algoritması
"""

import numpy as np


class Hucre:
    """
    Hucre sınıfı, dünyadaki bir hücreyi temsil eder ve şu özelliklere sahiptir:
    konum: Başlangıçta (0,0) olarak ayarlanan x ve y koordinatlarından oluşan bir demet.
    ebeveyn: Bu hücreye gelmeden önce ziyaret edilen ebeveyn hücre nesnesini içerir.
    g, h, f: Heuristic fonksiyonu çağrıldığında kullanılan parametreler.
    """

    def __init__(self):
        self.konum = (0, 0)
        self.ebeveyn = None
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, hucre):
        return self.konum == hucre.konum

    def hucreyi_goster(self):
        print(self.konum)


class IzgaraDunyasi:
    """
    IzgaraDunyasi sınıfı, burada bir M*M matrisi olan dış dünyayı temsil eder.
    dunya_boyutu: Varsayılan olarak 5 olan dunya_boyutu ile bir numpy array oluşturur.
    """

    def __init__(self, dunya_boyutu=(5, 5)):
        self.dunya = np.zeros(dunya_boyutu)
        self.dunya_x_limiti = dunya_boyutu[0]
        self.dunya_y_limiti = dunya_boyutu[1]

    def goster(self):
        print(self.dunya)

    def komsulari_getir(self, hucre):
        """
        Hücrenin komşularını döndürür
        """
        komsu_koordinatlari = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        mevcut_x = hucre.konum[0]
        mevcut_y = hucre.konum[1]
        komsular = []
        for k in komsu_koordinatlari:
            x = mevcut_x + k[0]
            y = mevcut_y + k[1]
            if 0 <= x < self.dunya_x_limiti and 0 <= y < self.dunya_y_limiti:
                c = Hucre()
                c.konum = (x, y)
                c.ebeveyn = hucre
                komsular.append(c)
        return komsular


def astar(dunya, baslangic, hedef):
    """
    A* algoritmasının uygulanması.
    dunya : Dünya nesnesinin bir örneği.
    baslangic : Başlangıç pozisyonu olarak hücre nesnesi.
    hedef  : Hedef pozisyonu olarak hücre nesnesi.

    >>> p = IzgaraDunyasi()
    >>> baslangic = Hucre()
    >>> baslangic.konum = (0,0)
    >>> hedef = Hucre()
    >>> hedef.konum = (4,4)
    >>> astar(p, baslangic, hedef)
    [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
    """
    acik_liste = []
    kapali_liste = []
    acik_liste.append(baslangic)

    while acik_liste:
        min_f = np.argmin([n.f for n in acik_liste])
        mevcut = acik_liste[min_f]
        kapali_liste.append(acik_liste.pop(min_f))
        if mevcut == hedef:
            break
        for n in dunya.komsulari_getir(mevcut):
            if n in kapali_liste:
                continue
            n.g = mevcut.g + 1
            x1, y1 = n.konum
            x2, y2 = hedef.konum
            n.h = (y2 - y1) ** 2 + (x2 - x1) ** 2
            n.f = n.h + n.g

            if any(c == n and c.f < n.f for c in acik_liste):
                continue
            acik_liste.append(n)
    yol = []
    while mevcut.ebeveyn is not None:
        yol.append(mevcut.konum)
        mevcut = mevcut.ebeveyn
    yol.append(mevcut.konum)
    return yol[::-1]


if __name__ == "__main__":
    dunya = IzgaraDunyasi()
    # Başlangıç pozisyonu ve hedef
    baslangic = Hucre()
    baslangic.konum = (0, 0)
    hedef = Hucre()
    hedef.konum = (4, 4)
    print(f"{baslangic.konum} konumundan {hedef.konum} konumuna yol")
    s = astar(dunya, baslangic, hedef)
    # Görsel nedenlerle.
    for i in s:
        dunya.dunya[i] = 1
    print(dunya.dunya)
