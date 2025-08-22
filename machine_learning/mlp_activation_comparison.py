import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier


def compare_activations() -> None:
    """
    Demonstrates the effect of different activation functions on a simple dataset
    using scikit-learn's MLPClassifier.

    >>> compare_activations()  # doctest: +SKIP
    This function trains models and plots decision boundaries for each activation.
    """
    x, y = make_moons(n_samples=200, noise=0.25, random_state=3)
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, stratify=y, random_state=42
    )

    activations = ["identity", "logistic", "tanh", "relu"]

    for activation in activations:
        mlp = MLPClassifier(
            hidden_layer_sizes=[50],
            max_iter=1000,
            activation=activation,
            random_state=0,
        )
        mlp.fit(x_train, y_train)

        print(
            f"Activation: {activation}, "
            f"Train Accuracy: {mlp.score(x_train, y_train):.2f}, "
            f"Test Accuracy: {mlp.score(x_test, y_test):.2f}"
        )

        # Decision boundary
        x_min, x_max = x[:, 0].min() - 0.5, x[:, 0].max() + 0.5
        y_min, y_max = x[:, 1].min() - 0.5, x[:, 1].max() + 0.5
        xx, yy = np.meshgrid(
            np.linspace(x_min, x_max, 200),
            np.linspace(y_min, y_max, 200),
        )
        z = mlp.predict(np.c_[xx.ravel(), yy.ravel()])
        z = z.reshape(xx.shape)

        plt.contourf(xx, yy, z, alpha=0.3)
        plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train, marker="o", label="Train")
        plt.scatter(x_test[:, 0], x_test[:, 1], c=y_test, marker="s", label="Test")
        plt.title(f"Activation: {activation}")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    compare_activations()
