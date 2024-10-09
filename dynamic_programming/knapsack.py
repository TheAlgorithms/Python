"""
n öğesinin ağırlıkları ve değerleri verildiğinde, bu öğeleri bir sırt çantasına
yerleştirerek sırt çantasındaki toplam değeri en üst düzeye çıkarın.

Not: Yalnızca tam sayı ağırlıkları 0-1 sırt çantası problemi dinamik programlama
kullanılarak çözülebilir.
"""


def mf_knapsack(i, wt, val, j):
    """
    Bu kod, bellek fonksiyonları kavramını içerir. Burada, aşağıdaki örnekte
    olduğu gibi gerekli alt problemleri çözüyoruz.
    F, -1'lerle doldurulmuş 2D bir dizidir.
    """
    global f  # sırt çantası için global dp tablosu
    if f[i][j] < 0:
        if j < wt[i - 1]:
            val = mf_knapsack(i - 1, wt, val, j)
        else:
            val = max(
                mf_knapsack(i - 1, wt, val, j),
                mf_knapsack(i - 1, wt, val, j - wt[i - 1]) + val[i - 1],
            )
        f[i][j] = val
    return f[i][j]


def knapsack(w, wt, val, n):
    dp = [[0] * (w + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w_ in range(1, w + 1):
            if wt[i - 1] <= w_:
                dp[i][w_] = max(val[i - 1] + dp[i - 1][w_ - wt[i - 1]], dp[i - 1][w_])
            else:
                dp[i][w_] = dp[i - 1][w_]

    return dp[n][w_], dp


def knapsack_with_example_solution(w: int, wt: list, val: list):
    """
    Tam sayı ağırlıkları sırt çantası problemini çözer ve
    birkaç olası optimal alt kümeden birini döndürür.

    Parametreler
    ---------

    W: int, verilen sırt çantası probleminin toplam maksimum ağırlığı.
    wt: list, tüm öğelerin ağırlık vektörü, burada wt[i], i. öğenin ağırlığıdır.
    val: list, tüm öğelerin değer vektörü, burada val[i], i. öğenin değeridir.

    Dönüş
    -------
    optimal_val: float, verilen sırt çantası problemi için optimal değer.
    example_optional_set: set, optimal değere yol açan optimal alt kümelerden
    birinin indeksleri.

    Örnekler
    -------
    >>> knapsack_with_example_solution(10, [1, 3, 5, 2], [10, 20, 100, 22])
    (142, {2, 3, 4})
    >>> knapsack_with_example_solution(6, [4, 3, 2, 3], [3, 2, 4, 4])
    (8, {3, 4})
    >>> knapsack_with_example_solution(6, [4, 3, 2, 3], [3, 2, 4])
    Traceback (most recent call last):
        ...
    ValueError: Ağırlıkların sayısı değerlerin sayısıyla aynı olmalıdır.
    Ancak 4 ağırlık ve 3 değer aldınız.
    """
    if not (isinstance(wt, (list, tuple)) and isinstance(val, (list, tuple))):
        raise ValueError(
            "Hem ağırlıklar hem de değerler vektörleri ya listeler ya da demetler olmalıdır"
        )

    num_items = len(wt)
    if num_items != len(val):
        msg = (
            "Ağırlıkların sayısı değerlerin sayısıyla aynı olmalıdır.\n"
            f"Ancak {num_items} ağırlık ve {len(val)} değer aldınız."
        )
        raise ValueError(msg)
    for i in range(num_items):
        if not isinstance(wt[i], int):
            msg = (
                "Tüm ağırlıklar tam sayı olmalıdır ancak "
                f"{i} indeksinde {type(wt[i])} türünde ağırlık aldınız."
            )
            raise TypeError(msg)

    optimal_val, dp_table = knapsack(w, wt, val, num_items)
    example_optional_set: set = set()
    _construct_solution(dp_table, wt, num_items, w, example_optional_set)

    return optimal_val, example_optional_set


def _construct_solution(dp: list, wt: list, i: int, j: int, optimal_set: set):
    """
    Doldurulmuş bir DP tablosu ve ağırlık vektörü verildiğinde
    optimal alt kümelerden birini yeniden oluşturur.

    Parametreler
    ---------

    dp: list of list, çözülmüş tam sayı ağırlıklı dinamik programlama probleminin tablosu.

    wt: list or tuple, öğelerin ağırlık vektörü.
    i: int, dikkate alınan öğenin indeksi.
    j: int, mevcut olası maksimum ağırlık.
    optimal_set: set, şimdiye kadar olan optimal alt küme. Bu fonksiyon tarafından değiştirilir.

    Dönüş
    -------
    Yok

    """
    # i. öğe için maksimum ağırlık j'de optimal alt kümenin bir parçası olması için,
    # (i, j) deki optimal değer (i-1, j) deki optimal değerden büyük olmalıdır.
    # burada i - 1, verilen maksimum ağırlıkta yalnızca önceki öğeleri dikkate alır.
    if i > 0 or j > 0:
        if dp[i - 1][j] == dp[i][j]:
            _construct_solution(dp, wt, i - 1, j, optimal_set)
        else:
            optimal_set.add(i)
            _construct_solution(dp, wt, i - 1, j - wt[i - 1], optimal_set)


if __name__ == "__main__":
    """
    Sırt çantası için test durumu ekleme
    """
    val = [3, 2, 4, 4]
    wt = [4, 3, 2, 3]
    n = 4
    w = 6
    f = [[0] * (w + 1)] + [[0] + [-1] * (w + 1) for _ in range(n + 1)]
    optimal_solution, _ = knapsack(w, wt, val, n)
    print(optimal_solution)
    print(mf_knapsack(n, wt, val, w))  # n ve w değiştirildi

    # örnekle dinamik programlama problemini test etme
    # yukarıdaki örnek için optimal alt kümeler 3 ve 4. öğelerdir
    optimal_solution, optimal_subset = knapsack_with_example_solution(w, wt, val)
    assert optimal_solution == 8
    assert optimal_subset == {3, 4}
    print("optimal_değer = ", optimal_solution)
    print("Optimal değere karşılık gelen optimal alt kümelerden biri", optimal_subset)
