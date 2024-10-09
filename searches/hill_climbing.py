# https://tr.wikipedia.org/wiki/Hill_climbing
import math

#Organiser: K. Umut Araz


class AramaProblemi:
    """
    Arama problemlerini tanımlamak için bir arayüz.
    Arayüz, matematiksel bir fonksiyon örneği ile gösterilecektir.
    """

    def __init__(self, x: int, y: int, adım_boyutu: int, optimize_edilecek_fonksiyon):
        """
        Arama probleminin yapıcı metodu.

        x: mevcut arama durumunun x koordinatı.
        y: mevcut arama durumunun y koordinatı.
        adım_boyutu: komşuları ararken atılacak adımın boyutu.
        optimize_edilecek_fonksiyon: f(x, y) imzasına sahip bir fonksiyon.
        """
        self.x = x
        self.y = y
        self.adım_boyutu = adım_boyutu
        self.fonksiyon = optimize_edilecek_fonksiyon

    def puan(self) -> int:
        """
        Mevcut x ve y koordinatları ile çağrılan fonksiyonun çıktısını döner.
        >>> def test_fonksiyonu(x, y):
        ...     return x + y
        >>> AramaProblemi(0, 0, 1, test_fonksiyonu).puan()  # 0 + 0 = 0
        0
        >>> AramaProblemi(5, 7, 1, test_fonksiyonu).puan()  # 5 + 7 = 12
        12
        """
        return self.fonksiyon(self.x, self.y)

    def komşuları_getir(self):
        """
        Mevcut koordinatlara bitişik komşuların koordinatlarının listesini döner.

        Komşular:
        | 0 | 1 | 2 |
        | 3 | _ | 4 |
        | 5 | 6 | 7 |
        """
        adım_boyutu = self.adım_boyutu
        return [
            AramaProblemi(x, y, adım_boyutu, self.fonksiyon)
            for x, y in (
                (self.x - adım_boyutu, self.y - adım_boyutu),
                (self.x - adım_boyutu, self.y),
                (self.x - adım_boyutu, self.y + adım_boyutu),
                (self.x, self.y - adım_boyutu),
                (self.x, self.y + adım_boyutu),
                (self.x + adım_boyutu, self.y - adım_boyutu),
                (self.x + adım_boyutu, self.y),
                (self.x + adım_boyutu, self.y + adım_boyutu),
            )
        ]

    def __hash__(self):
        """
        Mevcut arama durumunun string temsilini hashler.
        """
        return hash(str(self))

    def __eq__(self, obj):
        """
        İki nesnenin eşit olup olmadığını kontrol eder.
        """
        if isinstance(obj, AramaProblemi):
            return hash(str(self)) == hash(str(obj))
        return False

    def __str__(self):
        """
        Mevcut arama durumunun string temsilidir.
        >>> str(AramaProblemi(0, 0, 1, None))
        'x: 0 y: 0'
        >>> str(AramaProblemi(2, 5, 1, None))
        'x: 2 y: 5'
        """
        return f"x: {self.x} y: {self.y}"


def tepe_tırmanışı(
    arama_prob,
    maksimum_bul: bool = True,
    max_x: float = math.inf,
    min_x: float = -math.inf,
    max_y: float = math.inf,
    min_y: float = -math.inf,
    görselleştirme: bool = False,
    max_iter: int = 10000,
) -> AramaProblemi:
    """
    Tepe tırmanışı algoritmasının uygulanması.
    Verilen bir durumla başlarız, tüm komşularını buluruz,
    maksimum (veya minimum) değişimi sağlayan komşuya doğru hareket ederiz.
    Çözümü iyileştirebilecek komşumuz kalmadığında dururuz.
        Argümanlar:
            arama_prob: Başlangıçtaki arama durumu.
            maksimum_bul: Eğer True ise, algoritma maksimumu bulmalı, aksi takdirde minimumu.
            max_x, min_x, max_y, min_y: x ve y'nin maksimum ve minimum sınırları.
            görselleştirme: Eğer True ise, bir matplotlib grafiği gösterilir.
            max_iter: yineleme sayısı.
        Dönüş: maksimum (veya minimum) puana sahip bir arama durumu.
    """
    mevcut_durum = arama_prob
    puanlar = []  # her yinelemedeki mevcut puanı saklamak için liste
    yinelemeler = 0
    çözüm_bulundu = False
    ziyaret_edilen = set()
    while not çözüm_bulundu and yinelemeler < max_iter:
        ziyaret_edilen.add(mevcut_durum)
        yinelemeler += 1
        mevcut_puan = mevcut_durum.puan()
        puanlar.append(mevcut_puan)
        komşular = mevcut_durum.komşuları_getir()
        max_değişim = -math.inf
        min_değişim = math.inf
        sonraki_durum = None  # bir sonraki en iyi komşuyu tutmak için
        for komşu in komşular:
            if komşu in ziyaret_edilen:
                continue  # aynı durumu tekrar ziyaret etmek istemiyoruz
            if (
                komşu.x > max_x
                or komşu.x < min_x
                or komşu.y > max_y
                or komşu.y < min_y
            ):
                continue  # komşu sınırlarımızın dışında
            değişim = komşu.puan() - mevcut_puan
            if maksimum_bul:  # maksimum bulma
                # en büyük yükseliş yönüne gitme
                if değişim > max_değişim and değişim > 0:
                    max_değişim = değişim
                    sonraki_durum = komşu
            elif değişim < min_değişim and değişim < 0:  # minimum bulma
                # en büyük düşüş yönüne gitme
                min_değişim = değişim
                sonraki_durum = komşu
        if sonraki_durum is not None:
            # mevcut durumu iyileştiren en az bir komşu bulduk
            mevcut_durum = sonraki_durum
        else:
            # çözümü iyileştiren komşu kalmadığı için aramayı durduruyoruz
            çözüm_bulundu = True

    if görselleştirme:
        from matplotlib import pyplot as plt

        plt.plot(range(yinelemeler), puanlar)
        plt.xlabel("Yinelemeler")
        plt.ylabel("Fonksiyon değerleri")
        plt.show()

    return mevcut_durum


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    def test_f1(x, y):
        return (x**2) + (y**2)

    # Problemi başlangıç koordinatları (3, 4) ile başlatma
    prob = AramaProblemi(x=3, y=4, adım_boyutu=1, optimize_edilecek_fonksiyon=test_f1)
    yerel_min = tepe_tırmanışı(prob, maksimum_bul=False)
    print(
        "f(x, y) = x^2 + y^2 için tepe tırmanışı ile bulunan minimum puan: "
        f"{yerel_min.puan()}"
    )

    # Problemi başlangıç koordinatları (12, 47) ile başlatma
    prob = AramaProblemi(x=12, y=47, adım_boyutu=1, optimize_edilecek_fonksiyon=test_f1)
    yerel_min = tepe_tırmanışı(
        prob, maksimum_bul=False, max_x=100, min_x=5, max_y=50, min_y=-5, görselleştirme=True
    )
    print(
        "f(x, y) = x^2 + y^2 için 100 > x > 5 ve 50 > y > -5 aralığında "
        f"tepe tırmanışı ile bulunan minimum puan: {yerel_min.puan()}"
    )

    def test_f2(x, y):
        return (3 * x**2) - (6 * y)

    prob = AramaProblemi(x=3, y=4, adım_boyutu=1, optimize_edilecek_fonksiyon=test_f1)
    yerel_min = tepe_tırmanışı(prob, maksimum_bul=True)
    print(
        "f(x, y) = x^2 + y^2 için tepe tırmanışı ile bulunan maksimum puan: "
        f"{yerel_min.puan()}"
    )
