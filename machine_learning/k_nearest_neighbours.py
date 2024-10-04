"""
k-Nearest Neighbours (kNN) sınıflandırma için kullanılan basit, parametrik olmayan bir
denetimli öğrenme algoritmasıdır. Etiketlenmiş bazı eğitim verileri verildiğinde, belirli
bir nokta, belirli bir mesafe metriğine göre en yakın k komşusu kullanılarak sınıflandırılır.
Komşular arasında en sık görülen etiket, verilen noktanın etiketi olur. Etkili bir şekilde,
verilen noktanın etiketi çoğunluk oyu ile belirlenir.

Bu uygulama yaygın olarak kullanılan Öklid mesafe metriğini kullanır, ancak diğer mesafe
metrikleri de kullanılabilir.

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
        train_data: np.ndarray,
        train_target: np.ndarray,
        class_labels: list[str],
    ) -> None:
        """
        Verilen eğitim verileri ve sınıf etiketlerini kullanarak bir kNN sınıflandırıcı oluştur
        """
        self.data = list(zip(train_data, train_target))
        self.labels = class_labels

    @staticmethod
    def _euclidean_distance(a: np.ndarray, b: np.ndarray) -> float:
        """
        İki nokta arasındaki Öklid mesafesini hesapla
        >>> KNN._euclidean_distance(np.array([0, 0]), np.array([3, 4]))
        5.0
        >>> KNN._euclidean_distance(np.array([1, 2, 3]), np.array([1, 8, 11]))
        10.0
        """
        return float(np.linalg.norm(a - b))

    def classify(self, pred_point: np.ndarray, k: int = 5) -> str:
        """
        kNN algoritmasını kullanarak belirli bir noktayı sınıflandır
        >>> train_X = np.array(
        ...     [[0, 0], [1, 0], [0, 1], [0.5, 0.5], [3, 3], [2, 3], [3, 2]]
        ... )
        >>> train_y = np.array([0, 0, 0, 0, 1, 1, 1])
        >>> classes = ['A', 'B']
        >>> knn = KNN(train_X, train_y, classes)
        >>> point = np.array([1.2, 1.2])
        >>> knn.classify(point)
        'A'
        """
        # Sınıflandırılacak noktadan tüm noktalara olan mesafeler
        distances = (
            (self._euclidean_distance(data_point[0], pred_point), data_point[1])
            for data_point in self.data
        )

        # En kısa mesafeye sahip k noktayı seçme
        votes = (i[1] for i in nsmallest(k, distances))

        # En sık görülen sınıf, noktanın sınıflandırıldığı sınıf olur
        result = Counter(votes).most_common(1)[0][0]
        return self.labels[result]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    iris = datasets.load_iris()

    X = np.array(iris["data"])
    y = np.array(iris["target"])
    iris_classes = iris["target_names"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    iris_point = np.array([4.4, 3.1, 1.3, 1.4])
    classifier = KNN(X_train, y_train, iris_classes)
    print(classifier.classify(iris_point, k=3))
