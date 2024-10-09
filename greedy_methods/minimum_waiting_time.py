"""
Açgözlü bir algoritma kullanarak minimum bekleme süresini hesaplayın.
referans: https://www.youtube.com/watch?v=Sf3eiO12eJs

Doctest'leri çalıştırmak için şu komutu kullanın:
python -m doctest -v minimum_waiting_time.py

Produced By K. Umut Araz

minimum_waiting_time fonksiyonu, sorguların tamamlanması için minimum süreyi hesaplamak için açgözlü bir algoritma kullanır. Listeyi artmayan sırada sıralar, her sorgu için bekleme süresini, listedeki konumunu kalan tüm sorgu sürelerinin toplamı ile çarparak hesaplar ve toplam bekleme süresini döndürür. Bir doctest, fonksiyonun doğru çıktıyı ürettiğini garanti eder.
"""


def minimum_bekleme_suresi(sorgular: list[int]) -> int:
    """
    Bu fonksiyon bir sorgu süreleri listesini alır ve tüm sorguların tamamlanması için minimum bekleme süresini döndürür.

    Argümanlar:
        sorgular: Pikosaniye cinsinden ölçülen sorguların bir listesi

    Dönüş:
        toplam_bekleme_suresi: Pikosaniye cinsinden ölçülen minimum bekleme süresi

    Örnekler:
    >>> minimum_bekleme_suresi([3, 2, 1, 2, 6])
    17
    >>> minimum_bekleme_suresi([3, 2, 1])
    4
    >>> minimum_bekleme_suresi([1, 2, 3, 4])
    10
    >>> minimum_bekleme_suresi([5, 5, 5, 5])
    30
    >>> minimum_bekleme_suresi([])
    0
    """
    n = len(sorgular)
    if n in (0, 1):
        return 0
    return sum(sorgu * (n - i - 1) for i, sorgu in enumerate(sorted(sorgular)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
