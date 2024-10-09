class AkışAğı:
    def __init__(self, grafik, kaynaklar, hedefler):
        self.kaynak_indeksi = None
        self.hedef_indeksi = None
        self.grafik = grafik

        self._grafiği_normalize_et(kaynaklar, hedefler)
        self.düğüm_sayısı = len(grafik)
        self.maksimum_akış_algoritması = None

    # sadece bir kaynak ve bir hedef yap
    def _grafiği_normalize_et(self, kaynaklar, hedefler):
        if isinstance(kaynaklar, int):
            kaynaklar = [kaynaklar]
        if isinstance(hedefler, int):
            hedefler = [hedefler]

        if len(kaynaklar) == 0 or len(hedefler) == 0:
            return

        self.kaynak_indeksi = kaynaklar[0]
        self.hedef_indeksi = hedefler[0]

        # birden fazla kaynak veya hedef varsa sahte düğüm oluştur
        if len(kaynaklar) > 1 or len(hedefler) > 1:
            maksimum_girdi_akışı = 0
            for i in kaynaklar:
                maksimum_girdi_akışı += sum(self.grafik[i])

            boyut = len(self.grafik) + 1
            for oda in self.grafik:
                oda.insert(0, 0)
            self.grafik.insert(0, [0] * boyut)
            for i in kaynaklar:
                self.grafik[0][i + 1] = maksimum_girdi_akışı
            self.kaynak_indeksi = 0

            boyut = len(self.grafik) + 1
            for oda in self.grafik:
                oda.append(0)
            self.grafik.append([0] * boyut)
            for i in hedefler:
                self.grafik[i + 1][boyut - 1] = maksimum_girdi_akışı
            self.hedef_indeksi = boyut - 1

    def maksimum_akışı_bul(self):
        if self.maksimum_akış_algoritması is None:
            raise Exception("Önce maksimum akış algoritmasını ayarlamalısınız.")
        if self.kaynak_indeksi is None or self.hedef_indeksi is None:
            return 0

        self.maksimum_akış_algoritması.çalıştır()
        return self.maksimum_akış_algoritması.maksimum_akışı_al()

    def maksimum_akış_algoritmasını_ayarla(self, algoritma):
        self.maksimum_akış_algoritması = algoritma(self)


class AkışAğıAlgoritmaYürütücüsü:
    def __init__(self, akış_ağı):
        self.akış_ağı = akış_ağı
        self.düğüm_sayısı = akış_ağı.düğüm_sayısı
        self.kaynak_indeksi = akış_ağı.kaynak_indeksi
        self.hedef_indeksi = akış_ağı.hedef_indeksi
        # bu sadece bir referanstır, bu yüzden algoritmalarınızda değiştirmemelisiniz,
        # bunu yapmadan önce derin kopya kullanın
        self.grafik = akış_ağı.grafik
        self.çalıştırıldı = False

    def çalıştır(self):
        if not self.çalıştırıldı:
            self._algoritma()
            self.çalıştırıldı = True

    # Bunu geçersiz kılmalısınız
    def _algoritma(self):
        pass


class MaksimumAkışAlgoritmaYürütücüsü(AkışAğıAlgoritmaYürütücüsü):
    def __init__(self, akış_ağı):
        super().__init__(akış_ağı)
        # sonucu kaydetmek için bunu kullanın
        self.maksimum_akış = -1

    def maksimum_akışı_al(self):
        if not self.çalıştırıldı:
            raise Exception("Algoritmayı çalıştırmadan önce sonucunu kullanmamalısınız!")

        return self.maksimum_akış


class PushRelabelYürütücüsü(MaksimumAkışAlgoritmaYürütücüsü):
    def __init__(self, akış_ağı):
        super().__init__(akış_ağı)

        self.önakış = [[0] * self.düğüm_sayısı for i in range(self.düğüm_sayısı)]

        self.yükseklikler = [0] * self.düğüm_sayısı
        self.artıklar = [0] * self.düğüm_sayısı

    def _algoritma(self):
        self.yükseklikler[self.kaynak_indeksi] = self.düğüm_sayısı

        # grafiğe biraz madde it
        for sonraki_düğüm_indeksi, bant_genişliği in enumerate(self.grafik[self.kaynak_indeksi]):
            self.önakış[self.kaynak_indeksi][sonraki_düğüm_indeksi] += bant_genişliği
            self.önakış[sonraki_düğüm_indeksi][self.kaynak_indeksi] -= bant_genişliği
            self.artıklar[sonraki_düğüm_indeksi] += bant_genişliği

        # Relabel-to-front seçim kuralı
        düğüm_listesi = [
            i
            for i in range(self.düğüm_sayısı)
            if i not in {self.kaynak_indeksi, self.hedef_indeksi}
        ]

        # liste boyunca hareket et
        i = 0
        while i < len(düğüm_listesi):
            düğüm_indeksi = düğüm_listesi[i]
            önceki_yükseklik = self.yükseklikler[düğüm_indeksi]
            self.düğümü_işle(düğüm_indeksi)
            if self.yükseklikler[düğüm_indeksi] > önceki_yükseklik:
                # eğer yeniden etiketlendiyse, elemanları değiştir
                # ve 0 indeksinden başla
                düğüm_listesi.insert(0, düğüm_listesi.pop(i))
                i = 0
            else:
                i += 1

        self.maksimum_akış = sum(self.önakış[self.kaynak_indeksi])

    def düğümü_işle(self, düğüm_indeksi):
        while self.artıklar[düğüm_indeksi] > 0:
            for komşu_indeksi in range(self.düğüm_sayısı):
                # eğer komşuysa ve mevcut düğüm daha yüksekse
                if (
                    self.grafik[düğüm_indeksi][komşu_indeksi]
                    - self.önakış[düğüm_indeksi][komşu_indeksi]
                    > 0
                    and self.yükseklikler[düğüm_indeksi] > self.yükseklikler[komşu_indeksi]
                ):
                    self.it(düğüm_indeksi, komşu_indeksi)

            self.yeniden_etiketle(düğüm_indeksi)

    def it(self, kaynak_indeksi, hedef_indeksi):
        önakış_delta = min(
            self.artıklar[kaynak_indeksi],
            self.grafik[kaynak_indeksi][hedef_indeksi] - self.önakış[kaynak_indeksi][hedef_indeksi]
        )
        self.önakış[kaynak_indeksi][hedef_indeksi] += önakış_delta
        self.önakış[hedef_indeksi][kaynak_indeksi] -= önakış_delta
        self.artıklar[kaynak_indeksi] -= önakış_delta
        self.artıklar[hedef_indeksi] += önakış_delta

    def yeniden_etiketle(self, düğüm_indeksi):
        min_yükseklik = None
        for hedef_indeksi in range(self.düğüm_sayısı):
            if (
                self.grafik[düğüm_indeksi][hedef_indeksi]
                - self.önakış[düğüm_indeksi][hedef_indeksi]
                > 0
            ) and (min_yükseklik is None or self.yükseklikler[hedef_indeksi] < min_yükseklik):
                min_yükseklik = self.yükseklikler[hedef_indeksi]

        if min_yükseklik is not None:
            self.yükseklikler[düğüm_indeksi] = min_yükseklik + 1


if __name__ == "__main__":
    girişler = [0]
    çıkışlar = [3]
    # grafik = [
    #     [0, 0, 4, 6, 0, 0],
    #     [0, 0, 5, 2, 0, 0],
    #     [0, 0, 0, 0, 4, 4],
    #     [0, 0, 0, 0, 6, 6],
    #     [0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0],
    # ]
    grafik = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]

    # ağımızı hazırlayalım
    akış_ağı = AkışAğı(grafik, girişler, çıkışlar)
    # algoritmayı ayarla
    akış_ağı.maksimum_akış_algoritmasını_ayarla(PushRelabelYürütücüsü)
    # ve hesapla
    maksimum_akış = akış_ağı.maksimum_akışı_bul()

    print(f"maksimum akış {maksimum_akış}")
