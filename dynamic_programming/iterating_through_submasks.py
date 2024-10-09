"""
Yazar : Syed Faizan (3. Sınıf Öğrencisi IIIT Pune)
github : faizan2700
Size bir bitmask m verilir ve tüm alt maskelerini verimli bir şekilde
dolaşmak istersiniz. s maskesi, yalnızca bitmask'te yer alan bitlerin
ayarlanmış olması durumunda m'nin alt maskesidir.
"""

from __future__ import annotations


def alt_maskelerin_listesi(mask: int) -> list[int]:
    """
    Argümanlar:
        mask : maskeyi gösteren sayı (her zaman 0'dan büyük tamsayı, sıfırın
            alt maskesi yoktur)

    Dönüş:
        tüm_alt_maskeler : maskenin alt maskelerinin listesi (s maskesi, yalnızca
        orijinal maskede yer alan bitlerin ayarlanmış olması durumunda m maskesinin
        alt maskesi olarak adlandırılır)

    Hatalar:
        AssertionError: maske pozitif tamsayı değil

    >>> alt_maskelerin_listesi(15)
    [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> alt_maskelerin_listesi(13)
    [13, 12, 9, 8, 5, 4, 1]
    >>> alt_maskelerin_listesi(-7)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    AssertionError: mas maske pozitif tamsayı olmalı, girdiniz -7
    >>> alt_maskelerin_listesi(0)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    AssertionError: mas maske pozitif tamsayı olmalı, girdiniz 0

    """

    assert (
        isinstance(mask, int) and mask > 0
    ), f"maske pozitif tamsayı olmalı, girdiniz {mask}"

    """
    ilk alt maske maskenin kendisi olacaktır, ardından diğer alt maskeleri
    elde etmek için işlem yapılacaktır, sıfıra ulaşana kadar (sıfır nihai
    alt maskeler listesine dahil edilmez)
    """
    tüm_alt_maskeler = []
    alt_maske = mask

    while alt_maske:
        tüm_alt_maskeler.append(alt_maske)
        alt_maske = (alt_maske - 1) & mask

    return tüm_alt_maskeler


if __name__ == "__main__":
    import doctest

    doctest.testmod()
