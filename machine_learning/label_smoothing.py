"""
Label Smoothing is a regularization technique used during training of
classification models. Instead of using hard one-hot encoded targets
(e.g. [0, 0, 1, 0]), it softens the labels by distributing a small
amount of probability mass (epsilon) uniformly across all classes.

This prevents the model from becoming overconfident and improves
generalization, especially when training data is noisy or limited.

Formula:
    smoothed_label = (1 - epsilon) * one_hot + epsilon / num_classes

Reference:
    Szegedy et al., "Rethinking the Inception Architecture for Computer
    Vision", https://arxiv.org/abs/1512.00567

Example usage:
    >>> import numpy as np
    >>> smoother = LabelSmoother(num_classes=4, epsilon=0.1)
    >>> smoother.smooth(2)
    array([0.025, 0.025, 0.925, 0.025])
"""

import numpy as np


class LabelSmoother:
    """
    Applies label smoothing to a one-hot encoded target vector.

    Attributes:
        num_classes: Total number of classes.
        epsilon: Smoothing factor in the range [0.0, 1.0).
                 0.0 means no smoothing (standard one-hot).

    >>> smoother = LabelSmoother(num_classes=3, epsilon=0.0)
    >>> smoother.smooth(1)
    array([0., 1., 0.])

    >>> smoother = LabelSmoother(num_classes=3, epsilon=0.3)
    >>> smoother.smooth(0)
    array([0.8, 0.1, 0.1])
    """

    def __init__(self, num_classes: int, epsilon: float = 0.1) -> None:
        """
        Initialize LabelSmoother.

        Args:
            num_classes: Number of target classes (must be >= 2).
            epsilon: Smoothing factor. Must satisfy 0.0 <= epsilon < 1.0.

        Raises:
            ValueError: If num_classes < 2 or epsilon is out of range.

        >>> LabelSmoother(num_classes=1, epsilon=0.1)
        Traceback (most recent call last):
            ...
        ValueError: num_classes must be at least 2.

        >>> LabelSmoother(num_classes=3, epsilon=1.0)
        Traceback (most recent call last):
            ...
        ValueError: epsilon must be in [0.0, 1.0).
        """
        if num_classes < 2:
            raise ValueError("num_classes must be at least 2.")
        if not (0.0 <= epsilon < 1.0):
            raise ValueError("epsilon must be in [0.0, 1.0).")
        self.num_classes = num_classes
        self.epsilon = epsilon

    def smooth(self, true_class: int) -> np.ndarray:
        """
        Return a smoothed label vector for the given true class index.

        Args:
            true_class: The index of the correct class (0-indexed).

        Returns:
            A numpy array of shape (num_classes,) with smoothed probabilities.
            All values sum to 1.0.

        Raises:
            ValueError: If true_class is out of range.

        >>> smoother = LabelSmoother(num_classes=4, epsilon=0.1)
        >>> smoother.smooth(2)
        array([0.025, 0.025, 0.925, 0.025])

        >>> smoother.smooth(0)
        array([0.925, 0.025, 0.025, 0.025])

        >>> float(round(smoother.smooth(1).sum(), 10))
        1.0

        >>> smoother.smooth(5)
        Traceback (most recent call last):
            ...
        ValueError: true_class index 5 is out of range for 4 classes.
        """
        if not (0 <= true_class < self.num_classes):
            raise ValueError(
                f"true_class index {true_class} is out of range "
                f"for {self.num_classes} classes."
            )
        # Start with uniform distribution weighted by epsilon
        labels = np.full(self.num_classes, self.epsilon / self.num_classes)
        # Add the remaining probability mass to the true class
        labels[true_class] += 1.0 - self.epsilon
        return labels

    def smooth_batch(self, true_classes: list[int]) -> np.ndarray:
        """
        Return smoothed label vectors for a batch of true class indices.

        Args:
            true_classes: List of true class indices.

        Returns:
            A numpy array of shape (batch_size, num_classes).

        >>> smoother = LabelSmoother(num_classes=3, epsilon=0.3)
        >>> smoother.smooth_batch([0, 2])
        array([[0.8, 0.1, 0.1],
               [0.1, 0.1, 0.8]])
        """
        return np.array([self.smooth(c) for c in true_classes])


def cross_entropy_loss(
    smoothed_labels: np.ndarray, predicted_probs: np.ndarray
) -> float:
    """
    Compute cross-entropy loss between smoothed labels and predicted
    probability distribution.

    Args:
        smoothed_labels: Target distribution, shape (num_classes,).
        predicted_probs: Predicted probabilities, shape (num_classes,).
                         Values must be in (0, 1] and sum to 1.

    Returns:
        Scalar cross-entropy loss value.

    >>> import numpy as np
    >>> labels = np.array([0.025, 0.025, 0.925, 0.025])
    >>> preds  = np.array([0.01,  0.01,  0.97,  0.01])
    >>> round(cross_entropy_loss(labels, preds), 4)
    0.3736
    """
    # Clip to avoid log(0)
    predicted_probs = np.clip(predicted_probs, 1e-12, 1.0)
    return float(-np.sum(smoothed_labels * np.log(predicted_probs)))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    print("\n--- Label Smoothing Demo ---")
    smoother = LabelSmoother(num_classes=5, epsilon=0.1)

    print("\nHard one-hot (no smoothing, epsilon=0.0):")
    hard = LabelSmoother(num_classes=5, epsilon=0.0)
    print(f"  Class 2 -> {hard.smooth(2)}")

    print("\nSmoothed labels (epsilon=0.1):")
    print(f"  Class 2 -> {smoother.smooth(2)}")

    print("\nBatch smoothing for classes [0, 2, 4]:")
    print(smoother.smooth_batch([0, 2, 4]))

    print("\nCross-entropy loss with smoothed target vs confident prediction:")
    smoothed = smoother.smooth(2)
    confident_pred = np.array([0.01, 0.01, 0.96, 0.01, 0.01])
    print(f"  Loss = {cross_entropy_loss(smoothed, confident_pred):.4f}")