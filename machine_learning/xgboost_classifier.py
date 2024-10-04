# XGBoost Sınıflandırıcı Örneği
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier


def veri_isleme(veri: dict) -> tuple:
    # Veri setini özellikler ve hedef olarak ayır
    # veri, özelliklerdir
    """
    >>> veri_isleme(({'data':'[5.1, 3.5, 1.4, 0.2]','target':([0])}))
    ('[5.1, 3.5, 1.4, 0.2]', [0])
    >>> veri_isleme(
    ...     {'data': '[4.9, 3.0, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]', 'target': ([0, 0])}
    ... )
    ('[4.9, 3.0, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]', [0, 0])
    """
    return (veri["data"], veri["target"])


def xgboost_siniflandirici(ozellikler: np.ndarray, hedef: np.ndarray) -> XGBClassifier:
    """
    # BU TEST BOZUK!! >>> xgboost_siniflandirici(np.array([[5.1, 3.6, 1.4, 0.2]]), np.array([0]))
    XGBClassifier(base_score=0.5, booster='gbtree', callbacks=None,
                  colsample_bylevel=1, colsample_bynode=1, colsample_bytree=1,
                  early_stopping_rounds=None, enable_categorical=False,
                  eval_metric=None, gamma=0, gpu_id=-1, grow_policy='depthwise',
                  importance_type=None, interaction_constraints='',
                  learning_rate=0.300000012, max_bin=256, max_cat_to_onehot=4,
                  max_delta_step=0, max_depth=6, max_leaves=0, min_child_weight=1,
                  missing=nan, monotone_constraints='()', n_estimators=100,
                  n_jobs=0, num_parallel_tree=1, predictor='auto', random_state=0,
                  reg_alpha=0, reg_lambda=1, ...)
    """
    siniflandirici = XGBClassifier()
    siniflandirici.fit(ozellikler, hedef)
    return siniflandirici


def ana() -> None:
    """
    >>> ana()

    Algoritma için URL:
    https://xgboost.readthedocs.io/en/stable/
    Algoritmayı göstermek için Iris tipi veri seti kullanılmıştır.
    """

    # Iris veri setini yükle
    iris = load_iris()
    ozellikler, hedefler = veri_isleme(iris)
    x_egitim, x_test, y_egitim, y_test = train_test_split(
        ozellikler, hedefler, test_size=0.25
    )

    isimler = iris["target_names"]

    # Eğitim verilerinden bir XGBoost Sınıflandırıcı oluştur
    xgboost_siniflandirici = xgboost_siniflandirici(x_egitim, y_egitim)

    # Sınıflandırıcının hem eğitim hem de test setleri ile karışıklık matrisini göster
    ConfusionMatrixDisplay.from_estimator(
        xgboost_siniflandirici,
        x_test,
        y_test,
        display_labels=isimler,
        cmap="Blues",
        normalize="true",
    )
    plt.title("Normalize Edilmiş Karışıklık Matrisi - IRIS Veri Seti")
    plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    ana()
