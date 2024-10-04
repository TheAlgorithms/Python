from sklearn.neural_network import MLPClassifier
import numpy as np

# Eğitim verilerini numpy array olarak tanımla
X = np.array([[0.0, 0.0], [1.0, 1.0], [1.0, 0.0], [0.0, 1.0]])
y = np.array([0, 1, 0, 0])

# MLPClassifier modelini tanımla
clf = MLPClassifier(
    solver="lbfgs", alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1
)

# Modeli eğitim verileri ile eğit
clf.fit(X, y)

# Test verilerini numpy array olarak tanımla
test = np.array([[0.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
Y = clf.predict(test)

# Tahmin sonuçlarını listeye çeviren fonksiyon
def wrapper(y):
    """
    >>> [int(x) for x in wrapper(Y)]
    [0, 0, 1]
    """
    return list(y)

# Ana program bloğu
if __name__ == "__main__":
    import doctest

    doctest.testmod()
