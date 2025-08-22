import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = make_moons(n_samples=500, noise=0.2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

activations = ["logistic", "tanh", "relu"]
results = {}

for act in activations:
    clf = MLPClassifier(
        hidden_layer_sizes=(10, 5),
        activation=act,
        solver="adam",
        max_iter=1000,
        random_state=42,
    )
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    results[act] = acc

plt.bar(results.keys(), results.values())
plt.title("Activation Function Comparison")
plt.ylabel("Accuracy")
plt.show()
