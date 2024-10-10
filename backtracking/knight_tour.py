# Knight Tour Tanıtımı: https://www.youtube.com/watch?v=ab_dY3dZFHM

from __future__ import annotations
#Organiser: K. Umut Araz


def geçerli_pozisyonlar(position: tuple[int, int], n: int) -> list[tuple[int, int]]:
    """
    Mevcut pozisyondan bir atın hareket edebileceği tüm geçerli pozisyonları bulun.

    >>> geçerli_pozisyonlar((1, 3), 4)
    [(2, 1), (0, 1), (3, 2)]
    """

    y, x = position
    pozisyonlar = [
        (y + 1, x + 2),
        (y - 1, x + 2),
        (y + 1, x - 2),
        (y - 1, x - 2),
        (y + 2, x + 1),
        (y + 2, x - 1),
        (y - 2, x + 1),
        (y - 2, x - 1),
    ]
    geçerli_pozisyonlar = []

    for iç_pozisyon in pozisyonlar:
        y_test, x_test = iç_pozisyon
        if 0 <= y_test < n and 0 <= x_test < n:
            geçerli_pozisyonlar.append(iç_pozisyon)

    return geçerli_pozisyonlar


def tamamlandı_mı(tahta: list[list[int]]) -> bool:
    """
    Tahtanın (matrisin) tamamen sıfır olmayan değerlerle doldurulup doldurulmadığını kontrol edin.

    >>> tamamlandı_mı([[1]])
    True

    >>> tamamlandı_mı([[1, 2], [3, 0]])
    False
    """

    return not any(elem == 0 for row in tahta for elem in row)


def açık_at_turu_yardımcı(
    tahta: list[list[int]], poz: tuple[int, int], mevcut: int
) -> bool:
    """
    At turu problemini çözmek için yardımcı fonksiyon.
    """

    if tamamlandı_mı(tahta):
        return True

    for pozisyon in geçerli_pozisyonlar(poz, len(tahta)):
        y, x = pozisyon

        if tahta[y][x] == 0:
            tahta[y][x] = mevcut + 1
            if açık_at_turu_yardımcı(tahta, pozisyon, mevcut + 1):
                return True
            tahta[y][x] = 0

    return False


def açık_at_turu(n: int) -> list[list[int]]:
    """
    n boyutundaki bir tahta için at turu probleminin çözümünü bulun. Verilen boyut için
    tur yapılamazsa ValueError yükseltir.

    >>> açık_at_turu(1)
    [[1]]

    >>> açık_at_turu(2)
    Traceback (most recent call last):
        ...
    ValueError: Açık At Turu, 2 boyutundaki bir tahtada yapılamaz
    """

    tahta = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            tahta[i][j] = 1
            if açık_at_turu_yardımcı(tahta, (i, j), 1):
                return tahta
            tahta[i][j] = 0

    msg = f"Açık At Turu, {n} boyutundaki bir tahtada yapılamaz"
    raise ValueError(msg)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
