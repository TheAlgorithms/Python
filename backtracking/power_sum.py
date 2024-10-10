"""
Problem kaynağı: https://www.hackerrank.com/challenges/the-power-sum/problem
Verilen bir X tamsayısının, N'inci kuvvetlerinin toplamı olarak ifade edilebileceği
yolların sayısını bulun. Örneğin, X=13 ve N=2 ise. 13'e kadar olan benzersiz karelerin
tüm kombinasyonlarını bulmamız gerekiyor. Tek çözüm 2^2+3^2'dir. Kısıtlamalar: 1<=X<=1000, 2<=N<=10.

Organiser: K. Umut Araz
"""


def geri_izleme(
    gereken_toplam: int,
    kuvvet: int,
    mevcut_sayı: int,
    mevcut_toplam: int,
    çözüm_sayısı: int,
) -> tuple[int, int]:
    """
    >>> geri_izleme(13, 2, 1, 0, 0)
    (0, 1)
    >>> geri_izleme(10, 2, 1, 0, 0)
    (0, 1)
    >>> geri_izleme(10, 3, 1, 0, 0)
    (0, 0)
    >>> geri_izleme(20, 2, 1, 0, 0)
    (0, 1)
    >>> geri_izleme(15, 10, 1, 0, 0)
    (0, 0)
    >>> geri_izleme(16, 2, 1, 0, 0)
    (0, 1)
    >>> geri_izleme(20, 1, 1, 0, 0)
    (0, 64)
    """
    if mevcut_toplam == gereken_toplam:
        # Eğer kuvvetlerin toplamı gereken_toplam'a eşitse, bir çözümümüz var demektir.
        çözüm_sayısı += 1
        return mevcut_toplam, çözüm_sayısı

    i_kuvvet = mevcut_sayı**kuvvet
    if mevcut_toplam + i_kuvvet <= gereken_toplam:
        # Eğer kuvvetlerin toplamı gereken_toplam'dan küçükse, kuvvetleri eklemeye devam edin.
        mevcut_toplam += i_kuvvet
        mevcut_toplam, çözüm_sayısı = geri_izleme(
            gereken_toplam, kuvvet, mevcut_sayı + 1, mevcut_toplam, çözüm_sayısı
        )
        mevcut_toplam -= i_kuvvet
    if i_kuvvet < gereken_toplam:
        # Eğer i'nin kuvveti gereken_toplam'dan küçükse, bir sonraki kuvvetle deneyin.
        mevcut_toplam, çözüm_sayısı = geri_izleme(
            gereken_toplam, kuvvet, mevcut_sayı + 1, mevcut_toplam, çözüm_sayısı
        )
    return mevcut_toplam, çözüm_sayısı


def çöz(gereken_toplam: int, kuvvet: int) -> int:
    """
    >>> çöz(13, 2)
    1
    >>> çöz(10, 2)
    1
    >>> çöz(10, 3)
    0
    >>> çöz(20, 2)
    1
    >>> çöz(15, 10)
    0
    >>> çöz(16, 2)
    1
    >>> çöz(20, 1)
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz giriş
    gereken_toplam 1 ile 1000 arasında, kuvvet 2 ile 10 arasında olmalıdır.
    >>> çöz(-10, 5)
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz giriş
    gereken_toplam 1 ile 1000 arasında, kuvvet 2 ile 10 arasında olmalıdır.
    """
    if not (1 <= gereken_toplam <= 1000 and 2 <= kuvvet <= 10):
        raise ValueError(
            "Geçersiz giriş\n"
            "gereken_toplam 1 ile 1000 arasında, kuvvet 2 ile 10 arasında olmalıdır."
        )

    return geri_izleme(gereken_toplam, kuvvet, 1, 0, 0)[1]  # Çözüm sayısını döndür


if __name__ == "__main__":
    import doctest

    doctest.testmod()
