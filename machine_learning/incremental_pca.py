"""
Incremental Principal Component Analysis (Incremental PCA).

Implements the Sequential Karhunen-Loeve algorithm with exact mean updating
(Ross et al., 2008, "Incremental Learning for Robust Visual Tracking", IJCV),
using NumPy SVD without storing the full dataset in memory.

https://en.wikipedia.org/wiki/Principal_component_analysis
"""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray


def _validate_batch(
    batch: ArrayLike, expected_features: int | None
) -> NDArray[np.float64]:
    """
    Validate and convert an input batch to a 2D float64 NumPy array.

    >>> _validate_batch([[1.0, 2.0], [3.0, 4.0]], None).shape
    (2, 2)
    >>> _validate_batch([1.0, 2.0], None)
    Traceback (most recent call last):
        ...
    ValueError: input batch must be a 2D array
    >>> _validate_batch(np.empty((0, 2)), None)
    Traceback (most recent call last):
        ...
    ValueError: input batch must contain at least one sample
    >>> _validate_batch([[1.0, 2.0, 3.0]], expected_features=2)
    Traceback (most recent call last):
        ...
    ValueError: expected 2 features, got 3
    """
    array = np.asarray(batch, dtype=np.float64)
    if array.ndim != 2:
        raise ValueError("input batch must be a 2D array")
    if array.shape[0] == 0 or array.shape[1] == 0:
        raise ValueError("input batch must contain at least one sample")
    if expected_features is not None and array.shape[1] != expected_features:
        msg = f"expected {expected_features} features, got {array.shape[1]}"
        raise ValueError(msg)
    return array


def _svd_flip(vt: NDArray[np.float64]) -> NDArray[np.float64]:
    """
    Enforce deterministic sign for right singular vectors by largest-magnitude entry.

    >>> _svd_flip(np.array([[-0.8, 0.6], [0.1, -0.9]]))
    array([[ 0.8, -0.6],
           [-0.1,  0.9]])
    """
    max_abs_cols = np.argmax(np.abs(vt), axis=1)
    signs = np.sign(vt[np.arange(vt.shape[0]), max_abs_cols])
    signs[signs == 0.0] = 1.0
    return vt * signs[:, np.newaxis]


class IncrementalPCA:
    """
    Incremental PCA via mini-batch SVD updates with exact mean tracking.

    >>> data = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0], [7.0, 8.0]])
    >>> ipca = IncrementalPCA(n_components=1)
    >>> _ = ipca.partial_fit(data[:2]).partial_fit(data[2:])
    >>> ipca.n_samples_seen
    4
    >>> np.allclose(ipca.mean, [4.0, 5.0])
    True
    >>> projected = ipca.transform(data)
    >>> projected.shape
    (4, 1)
    >>> np.allclose(ipca.inverse_transform(projected), data)
    True
    """

    def __init__(self, n_components: int) -> None:
        """
        Initialize IncrementalPCA with target number of components.

        >>> IncrementalPCA(n_components=2).n_components
        2
        >>> IncrementalPCA(n_components=0)
        Traceback (most recent call last):
            ...
        ValueError: n_components must be a positive integer
        """
        if n_components <= 0:
            raise ValueError("n_components must be a positive integer")
        self.n_components = n_components
        self.n_samples_seen: int = 0
        self.n_features: int | None = None
        self.mean: NDArray[np.float64] = np.array([], dtype=np.float64)
        self.components: NDArray[np.float64] = np.array([], dtype=np.float64)
        self.singular_values: NDArray[np.float64] = np.array([], dtype=np.float64)
        self.explained_variance: NDArray[np.float64] = np.array([], dtype=np.float64)

    def partial_fit(self, batch: ArrayLike) -> IncrementalPCA:
        """
        Incrementally update PCA components and mean with a new mini-batch.

        >>> ipca = IncrementalPCA(n_components=2)
        >>> _ = ipca.partial_fit([[0.0, 0.0], [2.0, 0.0]])
        >>> _ = ipca.partial_fit([[0.0, 2.0], [2.0, 2.0]])
        >>> ipca.n_samples_seen
        4
        >>> np.allclose(ipca.mean, [1.0, 1.0])
        True
        >>> np.allclose(ipca.explained_variance, [4.0 / 3.0, 4.0 / 3.0])
        True
        """
        data = _validate_batch(batch, self.n_features)
        batch_samples, n_features = data.shape
        if self.n_components > n_features:
            msg = f"n_components={self.n_components} exceeds n_features={n_features}"
            raise ValueError(msg)

        batch_mean = np.mean(data, axis=0)
        centered_batch = data - batch_mean

        if self.n_samples_seen == 0:
            self.n_features = n_features
            updated_mean = batch_mean
            combined_matrix = centered_batch
        else:
            total_samples = self.n_samples_seen + batch_samples
            updated_mean = (
                self.n_samples_seen * self.mean + batch_samples * batch_mean
            ) / total_samples
            # Scale the mean-shift vector by sqrt(n*m/(n+m)) so the augmented
            # matrix preserves the exact combined scatter matrix X^T X.
            mean_correction = np.sqrt(
                (self.n_samples_seen * batch_samples) / total_samples
            ) * (batch_mean - self.mean)
            scaled_components = self.singular_values[:, np.newaxis] * self.components
            combined_matrix = np.vstack(
                (scaled_components, centered_batch, mean_correction)
            )

        _, singular_values, vt = np.linalg.svd(combined_matrix, full_matrices=False)
        vt = _svd_flip(vt)

        self.n_samples_seen += batch_samples
        self.mean = updated_mean
        n_kept = min(self.n_components, singular_values.shape[0])
        self.components = vt[:n_kept]
        self.singular_values = singular_values[:n_kept]
        self.explained_variance = (self.singular_values**2) / max(
            self.n_samples_seen - 1, 1
        )
        return self

    def fit(self, data: ArrayLike, batch_size: int | None = None) -> IncrementalPCA:
        """
        Fit the model on a dataset in mini-batches of size batch_size.

        >>> x = np.array([[1.0, 0.0], [2.0, 0.0], [3.0, 0.0], [4.0, 0.0]])
        >>> ipca = IncrementalPCA(n_components=1).fit(x, batch_size=2)
        >>> ipca.n_samples_seen
        4
        >>> np.allclose(np.abs(ipca.components), [[1.0, 0.0]])
        True
        >>> IncrementalPCA(n_components=1).fit(x, batch_size=0)
        Traceback (most recent call last):
            ...
        ValueError: batch_size must be a positive integer
        """
        validated = _validate_batch(data, expected_features=None)
        if batch_size is None:
            return self.partial_fit(validated)
        if batch_size <= 0:
            raise ValueError("batch_size must be a positive integer")

        self.n_samples_seen = 0
        self.n_features = None
        for start in range(0, validated.shape[0], batch_size):
            self.partial_fit(validated[start : start + batch_size])
        return self

    def transform(self, data: ArrayLike) -> NDArray[np.float64]:
        """
        Project data onto the learned principal components.

        >>> ipca = IncrementalPCA(n_components=1).fit([[0.0, 0.0], [2.0, 2.0]])
        >>> np.allclose(ipca.transform([[1.0, 1.0]]), [[0.0]])
        True
        >>> IncrementalPCA(n_components=1).transform([[1.0, 1.0]])
        Traceback (most recent call last):
            ...
        ValueError: model must be fitted before calling transform
        """
        if self.n_samples_seen == 0:
            raise ValueError("model must be fitted before calling transform")
        validated = _validate_batch(data, self.n_features)
        return (validated - self.mean) @ self.components.T

    def inverse_transform(self, projected: ArrayLike) -> NDArray[np.float64]:
        """
        Reconstruct approximate original-space samples from projected coordinates.

        >>> ipca = IncrementalPCA(n_components=1).fit([[0.0, 0.0], [2.0, 2.0]])
        >>> z = ipca.transform([[2.0, 2.0]])
        >>> np.allclose(ipca.inverse_transform(z), [[2.0, 2.0]])
        True
        >>> IncrementalPCA(n_components=1).inverse_transform([[0.0]])
        Traceback (most recent call last):
            ...
        ValueError: model must be fitted before calling inverse_transform
        """
        if self.n_samples_seen == 0:
            raise ValueError("model must be fitted before calling inverse_transform")
        validated = _validate_batch(projected, self.components.shape[0])
        return validated @ self.components + self.mean


if __name__ == "__main__":
    import doctest

    doctest.testmod()
