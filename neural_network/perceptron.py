"""Single-layer perceptron classifier.

This implementation focuses on binary linear classification for educational
use and avoids interactive I/O, making it suitable for automated testing.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Perceptron:
    """Perceptron for binary classification with labels ``{-1, 1}``.

    Args:
        learning_rate: Weight update step size.
        max_epochs: Maximum number of training epochs.
        bias: Constant bias term appended to each sample.

    Examples:
        >>> data = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
        >>> labels = [-1, -1, -1, 1]  # logical AND
        >>> model = Perceptron(learning_rate=0.2, max_epochs=20)
        >>> model.fit(data, labels)
        4
        >>> model.predict([1.0, 1.0])
        1
        >>> model.predict([0.0, 1.0])
        -1
    """

    learning_rate: float = 0.01
    max_epochs: int = 1_000
    bias: float = 1.0
    weights: list[float] = field(default_factory=list)

    def fit(self, samples: list[list[float]], targets: list[int]) -> int:
        """Train model and return number of epochs performed."""
        if not samples:
            raise ValueError("samples must be non-empty")
        if not targets:
            raise ValueError("targets must be non-empty")
        if len(samples) != len(targets):
            raise ValueError("samples and targets must have the same length")

        feature_count = len(samples[0])
        if feature_count == 0 or any(
            len(sample) != feature_count for sample in samples
        ):
            raise ValueError("all samples must share the same non-zero feature length")
        if any(target not in {-1, 1} for target in targets):
            raise ValueError("targets must only contain -1 or 1")

        if not self.weights:
            self.weights = [0.0] * (feature_count + 1)

        transformed_samples = [[self.bias, *sample] for sample in samples]

        for epoch in range(1, self.max_epochs + 1):
            has_error = False
            for sample, target in zip(transformed_samples, targets):
                prediction = self._sign(
                    sum(weight * value for weight, value in zip(self.weights, sample))
                )
                if prediction != target:
                    update = self.learning_rate * (target - prediction)
                    self.weights = [
                        weight + update * value
                        for weight, value in zip(self.weights, sample)
                    ]
                    has_error = True

            if not has_error:
                return epoch

        return self.max_epochs

    def predict(self, sample: list[float]) -> int:
        """Predict class ``-1`` or ``1`` for one sample."""
        if not self.weights:
            raise ValueError("fit must be called before predict")
        if len(sample) + 1 != len(self.weights):
            raise ValueError("sample size does not match trained model")

        weighted_sum = self.weights[0] * self.bias + sum(
            weight * value for weight, value in zip(self.weights[1:], sample)
        )
        return self._sign(weighted_sum)

    @staticmethod
    def _sign(value: float) -> int:
        return 1 if value >= 0 else -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
