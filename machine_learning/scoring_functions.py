import numpy as np

""" Burada puanlama fonksiyonlarını uyguladım.
    MAE, MSE, RMSE, RMSLE dahildir.

    Bunlar, tahmin edilen değerler ile gerçek değerler arasındaki
    farkları hesaplamak için kullanılır.

    Metrikler biraz farklılık gösterir. Bazen kare, kök,
    hatta logaritma kullanılır.

    Logaritma ve kök kullanmak büyük hataları cezalandırma
    araçları olarak algılanabilir. Ancak, uygun metriklerin kullanımı
    duruma ve veri türlerine bağlıdır.
"""


# Ortalama Mutlak Hata
def mae(predict, actual):
    """
    Örnekler (hassasiyet için yuvarlanmış):
    >>> actual = [1,2,3];predict = [1,4,3]
    >>> float(np.around(mae(predict,actual),decimals = 2))
    0.67

    >>> actual = [1,1,1];predict = [1,1,1]
    >>> float(mae(predict,actual))
    0.0
    """
    predict = np.array(predict)
    actual = np.array(actual)

    difference = abs(predict - actual)
    score = difference.mean()

    return score


# Ortalama Kare Hata
def mse(predict, actual):
    """
    Örnekler (hassasiyet için yuvarlanmış):
    >>> actual = [1,2,3];predict = [1,4,3]
    >>> float(np.around(mse(predict,actual),decimals = 2))
    1.33

    >>> actual = [1,1,1];predict = [1,1,1]
    >>> float(mse(predict,actual))
    0.0
    """
    predict = np.array(predict)
    actual = np.array(actual)

    difference = predict - actual
    square_diff = np.square(difference)

    score = square_diff.mean()
    return score


# Kök Ortalama Kare Hata
def rmse(predict, actual):
    """
    Örnekler (hassasiyet için yuvarlanmış):
    >>> actual = [1,2,3];predict = [1,4,3]
    >>> float(np.around(rmse(predict,actual),decimals = 2))
    1.15

    >>> actual = [1,1,1];predict = [1,1,1]
    >>> float(rmse(predict,actual))
    0.0
    """
    predict = np.array(predict)
    actual = np.array(actual)

    difference = predict - actual
    square_diff = np.square(difference)
    mean_square_diff = square_diff.mean()
    score = np.sqrt(mean_square_diff)
    return score


# Kök Ortalama Kare Logaritmik Hata
def rmsle(predict, actual):
    """
    Örnekler (hassasiyet için yuvarlanmış):
    >>> float(np.around(rmsle(predict=[10, 2, 30], actual=[10, 10, 30]), decimals=2))
    0.75

    >>> float(rmsle(predict=[1, 1, 1], actual=[1, 1, 1]))
    0.0
    """
    predict = np.array(predict)
    actual = np.array(actual)

    log_predict = np.log(predict + 1)
    log_actual = np.log(actual + 1)

    difference = log_predict - log_actual
    square_diff = np.square(difference)
    mean_square_diff = square_diff.mean()

    score = np.sqrt(mean_square_diff)

    return score


# Ortalama Sapma Hatası
def mbd(predict, actual):
    """
    Bu değer negatifse, model düşük tahmin yapar,
    pozitifse, aşırı tahmin yapar.

    Örnek (hassasiyet için yuvarlanmış):

    Burada model aşırı tahmin yapar
    >>> actual = [1,2,3];predict = [2,3,4]
    >>> float(np.around(mbd(predict,actual),decimals = 2))
    50.0

    Burada model düşük tahmin yapar
    >>> actual = [1,2,3];predict = [0,1,1]
    >>> float(np.around(mbd(predict,actual),decimals = 2))
    -66.67
    """
    predict = np.array(predict)
    actual = np.array(actual)

    difference = predict - actual
    numerator = np.sum(difference) / len(predict)
    denumerator = np.sum(actual) / len(predict)
    # print(numerator, denumerator)
    score = float(numerator) / denumerator * 100

    return score


def manual_accuracy(predict, actual):
    return np.mean(np.array(actual) == np.array(predict))
