"""
Federated Learning: enables machine learning on distributed data by moving the training to the data, instead of moving the data to the training.
Here’s a one-liner explanation:
 -Centralized machine learning: move the data to the computation.
 -Federated (machine) Learning: move the computation to the data.

This script demonstrates the working of the Federated Averaging algorithm (FedAvg)
using a minimal, from-scratch approach with only NumPy.

Overview:
- Synthetic data is generated and distributed among several clients.
- Each client performs local gradient-based updates on its dataset.
- The central server combines all updated client models by averaging them
  according to the number of samples each client has.
- The process repeats for multiple communication rounds.

Key Functions:
    ▪ create_client_datasets(...)
    ▪ initialize_parameters(...)
    ▪ client_update(...)
    ▪ aggregate_models(...)
    ▪ evaluate_global_model(...)
    ▪ run_federated_training(...)

Example Usage:
   we can use in python federated_learning_simulation.py

Reference :

-(GitHub): "Federated Learning from Scratch (NumPy-based)"
  Ex: https://github.com/omar-fl/federated-learning-from-scratch
-(Medium article): “Federated Learning from Scratch with NumPy”
  Ex: https://medium.com/@niveditapatnaik/federated-learning-from-scratch-with-numpy-ff9c62a2a4a9
"""

from typing import List, Tuple
import numpy as np


def create_client_datasets(
    n_clients: int,
    samples_each: int,
    n_features: int,
    noise: float = 0.1,
    seed: int = 42,
) -> List[Tuple[np.ndarray, np.ndarray]]:
    """
    Generates synthetic linear regression datasets for multiple clients.
    Each dataset includes a bias term and Gaussian noise.

    Returns:
        A list containing tuples of (X, y) for each client.
        X has shape (samples_each, n_features + 1).
    """
    rng = np.random.default_rng(seed)
    true_weights = rng.normal(0, 1, n_features + 1)
    clients = []

    for _ in range(n_clients):
        X = rng.normal(0, 1, (samples_each, n_features))
        X_bias = np.c_[np.ones((samples_each, 1)), X]
        y = X_bias @ true_weights + rng.normal(0, noise, samples_each)
        clients.append((X_bias, y))

    return clients


def initialize_parameters(n_params: int, seed: int = 0) -> np.ndarray:
    """
    Initialize model parameters (weights + bias) randomly.

    >>> params = initialize_parameters(3, seed=0)
    >>> len(params)
    3
    >>> isinstance(params, np.ndarray)
    True
    """
    rng = np.random.default_rng(seed)
    return rng.normal(0, 0.01, n_params)


def mean_squared_error(params: np.ndarray, X: np.ndarray, y: np.ndarray) -> float:
    """Computes mean squared error for predictions on dataset (X, y).
    >>> params = np.array([0.0, 1.0])
    >>> X = np.array([[1.0, 0.0], [1.0, 1.0]])
    >>> y = np.array([0.0, 2.0])
    >>> mean_squared_error(params, X, y)
    0.5
    """
    predictions = X @ params
    return float(np.mean((predictions - y) ** 2))


def evaluate_global_model(
    params: np.ndarray, client_data: List[Tuple[np.ndarray, np.ndarray]]
) -> float:
    """Evaluates the average global MSE across all client datasets."""
    total_loss, total_samples = 0.0, 0

    for X, y in client_data:
        total_loss += np.sum((X @ params - y) ** 2)
        total_samples += len(y)

    return float(total_loss / total_samples)


def client_update(
    params: np.ndarray,
    X: np.ndarray,
    y: np.ndarray,
    lr: float = 0.01,
    epochs: int = 1,
    batch_size: int = 0,
) -> np.ndarray:
    """
    Performs local training on a client's dataset.
    Uses basic gradient descent (full batch or mini-batch depending on batch_size).
    """
    updated_params = params.copy()
    n_samples = len(y)

    for _ in range(epochs):
        if batch_size <= 0 or batch_size >= n_samples:
            # Full-batch gradient descent
            preds = X @ updated_params
            grad = (2 / n_samples) * (X.T @ (preds - y))
            updated_params -= lr * grad
        else:
            # Mini-batch gradient descent
            order = np.random.permutation(n_samples)
            for i in range(0, n_samples, batch_size):
                idx = order[i : i + batch_size]
                Xb, yb = X[idx], y[idx]
                preds = Xb @ updated_params
                grad = (2 / len(yb)) * (Xb.T @ (preds - yb))
                updated_params -= lr * grad

    return updated_params


def aggregate_models(models: List[np.ndarray], sizes: List[int]) -> np.ndarray:
    """
    Combines client models by computing a weighted average
    based on the number of samples each client used.

      >>> w1 = np.array([1.0, 2.0])
      >>> w2 = np.array([3.0, 4.0])
      >>> aggregate_models([w1, w2], [1, 1])
    array([2., 3.])
    """
    total_samples = sum(sizes)
    if total_samples == 0:
        raise ValueError("Cannot aggregate: total sample size is zero.")

    aggregated = np.zeros_like(models[0], dtype=float)
    for w, n in zip(models, sizes):
        aggregated += (n / total_samples) * w
    return aggregated


def run_federated_training(
    clients: List[Tuple[np.ndarray, np.ndarray]],
    rounds: int = 10,
    local_epochs: int = 1,
    lr: float = 0.01,
    batch_size: int = 0,
    seed: int = 0,
) -> Tuple[np.ndarray, List[float]]:
    """
    Runs the full FedAvg simulation for the given client datasets.

    Returns:
        final_parameters : np.ndarray
        loss_history : list of MSE values over communication rounds
    """
    n_params = clients[0][0].shape[1]
    global_params = initialize_parameters(n_params, seed)
    history = []

    for round_num in range(1, rounds + 1):
        client_models, client_sizes = [], []

        for X, y in clients:
            local_params = client_update(
                global_params, X, y, lr, local_epochs, batch_size
            )
            client_models.append(local_params)
            client_sizes.append(len(y))

        global_params = aggregate_models(client_models, client_sizes)
        mse = evaluate_global_model(global_params, clients)
        history.append(mse)

        print(f"Round {round_num}/{rounds} - Global MSE: {mse:.6f}")

    return global_params, history


if __name__ == "__main__":
    # Example demonstration
    datasets = create_client_datasets(
        n_clients=5, samples_each=200, n_features=3, noise=0.5, seed=123
    )
    final_model, loss_curve = run_federated_training(
        datasets, rounds=12, local_epochs=2, lr=0.05
    )

    print("\nFinal model parameters:\n", np.round(final_model, 4))

    try:
        import matplotlib.pyplot as plt

        plt.plot(loss_curve, marker="o")
        plt.title("Federated Averaging - Training Loss Curve")
        plt.xlabel("Round")
        plt.ylabel("Mean Squared Error")
        plt.grid(True)
        plt.show()
    except ImportError:
        pass

"""
 for testing:
    Create "tests/test_federated_averaging.py"

    " import numpy as np
      from machine_learning.federated_learning import federated_averaging as fed

      def test_loss_reduction_in_fedavg():
      # Define a small, reproducible test scenario
      clients = fed.create_synthetic_clients(
        n_clients=3,
        samples_per_client=80,
        n_features=2,
        noise_level=0.3,
        seed=0
      ) "

"""
