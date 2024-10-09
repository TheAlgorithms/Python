"""
Kısmen doldurulmuş 9x9 2D dizisi verildiğinde, amaç 9x9
kare ızgarayı 1'den 9'a kadar numaralandırılmış rakamlarla doldurmaktır, böylece her satır, sütun ve
dokuz 3x3 alt ızgaranın her biri tüm rakamları içerir.

Bu, Geri İzleme kullanılarak çözülebilir ve n-vezir problemine benzerdir.
Bir hücrenin güvenli olup olmadığını kontrol ederiz ve fonksiyonu
bir sonraki sütunda rekürsif olarak çağırırız, eğer True dönerse,
bulmacayı çözmüşüz demektir. Aksi takdirde, geri izleriz ve o hücreye başka bir sayı
yerleştiririz ve bu işlemi tekrar ederiz.
"""

from __future__ import annotations

Matris = list[list[int]]

# ızgaraya başlangıç değerlerini atama
başlangıç_ızgarası: Matris = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]

# çözümü olmayan bir ızgara
çözüm_yok: Matris = [
    [5, 0, 6, 5, 0, 8, 4, 0, 3],
    [5, 2, 0, 0, 0, 0, 0, 0, 2],
    [1, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]


def güvenli_mi(ızgara: Matris, satır: int, sütun: int, n: int) -> bool:
    """
    Bu fonksiyon ızgarayı kontrol eder ve her satır,
    sütun ve 3x3 alt ızgaraların 'n' rakamını içerip içermediğini kontrol eder.
    Eğer 'güvenli' değilse (yani bir kopya rakam bulunursa) False döner,
    aksi takdirde 'güvenli' ise True döner.
    """
    for i in range(9):
        if n in {ızgara[satır][i], ızgara[i][sütun]}:
            return False

    for i in range(3):
        for j in range(3):
            if ızgara[(satır - satır % 3) + i][(sütun - sütun % 3) + j] == n:
                return False

    return True


def boş_konum_bul(ızgara: Matris) -> tuple[int, int] | None:
    """
    Bu fonksiyon boş bir konum bulur, böylece belirli bir satır ve sütun için bir sayı atayabiliriz.
    """
    for i in range(9):
        for j in range(9):
            if ızgara[i][j] == 0:
                return i, j
    return None


def sudoku(ızgara: Matris) -> Matris | None:
    """
    Kısmen doldurulmuş bir ızgarayı alır ve tüm atanmamış konumlara
    Sudoku çözümü gereksinimlerini karşılayacak şekilde değerler atamaya çalışır
    (satırlar, sütunlar ve kutular arasında tekrar olmaması).

    >>> sudoku(başlangıç_ızgarası)  # doctest: +NORMALIZE_WHITESPACE
    [[3, 1, 6, 5, 7, 8, 4, 9, 2],
     [5, 2, 9, 1, 3, 4, 7, 6, 8],
     [4, 8, 7, 6, 2, 9, 5, 3, 1],
     [2, 6, 3, 4, 1, 5, 9, 8, 7],
     [9, 7, 4, 8, 6, 3, 1, 2, 5],
     [8, 5, 1, 7, 9, 2, 6, 4, 3],
     [1, 3, 8, 9, 4, 7, 2, 5, 6],
     [6, 9, 2, 3, 5, 1, 8, 7, 4],
     [7, 4, 5, 2, 8, 6, 3, 1, 9]]
     >>> sudoku(çözüm_yok) is None
     True
    """
    if konum := boş_konum_bul(ızgara):
        satır, sütun = konum
    else:
        # Eğer konum ``None`` ise, ızgara çözülmüştür.
        return ızgara

    for rakam in range(1, 10):
        if güvenli_mi(ızgara, satır, sütun, rakam):
            ızgara[satır][sütun] = rakam

            if sudoku(ızgara) is not None:
                return ızgara

            ızgara[satır][sütun] = 0

    return None


def çözümü_yazdır(ızgara: Matris) -> None:
    """
    Çözümü 9x9 ızgara şeklinde yazdıran bir fonksiyon.
    """
    for satır in ızgara:
        for hücre in satır:
            print(hücre, end=" ")
        print()


if __name__ == "__main__":
    # ızgaranın bir kopyasını oluşturun, böylece değiştirilmemiş ızgara ile karşılaştırabilirsiniz
    for örnek_ızgara in (başlangıç_ızgarası, çözüm_yok):
        print("\nÖrnek ızgara:\n" + "=" * 20)
        çözümü_yazdır(örnek_ızgara)
        print("\nÖrnek ızgara çözümü:")
        çözüm = sudoku(örnek_ızgara)
        if çözüm is not None:
            çözümü_yazdır(çözüm)
        else:
            print("Çözüm bulunamıyor.")
