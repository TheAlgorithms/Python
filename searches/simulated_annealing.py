# https://tr.wikipedia.org/wiki/Simulated_annealing
import math
import random
from typing import Any

from .hill_climbing import SearchProblem

"""Organiser: K. Umut Araz"""


def simule_annealing(
    arama_prob: SearchProblem,
    maksimum_bul: bool = True,
    max_x: float = math.inf,
    min_x: float = -math.inf,
    max_y: float = math.inf,
    min_y: float = -math.inf,
    gorselleme: bool = False,
    baslangic_sicakligi: float = 100,
    azalma_orani: float = 0.01,
    esik_sicaklik: float = 1,
) -> Any:
    """
    Simüle edilmiş tavlama algoritmasının uygulanması. Belirli bir durumla başlıyoruz,
    tüm komşularını buluyoruz. Rastgele bir komşu seçiyoruz, eğer bu komşu çözümü
    iyileştiriyorsa o yöne hareket ediyoruz, eğer iyileştirmiyorsa 0 ile 1 arasında
    rastgele bir sayı üretiyoruz, eğer bu sayı belirli bir aralıkta (sicaklık kullanılarak
    hesaplanan) ise o yöne hareket ediyoruz, aksi takdirde başka bir komşu rastgele
    seçiliyor ve süreç tekrarlanıyor.

    Args:
        arama_prob: Başlangıçtaki arama durumu.
        maksimum_bul: Eğer True ise, algoritma maksimumu bulmalı, aksi takdirde minimumu.
        max_x, min_x, max_y, min_y: x ve y'nin maksimum ve minimum sınırları.
        gorselleme: Eğer True ise, bir matplotlib grafiği gösterilir.
        baslangic_sicakligi: Program başladığında sistemin başlangıç sıcaklığı.
        azalma_orani: Her iterasyonda sıcaklığın ne kadar azaldığı.
        esik_sicaklik: Aramayı sonlandırdığımız sıcaklık eşiği.
    Returns: Maksimum (veya minimum) skora sahip bir arama durumu.
    """
    arama_bitti = False
    mevcut_durum = arama_prob
    mevcut_sicaklik = baslangic_sicakligi
    skorlar = []
    iterasyonlar = 0
    en_iyi_durum = None

    while not arama_bitti:
        mevcut_skor = mevcut_durum.score()
        if en_iyi_durum is None or mevcut_skor > en_iyi_durum.score():
            en_iyi_durum = mevcut_durum
        skorlar.append(mevcut_skor)
        iterasyonlar += 1
        sonraki_durum = None
        komsular = mevcut_durum.get_neighbors()
        while (
            sonraki_durum is None and komsular
        ):  # Hareket edebileceğimiz bir komşu bulana kadar
            index = random.randint(0, len(komsular) - 1)  # Rastgele bir komşu seçiyoruz
            secilen_komsu = komsular.pop(index)
            degisim = secilen_komsu.score() - mevcut_skor

            if (
                secilen_komsu.x > max_x
                or secilen_komsu.x < min_x
                or secilen_komsu.y > max_y
                or secilen_komsu.y < min_y
            ):
                continue  # Komşu sınırlarımızın dışında

            if not maksimum_bul:
                degisim = degisim * -1  # Minimum bulmaya çalışıyorsak
            if degisim > 0:  # Çözümü iyileştiriyorsa
                sonraki_durum = secilen_komsu
            else:
                olasılık = (math.e) ** (
                    degisim / mevcut_sicaklik
                )  # Olasılık üretim fonksiyonu
                if random.random() < olasılık:  # Olasılık içinde rastgele sayı
                    sonraki_durum = secilen_komsu
        mevcut_sicaklik = mevcut_sicaklik - (mevcut_sicaklik * azalma_orani)

        if mevcut_sicaklik < esik_sicaklik or sonraki_durum is None:
            # Sıcaklık eşikten düşük, ya da uygun bir komşu bulamadık
            arama_bitti = True
        else:
            mevcut_durum = sonraki_durum

    if gorselleme:
        from matplotlib import pyplot as plt

        plt.plot(range(iterasyonlar), skorlar)
        plt.xlabel("Iterasyonlar")
        plt.ylabel("Fonksiyon Değerleri")
        plt.show()
    return en_iyi_durum


if __name__ == "__main__":

    def test_f1(x, y):
        return (x**2) + (y**2)

    # Problemi başlangıç koordinatları (12, 47) ile başlatma
    prob = SearchProblem(x=12, y=47, step_size=1, function_to_optimize=test_f1)
    yerel_min = simule_annealing(
        prob, maksimum_bul=False, max_x=100, min_x=5, max_y=50, min_y=-5, gorselleme=True
    )
    print(
        "f(x, y) = x^2 + y^2 için minimum skor, 100 > x > 5 "
        f"ve 50 > y > -5 aralığında, tepe tırmanışı ile bulundu: {yerel_min.score()}"
    )

    # Problemi başlangıç koordinatları (12, 47) ile başlatma
    prob = SearchProblem(x=12, y=47, step_size=1, function_to_optimize=test_f1)
    yerel_min = simule_annealing(
        prob, maksimum_bul=True, max_x=100, min_x=5, max_y=50, min_y=-5, gorselleme=True
    )
    print(
        "f(x, y) = x^2 + y^2 için maksimum skor, 100 > x > 5 "
        f"ve 50 > y > -5 aralığında, tepe tırmanışı ile bulundu: {yerel_min.score()}"
    )

    def test_f2(x, y):
        return (3 * x**2) - (6 * y)

    prob = SearchProblem(x=3, y=4, step_size=1, function_to_optimize=test_f1)
    yerel_min = simule_annealing(prob, maksimum_bul=False, gorselleme=True)
    print(
        "f(x, y) = 3*x^2 - 6*y için minimum skor, tepe tırmanışı ile bulundu: "
        f"{yerel_min.score()}"
    )

    prob = SearchProblem(x=3, y=4, step_size=1, function_to_optimize=test_f1)
    yerel_min = simule_annealing(prob, maksimum_bul=True, gorselleme=True)
    print(
        "f(x, y) = 3*x^2 - 6*y için maksimum skor, tepe tırmanışı ile bulundu: "
        f"{yerel_min.score()}"
    )
