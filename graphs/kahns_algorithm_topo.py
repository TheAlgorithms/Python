def topolojik_sıralama(grafik: dict[int, list[int]]) -> list[int] | None:
    """
    Kahn'ın Algoritmasını kullanarak Yönlendirilmiş Asiklik Grafiğin (DAG)
    topolojik sıralamasını gerçekleştirir.

    Topolojik sıralama, bir grafikteki düğümlerin doğrusal bir sıralamasıdır,
    öyle ki her yönlendirilmiş kenar u → v için, u düğümü v düğümünden önce gelir.

    Parametreler:
    grafik: Anahtarların düğümleri, değerlerin ise komşu düğümlerin listelerini
            temsil ettiği yönlendirilmiş grafiğin komşuluk listesi.

    Döndürür:
    Eğer grafik bir DAG ise düğümlerin topolojik sıralamasını döndürür.
    Eğer grafik bir döngü içeriyorsa None döner.

    Örnek:
    >>> grafik = {0: [1, 2], 1: [3], 2: [3], 3: [4, 5], 4: [], 5: []}
    >>> topolojik_sıralama(grafik)
    [0, 1, 2, 3, 4, 5]

    >>> döngülü_grafik = {0: [1], 1: [2], 2: [0]}
    >>> topolojik_sıralama(döngülü_grafik)
    """

    #Produced By K. Umut Araz

    giriş_derecesi = [0] * len(grafik)
    kuyruk = []
    topo_sıra = []
    işlenen_düğüm_sayısı = 0

    # Her düğümün giriş derecesini hesapla
    for değerler in grafik.values():
        for i in değerler:
            giriş_derecesi[i] += 1

    # Giriş derecesi 0 olan tüm düğümleri kuyruğa ekle
    for i in range(len(giriş_derecesi)):
        if giriş_derecesi[i] == 0:
            kuyruk.append(i)

    # BFS gerçekleştir
    while kuyruk:
        düğüm = kuyruk.pop(0)
        işlenen_düğüm_sayısı += 1
        topo_sıra.append(düğüm)

        # Komşuları dolaş
        for komşu in grafik[düğüm]:
            giriş_derecesi[komşu] -= 1
            if giriş_derecesi[komşu] == 0:
                kuyruk.append(komşu)

    if işlenen_düğüm_sayısı != len(grafik):
        return None  # döngü nedeniyle geçerli bir topolojik sıralama yok
    return topo_sıra  # geçerli topolojik sıralama


if __name__ == "__main__":
    import doctest

    doctest.testmod()
