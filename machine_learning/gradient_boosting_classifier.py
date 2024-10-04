import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


class GradientBoostingClassifier:
    def __init__(self, n_estimators: int = 100, learning_rate: float = 0.1) -> None:
        """
        GradientBoostingClassifier'ı başlat.

        Parametreler:
        - n_estimators (int): Eğitilecek zayıf öğrenicilerin sayısı.
        - learning_rate (float): Modeli güncellemek için öğrenme oranı.

        Özellikler:
        - n_estimators (int): Zayıf öğrenicilerin sayısı.
        - learning_rate (float): Öğrenme oranı.
        - models (list): Eğitilmiş zayıf öğrenicileri saklamak için bir liste.
        """
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.models: list[tuple[DecisionTreeRegressor, float]] = []

    def fit(self, features: np.ndarray, target: np.ndarray) -> None:
        """
        GradientBoostingClassifier'ı eğitim verilerine uydur.

        Parametreler:
        - features (np.ndarray): Eğitim özellikleri.
        - target (np.ndarray): Hedef değerler.

        Dönüş:
        Yok

        >>> import numpy as np
        >>> from sklearn.datasets import load_iris
        >>> clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)
        >>> iris = load_iris()
        >>> X, y = iris.data, iris.target
        >>> clf.fit(X, y)
        >>> # Modelin eğitilip eğitilmediğini kontrol et
        >>> len(clf.models) == 100
        True
        """
        for _ in range(self.n_estimators):
            # Pseudo-residuals hesapla
            residuals = -self.gradient(target, self.predict(features))
            # Pseudo-residuals'e zayıf bir öğrenici (örneğin, karar ağacı) uydur
            model = DecisionTreeRegressor(max_depth=1)
            model.fit(features, residuals)
            # Öğrenme oranı ile zayıf öğreniciyi ekleyerek modeli güncelle
            self.models.append((model, self.learning_rate))

    def predict(self, features: np.ndarray) -> np.ndarray:
        """
        Girdi verileri üzerinde tahminler yap.

        Parametreler:
        - features (np.ndarray): Tahmin yapmak için girdi verileri.

        Dönüş:
        - np.ndarray: İkili tahminlerin bir dizisi (-1 veya 1).

        >>> import numpy as np
        >>> from sklearn.datasets import load_iris
        >>> clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)
        >>> iris = load_iris()
        >>> X, y = iris.data, iris.target
        >>> clf.fit(X, y)
        >>> y_pred = clf.predict(X)
        >>> # Tahminlerin doğru şekle sahip olup olmadığını kontrol et
        >>> y_pred.shape == y.shape
        True
        """
        # Tahminleri sıfırlarla başlat
        predictions = np.zeros(features.shape[0])
        for model, learning_rate in self.models:
            predictions += learning_rate * model.predict(features)
        return np.sign(predictions)  # İkili tahminlere dönüştür (-1 veya 1)

    def gradient(self, target: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
        """
        Lojistik kayıp için negatif gradyanı (pseudo-residuals) hesapla.

        Parametreler:
        - target (np.ndarray): Hedef değerler.
        - y_pred (np.ndarray): Tahmin edilen değerler.

        Dönüş:
        - np.ndarray: Pseudo-residuals'lerin bir dizisi.

        >>> import numpy as np
        >>> clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)
        >>> target = np.array([0, 1, 0, 1])
        >>> y_pred = np.array([0.2, 0.8, 0.3, 0.7])
        >>> residuals = clf.gradient(target, y_pred)
        >>> # Pseudo-residuals'lerin doğru şekle sahip olup olmadığını kontrol et
        >>> residuals.shape == target.shape
        True
        """
        return -target / (1 + np.exp(target * y_pred))


if __name__ == "__main__":
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")
