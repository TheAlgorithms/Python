import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_moons
from sklearn.neural_network import MLPClassifier


# Generate synthetic dataset
X, y = make_moons(n_samples=200, noise=0.2, random_state=42)

# Define classifiers with different activation functions
classifiers = {
    "relu": MLPClassifier(hidden_layer_sizes=(10, 10), activation="relu", max_iter=2000, random_state=42),
    "tanh": MLPClassifier(hidden_layer_sizes=(10, 10), activation="tanh", max_iter=2000, random_state=42),
    "logistic": MLPClassifier(hidden_layer_sizes=(10, 10), activation="logistic", max_iter=2000, random_state=42),
}

# Plot decision boundaries
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for ax, (name, clf) in zip(axes, classifiers.items()):
    clf.fit(X, y)

    # Create a mesh grid
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200))

    # Predict on the mesh
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Plot the decision boundary and training data
    ax.contourf(xx, yy, Z, alpha=0.3)
    ax.scatter(X[:, 0], X[:, 1], c=y, edgecolor="k", s=20)
    ax.set_title(f"Activation: {name}")

plt.tight_layout()
plt.show()
