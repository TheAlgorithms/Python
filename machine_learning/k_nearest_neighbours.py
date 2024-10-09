"""
k-Nearest Neighbours (kNN) sınıflandırma için kullanılan basit, parametrik olmayan bir
denetimli öğrenme algoritmasıdır. Etiketlenmiş bazı eğitim verileri verildiğinde, belirli
bir nokta, belirli bir mesafe metriğine göre en yakın k komşusu kullanılarak sınıflandırılır.
Komşular arasında en sık görülen etiket, verilen noktanın etiketi olur. Etkili bir şekilde,
verilen noktanın etiketi çoğunluk oyu ile belirlenir.

Bu uygulama yaygın olarak kullanılan Öklid mesafe metriğini kullanır, ancak diğer mesafe
metrikleri de kullanılabilir.

Organised to K. Umut Araz

Referans: https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
"""

from collections import Counter
from heapq import nsmallest

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split


class KNN:
    def __init__(
        self,
        egitim_verisi: np.ndarray,
        egitim_etiketi: np.ndarray,
        sinif_etiketleri: list[str],
    ) -> None:
        """
        Verilen eğitim verileri ve sınıf etiketlerini kullanarak bir kNN sınıflandırıcı oluştur
        """
        self.veri = list(zip(egitim_verisi, egitim_etiketi))
        self.etiketler = sinif_etiketleri

    @staticmethod
    def _oklid_mesafesi(a: np.ndarray, b: np.ndarray) -> float:
        """
        İki nokta arasındaki Öklid mesafesini hesapla
        >>> KNN._oklid_mesafesi(np.array([0, 0]), np.array([3, 4]))
        5.0
        >>> KNN._oklid_mesafesi(np.array([1, 2, 3]), np.array([1, 8, 11]))
        10.0
        """
        return float(np.linalg.norm(a - b))

    def siniflandir(self, tahmin_noktasi: np.ndarray, k: int = 5) -> str:
        """
        kNN algoritmasını kullanarak belirli bir noktayı sınıflandır
        >>> egitim_X = np.array(
        ...     [[0, 0], [1, 0], [0, 1], [0.5, 0.5], [3, 3], [2, 3], [3, 2]]
        ... )
        >>> egitim_y = np.array([0, 0, 0, 0, 1, 1, 1])
        >>> siniflar = ['A', 'B']
        >>> knn = KNN(egitim_X, egitim_y, siniflar)
        >>> nokta = np.array([1.2, 1.2])
        >>> knn.siniflandir(nokta)
        'A'
        """
        # Sınıflandırılacak noktadan tüm noktalara olan mesafeler
        mesafeler = (
            (self._oklid_mesafesi(veri_noktasi[0], tahmin_noktasi), veri_noktasi[1])
            for veri_noktasi in self.veri
        )

        # En kısa mesafeye sahip k noktayı seçme
        oylar = (i[1] for i in nsmallest(k, mesafeler))

        # En sık görülen sınıf, noktanın sınıflandırıldığı sınıf olur
        sonuc = Counter(oylar).most_common(1)[0][0]
        return self.etiketler[sonuc]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    iris = datasets.load_iris()

    X = np.array(iris["data"])
    y = np.array(iris["target"])
    iris_siniflari = iris["target_names"]

    X_egitim, X_test, y_egitim, y_test = train_test_split(X, y, random_state=0)
    iris_noktasi = np.array([4.4, 3.1, 1.3, 1.4])
    siniflandirici = KNN(X_egitim, y_egitim, iris_siniflari)
    print(siniflandirici.siniflandir(iris_noktasi, k=3))
