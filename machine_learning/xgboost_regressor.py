# XGBoost Regresör Örneği
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor


def veri_isleme(veri: dict) -> tuple:
    # Veri setini özellikler ve hedef olarak ayır. Veri, özelliklerdir.
    """
    >>> veri_isleme((
    ...  {'data':'[ 8.3252 41. 6.9841269 1.02380952  322. 2.55555556   37.88 -122.23 ]'
    ...  ,'target':([4.526])}))
    ('[ 8.3252 41. 6.9841269 1.02380952  322. 2.55555556   37.88 -122.23 ]', [4.526])
    """
    return (veri["data"], veri["target"])


def xgboost_regresor(
    ozellikler: np.ndarray, hedef: np.ndarray, test_ozellikler: np.ndarray
) -> np.ndarray:
    """
    >>> xgboost_regresor(np.array([[ 2.3571 ,   52. , 6.00813008, 1.06775068,
    ...    907. , 2.45799458,   40.58 , -124.26]]),np.array([1.114]),
    ... np.array([[1.97840000e+00,  3.70000000e+01,  4.98858447e+00,  1.03881279e+00,
    ...    1.14300000e+03,  2.60958904e+00,  3.67800000e+01, -1.19780000e+02]]))
    array([[1.1139996]], dtype=float32)
    """
    xgb = XGBRegressor(
        verbosity=0, random_state=42, tree_method="exact", base_score=0.5
    )
    xgb.fit(ozellikler, hedef)
    # Test verileri için hedefi tahmin et
    tahminler = xgb.predict(test_ozellikler)
    tahminler = tahminler.reshape(len(tahminler), 1)
    return tahminler


def ana() -> None:
    """
    Bu algoritma için URL
    https://xgboost.readthedocs.io/en/stable/
    Algoritmayı göstermek için California ev fiyatı veri seti kullanılmıştır.

    Beklenen hata değerleri:
    Ortalama Mutlak Hata: 0.30957163379906033
    Ortalama Kare Hata: 0.22611560196662744
    """
    # California ev fiyatı veri setini yükle
    california = fetch_california_housing()
    veri, hedef = veri_isleme(california)
    x_egitim, x_test, y_egitim, y_test = train_test_split(
        veri, hedef, test_size=0.25, random_state=1
    )
    tahminler = xgboost_regresor(x_egitim, y_egitim, x_test)
    # Hata değerlerini yazdır
    print(f"Ortalama Mutlak Hata: {mean_absolute_error(y_test, tahminler)}")
    print(f"Ortalama Kare Hata: {mean_squared_error(y_test, tahminler)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    ana()
