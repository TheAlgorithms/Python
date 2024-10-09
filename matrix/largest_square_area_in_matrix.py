"""
Soru:
Boyutu n * m olan bir ikili matris (mat) verildiğinde, tüm elemanları 1 olan en büyük kare alt matrisin boyutunu bulun.

---
Örnek 1:

Girdi:
n = 2, m = 2
mat = [[1, 1],
       [1, 1]]

       Organised By K. Umut Araz

Çıktı:
2

Açıklama: Kare alt matrisin maksimum boyutu 2'dir. Bu durumda matrisin kendisi en büyük boyutlu alt matristir.
---
Örnek 2:

Girdi:
n = 2, m = 2
mat = [[0, 0],
       [0, 0]]
Çıktı: 0

Açıklama: Matriste 1 yoktur.

Yaklaşım:
Orijinal matrisle aynı boyutlarda, tüm elemanları 0 olan başka bir matris (dp) başlatıyoruz.

dp_array(i,j), orijinal matrisin (i,j) indeksine sahip hücresinin sağ alt köşesi olan en büyük karenin kenar uzunluğunu temsil eder.

(0,0) indeksinden başlayarak, orijinal matriste bulunan her 1 için, mevcut elemanın değerini şu şekilde güncelliyoruz:

dp_array(i,j) = min(dp_array(i-1,j), dp_array(i-1,j-1), dp_array(i,j-1)) + 1.
"""


def en_buyuk_kare_alani_bul(rows: int, cols: int, mat: list[list[int]]) -> int:
    """
    Fonksiyon, maksimum alanı bulan kareyi bulursa largest_square_area[0]'ı günceller.

    Burada dp_array kullanmıyoruz, bu nedenle zaman karmaşıklığı üssel olacaktır.

    >>> en_buyuk_kare_alani_bul(2, 2, [[1,1], [1,1]])
    2
    >>> en_buyuk_kare_alani_bul(2, 2, [[0,0], [0,0]])
    0
    """

    def kare_alani_guncelle(row: int, col: int) -> int:
        # TEMEL DURUM
        if row >= rows or col >= cols:
            return 0

        sag = kare_alani_guncelle(row, col + 1)
        diagonal = kare_alani_guncelle(row + 1, col + 1)
        asagi = kare_alani_guncelle(row + 1, col)

        if mat[row][col]:
            alt_problem_cozumu = 1 + min([sag, diagonal, asagi])
            en_buyuk_kare_alani[0] = max(en_buyuk_kare_alani[0], alt_problem_cozumu)
            return alt_problem_cozumu
        else:
            return 0

    en_buyuk_kare_alani = [0]
    kare_alani_guncelle(0, 0)
    return en_buyuk_kare_alani[0]


def en_buyuk_kare_alani_bul_dp_ile(rows: int, cols: int, mat: list[list[int]]) -> int:
    """
    Fonksiyon, maksimum alanı bulan kareyi bulursa largest_square_area[0]'ı günceller.

    Burada dp_array kullanıyoruz, bu nedenle zaman karmaşıklığı O(N^2) olacaktır.

    >>> en_buyuk_kare_alani_bul_dp_ile(2, 2, [[1,1], [1,1]])
    2
    >>> en_buyuk_kare_alani_bul_dp_ile(2, 2, [[0,0], [0,0]])
    0
    """

    def kare_alani_guncelle_dp_ile(row: int, col: int, dp_array: list[list[int]]) -> int:
        if row >= rows or col >= cols:
            return 0
        if dp_array[row][col] != -1:
            return dp_array[row][col]

        sag = kare_alani_guncelle_dp_ile(row, col + 1, dp_array)
        diagonal = kare_alani_guncelle_dp_ile(row + 1, col + 1, dp_array)
        asagi = kare_alani_guncelle_dp_ile(row + 1, col, dp_array)

        if mat[row][col]:
            alt_problem_cozumu = 1 + min([sag, diagonal, asagi])
            en_buyuk_kare_alani[0] = max(en_buyuk_kare_alani[0], alt_problem_cozumu)
            dp_array[row][col] = alt_problem_cozumu
            return alt_problem_cozumu
        else:
            return 0

    en_buyuk_kare_alani = [0]
    dp_array = [[-1] * cols for _ in range(rows)]
    kare_alani_guncelle_dp_ile(0, 0, dp_array)

    return en_buyuk_kare_alani[0]


def en_buyuk_kare_alani_bul_asagidan_yukarı(rows: int, cols: int, mat: list[list[int]]) -> int:
    """
    Fonksiyon, en büyük kare alanını günceller, aşağıdan yukarı yaklaşım kullanarak.

    >>> en_buyuk_kare_alani_bul_asagidan_yukarı(2, 2, [[1,1], [1,1]])
    2
    >>> en_buyuk_kare_alani_bul_asagidan_yukarı(2, 2, [[0,0], [0,0]])
    0
    """
    dp_array = [[0] * (cols + 1) for _ in range(rows + 1)]
    en_buyuk_kare_alani = 0
    for row in range(rows - 1, -1, -1):
        for col in range(cols - 1, -1, -1):
            sag = dp_array[row][col + 1]
            diagonal = dp_array[row + 1][col + 1]
            asagi = dp_array[row + 1][col]

            if mat[row][col] == 1:
                dp_array[row][col] = 1 + min(sag, diagonal, asagi)
                en_buyuk_kare_alani = max(dp_array[row][col], en_buyuk_kare_alani)
            else:
                dp_array[row][col] = 0

    return en_buyuk_kare_alani


def en_buyuk_kare_alani_bul_asagidan_yukarı_alan_optimizasyonu(
    rows: int, cols: int, mat: list[list[int]]
) -> int:
    """
    Fonksiyon, en büyük kare alanını günceller, aşağıdan yukarı
    yaklaşım kullanarak. Alan optimizasyonu ile.

    >>> en_buyuk_kare_alani_bul_asagidan_yukarı_alan_optimizasyonu(2, 2, [[1,1], [1,1]])
    2
    >>> en_buyuk_kare_alani_bul_asagidan_yukarı_alan_optimizasyonu(2, 2, [[0,0], [0,0]])
    0
    """
    mevcut_satir = [0] * (cols + 1)
    sonraki_satir = [0] * (cols + 1)
    en_buyuk_kare_alani = 0
    for row in range(rows - 1, -1, -1):
        for col in range(cols - 1, -1, -1):
            sag = mevcut_satir[col + 1]
            diagonal = sonraki_satir[col + 1]
            asagi = sonraki_satir[col]

            if mat[row][col] == 1:
                mevcut_satir[col] = 1 + min(sag, diagonal, asagi)
                en_buyuk_kare_alani = max(mevcut_satir[col], en_buyuk_kare_alani)
            else:
                mevcut_satir[col] = 0
        sonraki_satir = mevcut_satir

    return en_buyuk_kare_alani


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(en_buyuk_kare_alani_bul_asagidan_yukarı(2, 2, [[1, 1], [1, 1]]))
