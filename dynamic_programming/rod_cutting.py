"""
Bu modül, çubuk kesme problemi için iki farklı uygulama sağlar:
1. Üstel çalışma zamanına sahip olan naif özyinelemeli bir uygulama
2. Kare çalışma zamanına sahip iki dinamik programlama uygulaması

Çubuk kesme problemi, her bir tam sayı uzunluğundaki çubuk parçaları için verilen fiyat listesine göre
bir çubuktan elde edilebilecek maksimum geliri bulma problemidir. Maksimum gelir, çubuğu kesip parçaları
ayrı ayrı satarak veya çubuğu hiç kesmeden elde edilebilir.

"""


def naif_cubuk_kesme_ozinelemeli(n: int, fiyatlar: list) -> int:
    """
    Dinamik programlamanın avantajını kullanmadan naif bir şekilde çubuk kesme problemini çözer.
    Sonuç olarak, aynı alt problemler birden çok kez çözülür ve bu da üstel çalışma zamanına yol açar.

    Çalışma Zamanı: O(2^n)

    Parametreler
    -------
    n: int, çubuğun uzunluğu
    fiyatlar: list, her bir çubuk parçasının fiyatları. ``fiyatlar[i-1]`` uzunluğu ``i`` olan bir çubuğun fiyatıdır

    Dönüş
    -------
    Verilen fiyat listesine göre n uzunluğundaki bir çubuk için elde edilebilecek maksimum gelir

    Örnekler
    --------
    >>> naif_cubuk_kesme_ozinelemeli(4, [1, 5, 8, 9])
    10
    >>> naif_cubuk_kesme_ozinelemeli(10, [1, 5, 8, 9, 10, 17, 17, 20, 24, 30])
    30
    """

    _argumanlari_kontrol_et(n, fiyatlar)
    if n == 0:
        return 0
    max_gelir = float("-inf")
    for i in range(1, n + 1):
        max_gelir = max(
            max_gelir, fiyatlar[i - 1] + naif_cubuk_kesme_ozinelemeli(n - i, fiyatlar)
        )

    return max_gelir


def yukaridan_asagiya_cubuk_kesme(n: int, fiyatlar: list) -> int:
    """
    Çubuk kesme problemi için memoization kullanarak yukarıdan aşağıya dinamik programlama çözümü oluşturur.
    Bu fonksiyon, _yukaridan_asagiya_cubuk_kesme_ozinelemeli için bir sarmalayıcı olarak hizmet eder.

    Çalışma Zamanı: O(n^2)

    Parametreler
    --------
    n: int, çubuğun uzunluğu
    fiyatlar: list, her bir çubuk parçasının fiyatları. ``fiyatlar[i-1]`` uzunluğu ``i`` olan bir çubuğun fiyatıdır

    Not
    ----
    Kolaylık sağlamak ve Python'un listelerinin 0-indeksli olmasından dolayı, max_gelir uzunluğu n + 1'dir,
    0 uzunluğundaki bir çubuktan elde edilebilecek gelir için.

    Dönüş
    -------
    Verilen fiyat listesine göre n uzunluğundaki bir çubuk için elde edilebilecek maksimum gelir

    Örnekler
    -------
    >>> yukaridan_asagiya_cubuk_kesme(4, [1, 5, 8, 9])
    10
    >>> yukaridan_asagiya_cubuk_kesme(10, [1, 5, 8, 9, 10, 17, 17, 20, 24, 30])
    30
    """
    _argumanlari_kontrol_et(n, fiyatlar)
    max_gelir = [float("-inf") for _ in range(n + 1)]
    return _yukaridan_asagiya_cubuk_kesme_ozinelemeli(n, fiyatlar, max_gelir)


def _yukaridan_asagiya_cubuk_kesme_ozinelemeli(n: int, fiyatlar: list, max_gelir: list) -> int:
    """
    Çubuk kesme problemi için memoization kullanarak yukarıdan aşağıya dinamik programlama çözümü oluşturur.

    Çalışma Zamanı: O(n^2)

    Parametreler
    --------
    n: int, çubuğun uzunluğu
    fiyatlar: list, her bir çubuk parçasının fiyatları. ``fiyatlar[i-1]`` uzunluğu ``i`` olan bir çubuğun fiyatıdır
    max_gelir: list, hesaplanmış maksimum gelir. ``max_gelir[i]`` uzunluğu ``i`` olan bir çubuk için elde edilebilecek maksimum gelirdir

    Dönüş
    -------
    Verilen fiyat listesine göre n uzunluğundaki bir çubuk için elde edilebilecek maksimum gelir
    """
    if max_gelir[n] >= 0:
        return max_gelir[n]
    elif n == 0:
        return 0
    else:
        max_gelir_n = float("-inf")
        for i in range(1, n + 1):
            max_gelir_n = max(
                max_gelir_n,
                fiyatlar[i - 1] + _yukaridan_asagiya_cubuk_kesme_ozinelemeli(n - i, fiyatlar, max_gelir),
            )

        max_gelir[n] = max_gelir_n

    return max_gelir[n]


def asagidan_yukariya_cubuk_kesme(n: int, fiyatlar: list) -> int:
    """
    Çubuk kesme problemi için aşağıdan yukarıya dinamik programlama çözümü oluşturur

    Çalışma Zamanı: O(n^2)

    Parametreler
    ----------
    n: int, çubuğun maksimum uzunluğu
    fiyatlar: list, her bir çubuk parçasının fiyatları. ``fiyatlar[i-1]`` uzunluğu ``i`` olan bir çubuğun fiyatıdır

    Dönüş
    -------
    Verilen fiyat listesine göre n uzunluğundaki bir çubuktan elde edilebilecek maksimum gelir

    Örnekler
    -------
    >>> asagidan_yukariya_cubuk_kesme(4, [1, 5, 8, 9])
    10
    >>> asagidan_yukariya_cubuk_kesme(10, [1, 5, 8, 9, 10, 17, 17, 20, 24, 30])
    30
    """
    _argumanlari_kontrol_et(n, fiyatlar)

    # max_gelir uzunluğu n + 1'dir, 0 uzunluğundaki bir çubuktan elde edilebilecek gelir için.
    max_gelir = [float("-inf") for _ in range(n + 1)]
    max_gelir[0] = 0

    for i in range(1, n + 1):
        max_gelir_i = max_gelir[i]
        for j in range(1, i + 1):
            max_gelir_i = max(max_gelir_i, fiyatlar[j - 1] + max_gelir[i - j])

        max_gelir[i] = max_gelir_i

    return max_gelir[n]


def _argumanlari_kontrol_et(n: int, fiyatlar: list):
    """
    Çubuk kesme algoritmaları için temel argüman kontrolleri

    n: int, çubuğun uzunluğu
    fiyatlar: list, her bir çubuk parçasının fiyat listesi.

    ValueError fırlatır:

    eğer n negatifse veya fiyat listesinde çubuk uzunluğundan daha az öğe varsa
    """
    if n < 0:
        msg = f"n 0 veya daha büyük olmalıdır. Verilen n = {n}"
        raise ValueError(msg)

    if n > len(fiyatlar):
        msg = (
            "Her bir tam sayı uzunluğundaki çubuk parçasının bir fiyatı olmalıdır. "
            f"Verilen n = {n} ancak fiyatlar uzunluğu = {len(fiyatlar)}"
        )
        raise ValueError(msg)


def main():
    fiyatlar = [6, 10, 12, 15, 20, 23]
    n = len(fiyatlar)

    # En iyi gelir, çubuğu 6 parçaya kesmekten gelir, her biri
    # 1 uzunluğunda olup 6 * 6 = 36 gelir sağlar.
    beklenen_max_gelir = 36

    max_gelir_yukaridan_asagiya = yukaridan_asagiya_cubuk_kesme(n, fiyatlar)
    max_gelir_asagidan_yukariya = asagidan_yukariya_cubuk_kesme(n, fiyatlar)
    max_gelir_naif = naif_cubuk_kesme_ozinelemeli(n, fiyatlar)

    assert beklenen_max_gelir == max_gelir_yukaridan_asagiya
    assert max_gelir_yukaridan_asagiya == max_gelir_asagidan_yukariya
    assert max_gelir_asagidan_yukariya == max_gelir_naif


if __name__ == "__main__":
    main()
