"""
Graf Boyama, "m boyama problemi" olarak da adlandırılır
verilen bir grafiği en fazla m renk ile boyamaktan oluşur
öyle ki bitişik düğümlere aynı renk atanmaz

Wikipedia: https://en.wikipedia.org/wiki/Graph_coloring
"""


def geçerli_boyama(
    komşular: list[int], boyanmış_düğümler: list[int], renk: int
) -> bool:
    """
    Her komşu için boyama kısıtının sağlanıp sağlanmadığını kontrol edin
    Eğer komşulardan herhangi biri kısıtı sağlamazsa False döndür
    Eğer tüm komşular kısıtı sağlarsa True döndür

    >>> komşular = [0,1,0,1,0]
    >>> boyanmış_düğümler = [0, 2, 1, 2, 0]

    >>> renk = 1
    >>> geçerli_boyama(komşular, boyanmış_düğümler, renk)
    True

    >>> renk = 2
    >>> geçerli_boyama(komşular, boyanmış_düğümler, renk)
    False
    """
    # Herhangi bir komşu kısıtları sağlamıyor mu
    return not any(
        komşu == 1 and boyanmış_düğümler[i] == renk
        for i, komşu in enumerate(komşular)
    )


def yardımcı_boya(
    grafik: list[list[int]], max_renk: int, boyanmış_düğümler: list[int], indeks: int
) -> bool:
    """
    Pseudo-Kod

    Temel Durum:
    1. Boyamanın tamamlanıp tamamlanmadığını kontrol edin
        1.1 Eğer tamamlanmışsa True döndür (grafiği başarıyla boyadığımız anlamına gelir)

    Özyinelemeli Adım:
    2. Her renk için yineleyin:
        Mevcut boyamanın geçerli olup olmadığını kontrol edin:
            2.1. Verilen düğümü boyayın
            2.2. Özyinelemeli çağrı yapın, bu boyamanın bir çözüme yol açıp açmadığını kontrol edin
            2.4. Eğer mevcut boyama bir çözüme yol açarsa döndür
            2.5. Verilen düğümü boyamayı geri alın

    >>> grafik = [[0, 1, 0, 0, 0],
    ...           [1, 0, 1, 0, 1],
    ...           [0, 1, 0, 1, 0],
    ...           [0, 1, 1, 0, 0],
    ...           [0, 1, 0, 0, 0]]
    >>> max_renk = 3
    >>> boyanmış_düğümler = [0, 1, 0, 0, 0]
    >>> indeks = 3

    >>> yardımcı_boya(grafik, max_renk, boyanmış_düğümler, indeks)
    True

    >>> max_renk = 2
    >>> yardımcı_boya(grafik, max_renk, boyanmış_düğümler, indeks)
    False
    """

    # Temel Durum
    if indeks == len(grafik):
        return True

    # Özyinelemeli Adım
    for i in range(max_renk):
        if geçerli_boyama(grafik[indeks], boyanmış_düğümler, i):
            # Mevcut düğümü boya
            boyanmış_düğümler[indeks] = i
            # Boyamayı doğrula
            if yardımcı_boya(grafik, max_renk, boyanmış_düğümler, indeks + 1):
                return True
            # Geri izleme
            boyanmış_düğümler[indeks] = -1
    return False


def boya(grafik: list[list[int]], max_renk: int) -> list[int]:
    """
    yardımcı_boya adlı alt yordamı çağırmak için sarmalayıcı fonksiyon
    bu ya True ya da False döndürecektir.
    Eğer True dönerse boyanmış_düğümler listesi doğru boyamalarla doldurulur

    >>> grafik = [[0, 1, 0, 0, 0],
    ...           [1, 0, 1, 0, 1],
    ...           [0, 1, 0, 1, 0],
    ...           [0, 1, 1, 0, 0],
    ...           [0, 1, 0, 0, 0]]

    >>> max_renk = 3
    >>> boya(grafik, max_renk)
    [0, 1, 0, 2, 0]

    >>> max_renk = 2
    >>> boya(grafik, max_renk)
    []
    """
    boyanmış_düğümler = [-1] * len(grafik)

    if yardımcı_boya(grafik, max_renk, boyanmış_düğümler, 0):
        return boyanmış_düğümler

    return []
