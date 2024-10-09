"""
Hamiltonian döngüsü (Hamiltonian devresi), bir grafikte her düğümü
tam olarak bir kez ziyaret eden bir grafik döngüsüdür.
Bu tür yolların ve döngülerin grafikte var olup olmadığını belirlemek,
NP-tam olan 'Hamiltonian yol problemi'dir.

Wikipedia: https://en.wikipedia.org/wiki/Hamiltonian_path
"""


def geçerli_bağlantı(
    grafik: list[list[int]], sonraki_düğüm: int, mevcut_indeks: int, yol: list[int]
) -> bool:
    """
    Sonraki düğümü yola eklemenin mümkün olup olmadığını kontrol eder
    1. Mevcut ve sonraki düğüm arasında yol olmalıdır
    2. Sonraki düğüm yol içinde olmamalıdır
    Eğer her iki doğrulama da başarılı olursa, bu düğümleri bağlamanın mümkün olduğunu
    belirten True döndürürüz, aksi takdirde False döndürürüz.

    Durum 1: Ana fonksiyondaki gibi tam grafiği kullanın, başlatılmış değerlerle
    >>> grafik = [[0, 1, 0, 1, 0],
    ...           [1, 0, 1, 1, 1],
    ...           [0, 1, 0, 0, 1],
    ...           [1, 1, 0, 0, 1],
    ...           [0, 1, 1, 1, 0]]
    >>> yol = [0, -1, -1, -1, -1, 0]
    >>> mevcut_indeks = 1
    >>> sonraki_düğüm = 1
    >>> geçerli_bağlantı(grafik, sonraki_düğüm, mevcut_indeks, yol)
    True

    Durum 2: Aynı grafik, ancak yolda zaten bulunan bir düğüme bağlanmaya çalışılıyor
    >>> yol = [0, 1, 2, 4, -1, 0]
    >>> mevcut_indeks = 4
    >>> sonraki_düğüm = 1
    >>> geçerli_bağlantı(grafik, sonraki_düğüm, mevcut_indeks, yol)
    False
    """

    # 1. Mevcut ve sonraki düğümler arasında yol olup olmadığını doğrula
    if grafik[yol[mevcut_indeks - 1]][sonraki_düğüm] == 0:
        return False

    # 2. Sonraki düğümün yol içinde olup olmadığını doğrula
    return not any(düğüm == sonraki_düğüm for düğüm in yol)


def yardımcı_hamilton_döngüsü(grafik: list[list[int]], yol: list[int], mevcut_indeks: int) -> bool:
    """
    Pseudo-Kod
    Temel Durum:
    1. Tüm düğümleri ziyaret edip etmediğimizi kontrol edin
        1.1 Eğer son ziyaret edilen düğüm başlangıç düğümüne yol içeriyorsa True döndür
            aksi takdirde False döndür
    Özyinelemeli Adım:
    2. Her düğüm için yineleyin
        Sonraki düğümün mevcut düğümden geçiş için geçerli olup olmadığını kontrol edin
            2.1 Sonraki düğümü bir sonraki geçiş olarak hatırlayın
            2.2 Özyinelemeli çağrı yapın ve bu düğüme gitmenin sorunu çözüp çözmediğini kontrol edin
            2.3 Eğer sonraki düğüm çözüme yol açarsa True döndür
            2.4 Aksi takdirde geri izleyin, hatırlanan düğümü silin

    Durum 1: Ana fonksiyondaki gibi tam grafiği kullanın, başlatılmış değerlerle
    >>> grafik = [[0, 1, 0, 1, 0],
    ...           [1, 0, 1, 1, 1],
    ...           [0, 1, 0, 0, 1],
    ...           [1, 1, 0, 0, 1],
    ...           [0, 1, 1, 1, 0]]
    >>> yol = [0, -1, -1, -1, -1, 0]
    >>> mevcut_indeks = 1
    >>> yardımcı_hamilton_döngüsü(grafik, yol, mevcut_indeks)
    True
    >>> yol
    [0, 1, 2, 4, 3, 0]

    Durum 2: Önceki durumda olduğu gibi tam grafiği kullanın, ancak hesaplamanın ortasından alınan özelliklerle
    >>> grafik = [[0, 1, 0, 1, 0],
    ...           [1, 0, 1, 1, 1],
    ...           [0, 1, 0, 0, 1],
    ...           [1, 1, 0, 0, 1],
    ...           [0, 1, 1, 1, 0]]
    >>> yol = [0, 1, 2, -1, -1, 0]
    >>> mevcut_indeks = 3
    >>> yardımcı_hamilton_döngüsü(grafik, yol, mevcut_indeks)
    True
    >>> yol
    [0, 1, 2, 4, 3, 0]
    """

    # Temel Durum
    if mevcut_indeks == len(grafik):
        # mevcut ve başlangıç düğümleri arasında yol olup olmadığını döndür
        return grafik[yol[mevcut_indeks - 1]][yol[0]] == 1

    # Özyinelemeli Adım
    for sonraki_düğüm in range(len(grafik)):
        if geçerli_bağlantı(grafik, sonraki_düğüm, mevcut_indeks, yol):
            # Mevcut düğümü bir sonraki geçiş olarak yola ekle
            yol[mevcut_indeks] = sonraki_düğüm
            # Oluşturulan yolu doğrula
            if yardımcı_hamilton_döngüsü(grafik, yol, mevcut_indeks + 1):
                return True
            # Geri izleme
            yol[mevcut_indeks] = -1
    return False


def hamilton_döngüsü(grafik: list[list[int]], başlangıç_indeksi: int = 0) -> list[int]:
    r"""
    yardımcı_hamilton_döngüsü adlı alt yordamı çağırmak için sarmalayıcı fonksiyon,
    bu ya Hamiltonian döngüsünü belirten düğümlerin dizisini ya da Hamiltonian döngüsünün
    bulunmadığını belirten boş bir liste döndürecektir.
    Durum 1:
    Aşağıdaki grafik 5 kenardan oluşur.
    Yakından bakarsak, birden fazla Hamiltonian döngüsü olduğunu görebiliriz.
    Örneğin, bir sonuç şu şekilde yinelediğimizde elde edilir:
    (0)->(1)->(2)->(4)->(3)->(0)

    (0)---(1)---(2)
     |   /   \   |
     |  /     \  |
     | /       \ |
     |/         \|
    (3)---------(4)
    >>> grafik = [[0, 1, 0, 1, 0],
    ...           [1, 0, 1, 1, 1],
    ...           [0, 1, 0, 0, 1],
    ...           [1, 1, 0, 0, 1],
    ...           [0, 1, 1, 1, 0]]
    >>> hamilton_döngüsü(grafik)
    [0, 1, 2, 4, 3, 0]

    Durum 2:
    Durum 1'de olduğu gibi aynı grafik, başlangıç indeksini varsayılandan 3'e değiştirdik

    (0)---(1)---(2)
     |   /   \   |
     |  /     \  |
     | /       \ |
     |/         \|
    (3)---------(4)
    >>> grafik = [[0, 1, 0, 1, 0],
    ...           [1, 0, 1, 1, 1],
    ...           [0, 1, 0, 0, 1],
    ...           [1, 1, 0, 0, 1],
    ...           [0, 1, 1, 1, 0]]
    >>> hamilton_döngüsü(grafik, 3)
    [3, 0, 1, 2, 4, 3]

    Durum 3:
    Aşağıdaki Grafik, daha önce olduğu gibi, ancak 3-4 kenarı kaldırıldı.
    Sonuç olarak artık Hamiltonian Döngüsü yok.

    (0)---(1)---(2)
     |   /   \   |
     |  /     \  |
     | /       \ |
     |/         \|
    (3)         (4)
    >>> grafik = [[0, 1, 0, 1, 0],
    ...           [1, 0, 1, 1, 1],
    ...           [0, 1, 0, 0, 1],
    ...           [1, 1, 0, 0, 0],
    ...           [0, 1, 1, 0, 0]]
    >>> hamilton_döngüsü(grafik,4)
    []
    """

    # Henüz ziyaret edilmediğini belirten -1 ile yolu başlat
    yol = [-1] * (len(grafik) + 1)
    # yolu başlangıç indeksi ile başlat ve bitir
    yol[0] = yol[-1] = başlangıç_indeksi
    # değerlendir ve eğer cevap bulursak yolu döndür, aksi takdirde boş dizi döndür
    return yol if yardımcı_hamilton_döngüsü(grafik, yol, 1) else []
