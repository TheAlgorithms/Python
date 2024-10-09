def gri_kod(bit_sayisi: int) -> list:
    """
    Bir tamsayı n alır ve n-bit gri kod dizisini döndürür.
    Bir n-bit gri kod dizisi, 2^n tamsayıdan oluşan bir dizidir ve:

    a) Her tamsayı [0, 2^n -1] aralığındadır (dahil)
    b) Dizi 0 ile başlar
    c) Bir tamsayı dizide en fazla bir kez görünür
    d) Her çift tamsayının ikili gösterimi tam olarak bir bit ile farklıdır
    e) İlk ve son bitin ikili gösterimi de tam olarak bir bit ile farklıdır

    >>> gri_kod(2)
    [0, 1, 3, 2]

    >>> gri_kod(1)
    [0, 1]

    >>> gri_kod(3)
    [0, 1, 3, 2, 6, 7, 5, 4]

    >>> gri_kod(-1)
    Traceback (most recent call last):
        ...
    ValueError: Verilen giriş pozitif olmalıdır

    >>> gri_kod(10.6)
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for <<: 'int' and 'float'
    """

    # bit_sayisi gri koddaki bit sayısını temsil eder
    if bit_sayisi < 0:
        raise ValueError("Verilen giriş pozitif olmalıdır")

    # oluşturulan dizi dizisini al
    dizi = gri_kod_dizisi_string(bit_sayisi)
    #
    # bunları tamsayıya dönüştür
    for i in range(len(dizi)):
        dizi[i] = int(dizi[i], 2)

    return dizi


def gri_kod_dizisi_string(bit_sayisi: int) -> list:
    """
    n-bit gri dizisini bit dizisi olarak çıktılar

    >>> gri_kod_dizisi_string(2)
    ['00', '01', '11', '10']

    >>> gri_kod_dizisi_string(1)
    ['0', '1']
    """

    # Yaklaşım özyinelemeli bir yaklaşımdır
    # Temel durum n = 0 veya n = 1 olduğunda elde edilir
    if bit_sayisi == 0:
        return ["0"]

    if bit_sayisi == 1:
        return ["0", "1"]

    dizi_uzunlugu = 1 << bit_sayisi  # dizinin uzunluğunu tanımlar
    # 1 << n, 2^n'ye eşdeğerdir

    # özyinelemeli cevap n-1 bit için cevap üretecektir
    daha_kucuk_dizi = gri_kod_dizisi_string(bit_sayisi - 1)

    dizi = []

    # oluşturulan daha küçük dizinin ilk yarısına 0 ekle
    for i in range(dizi_uzunlugu // 2):
        olusturulan_no = "0" + daha_kucuk_dizi[i]
        dizi.append(olusturulan_no)

    # ikinci yarısına 1 ekle ... listenin sonundan başla
    for i in reversed(range(dizi_uzunlugu // 2)):
        olusturulan_no = "1" + daha_kucuk_dizi[i]
        dizi.append(olusturulan_no)

    return dizi


if __name__ == "__main__":
    import doctest

    doctest.testmod()
