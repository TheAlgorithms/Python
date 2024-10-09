import numpy as np

""" Burada puanlama fonksiyonlarını uyguladım.
    MAE, MSE, RMSE, RMSLE ve MBD dahildir.

    Bunlar, tahmin edilen değerler ile gerçek değerler arasındaki
    farkları hesaplamak için kullanılır.

    Metrikler biraz farklılık gösterir. Bazen kare, kök,
    hatta logaritma kullanılır.

    Logaritma ve kök kullanmak büyük hataları cezalandırma
    araçları olarak algılanabilir. Ancak, uygun metriklerin kullanımı
    duruma ve veri türlerine bağlıdır.
    Katkı: K. Umut Araz
"""


# Ortalama Mutlak Hata (MAE)
def ortalama_mutlak_hata(tahmin, gercek):
    """
    Örnekler (hassasiyet için yuvarlanmış):
    >>> gercek = [1,2,3]; tahmin = [1,4,3]
    >>> float(np.around(ortalama_mutlak_hata(tahmin, gercek), decimals=2))
    0.67

    >>> gercek = [1,1,1]; tahmin = [1,1,1]
    >>> float(ortalama_mutlak_hata(tahmin, gercek))
    0.0
    """
    tahmin = np.array(tahmin)
    gercek = np.array(gercek)

    fark = abs(tahmin - gercek)
    skor = fark.mean()

    return skor


# Ortalama Kare Hata (MSE)
def ortalama_kare_hata(tahmin, gercek):
    """
    Örnekler (hassasiyet için yuvarlanmış):
    >>> gercek = [1,2,3]; tahmin = [1,4,3]
    >>> float(np.around(ortalama_kare_hata(tahmin, gercek), decimals=2))
    1.33

    >>> gercek = [1,1,1]; tahmin = [1,1,1]
    >>> float(ortalama_kare_hata(tahmin, gercek))
    0.0
    """
    tahmin = np.array(tahmin)
    gercek = np.array(gercek)

    fark = tahmin - gercek
    kare_fark = np.square(fark)

    skor = kare_fark.mean()
    return skor


# Kök Ortalama Kare Hata (RMSE)
def kok_ortalama_kare_hata(tahmin, gercek):
    """
    Örnekler (hassasiyet için yuvarlanmış):
    >>> gercek = [1,2,3]; tahmin = [1,4,3]
    >>> float(np.around(kok_ortalama_kare_hata(tahmin, gercek), decimals=2))
    1.15

    >>> gercek = [1,1,1]; tahmin = [1,1,1]
    >>> float(kok_ortalama_kare_hata(tahmin, gercek))
    0.0
    """
    tahmin = np.array(tahmin)
    gercek = np.array(gercek)

    fark = tahmin - gercek
    kare_fark = np.square(fark)
    ortalama_kare_fark = kare_fark.mean()
    skor = np.sqrt(ortalama_kare_fark)
    return skor


# Kök Ortalama Kare Logaritmik Hata (RMSLE)
def kok_ortalama_kare_logaritmik_hata(tahmin, gercek):
    """
    Örnekler (hassasiyet için yuvarlanmış):
    >>> float(np.around(kok_ortalama_kare_logaritmik_hata(tahmin=[10, 2, 30], gercek=[10, 10, 30]), decimals=2))
    0.75

    >>> float(kok_ortalama_kare_logaritmik_hata(tahmin=[1, 1, 1], gercek=[1, 1, 1]))
    0.0
    """
    tahmin = np.array(tahmin)
    gercek = np.array(gercek)

    log_tahmin = np.log(tahmin + 1)
    log_gercek = np.log(gercek + 1)

    fark = log_tahmin - log_gercek
    kare_fark = np.square(fark)
    ortalama_kare_fark = kare_fark.mean()

    skor = np.sqrt(ortalama_kare_fark)

    return skor


# Ortalama Sapma Hatası (MBD)
def ortalama_sapma_hatasi(tahmin, gercek):
    """
    Bu değer negatifse, model düşük tahmin yapar,
    pozitifse, aşırı tahmin yapar.

    Örnek (hassasiyet için yuvarlanmış):

    Burada model aşırı tahmin yapar
    >>> gercek = [1,2,3]; tahmin = [2,3,4]
    >>> float(np.around(ortalama_sapma_hatasi(tahmin, gercek), decimals=2))
    50.0

    Burada model düşük tahmin yapar
    >>> gercek = [1,2,3]; tahmin = [0,1,1]
    >>> float(np.around(ortalama_sapma_hatasi(tahmin, gercek), decimals=2))
    -66.67
    """
    tahmin = np.array(tahmin)
    gercek = np.array(gercek)

    fark = tahmin - gercek
    pay = np.sum(fark) / len(tahmin)
    payda = np.sum(gercek) / len(tahmin)
    skor = float(pay) / payda * 100

    return skor


def manuel_dogruluk(tahmin, gercek):
    return np.mean(np.array(gercek) == np.array(tahmin))
