"""
N vezir problemi, N * N boyutundaki bir satranç tahtasına N vezir yerleştirme problemidir.
Bu, hiçbir vezirin yatay, dikey ve çapraz çizgilerde başka bir veziri tehdit etmemesi gerektiği anlamına gelir.

Organiser: K. Umut Araz
"""

from __future__ import annotations

çözüm = []


def güvenli_mi(tahta: list[list[int]], satır: int, sütun: int) -> bool:
    """
    Bu fonksiyon, tahtanın mevcut durumunu göz önünde bulundurarak oraya bir vezir yerleştirmenin güvenli olup olmadığını belirten bir boolean değer döndürür.

    Parametreler:
    tahta (2D matris): Satranç tahtası
    satır, sütun: Tahtadaki hücrenin koordinatları

    Dönüş:
    Boolean Değer

    >>> güvenli_mi([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 1, 1)
    True
    >>> güvenli_mi([[1, 0, 0], [0, 0, 0], [0, 0, 0]], 1, 1)
    False
    """

    n = len(tahta)  # Tahtanın boyutu

    # Aynı satır, sütun, sol üst çapraz ve sağ üst çaprazda vezir olup olmadığını kontrol et
    return (
        all(tahta[i][j] != 1 for i, j in zip(range(satır, -1, -1), range(sütun, n)))
        and all(
            tahta[i][j] != 1 for i, j in zip(range(satır, -1, -1), range(sütun, -1, -1))
        )
        and all(tahta[i][j] != 1 for i, j in zip(range(satır, n), range(sütun, n)))
        and all(tahta[i][j] != 1 for i, j in zip(range(satır, n), range(sütun, -1, -1)))
    )


def çöz(tahta: list[list[int]], satır: int) -> bool:
    """
    Bu fonksiyon bir durum uzayı ağacı oluşturur ve güvenli fonksiyonunu çağırır, False boolean değeri alana kadar devam eder ve o dalı sonlandırır, ardından bir sonraki olası çözüm dalına geri döner.
    """
    if satır >= len(tahta):
        """
        Satır numarası N'yi aşarsa, başarılı bir kombinasyona sahip bir tahtamız var demektir ve bu kombinasyon çözüm listesine eklenir ve tahta yazdırılır.
        """
        çözüm.append(tahta)
        tahta_yazdır(tahta)
        print()
        return True
    for i in range(len(tahta)):
        """
        Her satır için, bir vezir yerleştirmenin mümkün olup olmadığını kontrol etmek için her sütunu iter.
        Bu dal için tüm kombinasyonlar başarılı olursa, tahta bir sonraki olası kombinasyon için yeniden başlatılır.
        """
        if güvenli_mi(tahta, satır, i):
            tahta[satır][i] = 1
            çöz(tahta, satır + 1)
            tahta[satır][i] = 0
    return False


def tahta_yazdır(tahta: list[list[int]]) -> None:
    """
    Başarılı bir kombinasyona sahip tahtaları yazdırır.
    """
    for i in range(len(tahta)):
        for j in range(len(tahta)):
            if tahta[i][j] == 1:
                print("V", end=" ")  # Vezir mevcut
            else:
                print(".", end=" ")  # Boş hücre
        print()


# Vezir sayısı (örneğin, n=8 için 8x8 tahta)
n = 8
tahta = [[0 for i in range(n)] for j in range(n)]
çöz(tahta, 0)
print("Toplam çözüm sayısı:", len(çözüm))
