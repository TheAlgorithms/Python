from __future__ import annotations

from decimal import Decimal
from numpy import array

def matrisin_tersi(matris: list[list[float]]) -> list[list[float]]:
    """
    Bir matrisin tersi, o matris ile çarpıldığında birim matrisi verir.
    Bu fonksiyon, 2x2 ve 3x3 matrislerin tersini bulur.
    Eğer bir matrisin determinantı 0 ise, tersi yoktur.

    Doctest örnekleri için 2x2
    >>> matrisin_tersi([[2, 5], [2, 0]])
    [[0.0, 0.5], [0.2, -0.2]]
    >>> matrisin_tersi([[2.5, 5], [1, 2]])
    Traceback (most recent call last):
        ...
    ValueError: Bu matrisin tersi yok.
    >>> matrisin_tersi([[12, -16], [-9, 0]])
    [[0.0, -0.1111111111111111], [-0.0625, -0.08333333333333333]]
    >>> matrisin_tersi([[12, 3], [16, 8]])
    [[0.16666666666666666, -0.0625], [-0.3333333333333333, 0.25]]
    >>> matrisin_tersi([[10, 5], [3, 2.5]])
    [[0.25, -0.5], [-0.3, 1.0]]

    Doctest örnekleri için 3x3
    >>> matrisin_tersi([[2, 5, 7], [2, 0, 1], [1, 2, 3]])
    [[2.0, 5.0, -4.0], [1.0, 1.0, -1.0], [-5.0, -12.0, 10.0]]
    >>> matrisin_tersi([[1, 2, 2], [1, 2, 2], [3, 2, -1]])
    Traceback (most recent call last):
        ...
    ValueError: Bu matrisin tersi yok.

    >>> matrisin_tersi([[],[]])
    Traceback (most recent call last):
        ...
    ValueError: Lütfen 2x2 veya 3x3 boyutunda bir matris sağlayın.

    >>> matrisin_tersi([[1, 2], [3, 4], [5, 6]])
    Traceback (most recent call last):
        ...
    ValueError: Lütfen 2x2 veya 3x3 boyutunda bir matris sağlayın.

    >>> matrisin_tersi([[1, 2, 1], [0,3, 4]])
    Traceback (most recent call last):
        ...
    ValueError: Lütfen 2x2 veya 3x3 boyutunda bir matris sağlayın.

    >>> matrisin_tersi([[1, 2, 3], [7, 8, 9], [7, 8, 9]])
    Traceback (most recent call last):
        ...
    ValueError: Bu matrisin tersi yok.

    >>> matrisin_tersi([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    """

    d = Decimal

    # Sağlanan matrisin 2 satır ve 2 sütun içerip içermediğini kontrol et
    if len(matris) == 2 and len(matris[0]) == 2 and len(matris[1]) == 2:
        # Matrisin determinantını hesapla
        determinant = float(
            d(matris[0][0]) * d(matris[1][1]) - d(matris[1][0]) * d(matris[0][1])
        )
        if determinant == 0:
            raise ValueError("Bu matrisin tersi yok.")

        # Elemanların yerlerini değiştirilmiş bir matris oluştur
        degistirilmis_matris = [[0.0, 0.0], [0.0, 0.0]]
        degistirilmis_matris[0][0], degistirilmis_matris[1][1] = matris[1][1], matris[0][0]
        degistirilmis_matris[1][0], degistirilmis_matris[0][1] = -matris[1][0], -matris[0][1]

        # Matrisin tersini hesapla
        return [
            [(float(d(n)) / determinant) or 0.0 for n in row] for row in degistirilmis_matris
        ]
    elif (
        len(matris) == 3
        and len(matris[0]) == 3
        and len(matris[1]) == 3
        and len(matris[2]) == 3
    ):
        # Matrisin determinantını Sarrus kuralını kullanarak hesapla
        determinant = float(
            (
                (d(matris[0][0]) * d(matris[1][1]) * d(matris[2][2]))
                + (d(matris[0][1]) * d(matris[1][2]) * d(matris[2][0]))
                + (d(matris[0][2]) * d(matris[1][0]) * d(matris[2][1]))
            )
            - (
                (d(matris[0][2]) * d(matris[1][1]) * d(matris[2][0]))
                + (d(matris[0][1]) * d(matris[1][0]) * d(matris[2][2]))
                + (d(matris[0][0]) * d(matris[1][2]) * d(matris[2][1]))
            )
        )
        if determinant == 0:
            raise ValueError("Bu matrisin tersi yok.")

        # Cofaktör matrisini oluştur
        cofactor_matrix = [
            [d(0.0), d(0.0), d(0.0)],
            [d(0.0), d(0.0), d(0.0)],
            [d(0.0), d(0.0), d(0.0)],
        ]
        cofactor_matrix[0][0] = (d(matris[1][1]) * d(matris[2][2])) - (
            d(matris[1][2]) * d(matris[2][1])
        )
        cofactor_matrix[0][1] = -(
            (d(matris[1][0]) * d(matris[2][2])) - (d(matris[1][2]) * d(matris[2][0]))
        )
        cofactor_matrix[0][2] = (d(matris[1][0]) * d(matris[2][1])) - (
            d(matris[1][1]) * d(matris[2][0])
        )
        cofactor_matrix[1][0] = -(
            (d(matris[0][1]) * d(matris[2][2])) - (d(matris[0][2]) * d(matris[2][1]))
        )
        cofactor_matrix[1][1] = (d(matris[0][0]) * d(matris[2][2])) - (
            d(matris[0][2]) * d(matris[2][0])
        )
        cofactor_matrix[1][2] = -(
            (d(matris[0][0]) * d(matris[2][1])) - (d(matris[0][1]) * d(matris[2][0]))
        )
        cofactor_matrix[2][0] = (d(matris[0][1]) * d(matris[1][2])) - (
            d(matris[0][2]) * d(matris[1][1])
        )
        cofactor_matrix[2][1] = -(
            (d(matris[0][0]) * d(matris[1][2])) - (d(matris[0][2]) * d(matris[1][0]))
        )
        cofactor_matrix[2][2] = (d(matris[0][0]) * d(matris[1][1])) - (
            d(matris[0][1]) * d(matris[1][0])
        )

        # Cofaktör matrisinin transpozunu al (Adjoint matris)
        adjoint_matrix = array(cofactor_matrix)
        for i in range(3):
            for j in range(3):
                adjoint_matrix[i][j] = cofactor_matrix[j][i]

        # Matrisin tersini (1/determinant) * adjoint matris formülü ile hesapla
        inverse_matrix = array(cofactor_matrix)
        for i in range(3):
            for j in range(3):
                inverse_matrix[i][j] /= d(determinant)

        # Matrisin tersini hesapla
        return [[float(d(n)) or 0.0 for n in row] for row in inverse_matrix]
    
    raise ValueError("Lütfen 2x2 veya 3x3 boyutunda bir matris sağlayın.")
