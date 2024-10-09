"""
Mandelbrot kümesi, "z_(n+1) = z_n * z_n + c" serisinin
dağılmadığı, yani sınırlı kaldığı karmaşık sayılar "c" kümesidir. Bu nedenle,
"z_0 = 0" ile başlayıp iterasyonu tekrar tekrar uyguladığınızda, "z_n" nin
mutlak değeri tüm "n > 0" için sınırlı kalırsa, bir karmaşık sayı "c" Mandelbrot
kümesinin bir üyesidir. Karmaşık sayılar "a + b*i" olarak yazılabilir: "a" gerçek
bileşendir ve genellikle x ekseninde çizilir, "b*i" ise sanal bileşendir ve genellikle
y ekseninde çizilir. Mandelbrot kümesinin çoğu görselleştirmesi, kümenin dışındaki
sayıların seride kaç adım sonra dağıldığını göstermek için bir renk kodlaması kullanır.
Mandelbrot kümesinin görüntüleri, artan büyütmelerde giderek daha ince tekrarlayan
detayları ortaya çıkaran karmaşık ve sonsuz derecede karmaşık bir sınır sergiler,
bu da Mandelbrot kümesinin sınırını bir fraktal eğri yapar.
(açıklama https://en.wikipedia.org/wiki/Mandelbrot_set adresinden uyarlanmıştır)
(ayrıca bkz. https://en.wikipedia.org/wiki/Plotting_algorithms_for_the_Mandelbrot_set )
"""

import colorsys
from PIL import Image


def uzaklik_hesapla(x: float, y: float, max_adim: int) -> float:
    """
    Bu x-y çifti tarafından oluşturulan karmaşık sayının dağıldığı
    göreceli mesafeyi (= adım/max_adim) döndürür. Mandelbrot kümesinin
    üyeleri dağılmaz, bu nedenle mesafeleri 1'dir.

    >>> uzaklik_hesapla(0, 0, 50)
    1.0
    >>> uzaklik_hesapla(0.5, 0.5, 50)
    0.061224489795918366
    >>> uzaklik_hesapla(2, 0, 50)
    0.0
    """
    a = x
    b = y
    for adim in range(max_adim):
        a_yeni = a * a - b * b + x
        b = 2 * a * b + y
        a = a_yeni

        # dağılım, mutlak değeri 4'ten büyük olan tüm karmaşık sayılar için gerçekleşir
        if a * a + b * b > 4:
            break
    return adim / (max_adim - 1)


def siyah_beyaz_rgb(uzaklik: float) -> tuple:
    """
    Göreceli mesafeyi göz ardı eden siyah-beyaz renk kodlaması. Mandelbrot
    kümesi siyahtır, diğer her şey beyazdır.

    >>> siyah_beyaz_rgb(0)
    (255, 255, 255)
    >>> siyah_beyaz_rgb(0.5)
    (255, 255, 255)
    >>> siyah_beyaz_rgb(1)
    (0, 0, 0)
    """
    if uzaklik == 1:
        return (0, 0, 0)
    else:
        return (255, 255, 255)


def renkli_rgb(uzaklik: float) -> tuple:
    """
    Göreceli mesafeyi dikkate alan renk kodlaması. Mandelbrot kümesi siyahtır.

    >>> renkli_rgb(0)
    (255, 0, 0)
    >>> renkli_rgb(0.5)
    (0, 255, 255)
    >>> renkli_rgb(1)
    (0, 0, 0)
    """
    if uzaklik == 1:
        return (0, 0, 0)
    else:
        return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(uzaklik, 1, 1))


def goruntu_olustur(
    goruntu_genisligi: int = 800,
    goruntu_yuksekligi: int = 600,
    sekil_merkezi_x: float = -0.6,
    sekil_merkezi_y: float = 0,
    sekil_genisligi: float = 3.2,
    max_adim: int = 50,
    uzaklik_renk_kodlamasi: bool = True,
) -> Image.Image:
    """
    Mandelbrot kümesinin görüntüsünü oluşturma fonksiyonu. İki tür koordinat
    kullanılır: piksellere atıfta bulunan görüntü koordinatları ve Mandelbrot
    kümesinin içindeki ve dışındaki karmaşık sayılara atıfta bulunan şekil
    koordinatları. Bu fonksiyonun argümanlarındaki şekil koordinatları,
    Mandelbrot kümesinin hangi bölümünün görüntülendiğini belirler. Mandelbrot
    kümesinin ana alanı kabaca "-1.5 < x < 0.5" ve "-1 < y < 1" arasında
    şekil koordinatlarında yer alır.

    Yavaşlatan testleri yorum satırına al...
    # 13.35s call     fractals/mandelbrot.py::mandelbrot.goruntu_olustur
    # >>> goruntu_olustur().load()[0,0]
    (255, 0, 0)
    # >>> goruntu_olustur(uzaklik_renk_kodlamasi = False).load()[0,0]
    (255, 255, 255)
    """
    img = Image.new("RGB", (goruntu_genisligi, goruntu_yuksekligi))
    pikseller = img.load()

    # görüntü koordinatları boyunca döngü
    for goruntu_x in range(goruntu_genisligi):
        for goruntu_y in range(goruntu_yuksekligi):
            # görüntü koordinatlarına dayalı olarak şekil koordinatlarını belirle
            sekil_yuksekligi = sekil_genisligi / goruntu_genisligi * goruntu_yuksekligi
            sekil_x = sekil_merkezi_x + (goruntu_x / goruntu_genisligi - 0.5) * sekil_genisligi
            sekil_y = sekil_merkezi_y + (goruntu_y / goruntu_yuksekligi - 0.5) * sekil_yuksekligi

            uzaklik = uzaklik_hesapla(sekil_x, sekil_y, max_adim)

            # seçilen renklendirme fonksiyonuna göre ilgili pikseli renklendir
            if uzaklik_renk_kodlamasi:
                pikseller[goruntu_x, goruntu_y] = renkli_rgb(uzaklik)
            else:
                pikseller[goruntu_x, goruntu_y] = siyah_beyaz_rgb(uzaklik)

    return img


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # renkli versiyon, tam şekil
    img = goruntu_olustur()

    # farklı bölüm, yakınlaştırılmış renkli versiyon için yorumu kaldırın
    # img = goruntu_olustur(sekil_merkezi_x = -0.6, sekil_merkezi_y = -0.4,
    # sekil_genisligi = 0.8)

    # siyah beyaz versiyon, tam şekil için yorumu kaldırın
    # img = goruntu_olustur(uzaklik_renk_kodlamasi = False)

    # görüntüyü kaydetmek için yorumu kaldırın
    # img.save("mandelbrot.png")

    img.show()
