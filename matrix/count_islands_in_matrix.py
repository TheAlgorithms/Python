# Matris içindeki bir ada, aynı değere sahip bağlı alanlar grubudur.
# Bu kod, verilen bir matris içindeki adaların sayısını, çapraz bağlantıları da dahil ederek sayar.

class Matris:  # Grafiği uygulamak için genel sınıf
    def __init__(self, satır: int, sütun: int, grafik: list[list[bool]]) -> None:
        self.SATIR = satır
        self.SÜTUN = sütun
        self.grafik = grafik

    def güvenli_mi(self, i: int, j: int, ziyaret_edildi: list[list[bool]]) -> bool:
        return (
            0 <= i < self.SATIR
            and 0 <= j < self.SÜTUN
            and not ziyaret_edildi[i][j]
            and self.grafik[i][j]
        )

    def komşuları_kontrol_et(self, i: int, j: int, ziyaret_edildi: list[list[bool]]) -> None:
        # n. elemanın etrafındaki 8 elemanı kontrol etme
        satır_komşuları = [-1, -1, -1, 0, 0, 1, 1, 1]  # Koordinat sırası
        sütun_komşuları = [-1, 0, 1, -1, 1, -1, 0, 1]
        ziyaret_edildi[i][j] = True  # Bu hücreleri ziyaret edildi olarak işaretle
        for k in range(8):
            if self.güvenli_mi(i + satır_komşuları[k], j + sütun_komşuları[k], ziyaret_edildi):
                self.komşuları_kontrol_et(i + satır_komşuları[k], j + sütun_komşuları[k], ziyaret_edildi)

    def ada_sayısını_hesapla(self) -> int:  # Son olarak, tüm adaları say
        ziyaret_edildi = [[False for j in range(self.SÜTUN)] for i in range(self.SATIR)]
        sayac = 0
        for i in range(self.SATIR):
            for j in range(self.SÜTUN):
                if not ziyaret_edildi[i][j] and self.grafik[i][j] == 1:
                    self.komşuları_kontrol_et(i, j, ziyaret_edildi)
                    sayac += 1
        return sayac
