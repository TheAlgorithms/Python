"""
Multilayer Perceptron (MLP) Classifier Example

A Multilayer Perceptron (MLP) is a type of feedforward artificial neural network
that consists of at least three layers of nodes: an input layer, one or more hidden
layers, and an output layer. Each node (except for the input nodes) is a neuron
that uses a nonlinear activation function.

Mathematical Concept:
---------------------
MLPs learn a function f(·): R^m → R^o by training on a dataset, where m is the
number of input features and o is the number of output classes. The network
adjusts its weights using backpropagation to minimize the difference between
predicted and actual outputs.

Practical Use Cases:
--------------------
- Handwritten digit recognition (e.g., MNIST dataset)
- Binary and multiclass classification tasks
- Predicting outcomes based on multiple features
  (e.g., medical diagnosis, spam detection)

References:
-----------
- https://en.wikipedia.org/wiki/Multilayer_perceptron
- https://scikit-learn.org/stable/modules/neural_networks_supervised.html
- https://medium.com/@aryanrusia8/multi-layer-perceptrons-explained-7cb9a6e318c3

Example:
--------
>>> X = [[0.0, 0.0], [1.0, 1.0], [1.0, 0.0], [0.0, 1.0]]
>>> y = [0, 1, 0, 0]
>>> multilayer_perceptron_classifier(X, y, [[0.0, 0.0], [1.0, 1.0]])
[0, 1]
"""

from collections.abc import Sequence

from sklearn.neural_network import MLPClassifier


def multilayer_perceptron_classifier(
    train_features: Sequence[Sequence[float]],
    train_labels: Sequence[int],
    test_features: Sequence[Sequence[float]],
) -> list[int]:
    """
    Train a Multilayer Perceptron classifier and predict labels for test data.

    Args:
        train_features: Training data features, shape (n_samples, n_features).
        train_labels: Training data labels, shape (n_samples,).
        test_features: Test data features to predict, shape (m_samples, n_features).

    Returns:
        List of predicted labels for the test data.

    Raises:
        ValueError: If the number of training samples and labels do not match.

    Example:
        >>> X = [[0.0, 0.0], [1.0, 1.0], [1.0, 0.0], [0.0, 1.0]]
        >>> y = [0, 1, 0, 0]
        >>> multilayer_perceptron_classifier(X, y, [[0.0, 0.0], [1.0, 1.0]])
        # Multiple possible outputs True
    """
    if len(train_features) != len(train_labels):
        raise ValueError("Number of training samples and labels must match.")

    clf = MLPClassifier(
        solver="lbfgs", alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1
    )
    clf.fit(train_features, train_labels)
    predictions = clf.predict(test_features)
    return list(predictions)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
