"""
Compare MLP activation functions (ReLU, Sigmoid, Tanh) using sklearn.

This script trains an MLPClassifier on the sklearn digits dataset
with different activation functions and prints their accuracy scores.

Example:
    >>> # Run the script directly
    >>> # python mlp_activation_comparison.py
    Activation: relu, Accuracy: 0.9722
    Activation: logistic, Accuracy: 0.9200
    Activation: tanh, Accuracy: 0.9444
"""

from __future__ import annotations
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


def compare_mlp_activations() -> None:
    """
    Train and evaluate MLPClassifier with ReLU, Sigmoid, and Tanh activations.

    Prints the accuracy for each activation function.
    """
    digits = load_digits()
    x_train, x_test, y_train, y_test = train_test_split(
        digits.data, digits.target, test_size=0.2, random_state=42
    )

    for activation in ["relu", "logistic", "tanh"]:
        mlp = MLPClassifier(
            hidden_layer_sizes=(50,),
            activation=activation,
            max_iter=500,
            random_state=42,
        )
        mlp.fit(x_train, y_train)
        y_pred = mlp.predict(x_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"Activation: {activation}, Accuracy: {acc:.4f}")


if __name__ == "__main__":
    compare_mlp_activations()
