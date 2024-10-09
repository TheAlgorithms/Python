"""
Yazar Anurag Kumar | anuragkumarak95@gmail.com | git/anuragkumarak95

Özyineleme kullanarak fraktal oluşturmanın basit bir örneği.

Sierpiński Üçgeni nedir?
    Sierpiński üçgeni (bazen Sierpinski olarak yazılır), Sierpiński contası veya
Sierpiński eleği olarak da adlandırılır, eşkenar üçgen şeklinde olan ve
özyinelemeli olarak daha küçük eşkenar üçgenlere bölünen bir fraktal çekici sabit
kümeyle genel şekli olan bir fraktaldır. Başlangıçta bir eğri olarak oluşturulmuş,
bu, kendine benzer kümelerin temel örneklerinden biridir - yani, herhangi bir
büyütme veya küçültme oranında yeniden üretilebilen matematiksel olarak
oluşturulmuş bir desendir. Polonyalı matematikçi Wacław Sierpiński'nin adını
taşır, ancak Sierpiński'nin çalışmasından yüzyıllar önce dekoratif bir desen
olarak ortaya çıkmıştır.


Kullanım: python sierpinski_triangle.py <int:fraktal_derinliği>

Krediler:
    Yukarıdaki açıklama
    https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle
    adresinden alınmıştır. Bu kod,
    https://www.riannetrujillo.com/blog/python-fractal/
    adresindeki kod düzenlenerek yazılmıştır.
"""

import sys
import turtle


def orta_nokta_bul(nokta1: tuple[float, float], nokta2: tuple[float, float]) -> tuple[float, float]:
    """
    İki noktanın orta noktasını bul

    >>> orta_nokta_bul((0, 0), (2, 2))
    (1.0, 1.0)
    >>> orta_nokta_bul((-3, -3), (3, 3))
    (0.0, 0.0)
    >>> orta_nokta_bul((1, 0), (3, 2))
    (2.0, 1.0)
    >>> orta_nokta_bul((0, 0), (1, 1))
    (0.5, 0.5)
    >>> orta_nokta_bul((0, 0), (0, 0))
    (0.0, 0.0)
    """
    return (nokta1[0] + nokta2[0]) / 2, (nokta1[1] + nokta2[1]) / 2


def ucgen_ciz(
    kose1: tuple[float, float],
    kose2: tuple[float, float],
    kose3: tuple[float, float],
    derinlik: int,
) -> None:
    """
    Üçgenin köşeleri ve özyineleme derinliği verilerek Sierpinski üçgenini özyinelemeli olarak çiz
    """
    kalem.up()
    kalem.goto(kose1[0], kose1[1])
    kalem.down()
    kalem.goto(kose2[0], kose2[1])
    kalem.goto(kose3[0], kose3[1])
    kalem.goto(kose1[0], kose1[1])

    if derinlik == 0:
        return

    ucgen_ciz(kose1, orta_nokta_bul(kose1, kose2), orta_nokta_bul(kose1, kose3), derinlik - 1)
    ucgen_ciz(kose2, orta_nokta_bul(kose1, kose2), orta_nokta_bul(kose2, kose3), derinlik - 1)
    ucgen_ciz(kose3, orta_nokta_bul(kose3, kose2), orta_nokta_bul(kose1, kose3), derinlik - 1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError(
            "Bu betiği kullanmanın doğru formatı: "
            "python fractals.py <int:fraktal_derinliği>"
        )
    kalem = turtle.Turtle()
    kalem.ht()
    kalem.speed(5)
    kalem.pencolor("kırmızı")

    koseler = [(-175, -125), (0, 175), (175, -125)]  # üçgenin köşeleri
    ucgen_ciz(koseler[0], koseler[1], koseler[2], int(sys.argv[1]))
    turtle.Screen().exitonclick()
