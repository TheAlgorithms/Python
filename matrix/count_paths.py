"""
Bir ızgara verildiğinde, sol üst köşe [0, 0] pozisyonundan başlayarak,
sağ alt köşe pozisyonuna ulaşmak için kaç farklı yol alabileceğinizi bulmak istiyorsunuz.

buradan başlayın  ->   0  0  0  0
                      1  1  0  0
                      0  0  0  1
                      0  1  0  0  <- burada bitirin
Tamamlanma noktasına ulaşmak için kaç 'farklı' yol alabilirsiniz?
Aşağıdaki geri izleme derinlik öncelikli arama algoritmasını kullanarak,
farklı benzersiz yolların sayısını (count) bulabilirsiniz.

'*' bir yolu gösterecektir.
Yukarıdaki örnekte, iki farklı yol vardır:
1.                2.
    *  *  *  0      *  *  *  *
    1  1  *  0      1  1  *  *
    0  0  *  1      0  0  *  1
    0  1  *  *      0  1  *  *
"""


def derinlik_oncelikli_arama(izgara: list[list[int]], satir: int, sutun: int, ziyaret: set) -> int:
    """
    Geri İzleme Derinlik Öncelikli Arama Algoritması

    Bir matrisin sol üst köşesinden başlayarak, matrisin sağ alt köşesine ulaşabilecek
    yolların sayısını sayın.
    1, bir engeli (ulaşılamaz) temsil eder.
    0, geçerli bir alanı (ulaşılabilir) temsil eder.

    0  0  0  0
    1  1  0  0
    0  0  0  1
    0  1  0  0
    >>> ızgara = [[0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]
    >>> derinlik_oncelikli_arama(ızgara, 0, 0, set())
    2

    0  0  0  0  0
    0  1  1  1  0
    0  1  1  1  0
    0  0  0  0  0
    >>> ızgara = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]
    >>> derinlik_oncelikli_arama(ızgara, 0, 0, set())
    2
    """
    satir_uzunlugu, sutun_uzunlugu = len(ızgara), len(ızgara[0])
    if (
        min(satir, sutun) < 0
        or satir == satir_uzunlugu
        or sutun == sutun_uzunlugu
        or (satir, sutun) in ziyaret
        or ızgara[satir][sutun] == 1
    ):
        return 0
    if satir == satir_uzunlugu - 1 and sutun == sutun_uzunlugu - 1:
        return 1

    ziyaret.add((satir, sutun))

    say = 0
    say += derinlik_oncelikli_arama(ızgara, satir + 1, sutun, ziyaret)
    say += derinlik_oncelikli_arama(ızgara, satir - 1, sutun, ziyaret)
    say += derinlik_oncelikli_arama(ızgara, satir, sutun + 1, ziyaret)
    say += derinlik_oncelikli_arama(ızgara, satir, sutun - 1, ziyaret)

    ziyaret.remove((satir, sutun))
    return say


if __name__ == "__main__":
    import doctest

    doctest.testmod()
