"""Yazarlar Bastien Capiaux & Mehdi Oudghiri

Vicsek fraktal algoritması, Vicsek fraktalı veya Vicsek karesi olarak bilinen bir
desen oluşturan özyinelemeli bir algoritmadır.
Her özyineleme seviyesindeki desenin genel desene benzediği
özyineleme kavramına dayanır.
Algoritma, bir kareyi 9 eşit küçük kareye bölmeyi,
merkez kareyi çıkarmayı ve ardından bu işlemi kalan 8 karede tekrarlamayı içerir.
Bu, özyinelemeyi sergileyen ve içinde daha küçük kareler bulunan
kare şeklinde bir dış hat deseni ile sonuçlanır.

Kaynak: https://en.wikipedia.org/wiki/Vicsek_fractal
"""

import turtle


def haç_çiz(x: float, y: float, uzunluk: float):
    """
    Belirtilen konumda ve belirtilen uzunlukta bir haç çiz.
    """
    turtle.up()
    turtle.goto(x - uzunluk / 2, y - uzunluk / 6)
    turtle.down()
    turtle.seth(0)
    turtle.begin_fill()
    for _ in range(4):
        turtle.fd(uzunluk / 3)
        turtle.right(90)
        turtle.fd(uzunluk / 3)
        turtle.left(90)
        turtle.fd(uzunluk / 3)
        turtle.left(90)
    turtle.end_fill()


def fraktal_çiz_özyinelemeli(x: float, y: float, uzunluk: float, derinlik: float):
    """
    Belirtilen konumda, belirtilen uzunluk ve derinlikte Vicsek fraktalını özyinelemeli olarak çiz.
    """
    if derinlik == 0:
        haç_çiz(x, y, uzunluk)
        return

    fraktal_çiz_özyinelemeli(x, y, uzunluk / 3, derinlik - 1)
    fraktal_çiz_özyinelemeli(x + uzunluk / 3, y, uzunluk / 3, derinlik - 1)
    fraktal_çiz_özyinelemeli(x - uzunluk / 3, y, uzunluk / 3, derinlik - 1)
    fraktal_çiz_özyinelemeli(x, y + uzunluk / 3, uzunluk / 3, derinlik - 1)
    fraktal_çiz_özyinelemeli(x, y - uzunluk / 3, uzunluk / 3, derinlik - 1)


def renk_ayarla(rgb: str):
    turtle.color(rgb)


def vicsek_fraktal_çiz(x: float, y: float, uzunluk: float, derinlik: float, renk="mavi"):
    """
    Belirtilen konumda, belirtilen uzunluk ve derinlikte Vicsek fraktalını çiz.
    """
    turtle.speed(0)
    turtle.hideturtle()
    renk_ayarla(renk)
    fraktal_çiz_özyinelemeli(x, y, uzunluk, derinlik)
    turtle.Screen().update()


def ana():
    vicsek_fraktal_çiz(0, 0, 800, 4)

    turtle.done()


if __name__ == "__main__":
    ana()
