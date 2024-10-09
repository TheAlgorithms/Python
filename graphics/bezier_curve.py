# https://en.wikipedia.org/wiki/B%C3%A9zier_curve
# https://www.tutorialspoint.com/computer_graphics/computer_graphics_curves.htm
from __future__ import annotations

from scipy.special import comb


class BezierEğrisi:
    """
    Bezier eğrisi, bir dizi kontrol noktasının ağırlıklı toplamıdır.
    Verilen bir dizi kontrol noktasından Bezier eğrileri oluştur.
    Bu uygulama yalnızca xy düzlemindeki 2d koordinatlar için çalışır.
    """

    def __init__(self, nokta_listesi: list[tuple[float, float]]):
        """
        nokta_listesi: Bezier eğrisinin davranışını (şeklini) kontrol eden xy düzlemindeki kontrol noktaları.
        """
        self.nokta_listesi = nokta_listesi
        # Derece, eğrinin esnekliğini belirler.
        # Derece = 1, düz bir çizgi oluşturur.
        self.derece = len(nokta_listesi) - 1

    def temel_fonksiyon(self, t: float) -> list[float]:
        """
        Temel fonksiyon, her kontrol noktasının t anındaki ağırlığını belirler.
            t: eğrinin temelini değerlendirmek için 0 ile 1 arasında (dahil) bir zaman değeri.
        t anındaki temel fonksiyonun x, y değerlerini döndürür

        >>> eğri = BezierEğrisi([(1,1), (1,2)])
        >>> [float(x) for x in eğri.temel_fonksiyon(0)]
        [1.0, 0.0]
        >>> [float(x) for x in eğri.temel_fonksiyon(1)]
        [0.0, 1.0]
        """
        assert 0 <= t <= 1, "Zaman t, 0 ile 1 arasında olmalıdır."
        çıktı_değerleri: list[float] = []
        for i in range(len(self.nokta_listesi)):
            # her i için temel fonksiyon
            çıktı_değerleri.append(
                comb(self.derece, i) * ((1 - t) ** (self.derece - i)) * (t**i)
            )
        # geçerli bir Bezier eğrisi üretmesi için temel toplamı 1 olmalıdır.
        assert round(sum(çıktı_değerleri), 5) == 1
        return çıktı_değerleri

    def bezier_eğrisi_fonksiyonu(self, t: float) -> tuple[float, float]:
        """
        Bezier eğrisinin t anındaki değerlerini üretmek için fonksiyon.
            t: Bezier fonksiyonunu değerlendirmek için t zaman değeri
        Bezier eğrisinin t anındaki x, y koordinatlarını döndürür.
            Eğrinin ilk noktası t = 0 olduğunda.
            Eğrinin son noktası t = 1 olduğunda.

        >>> eğri = BezierEğrisi([(1,1), (1,2)])
        >>> tuple(float(x) for x in eğri.bezier_eğrisi_fonksiyonu(0))
        (1.0, 1.0)
        >>> tuple(float(x) for x in eğri.bezier_eğrisi_fonksiyonu(1))
        (1.0, 2.0)
        """

        assert 0 <= t <= 1, "Zaman t, 0 ile 1 arasında olmalıdır."

        temel_fonksiyon = self.temel_fonksiyon(t)
        x = 0.0
        y = 0.0
        for i in range(len(self.nokta_listesi)):
            # Tüm noktalar için, i'inci temel fonksiyon ve i'inci noktanın çarpımını topla.
            x += temel_fonksiyon[i] * self.nokta_listesi[i][0]
            y += temel_fonksiyon[i] * self.nokta_listesi[i][1]
        return (x, y)

    def eğriyi_çiz(self, adım_boyutu: float = 0.01):
        """
        Matplotlib çizim yeteneklerini kullanarak Bezier eğrisini çizer.
            adım_boyutu: Bezier eğrisini değerlendirmek için adım(lar)ı tanımlar.
            Adım boyutu ne kadar küçük olursa, üretilen eğri o kadar ince olur.
        """
        from matplotlib import pyplot as plt

        çizilecek_x: list[float] = []  # çizilecek noktaların x koordinatları
        çizilecek_y: list[float] = []  # çizilecek noktaların y koordinatları

        t = 0.0
        while t <= 1:
            değer = self.bezier_eğrisi_fonksiyonu(t)
            çizilecek_x.append(değer[0])
            çizilecek_y.append(değer[1])
            t += adım_boyutu

        x = [i[0] for i in self.nokta_listesi]
        y = [i[1] for i in self.nokta_listesi]

        plt.plot(
            çizilecek_x,
            çizilecek_y,
            color="blue",
            label="Derece " + str(self.derece) + " Eğrisi",
        )
        plt.scatter(x, y, color="red", label="Kontrol Noktaları")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    BezierEğrisi([(1, 2), (3, 5)]).eğriyi_çiz()  # derece 1
    BezierEğrisi([(0, 0), (5, 5), (5, 0)]).eğriyi_çiz()  # derece 2
    BezierEğrisi([(0, 0), (5, 5), (5, 0), (2.5, -2.5)]).eğriyi_çiz()  # derece 3
