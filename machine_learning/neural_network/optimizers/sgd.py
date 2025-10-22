"""
Stochastic Gradient Descent (SGD) optimizer.
"""

from typing import List

def sgd_update(weights: List[float], grads: List[float], lr: float) -> List[float]:
    """
    Update weights using SGD.

    Args:
        weights (List[float]): Current weights
        grads (List[float]): Gradients
        lr (float): Learning rate

    Returns:
        List[float]: Updated weights

    Example:
        >>> sgd_update([0.5, -0.2], [0.1, -0.1], 0.01)
        [0.499, -0.199]
    """
    return [w - lr * g for w, g in zip(weights, grads)]
