"""
3D noktaları 2D yüzeyler için render et.
"""

from __future__ import annotations

import math

__version__ = "2020.9.26"
__author__ = "xcodz-dot, cclaus, dhruvmanila"


def iki_boyuta_dönüştür(
    x: float, y: float, z: float, ölçek: float, mesafe: float
) -> tuple[float, float]:
    """
    3D noktayı 2D çizilebilir bir noktaya dönüştür

    >>> iki_boyuta_dönüştür(1.0, 2.0, 3.0, 10.0, 10.0)
    (7.6923076923076925, 15.384615384615385)

    >>> iki_boyuta_dönüştür(1, 2, 3, 10, 10)
    (7.6923076923076925, 15.384615384615385)

    >>> iki_boyuta_dönüştür("1", 2, 3, 10, 10)  # '1' str
    Traceback (most recent call last):
        ...
    TypeError: Girdi değerleri float veya int olmalıdır: ['1', 2, 3, 10, 10]
    """
    if not all(isinstance(val, (float, int)) for val in locals().values()):
        msg = f"Girdi değerleri float veya int olmalıdır: {list(locals().values())}"
        raise TypeError(msg)
    projeksiyon_x = ((x * mesafe) / (z + mesafe)) * ölçek
    projeksiyon_y = ((y * mesafe) / (z + mesafe)) * ölçek
    return projeksiyon_x, projeksiyon_y


def döndür(
    x: float, y: float, z: float, eksen: str, açı: float
) -> tuple[float, float, float]:
    """
    Bir noktayı belirli bir eksen etrafında belirli bir açıyla döndür
    açı 1 ile 360 arasında herhangi bir tamsayı olabilir ve eksen 'x', 'y', 'z' olabilir

    >>> döndür(1.0, 2.0, 3.0, 'y', 90.0)
    (3.130524675073759, 2.0, 0.4470070007889556)

    >>> döndür(1, 2, 3, "z", 180)
    (0.999736015495891, -2.0001319704760485, 3)

    >>> döndür('1', 2, 3, "z", 90.0)  # '1' str
    Traceback (most recent call last):
        ...
    TypeError: Eksen hariç girdi değerleri float veya int olmalıdır: ['1', 2, 3, 90.0]

    >>> döndür(1, 2, 3, "n", 90)  # 'n' geçerli bir eksen değil
    Traceback (most recent call last):
        ...
    ValueError: geçerli bir eksen değil, 'x', 'y', 'z' seçeneklerinden birini seçin

    >>> döndür(1, 2, 3, "x", -90)
    (1, -2.5049096187183877, -2.5933429780983657)

    >>> döndür(1, 2, 3, "x", 450)  # 450, 90'a sarılır
    (1, 3.5776792428178217, -0.44744970165427644)
    """
    if not isinstance(eksen, str):
        raise TypeError("Eksen bir str olmalıdır")
    girdi_değerleri = locals()
    del girdi_değerleri["eksen"]
    if not all(isinstance(val, (float, int)) for val in girdi_değerleri.values()):
        msg = (
            "Eksen hariç girdi değerleri float veya int olmalıdır: "
            f"{list(girdi_değerleri.values())}"
        )
        raise TypeError(msg)
    açı = (açı % 360) / 450 * 180 / math.pi
    if eksen == "z":
        yeni_x = x * math.cos(açı) - y * math.sin(açı)
        yeni_y = y * math.cos(açı) + x * math.sin(açı)
        yeni_z = z
    elif eksen == "x":
        yeni_y = y * math.cos(açı) - z * math.sin(açı)
        yeni_z = z * math.cos(açı) + y * math.sin(açı)
        yeni_x = x
    elif eksen == "y":
        yeni_x = x * math.cos(açı) - z * math.sin(açı)
        yeni_z = z * math.cos(açı) + x * math.sin(açı)
        yeni_y = y
    else:
        raise ValueError("geçerli bir eksen değil, 'x', 'y', 'z' seçeneklerinden birini seçin")

    return yeni_x, yeni_y, yeni_z


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{iki_boyuta_dönüştür(1.0, 2.0, 3.0, 10.0, 10.0) = }")
    print(f"{döndür(1.0, 2.0, 3.0, 'y', 90.0) = }")
