"""
t_stochastic_neighbour_embedding.py

Run t-SNE on the Iris dataset, with CI-safe doctests and visualization.
"""

# Standard library
import doctest
from typing import Tuple

# Third-party
import numpy as np
from numpy import ndarray

try:
    from sklearn.datasets import load_iris
    from sklearn.manifold import TSNE
except ImportError as e:
    raise ImportError(
        "Required package 'scikit-learn' not found. Please install it using:\n"
        "pip install scikit-learn"
    ) from e


def collect_dataset() -> Tuple[ndarray, ndarray]:
    """
    Load the Iris dataset and return features and labels.

    Returns:
        Tuple[ndarray, ndarray]: Feature matrix and target labels.

    >>> features, targets = collect_dataset()
    >>> features.shape
    (150, 4)
    >>> targets.shape
    (150,)
    """
    iris_dataset = load_iris()
    return np.array(iris_dataset.data), np.array(iris_dataset.target)


def apply_tsne(
    data_matrix: ndarray,
    n_components: int = 2,
    perplexity: float = 30.0,
    learning_rate: float = 200.0,
    max_iter: int = 1000,
    random_state: int = 42,
) -> ndarray:
    """
    Apply t-SNE for dimensionality reduction using scikit-learn's implementation.

    Args:
        data_matrix: Original dataset (features).
        n_components: Target dimension (2D or 3D).
        perplexity: Controls balance between local/global aspects.
        learning_rate: Step size for optimization.
        max_iter: Number of iterations for optimization.
        random_state: Ensures reproducibility.

    Returns:
        ndarray: Low-dimensional embedding of the data.

    >>> features, _ = collect_dataset()
    >>> embedding = apply_tsne(features, n_components=2, max_iter=250)
    >>> embedding.shape
    (150, 2)
    """
    tsne = TSNE(
        n_components=n_components,
        perplexity=perplexity,
        learning_rate=learning_rate,
        max_iter=max_iter,
        random_state=random_state,
        init="random",
    )
    return tsne.fit_transform(data_matrix)


def main() -> None:
    """
    Run t-SNE on the Iris dataset, print embeddings, and visualize results.
    """
    features, labels = collect_dataset()
    embedding = apply_tsne(
        features,
        n_components=2,
        perplexity=40.0,
        learning_rate=150.0,
        max_iter=1000,
        random_state=42,
    )

    if not isinstance(embedding, np.ndarray):
        raise TypeError("t-SNE embedding must be an ndarray")

    print("t-SNE embedding (first 5 points):")
    print(embedding[:5])

    try:
        import matplotlib.pyplot as plt

        plt.figure(figsize=(7, 5))
        scatter = plt.scatter(
            embedding[:, 0], embedding[:, 1], c=labels, cmap="viridis"
        )
        plt.title("t-SNE Visualization of the Iris Dataset")
        plt.xlabel("Dimension 1")
        plt.ylabel("Dimension 2")
        plt.colorbar(scatter, label="Class Label")
        plt.tight_layout()
        plt.show()
    except ImportError:
        print("matplotlib not installed; skipping visualization.")


if __name__ == "__main__":
    doctest.testmod()
    main()
