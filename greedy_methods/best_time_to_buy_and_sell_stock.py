"""
Verilen bir hisse senedi fiyatları listesi ile, tek bir alım ve satım işlemiyle elde edilebilecek maksimum karı hesaplayın.
Sadece bir alım ve bir satım işlemi yapmamıza izin verilir, ancak satmadan önce satın almalıyız.

Örnek: fiyatlar = [7, 1, 5, 3, 6, 4]
max_kar 5 dönecektir - bu, 1 fiyatından alıp 6 fiyatından satarak elde edilir.

Produced By. K. Umut Araz

Bu problem "AÇGÖZLÜ ALGORİTMA" kavramı kullanılarak çözülebilir.

Fiyat dizisini bir kez iterasyon yaparak, en düşük fiyat noktasını (alım) ve her noktada elde edebileceğimiz maksimum karı takip ederiz.
Her noktadaki açgözlü seçim, mevcut alım fiyatımızdan daha düşükse mevcut fiyattan satın almak veya kar mevcut maksimum kardan fazlaysa mevcut fiyattan satmaktır.
"""


def max_kar(fiyatlar: list[int]) -> int:
    """
    >>> max_kar([7, 1, 5, 3, 6, 4])
    5
    >>> max_kar([7, 6, 4, 3, 1])
    0
    """
    if not fiyatlar:
        return 0

    min_fiyat = fiyatlar[0]
    max_kar: int = 0

    for fiyat in fiyatlar:
        min_fiyat = min(fiyat, min_fiyat)
        max_kar = max(fiyat - min_fiyat, max_kar)

    return max_kar


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(max_kar([7, 1, 5, 3, 6, 4]))
