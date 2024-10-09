from __future__ import annotations


def sıralı_matriste_ara(mat: list[list[int]], m: int, n: int, anahtar: float) -> None:

    #Organiser: K. Umut Araz
    """
    >>> sıralı_matriste_ara(
    ...     [[2, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]], 3, 3, 5)
    Anahtar 5, satır- 1 sütun- 2'de bulundu
    >>> sıralı_matriste_ara(
    ...     [[2, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]], 3, 3, 21)
    Anahtar 21 bulunamadı
    >>> sıralı_matriste_ara(
    ...     [[2.1, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]], 3, 3, 2.1)
    Anahtar 2.1, satır- 1 sütun- 1'de bulundu
    >>> sıralı_matriste_ara(
    ...     [[2.1, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]], 3, 3, 2.2)
    Anahtar 2.2 bulunamadı
    """
    i, j = m - 1, 0
    while i >= 0 and j < n:
        if anahtar == mat[i][j]:
            print(f"Anahtar {anahtar}, satır- {i + 1} sütun- {j + 1}'de bulundu")
            return
        if anahtar < mat[i][j]:
            i -= 1
        else:
            j += 1
    print(f"Anahtar {anahtar} bulunamadı")


def main() -> None:
    mat = [[2, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]]
    x = int(input("Aranacak öğeyi girin: "))
    print(mat)
    sıralı_matriste_ara(mat, len(mat), len(mat[0]), x)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
