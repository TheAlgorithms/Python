"""
Matris zincirini çarpmak için gereken minimum çarpma sayısını bulun.
Referans: https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/

Algoritmanın ilginç gerçek dünya uygulamaları vardır. Örnek:
1. Bilgisayar Grafikleri'nde görüntü dönüşümleri, çünkü görüntüler matrislerden oluşur.
2. En az işlem gücü kullanarak cebir alanında karmaşık polinom denklemlerini çözmek.
3. Makroekonomik kararların genel etkisini hesaplamak, çünkü ekonomik denklemler bir
   dizi değişken içerir.
4. Matris çarpımı, engellerin konumunu ve yönünü kısa sürede doğru bir şekilde belirleyebildiği için
   kendi kendine giden araba navigasyonu daha doğru hale getirilebilir.

Python doctest'leri aşağıdaki komutla çalıştırılabilir:
python -m doctest -v matrix_chain_multiply.py

arr[] dizisi verildiğinde, bu dizi 2D matrislerin zincirini temsil eder, böylece
i. matrisin boyutu arr[i-1]*arr[i] olur.
Örneğin, arr = [40, 20, 30, 10, 30] olduğunu varsayalım, bu 40*20, 20*30, 30*10 ve 10*30
boyutlarında 4 matrisimiz olduğu anlamına gelir.

matrix_chain_multiply() fonksiyonu, zinciri çarpmak için gereken minimum çarpma sayısını
döndüren bir tamsayı döndürür.

Burada gerçek çarpma işlemini gerçekleştirmemize gerek yok.
Sadece çarpma işlemini gerçekleştirme sırasını belirlememiz gerekiyor.

İpuçları:
1. Boyutları m*p ve p*n olan 2 matrisi çarpmak için gereken çarpma sayısı (yani maliyet) m*p*n'dir.
2. Matris çarpma maliyeti birleşimlidir, yani (M1*M2)*M3 != M1*(M2*M3)
3. Matris çarpma işlemi değişmeli değildir. Yani, M1*M2, M2*M1 yapılabilir anlamına gelmez.
4. Gerekli sırayı belirlemek için farklı kombinasyonları deneyebiliriz.
Bu nedenle, bu problem örtüşen alt problemler içerir ve özyineleme kullanılarak çözülebilir.
Optimal zaman karmaşıklığı için Dinamik Programlama kullanırız.

Örnek giriş:
arr = [40, 20, 30, 10, 30]
çıkış: 26000
"""

from collections.abc import Iterator
from contextlib import contextmanager
from functools import cache
from sys import maxsize


def matrix_chain_multiply(arr: list[int]) -> int:
    """
    Matris zincirini çarpmak için gereken minimum çarpma sayısını bulun

    Args:
        arr: Girdi tamsayı dizisi.

    Returns:
        Zinciri çarpmak için gereken minimum çarpma sayısı

    Örnekler:
        >>> matrix_chain_multiply([1, 2, 3, 4, 3])
        30
        >>> matrix_chain_multiply([10])
        0
        >>> matrix_chain_multiply([10, 20])
        0
        >>> matrix_chain_multiply([19, 2, 19])
        722
        >>> matrix_chain_multiply(list(range(1, 100)))
        323398

        # >>> matrix_chain_multiply(list(range(1, 251)))
        # 2626798
    """
    if len(arr) < 2:
        return 0
    # 2D dp matrisini başlatma
    n = len(arr)
    dp = [[maxsize for j in range(n)] for i in range(n)]
    # (i*k) ve (k*j) boyutlarındaki matrislerin çarpma maliyetinin minimum olmasını istiyoruz.
    # Bu maliyet arr[i-1]*arr[k]*arr[j] dir.
    for i in range(n - 1, 0, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = 0
                continue
            for k in range(i, j):
                dp[i][j] = min(
                    dp[i][j], dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                )

    return dp[1][n - 1]


def matrix_chain_order(dims: list[int]) -> int:
    """
    Kaynak: https://en.wikipedia.org/wiki/Matrix_chain_multiplication
    Dinamik programlama çözümü, özyinelemeli çözümden daha hızlıdır ve
    daha büyük girdileri işleyebilir.
    >>> matrix_chain_order([1, 2, 3, 4, 3])
    30
    >>> matrix_chain_order([10])
    0
    >>> matrix_chain_order([10, 20])
    0
    >>> matrix_chain_order([19, 2, 19])
    722
    >>> matrix_chain_order(list(range(1, 100)))
    323398

    # >>> matrix_chain_order(list(range(1, 251)))  # RecursionError oluşmadan önceki maksimum
    # 2626798
    """

    @cache
    def a(i: int, j: int) -> int:
        return min(
            (a(i, k) + dims[i] * dims[k] * dims[j] + a(k, j) for k in range(i + 1, j)),
            default=0,
        )

    return a(0, len(dims) - 1)


@contextmanager
def elapsed_time(msg: str) -> Iterator:
    # print(f"Başlıyor: {msg}")
    from time import perf_counter_ns

    start = perf_counter_ns()
    yield
    print(f"Bitti: {msg} {(perf_counter_ns() - start) / 10 ** 9} saniye sürdü.")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    with elapsed_time("matrix_chain_order"):
        print(f"{matrix_chain_order(list(range(1, 251)))}")
    with elapsed_time("matrix_chain_multiply"):
        print(f"{matrix_chain_multiply(list(range(1, 251)))}")
    with elapsed_time("matrix_chain_order"):
        print(f"{matrix_chain_order(list(range(1, 251)))}")
    with elapsed_time("matrix_chain_multiply"):
        print(f"{matrix_chain_multiply(list(range(1, 251)))}")
