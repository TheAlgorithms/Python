from sklearn.neural_network import MLPClassifier
import numpy as np

# Eğitim verilerini numpy array olarak tanımla
X = np.array([[0.0, 0.0], [1.0, 1.0], [1.0, 0.0], [0.0, 1.0]])
y = np.array([0, 1, 0, 0])

# MLPClassifier modelini tanımla
model = MLPClassifier(
    solver="lbfgs", alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1
)

# Modeli eğitim verileri ile eğit
model.fit(X, y)

# Test verilerini numpy array olarak tanımla
test_verileri = np.array([[0.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
tahminler = model.predict(test_verileri)

# Tahmin sonuçlarını listeye çeviren fonksiyon
def tahminleri_listeye_cevir(tahminler):
    """
    >>> [int(x) for x in tahminleri_listeye_cevir(tahminler)]
    [0, 0, 1]
    """
    return list(tahminler)

# Ana program bloğu
if __name__ == "__main__":
    import doctest

    doctest.testmod()
