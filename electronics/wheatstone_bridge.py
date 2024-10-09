# https://en.wikipedia.org/wiki/Wheatstone_bridge
from __future__ import annotations


def wheatstone_solver(
    direnç_1: float, direnç_2: float, direnç_3: float
) -> float:
    """
    Bu fonksiyon, bir wheatstone ağındaki bilinmeyen direnci, ağdaki diğer üç direnç bilindiğinde hesaplayabilir.
    Hesaplama formülü:

    ---------------
    |Rx=(R2/R1)*R3|
    ---------------

    Kullanım örnekleri:
    >>> wheatstone_solver(direnç_1=2, direnç_2=4, direnç_3=5)
    10.0
    >>> wheatstone_solver(direnç_1=356, direnç_2=234, direnç_3=976)
    641.5280898876405
    >>> wheatstone_solver(direnç_1=2, direnç_2=-1, direnç_3=2)
    Traceback (most recent call last):
        ...
    ValueError: Tüm direnç değerleri pozitif olmalıdır
    >>> wheatstone_solver(direnç_1=0, direnç_2=0, direnç_3=2)
    Traceback (most recent call last):
        ...
    ValueError: Tüm direnç değerleri pozitif olmalıdır
    """

    if direnç_1 <= 0 or direnç_2 <= 0 or direnç_3 <= 0:
        raise ValueError("Tüm direnç değerleri pozitif olmalıdır")
    else:
        return float((direnç_2 / direnç_1) * direnç_3)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
