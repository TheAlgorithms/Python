"""
Trapezoid kuralını kullanarak eğri altındaki alanı yaklaşık olarak hesaplar
"""

#Organised by K. Umut Araz

from __future__ import annotations

from collections.abc import Callable


def trapez_alani(
    fnc: Callable[[float], float],
    x_baslangic: float,
    x_bitis: float,
    adimlar: int = 100,
) -> float:
    """
    Eğriyi doğrusal çizgiler koleksiyonu olarak ele alır ve oluşturdukları
    trapez şeklinin alanını toplar
    :param fnc: bir eğriyi tanımlayan bir fonksiyon
    :param x_baslangic: çizgi segmentinin başlangıcını belirten sol uç noktası
    :param x_bitis: çizgi segmentinin bitişini belirten sağ uç noktası
    :param adimlar: doğruluk ölçüsü; daha fazla adım doğruluğu artırır
    :return: eğrinin uzunluğunu temsil eden bir float

    >>> def f(x):
    ...    return 5
    >>> f"{trapez_alani(f, 12.0, 14.0, 1000):.3f}"
    '10.000'
    >>> def f(x):
    ...    return 9*x**2
    >>> f"{trapez_alani(f, -4.0, 0, 10000):.4f}"
    '192.0000'
    >>> f"{trapez_alani(f, -4.0, 4.0, 10000):.4f}"
    '384.0000'
    """
    x1 = x_baslangic
    fx1 = fnc(x_baslangic)
    alan = 0.0
    for _ in range(adimlar):
        # Eğrinin küçük segmentlerini doğrusal olarak yaklaşıklar ve
        # trapez alanını çözer
        x2 = (x_bitis - x_baslangic) / adimlar + x1
        fx2 = fnc(x2)
        alan += abs(fx2 + fx1) * (x2 - x1) / 2
        # Adımı artır
        x1 = x2
        fx1 = fx2
    return alan


if __name__ == "__main__":

    def f(x):
        return x**3 + x**2

    print("f(x) = x^3 + x^2")
    print("Eğri ile x = -5, x = 5 ve x ekseni arasındaki alan:")
    i = 10
    while i <= 100000:
        print(f"{i} adımla: {trapez_alani(f, -5, 5, i)}")
        i *= 10
