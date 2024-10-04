"""
Temel bir regresyon karar ağacının uygulanması.
Girdi veri seti: Girdi veri seti sürekli etiketlere sahip tek boyutlu olmalıdır.
Çıktı: Karar ağacı, gerçek bir sayı girdisini gerçek bir sayı çıktısına eşler.
"""

import numpy as np


class KararAgaci:
    def __init__(self, derinlik=5, min_yaprak_boyutu=5):
        self.derinlik = derinlik
        self.karar_siniri = 0
        self.sol = None
        self.sag = None
        self.min_yaprak_boyutu = min_yaprak_boyutu
        self.tahmin = None

    def ortalama_kare_hatasi(self, etiketler, tahmin):
        """
        ortalama_kare_hatasi:
        @param etiketler: tek boyutlu bir numpy dizisi
        @param tahmin: bir kayan nokta değeri
        dönüş değeri: ortalama_kare_hatasi, tahminin etiketleri tahmin etmek için
            kullanılması durumunda hatayı hesaplar
        >>> tester = KararAgaci()
        >>> test_etiketler = np.array([1,2,3,4,5,6,7,8,9,10])
        >>> test_tahmin = float(6)
        >>> bool(tester.ortalama_kare_hatasi(test_etiketler, test_tahmin) == (
        ...     TestKararAgaci.helper_ortalama_kare_hatasi_test(test_etiketler,
        ...         test_tahmin)))
        True
        >>> test_etiketler = np.array([1,2,3])
        >>> test_tahmin = float(2)
        >>> bool(tester.ortalama_kare_hatasi(test_etiketler, test_tahmin) == (
        ...     TestKararAgaci.helper_ortalama_kare_hatasi_test(test_etiketler,
        ...         test_tahmin)))
        True
        """
        if etiketler.ndim != 1:
            print("Hata: Girdi etiketleri tek boyutlu olmalıdır")

        return np.mean((etiketler - tahmin) ** 2)

    def egit(self, x, y):
        """
        egit:
        @param x: tek boyutlu bir numpy dizisi
        @param y: tek boyutlu bir numpy dizisi.
        y'nin içeriği, X değerlerine karşılık gelen etiketlerdir

        egit() bir dönüş değeri yoktur

        Örnekler:
        1. x ve y aynı uzunlukta ve tek boyutlu olduğunda eğitmeye çalışın (Hata yok)
        >>> dt = KararAgaci()
        >>> dt.egit(np.array([10,20,30,40,50]),np.array([0,0,0,1,1]))

        2. x 2 boyutlu olduğunda eğitmeye çalışın
        >>> dt = KararAgaci()
        >>> dt.egit(np.array([[1,2,3,4,5],[1,2,3,4,5]]),np.array([0,0,0,1,1]))
        Traceback (most recent call last):
            ...
        ValueError: Girdi veri seti tek boyutlu olmalıdır

        3. x ve y aynı uzunlukta olmadığında eğitmeye çalışın
        >>> dt = KararAgaci()
        >>> dt.egit(np.array([1,2,3,4,5]),np.array([[0,0,0,1,1],[0,0,0,1,1]]))
        Traceback (most recent call last):
            ...
        ValueError: x ve y farklı uzunluklarda

        4. x ve y aynı uzunlukta ancak farklı boyutlarda olduğunda eğitmeye çalışın
        >>> dt = KararAgaci()
        >>> dt.egit(np.array([1,2,3,4,5]),np.array([[1],[2],[3],[4],[5]]))
        Traceback (most recent call last):
            ...
        ValueError: Veri seti etiketleri tek boyutlu olmalıdır

        Bu bölüm, girdilerin boyutsallık kısıtlamalarımıza uygun olup olmadığını kontrol eder
        """
        if x.ndim != 1:
            raise ValueError("Girdi veri seti tek boyutlu olmalıdır")
        if len(x) != len(y):
            raise ValueError("x ve y farklı uzunluklarda")
        if y.ndim != 1:
            raise ValueError("Veri seti etiketleri tek boyutlu olmalıdır")

        if len(x) < 2 * self.min_yaprak_boyutu:
            self.tahmin = np.mean(y)
            return

        if self.derinlik == 1:
            self.tahmin = np.mean(y)
            return

        en_iyi_bolme = 0
        min_hata = self.ortalama_kare_hatasi(x, np.mean(y)) * 2

        """
        karar ağacı için tüm olası bölmeleri döngüye al. en iyi bölmeyi bul.
        tüm dizi için hatadan daha az olan 2 * hata yoksa
        o zaman veri seti bölünmez ve tüm dizi için ortalama
        tahmin olarak kullanılır
        """
        for i in range(len(x)):
            if len(x[:i]) < self.min_yaprak_boyutu:  # noqa: SIM114
                continue
            elif len(x[i:]) < self.min_yaprak_boyutu:
                continue
            else:
                hata_sol = self.ortalama_kare_hatasi(x[:i], np.mean(y[:i]))
                hata_sag = self.ortalama_kare_hatasi(x[i:], np.mean(y[i:]))
                hata = hata_sol + hata_sag
                if hata < min_hata:
                    en_iyi_bolme = i
                    min_hata = hata

        if en_iyi_bolme != 0:
            sol_x = x[:en_iyi_bolme]
            sol_y = y[:en_iyi_bolme]
            sag_x = x[en_iyi_bolme:]
            sag_y = y[en_iyi_bolme:]

            self.karar_siniri = x[en_iyi_bolme]
            self.sol = KararAgaci(
                derinlik=self.derinlik - 1, min_yaprak_boyutu=self.min_yaprak_boyutu
            )
            self.sag = KararAgaci(
                derinlik=self.derinlik - 1, min_yaprak_boyutu=self.min_yaprak_boyutu
            )
            self.sol.egit(sol_x, sol_y)
            self.sag.egit(sag_x, sag_y)
        else:
            self.tahmin = np.mean(y)

        return

    def tahmin_et(self, x):
        """
        tahmin_et:
        @param x: etiketini tahmin etmek için bir kayan nokta değeri
        tahmin fonksiyonu, ağacın karar sınırına göre uygun alt ağaçların tahmin fonksiyonunu
        yineleyerek çağırarak çalışır
        """
        if self.tahmin is not None:
            return self.tahmin
        elif self.sol or self.sag is not None:
            if x >= self.karar_siniri:
                return self.sag.tahmin_et(x)
            else:
                return self.sol.tahmin_et(x)
        else:
            print("Hata: Karar ağacı henüz eğitilmedi")
            return None


class TestKararAgaci:
    """Karar Ağacı test sınıfı"""

    @staticmethod
    def helper_ortalama_kare_hatasi_test(etiketler, tahmin):
        """
        helper_ortalama_kare_hatasi_test:
        @param etiketler: tek boyutlu bir numpy dizisi
        @param tahmin: bir kayan nokta değeri
        dönüş değeri: helper_ortalama_kare_hatasi_test, ortalama kare hatasını hesaplar
        """
        kare_hata_toplam = float(0)
        for etiket in etiketler:
            kare_hata_toplam += (etiket - tahmin) ** 2

        return float(kare_hata_toplam / etiketler.size)


def main():
    """
    Bu gösterimde, numpy'daki sin fonksiyonundan bir örnek veri seti oluşturuyoruz.
    Daha sonra bu veri seti üzerinde bir karar ağacı eğitiyoruz ve karar ağacını kullanarak
    10 farklı test değerinin etiketini tahmin ediyoruz. Daha sonra bu test üzerindeki ortalama
    kare hata gösterilir.
    """
    x = np.arange(-1.0, 1.0, 0.005)
    y = np.sin(x)

    agac = KararAgaci(derinlik=10, min_yaprak_boyutu=10)
    agac.egit(x, y)

    rng = np.random.default_rng()
    test_durumlari = (rng.random(10) * 2) - 1
    tahminler = np.array([agac.tahmin_et(x) for x in test_durumlari])
    ortalama_hata = np.mean((tahminler - test_durumlari) ** 2)

    print("Test değerleri: " + str(test_durumlari))
    print("Tahminler: " + str(tahminler))
    print("Ortalama hata: " + str(ortalama_hata))


if __name__ == "__main__":
    main()
    import doctest

    doctest.testmod(name="ortalama_kare_hatasi", verbose=True)
