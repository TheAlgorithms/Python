"""
Federated averaging (FedAvg) utilities.

This module provides a simple NumPy-based implementation of the FedAvg
aggregation algorithm. It supports equal weighting and custom non-negative
weights that are normalized internally.

Doctests
========

Basic equal-weight averaging across two "clients" with two tensors each
(vector and 2x2 matrix):

>>> A = [np.array([1.0, 2.0]), np.array([[1.0, 2.0], [3.0, 4.0]])]
>>> B = [np.array([3.0, 4.0]), np.array([[5.0, 6.0], [7.0, 8.0]])]
>>> eq = federated_average([A, B])
>>> eq[0].tolist()
[2.0, 3.0]
>>> eq[1].tolist()
[[3.0, 4.0], [5.0, 6.0]]

Weighted averaging with weights [2, 1] (normalized to [2/3, 1/3]):

>>> w = federated_average([A, B], weights=np.array([2.0, 1.0]))
>>> w[0].tolist()
[1.6666666666666665, 2.6666666666666665]
>>> w[1].tolist()
[[2.333333333333333, 3.333333333333333], [4.333333333333333, 5.333333333333333]]

Error cases:

- No clients

>>> federated_average([])  # doctest: +ELLIPSIS
Traceback (most recent call last):
...
ValueError: client_models must be a non-empty list

- Mismatched number of tensors per client

>>> C = [np.array([1.0, 2.0])]  # only one tensor
>>> federated_average([A, C])  # doctest: +ELLIPSIS
Traceback (most recent call last):
...
ValueError: All clients must have the same number of tensors

- Mismatched tensor shapes across clients

>>> C2 = [np.array([1.0, 2.0]), np.array([[1.0, 2.0]])]  # second tensor has different shape
>>> federated_average([A, C2])  # doctest: +ELLIPSIS
Traceback (most recent call last):
...
ValueError: Client 2 tensor shape (1, 2) does not match (2, 2)

- Invalid weights: negative or wrong shape or zero-sum

>>> federated_average([A, B], weights=np.array([1.0, -1.0]))  # doctest: +ELLIPSIS
Traceback (most recent call last):
...
ValueError: weights must be non-negative

>>> federated_average([A, B], weights=np.array([0.0, 0.0]))  # doctest: +ELLIPSIS
Traceback (most recent call last):
...
ValueError: weights must sum to a positive value

>>> federated_average([A, B], weights=np.array([1.0, 2.0, 3.0]))  # doctest: +ELLIPSIS
Traceback (most recent call last):
...
ValueError: weights must have shape (2,)
"""

from __future__ import annotations
from typing import Iterable, List, Sequence
import numpy as np


def _validate_clients(client_models: Sequence[Sequence[np.ndarray]]) -> None:
    if not client_models:
        raise ValueError("client_models must be a non-empty list")
    # Ensure all clients have same number of layers and shapes
    ref_shapes = [tuple(arr.shape) for arr in client_models[0]]
    for idx, cm in enumerate(client_models, start=1):
        if len(cm) != len(ref_shapes):
            raise ValueError("All clients must have the same number of tensors")
        for s_ref, arr in zip(ref_shapes, cm):
            if tuple(arr.shape) != s_ref:
                raise ValueError(
                    f"Client {idx} tensor shape {tuple(arr.shape)} does not match {s_ref}"
                )


def _normalize_weights(weights: np.ndarray, n: int) -> np.ndarray:
    if weights.shape != (n,):
        raise ValueError(f"weights must have shape ({n},)")
    if np.any(weights < 0):
        raise ValueError("weights must be non-negative")
    total = float(weights.sum())
    if total <= 0.0:
        raise ValueError("weights must sum to a positive value")
    return weights / total


def federated_average(
    client_models: Sequence[Sequence[np.ndarray]],
    weights: np.ndarray | None = None,
) -> List[np.ndarray]:
    """Compute the weighted average of clients' model tensors.

    Parameters
    ----------
    client_models : Sequence[Sequence[np.ndarray]]
        A list of clients, each being a sequence of NumPy arrays (tensors).
        All clients must have the same number of tensors with identical shapes.
    weights : np.ndarray | None, optional
        A 1-D array of non-negative weights, one per client. If None,
        equal weighting is used. Weights are normalized to sum to 1.

    Returns
    -------
    List[np.ndarray]
        The list of aggregated tensors with the same shapes as the inputs.
    """
    _validate_clients(client_models)
    num_clients = len(client_models)

    if weights is None:
        weights_n = np.full((num_clients,), 1.0 / num_clients, dtype=float)
    else:
        weights = np.asarray(weights, dtype=float)
        weights_n = _normalize_weights(weights, num_clients)

    num_tensors = len(client_models[0])
    aggregated: List[np.ndarray] = []
    for t_idx in range(num_tensors):
        # Stack the t_idx-th tensor from each client into shape (num_clients, ...)
        stacked = np.stack([np.asarray(cm[t_idx]) for cm in client_models], axis=0)
        # Weighted sum across clients axis=0
        # np.tensordot weights of shape (n,) with stacked of shape (n, *dims)
        agg = np.tensordot(weights_n, stacked, axes=(0, 0))
        aggregated.append(np.asarray(agg))

    return aggregated


if __name__ == "__main__":
    import doctest

    doctest.testmod()
