"""
Federated Averaging (FedAvg)
https://arxiv.org/abs/1602.05629

This module provides a minimal, educational implementation of the Federated
Learning paradigm using the Federated Averaging algorithm. Multiple clients
compute local model updates on their private data and the server aggregates
their updates by (weighted) averaging without collecting raw data.

Notes
-----
- This implementation is framework-agnostic and uses NumPy arrays to represent
  model parameters for simplicity and portability within this repository.
- It demonstrates the mechanics of FedAvg, not production concerns like
  privacy amplification (e.g., differential privacy), robustness, or security.

Terminology
-----------
- Global model: a list of NumPy arrays representing model parameters.
- Client update: new model parameters produced locally, or the delta from the
  global model; we aggregate parameters directly here for clarity.

Examples
--------
Create three synthetic "clients" whose local training produces simple parameter
arrays, then aggregate them with FedAvg.

>>> import numpy as np
>>> # Global model with two parameter tensors
>>> global_model = [np.array([0.0, 0.0]), np.array([[0.0]])]
>>> # Client models after local training
>>> client_models = [
...     [np.array([1.0, 2.0]), np.array([[1.0]])],
...     [np.array([3.0, 4.0]), np.array([[3.0]])],
...     [np.array([5.0, 6.0]), np.array([[5.0]])],
... ]
>>> # Equal weights -> simple average
>>> new_global = federated_average(client_models)
>>> [arr.tolist() for arr in new_global]
[[3.0, 4.0], [[3.0]]]

Weighted averaging by client data sizes:

>>> weights = np.array([10, 20, 30], dtype=float)
>>> new_global_w = federated_average(client_models, weights)
>>> [arr.tolist() for arr in new_global_w]
[[3.6666666666666665, 4.666666666666666], [[3.6666666666666665]]]

Contract
--------
Inputs:
  - client_models: list[list[np.ndarray]]: each inner list mirrors model layers
  - weights: Optional[np.ndarray] of shape (num_clients,), non-negative, sums to > 0
Output:
  - list[np.ndarray]: aggregated model parameters, same shapes as client models
Error modes:
  - ValueError for empty clients, shape mismatch, or invalid weights
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
    """
    Aggregate client model parameters using (weighted) averaging.

    Parameters
    ----------
    client_models : list[list[np.ndarray]]
        Model parameters for each client; all clients must have same shapes.
    weights : np.ndarray | None
        Optional non-negative weights per client. If None, equal weights.

    Returns
    -------
    list[np.ndarray]
        Aggregated model parameters (same shapes as client tensors).

    Examples
    --------
    >>> import numpy as np
    >>> cm = [
    ...     [np.array([1.0, 2.0])],
    ...     [np.array([3.0, 4.0])],
    ... ]
    >>> [arr.tolist() for arr in federated_average(cm)]
    [[2.0, 3.0]]
    >>> w = np.array([1.0, 3.0])
    >>> [arr.tolist() for arr in federated_average(cm, w)]
    [[2.5, 3.5]]
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
