"""
Approximate Nearest Neighbor (ANN) Search
https://en.wikipedia.org/wiki/Nearest_neighbor_search#Approximate_nearest_neighbor

ANN search finds "close enough" vectors instead of the exact nearest neighbor,
which makes it much faster for large datasets.

This implementation uses a simple **random projection hashing** method.
Steps:
1. Generate random hyperplanes to hash vectors into buckets.
2. Place dataset vectors into buckets.
3. For a query vector, look into its bucket (and maybe nearby buckets).
4. Return the approximate nearest neighbor from those candidates.

Each result contains:
    1. The nearest (approximate) vector.
    2. Its distance from the query vector.
"""

from __future__ import annotations

import math
from collections import defaultdict

import numpy as np


def euclidean(input_a: np.ndarray, input_b: np.ndarray) -> float:
    """
    Calculates Euclidean distance between two vectors.
    >>> euclidean(np.array([0]), np.array([1]))
    1.0
    >>> euclidean(np.array([1, 2]), np.array([1, 5]))
    3.0
    """
    return math.sqrt(sum(pow(a - b, 2) for a, b in zip(input_a, input_b)))


class ANN:
    """
    Approximate Nearest Neighbor using random projection hashing.
    """

    def __init__(self, dataset: np.ndarray, n_planes: int = 5, seed: int = 42) -> None:
        """
        :param dataset: ndarray of shape (n_samples, n_features)
        :param n_planes: number of random hyperplanes for hashing
        :param seed: random seed for reproducibility
        """
        self.dataset = dataset
        self.n_planes = n_planes
        rng = np.random.default_rng(seed)
        self.planes = rng.standard_normal((n_planes, dataset.shape[1]))
        self.buckets: dict[str, list[np.ndarray]] = defaultdict(list)
        self._build_index()

    def _hash_vector(self, vec: np.ndarray) -> str:
        """
        Hash a vector based on which side of each hyperplane it falls on.
        Returns a bit string.

        >>> dataset = np.array([[1, 2]])
        >>> ann = ANN(dataset, n_planes=2, seed=0)
        >>> h = ann._hash_vector(np.array([1, 2]))
        >>> isinstance(h, str)
        True
        >>> len(h) == ann.n_planes
        True
        """
        signs = (vec @ self.planes.T) >= 0
        return "".join(["1" if s else "0" for s in signs])

    def _build_index(self) -> None:
        """
        Build hash buckets for all dataset vectors.

        >>> dataset = np.array([[0, 0], [1, 1]])
        >>> ann = ANN(dataset, n_planes=2, seed=0)
        >>> all(isinstance(k, str) for k in ann.buckets.keys())
        True
        >>> sum(len(v) for v in ann.buckets.values()) == len(dataset)
        True
        """
        for vec in self.dataset:
            h = self._hash_vector(vec)
            self.buckets[h].append(vec)

    def query(self, query_vectors: np.ndarray) -> list[list[list[float] | float]]:
        """
        Find approximate nearest neighbor for query vector(s).
        :param query_vectors: ndarray of shape (m, n_features)
        :return: list of [nearest_vector, distance]

        >>> dataset = np.array([[0, 0], [1, 1], [2, 2], [10, 10]])
        >>> ann = ANN(dataset, n_planes=4, seed=0)
        >>> ann.query(np.array([[0, 1]]))  # doctest: +NORMALIZE_WHITESPACE
        [[[0, 0], 1.0]]
        """
        results = []
        for vec in query_vectors:
            h = self._hash_vector(vec)
            candidates = self.buckets[h]

            if not candidates:  # fallback: search entire dataset
                candidates = self.dataset

            # Approximate NN search among candidates
            best_vec = candidates[0]
            best_dist = euclidean(vec, best_vec)
            for cand in candidates[1:]:
                d = euclidean(vec, cand)
                if d < best_dist:
                    best_vec, best_dist = cand, d
            results.append([best_vec.tolist(), best_dist])
        return results


if __name__ == "__main__":
    import doctest

    doctest.testmod()
