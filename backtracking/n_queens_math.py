r"""
Problem:

N vezir problemi: N * N satranç tahtasına N vezir yerleştirmek, öyle ki hiçbir vezir
diğer vezirleri yatay, dikey ve çapraz olarak tehdit edemez.

Çözüm:

Bu problemi çözmek için basit matematik kullanacağız. İlk olarak, vezirin tüm olası
yönlerde hareket edebileceğini biliyoruz: dikey, yatay, sol çapraz ve sağ çapraz.

Bunu şu şekilde görselleştirebiliriz:

sol çapraz = \
sağ çapraz = /

Satranç tahtasında dikey hareket satırlar, yatay hareket ise sütunlar olabilir.

Programlamada bir dizi kullanabiliriz ve bu dizide her indeks satırları, her değer ise
sütunları temsil edebilir. Örneğin:

    . V . .     Bu satranç tahtasında her sütunda bir vezir var ve her vezir
    . . . V     birbirini tehdit edemez.
    V . . .     Bu örneğin dizisi şu şekilde olur: [1, 3, 0, 2]
    . . V .

Bu noktada, dizideki her değerin birbirinden farklı olduğunu doğrularsak, vezirlerin
en azından yatay ve dikey olarak birbirini tehdit edemeyeceğini biliriz.

Bu noktada, satranç tahtasını bir Kartezyen düzlem olarak ele alacağız. Buradan sonra
temel matematiği hatırlayacağız, okulda bu formülü öğrenmiştik:

    Bir doğrunun eğimi:

           y2 - y1
     m = ----------
          x2 - x1

Bu formül bize eğimi verir. 45º (sağ çapraz) ve 135º (sol çapraz) açıları için bu
formül sırasıyla m = 1 ve m = -1 değerlerini verir.

Bakınız::
https://www.enotes.com/homework-help/write-equation-line-that-hits-origin-45-degree-1474860

Sonra bu diğer formüle sahibiz:

Eğim kesişimi:

y = mx + b

b, doğrunun Y eksenini kestiği yerdir (daha fazla bilgi için bakınız:
https://www.mathsisfun.com/y_intercept.html), formülü b'yi çözmek için değiştirirsek
şu şekilde olur:

y - mx = b

Ve 45º ve 135º açıları için m değerlerine zaten sahip olduğumuzdan, bu formül şu
şekilde olur:

45º: y - (1)x = b
45º: y - x = b

135º: y - (-1)x = b
135º: y + x = b

y = satır
x = sütun

Bu iki formülü uygulayarak, bir pozisyondaki bir vezirin başka bir vezir tarafından
tehdit edilip edilmediğini veya tam tersini kontrol edebiliriz.

"""

from __future__ import annotations


def derinlik_öncelikli_arama(
    olası_tahta: list[int],
    sağ_çapraz_çakışmaları: list[int],
    sol_çapraz_çakışmaları: list[int],
    tahtalar: list[list[str]],
    n: int,
) -> None:
    """
    >>> tahtalar = []
    >>> derinlik_öncelikli_arama([], [], [], tahtalar, 4)
    >>> for tahta in tahtalar:
    ...     print(tahta)
    ['. V . . ', '. . . V ', 'V . . . ', '. . V . ']
    ['. . V . ', 'V . . . ', '. . . V ', '. V . . ']
    """

    # Mevcut tahtadaki (olası_tahta) bir sonraki satırı bir vezirle doldurmak için alın
    satır = len(olası_tahta)

    # Eğer satır, tahtanın boyutuna eşitse, bu mevcut tahtada (olası_tahta) her satırda
    # bir vezir olduğu anlamına gelir
    if satır == n:
        # olası_tahta değişkenini şu şekilde dönüştürürüz: [1, 3, 0, 2] bu: ['. V . . ', '. . . V ', 'V . . . ', '. . V . ']
        tahtalar.append([". " * i + "V " + ". " * (n - 1 - i) for i in olası_tahta])
        return

    # Her satırda tüm olası sonuçları bulmak için her sütunu yineleyin
    for sütun in range(n):
        # Daha önce öğrendiklerimizi uygularız. İlk olarak, mevcut tahtada (olası_tahta)
        # başka aynı değerin olmadığını kontrol ederiz, çünkü varsa bu, dikeyde bir
        # çakışma olduğu anlamına gelir. Sonra daha önce öğrendiğimiz iki formülü
        # uygularız:
        #
        # 45º: y - x = b veya 45: satır - sütun = b
        # 135º: y + x = b veya satır + sütun = b.
        #
        # Ve bu iki formülün sonuçlarının kendi değişkenlerinde bulunmadığını doğrularız
        # (sağ_çapraz_çakışmaları, sol_çapraz_çakışmaları)
        #
        # Eğer bunlardan herhangi biri True ise, bu bir çakışma olduğu anlamına gelir,
        # bu yüzden for döngüsündeki bir sonraki değere geçeriz.
        if (
            sütun in olası_tahta
            or satır - sütun in sağ_çapraz_çakışmaları
            or satır + sütun in sol_çapraz_çakışmaları
        ):
            continue

        # Eğer False ise, dfs fonksiyonunu tekrar çağırırız ve girdileri güncelleriz
        derinlik_öncelikli_arama(
            [*olası_tahta, sütun],
            [*sağ_çapraz_çakışmaları, satır - sütun],
            [*sol_çapraz_çakışmaları, satır + sütun],
            tahtalar,
            n,
        )


def n_vezir_çözümü(n: int) -> None:
    tahtalar: list[list[str]] = []
    derinlik_öncelikli_arama([], [], [], tahtalar, n)

    # Tüm tahtaları yazdır
    for tahta in tahtalar:
        for sütun in tahta:
            print(sütun)
        print("")

    print(len(tahtalar), "çözüm bulundu.")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    n_vezir_çözümü(4)
