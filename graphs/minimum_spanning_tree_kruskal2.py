from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")

#Produced By K. Umut Araz


class AyrıkKümeAğaçDüğümü(Generic[T]):
    # Ayrık Küme Düğümü, ebeveyn ve rütbeyi saklar
    def __init__(self, veri: T) -> None:
        self.veri = veri
        self.ebeveyn = self
        self.rütbe = 0


class AyrıkKümeAğacı(Generic[T]):
    # Ayrık Küme Veri Yapısı
    def __init__(self) -> None:
        # düğüm adından düğüm nesnesine harita
        self.harita: dict[T, AyrıkKümeAğaçDüğümü[T]] = {}

    def küme_oluştur(self, veri: T) -> None:
        # x'i üye olarak içeren yeni bir küme oluştur
        self.harita[veri] = AyrıkKümeAğaçDüğümü(veri)

    def küme_bul(self, veri: T) -> AyrıkKümeAğaçDüğümü[T]:
        # x'in ait olduğu kümeyi bul (yol sıkıştırma ile)
        eleman_ref = self.harita[veri]
        if eleman_ref != eleman_ref.ebeveyn:
            eleman_ref.ebeveyn = self.küme_bul(eleman_ref.ebeveyn.veri)
        return eleman_ref.ebeveyn

    def bağla(
        self, düğüm1: AyrıkKümeAğaçDüğümü[T], düğüm2: AyrıkKümeAğaçDüğümü[T]
    ) -> None:
        # birleşim işlemi için yardımcı fonksiyon
        if düğüm1.rütbe > düğüm2.rütbe:
            düğüm2.ebeveyn = düğüm1
        else:
            düğüm1.ebeveyn = düğüm2
            if düğüm1.rütbe == düğüm2.rütbe:
                düğüm2.rütbe += 1

    def birleştir(self, veri1: T, veri2: T) -> None:
        # 2 ayrık kümeyi birleştir
        self.bağla(self.küme_bul(veri1), self.küme_bul(veri2))


class AğırlıklıYönsüzGrafik(Generic[T]):
    def __init__(self) -> None:
        # bağlantılar: düğümden komşu düğümlere (ağırlıklarla birlikte) harita
        self.bağlantılar: dict[T, dict[T, int]] = {}

    def düğüm_ekle(self, düğüm: T) -> None:
        # düğüm grafikte yoksa ekle
        if düğüm not in self.bağlantılar:
            self.bağlantılar[düğüm] = {}

    def kenar_ekle(self, düğüm1: T, düğüm2: T, ağırlık: int) -> None:
        # verilen ağırlıkla bir kenar ekle
        self.düğüm_ekle(düğüm1)
        self.düğüm_ekle(düğüm2)
        self.bağlantılar[düğüm1][düğüm2] = ağırlık
        self.bağlantılar[düğüm2][düğüm1] = ağırlık

    def kruskal(self) -> AğırlıklıYönsüzGrafik[T]:
        # Kruskal Algoritması ile Minimum Yayılım Ağacı (MST) oluşturma
        """
        Detaylar: https://tr.wikipedia.org/wiki/Kruskal_algoritmas%C4%B1

        Örnek:
        >>> g1 = AğırlıklıYönsüzGrafik[int]()
        >>> g1.kenar_ekle(1, 2, 1)
        >>> g1.kenar_ekle(2, 3, 2)
        >>> g1.kenar_ekle(3, 4, 1)
        >>> g1.kenar_ekle(3, 5, 100) # MST'de kaldırıldı
        >>> g1.kenar_ekle(4, 5, 5)
        >>> assert 5 in g1.bağlantılar[3]
        >>> mst = g1.kruskal()
        >>> assert 5 not in mst.bağlantılar[3]

        >>> g2 = AğırlıklıYönsüzGrafik[str]()
        >>> g2.kenar_ekle('A', 'B', 1)
        >>> g2.kenar_ekle('B', 'C', 2)
        >>> g2.kenar_ekle('C', 'D', 1)
        >>> g2.kenar_ekle('C', 'E', 100) # MST'de kaldırıldı
        >>> g2.kenar_ekle('D', 'E', 5)
        >>> assert 'E' in g2.bağlantılar["C"]
        >>> mst = g2.kruskal()
        >>> assert 'E' not in mst.bağlantılar['C']
        """

        # kenarları ağırlıklarına göre artan sırayla alma
        kenarlar = []
        görülen = set()
        for başlangıç in self.bağlantılar:
            for bitiş in self.bağlantılar[başlangıç]:
                if (başlangıç, bitiş) not in görülen:
                    görülen.add((bitiş, başlangıç))
                    kenarlar.append((başlangıç, bitiş, self.bağlantılar[başlangıç][bitiş]))
        kenarlar.sort(key=lambda x: x[2])

        # ayrık küme oluşturma
        ayrık_küme = AyrıkKümeAğacı[T]()
        for düğüm in self.bağlantılar:
            ayrık_küme.küme_oluştur(düğüm)

        # MST oluşturma
        kenar_sayısı = 0
        indeks = 0
        grafik = AğırlıklıYönsüzGrafik[T]()
        while kenar_sayısı < len(self.bağlantılar) - 1:
            u, v, w = kenarlar[indeks]
            indeks += 1
            ebeveyn_u = ayrık_küme.küme_bul(u)
            ebeveyn_v = ayrık_küme.küme_bul(v)
            if ebeveyn_u != ebeveyn_v:
                kenar_sayısı += 1
                grafik.kenar_ekle(u, v, w)
                ayrık_küme.birleştir(u, v)
        return grafik
