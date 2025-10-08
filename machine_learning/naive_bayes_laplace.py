"""
Naive Bayes Classifier with Laplace Smoothing implementation from scratch.

Naive Bayes is a probabilistic classifier based on applying Bayes' theorem with
strong independence assumptions between features. This implementation includes
Laplace smoothing (also known as add-one smoothing) to handle zero probabilities
and improve generalization.

Key features:
- Multinomial Naive Bayes with Laplace smoothing
- Support for both discrete and continuous features
- Gaussian Naive Bayes for continuous features
- Comprehensive probability calculations
- Robust handling of unseen features/values

Reference: https://en.wikipedia.org/wiki/Naive_Bayes_classifier
"""

import doctest

import numpy as np


class NaiveBayesLaplace:
    """
    Naive Bayes Classifier with Laplace Smoothing.

    This implementation provides both multinomial and Gaussian variants
    of the Naive Bayes algorithm with Laplace smoothing for robust
    probability estimation.
    """

    def __init__(self, alpha: float = 1.0, feature_type: str = "discrete") -> None:
        """
        Initialize Naive Bayes classifier.

        Args:
            alpha: Laplace smoothing parameter (alpha > 0)
            feature_type: Type of features ('discrete' or 'continuous')

        >>> nb = NaiveBayesLaplace(alpha=1.0, feature_type="discrete")
        >>> nb.alpha
        1.0
        >>> nb.feature_type
        'discrete'
        """
        self.alpha = alpha
        self.feature_type = feature_type

        # Model parameters
        self.classes_: np.ndarray | None = None
        self.class_prior_: dict[int, float] = {}
        self.feature_count_: dict[int, dict[int, dict[int, int]]] = {}
        self.feature_log_prob_: dict[int, dict[int, dict[int, float]]] = {}
        self.feature_mean_: dict[int, dict[int, float]] = {}
        self.feature_var_: dict[int, dict[int, float]] = {}
        self.n_features_: int | None = None

    def _check_input(self, x: np.ndarray, y: np.ndarray) -> None:
        """
        Validate input data.

        Args:
            x: Feature matrix
            y: Target labels

        Raises:
            ValueError: If input is invalid
        """
        if x.ndim != 2:
            raise ValueError("x must be 2-dimensional")
        if len(x) != len(y):
            raise ValueError("x and y must have the same length")
        if self.alpha <= 0:
            raise ValueError("Alpha must be positive")
        if self.feature_type not in ["discrete", "continuous"]:
            raise ValueError("feature_type must be 'discrete' or 'continuous'")

    def _compute_class_prior(self, y: np.ndarray) -> dict[int, float]:
        """
        Compute prior probabilities for each class.

        Args:
            y: Target labels

        Returns:
            Dictionary mapping class to prior probability

        >>> nb = NaiveBayesLaplace()
        >>> y = np.array([0, 1, 0, 1, 1])
        >>> prior = nb._compute_class_prior(y)
        >>> len(prior)
        2
        >>> bool(np.isclose(sum(prior.values()), 1.0))
        True
        """
        classes, counts = np.unique(y, return_counts=True)
        total_samples = len(y)

        prior = {}
        for class_label, count in zip(classes, counts):
            prior[class_label] = count / total_samples

        return prior

    def _compute_feature_counts(
        self, x: np.ndarray, y: np.ndarray
    ) -> dict[int, dict[int, dict[int, int]]]:
        """
        Compute feature counts for each class (for discrete features).

        Args:
            x: Feature matrix
            y: Target labels

        Returns:
            Nested dictionary: class -> feature -> count

        >>> nb = NaiveBayesLaplace()
        >>> x = np.array([[0, 1], [1, 0], [0, 1]])
        >>> y = np.array([0, 1, 0])
        >>> counts = nb._compute_feature_counts(x, y)
        >>> int(counts[0][0][0])  # class 0, feature 0, value 0
        2
        >>> int(counts[1][1][0])  # class 1, feature 1, value 0
        1
        """
        feature_counts: dict[int, dict[int, dict[int, int]]] = {}

        for class_label in np.unique(y):
            feature_counts[class_label] = {}

            # Get samples for this class
            class_mask = y == class_label
            x_class = x[class_mask]

            # Count occurrences of each feature value
            for feature_idx in range(x.shape[1]):
                feature_counts[class_label][feature_idx] = {}

                for feature_value in np.unique(x[:, feature_idx]):
                    count = np.sum(x_class[:, feature_idx] == feature_value)
                    feat_val_int = int(feature_value)
                    feature_counts[class_label][feature_idx][feat_val_int] = int(count)

        return feature_counts

    def _compute_feature_statistics(
        self, x: np.ndarray, y: np.ndarray
    ) -> tuple[dict[int, dict[int, float]], dict[int, dict[int, float]]]:
        """
        Compute mean and variance for each feature in each class (continuous features).

        Args:
            x: Feature matrix
            y: Target labels

        Returns:
            Tuple of (means, variances) dictionaries

        >>> nb = NaiveBayesLaplace(feature_type="continuous")
        >>> x = np.array([[1.0, 2.0], [2.0, 3.0], [1.5, 2.5]])
        >>> y = np.array([0, 1, 0])
        >>> means, vars = nb._compute_feature_statistics(x, y)
        >>> len(means)
        2
        >>> len(vars)
        2
        """
        means: dict[int, dict[int, float]] = {}
        variances: dict[int, dict[int, float]] = {}

        for class_label in np.unique(y):
            means[class_label] = {}
            variances[class_label] = {}

            # Get samples for this class
            class_mask = y == class_label
            x_class = x[class_mask]

            # Compute mean and variance for each feature
            for feature_idx in range(x.shape[1]):
                feature_values = x_class[:, feature_idx]
                means[class_label][feature_idx] = np.mean(feature_values)
                # Add small epsilon to avoid division by zero
                variances[class_label][feature_idx] = np.var(feature_values) + 1e-9

        return means, variances

    def _compute_log_probabilities_discrete(
        self, x: np.ndarray, y: np.ndarray
    ) -> dict[int, dict[int, dict[int, float]]]:
        """
        Compute log probabilities for discrete features with Laplace smoothing.

        Args:
            x: Feature matrix
            y: Target labels

        Returns:
            Nested dictionary: class -> feature -> value -> log_probability
        """
        feature_counts = self._compute_feature_counts(x, y)
        log_probabilities: dict[int, dict[int, dict[int, float]]] = {}

        for class_label in np.unique(y):
            log_probabilities[class_label] = {}
            class_mask = y == class_label
            n_class_samples = np.sum(class_mask)

            for feature_idx in range(x.shape[1]):
                log_probabilities[class_label][feature_idx] = {}

                # Get all possible values for this feature
                all_values = np.unique(x[:, feature_idx])

                for feature_value in all_values:
                    # Count occurrences of this value in this class
                    count = feature_counts[class_label][feature_idx].get(
                        int(feature_value), 0
                    )

                    # Apply Laplace smoothing formula
                    n_unique_values = len(all_values)
                    smoothed_prob = (count + self.alpha) / (
                        n_class_samples + self.alpha * n_unique_values
                    )

                    # Store log probability
                    log_probabilities[class_label][feature_idx][feature_value] = np.log(
                        smoothed_prob
                    )

        return log_probabilities

    def _gaussian_log_probability(self, x: float, mean: float, var: float) -> float:
        """
        Compute log probability of x under Gaussian distribution.

        Args:
            x: Input value
            mean: Mean of Gaussian distribution
            var: Variance of Gaussian distribution

        Returns:
            Log probability

        >>> nb = NaiveBayesLaplace(feature_type="continuous")
        >>> log_prob = nb._gaussian_log_probability(0.0, 0.0, 1.0)
        >>> isinstance(log_prob, float)
        True
        """
        # Gaussian log probability: -0.5 * log(2*pi*var) - (x-mean)^2/(2*var)
        return -0.5 * (np.log(2 * np.pi * var) + (x - mean) ** 2 / var)

    def fit(self, x: np.ndarray, y: np.ndarray) -> "NaiveBayesLaplace":
        """
        Fit the Naive Bayes classifier.

        Args:
            x: Feature matrix of shape (n_samples, n_features)
            y: Target labels of shape (n_samples,)

        Returns:
            Self for method chaining

        >>> nb = NaiveBayesLaplace()
        >>> x = np.array([[0, 1], [1, 0], [0, 1], [1, 1]])
        >>> y = np.array([0, 1, 0, 1])
        >>> _ = nb.fit(x, y)
        """
        self._check_input(x, y)

        self.classes_ = np.unique(y)
        self.n_features_ = x.shape[1]

        # Compute class priors
        self.class_prior_ = self._compute_class_prior(y)

        if self.feature_type == "discrete":
            # For discrete features: compute feature counts and log probabilities
            self.feature_count_ = self._compute_feature_counts(x, y)
            self.feature_log_prob_ = self._compute_log_probabilities_discrete(x, y)

        elif self.feature_type == "continuous":
            # For continuous features: compute means and variances
            self.feature_mean_, self.feature_var_ = self._compute_feature_statistics(
                x, y
            )

        return self

    def _predict_log_proba_discrete(self, x: np.ndarray) -> np.ndarray:
        """
        Predict log probabilities for discrete features.

        Args:
            x: Feature matrix

        Returns:
            Log probability matrix of shape (n_samples, n_classes)
        """
        if self.classes_ is None:
            raise ValueError("Model must be fitted before predict")

        n_samples = x.shape[0]
        n_classes = len(self.classes_)
        log_proba = np.zeros((n_samples, n_classes))

        for i, class_label in enumerate(self.classes_):
            # Start with log prior probability
            log_proba[:, i] = np.log(self.class_prior_[class_label])

            # Add log likelihood for each feature
            for feature_idx in range(x.shape[1]):
                for sample_idx in range(n_samples):
                    feature_value = x[sample_idx, feature_idx]

                    # Get log probability for this feature value in this class
                    feature_value_int = int(feature_value)
                    if (
                        feature_value_int
                        in self.feature_log_prob_[class_label][feature_idx]
                    ):
                        log_prob = self.feature_log_prob_[class_label][feature_idx][
                            feature_value_int
                        ]
                    else:
                        # Unseen feature value: use Laplace smoothing
                        all_values = list(
                            self.feature_log_prob_[class_label][feature_idx].keys()
                        )
                        n_unique_values = len(all_values) + 1  # +1 for the unseen value

                        # Estimate class size from existing counts
                        class_samples = sum(
                            self.feature_count_[class_label][feature_idx].values()
                        )
                        smoothed_prob = self.alpha / (
                            class_samples + self.alpha * n_unique_values
                        )
                        log_prob = np.log(smoothed_prob)

                    log_proba[sample_idx, i] += log_prob

        return log_proba

    def _predict_log_proba_continuous(self, x: np.ndarray) -> np.ndarray:
        """
        Predict log probabilities for continuous features.

        Args:
            x: Feature matrix

        Returns:
            Log probability matrix of shape (n_samples, n_classes)
        """
        if self.classes_ is None:
            raise ValueError("Model must be fitted before predict")

        n_samples = x.shape[0]
        n_classes = len(self.classes_)
        log_proba = np.zeros((n_samples, n_classes))

        for i, class_label in enumerate(self.classes_):
            # Start with log prior probability
            log_proba[:, i] = np.log(self.class_prior_[class_label])

            # Add log likelihood for each feature
            for feature_idx in range(x.shape[1]):
                means = self.feature_mean_[class_label][feature_idx]
                variances = self.feature_var_[class_label][feature_idx]

                # Compute Gaussian log probabilities for all samples
                feature_values = x[:, feature_idx]
                log_proba[:, i] += np.array(
                    [
                        self._gaussian_log_probability(val, means, variances)
                        for val in feature_values
                    ]
                )

        return log_proba

    def predict_log_proba(self, x: np.ndarray) -> np.ndarray:
        """
        Predict log probabilities for each class.

        Args:
            x: Feature matrix of shape (n_samples, n_features)

        Returns:
            Log probability matrix of shape (n_samples, n_classes)

        >>> nb = NaiveBayesLaplace()
        >>> x_train = np.array([[0, 1], [1, 0], [0, 1], [1, 1]])
        >>> y_train = np.array([0, 1, 0, 1])
        >>> _ = nb.fit(x_train, y_train)
        >>> x_test = np.array([[0, 1], [1, 0]])
        >>> log_proba = nb.predict_log_proba(x_test)
        >>> log_proba.shape
        (2, 2)
        """
        if self.classes_ is None:
            raise ValueError("Model must be fitted before prediction")

        if self.feature_type == "discrete":
            return self._predict_log_proba_discrete(x)
        else:
            return self._predict_log_proba_continuous(x)

    def predict_proba(self, x: np.ndarray) -> np.ndarray:
        """
        Predict class probabilities.

        Args:
            x: Feature matrix of shape (n_samples, n_features)

        Returns:
            Probability matrix of shape (n_samples, n_classes)

        >>> nb = NaiveBayesLaplace()
        >>> x_train = np.array([[0, 1], [1, 0], [0, 1], [1, 1]])
        >>> y_train = np.array([0, 1, 0, 1])
        >>> _ = nb.fit(x_train, y_train)
        >>> x_test = np.array([[0, 1], [1, 0]])
        >>> proba = nb.predict_proba(x_test)
        >>> proba.shape
        (2, 2)
        >>> np.allclose(np.sum(proba, axis=1), 1.0)
        True
        """
        log_proba = self.predict_log_proba(x)

        # Convert log probabilities to probabilities using log-sum-exp trick
        # for numerical stability
        max_log_proba = np.max(log_proba, axis=1, keepdims=True)
        exp_log_proba = np.exp(log_proba - max_log_proba)
        proba = exp_log_proba / np.sum(exp_log_proba, axis=1, keepdims=True)

        return proba

    def predict(self, x: np.ndarray) -> np.ndarray:
        """
        Predict class labels.

        Args:
            x: Feature matrix of shape (n_samples, n_features)

        Returns:
            Predicted class labels

        >>> nb = NaiveBayesLaplace()
        >>> x_train = np.array([[0, 1], [1, 0], [0, 1], [1, 1]])
        >>> y_train = np.array([0, 1, 0, 1])
        >>> _ = nb.fit(x_train, y_train)
        >>> x_test = np.array([[0, 1], [1, 0]])
        >>> predictions = nb.predict(x_test)
        >>> len(predictions) == x_test.shape[0]
        True
        """
        if self.classes_ is None:
            raise ValueError("Model must be fitted before predict")

        log_proba = self.predict_log_proba(x)
        predictions = self.classes_[np.argmax(log_proba, axis=1)]
        return predictions

    def score(self, x: np.ndarray, y: np.ndarray) -> float:
        """
        Compute accuracy score.

        Args:
            x: Feature matrix
            y: True labels

        Returns:
            Accuracy score between 0 and 1

        >>> nb = NaiveBayesLaplace()
        >>> x = np.array([[0, 1], [1, 0], [0, 1], [1, 1]])
        >>> y = np.array([0, 1, 0, 1])
        >>> _ = nb.fit(x, y)
        >>> score = nb.score(x, y)
        >>> bool(0 <= score <= 1)
        True
        """
        predictions = self.predict(x)
        return np.mean(predictions == y)


def generate_discrete_data(
    n_samples: int = 100,
    n_features: int = 3,
    n_classes: int = 2,
    random_state: int = 42,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate discrete sample data for testing.

    Args:
        n_samples: Number of samples
        n_features: Number of features
        n_classes: Number of classes
        random_state: Random seed

    Returns:
        Tuple of (x, y)
    """
    rng = np.random.default_rng(random_state)

    # Generate random discrete features (0, 1, 2)
    x = rng.integers(0, 3, size=(n_samples, n_features))

    # Create simple decision rule for labels
    y = np.sum(x, axis=1) % n_classes

    return x, y


def generate_continuous_data(
    n_samples: int = 100,
    n_features: int = 2,
    n_classes: int = 2,
    random_state: int = 42,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate continuous sample data for testing.

    Args:
        n_samples: Number of samples
        n_features: Number of features
        n_classes: Number of classes
        random_state: Random seed

    Returns:
        Tuple of (x, y)
    """
    rng = np.random.default_rng(random_state)

    # Generate continuous features with different means for different classes
    x = rng.standard_normal((n_samples, n_features))
    y = rng.integers(0, n_classes, size=n_samples)

    # Add class-specific offsets
    for class_label in range(n_classes):
        mask = y == class_label
        x[mask] += class_label * 2  # Separate classes by offset

    return x, y


def compare_with_sklearn() -> None:
    """
    Compare our implementation with scikit-learn's NaiveBayes.
    """
    try:
        from sklearn.metrics import accuracy_score
        from sklearn.naive_bayes import GaussianNB, MultinomialNB

        print("=== Discrete Features Comparison ===")
        x_disc, y_disc = generate_discrete_data(n_samples=100, n_features=4)

        # Split data
        split_idx = int(0.8 * len(x_disc))
        x_train, x_test = x_disc[:split_idx], x_disc[split_idx:]
        y_train, y_test = y_disc[:split_idx], y_disc[split_idx:]

        # Our implementation
        nb_ours = NaiveBayesLaplace(alpha=1.0, feature_type="discrete")
        nb_ours.fit(x_train, y_train)
        nb_ours.predict(x_test)
        accuracy_ours = nb_ours.score(x_test, y_test)

        # Scikit-learn implementation
        nb_sklearn = MultinomialNB(alpha=1.0)
        nb_sklearn.fit(x_train, y_train)
        predictions_sklearn = nb_sklearn.predict(x_test)
        accuracy_sklearn = accuracy_score(y_test, predictions_sklearn)

        print(f"Our implementation accuracy: {accuracy_ours:.4f}")
        print(f"Scikit-learn accuracy: {accuracy_sklearn:.4f}")
        print(f"Difference: {abs(accuracy_ours - accuracy_sklearn):.4f}")

        print("\n=== Continuous Features Comparison ===")
        x_cont, y_cont = generate_continuous_data(n_samples=100, n_features=2)

        # Split data
        split_idx = int(0.8 * len(x_cont))
        x_train, x_test = x_cont[:split_idx], x_cont[split_idx:]
        y_train, y_test = y_cont[:split_idx], y_cont[split_idx:]

        # Our implementation
        nb_ours_cont = NaiveBayesLaplace(alpha=1.0, feature_type="continuous")
        nb_ours_cont.fit(x_train, y_train)
        nb_ours_cont.predict(x_test)
        accuracy_ours_cont = nb_ours_cont.score(x_test, y_test)

        # Scikit-learn implementation
        nb_sklearn_cont = GaussianNB()
        nb_sklearn_cont.fit(x_train, y_train)
        predictions_sklearn_cont = nb_sklearn_cont.predict(x_test)
        accuracy_sklearn_cont = accuracy_score(y_test, predictions_sklearn_cont)

        print(f"Our implementation accuracy: {accuracy_ours_cont:.4f}")
        print(f"Scikit-learn accuracy: {accuracy_sklearn_cont:.4f}")
        print(f"Difference: {abs(accuracy_ours_cont - accuracy_sklearn_cont):.4f}")

    except ImportError:
        print("Scikit-learn not available for comparison")


def main() -> None:
    """
    Demonstrate Naive Bayes with Laplace smoothing implementation.
    """
    print("=== Discrete Features Example ===")

    # Generate discrete data
    x_disc, y_disc = generate_discrete_data(n_samples=100, n_features=3, n_classes=2)

    print(f"Data shape: {x_disc.shape}")
    print(f"Classes: {np.unique(y_disc)}")
    print(f"Feature values: {np.unique(x_disc)}")

    # Train model
    nb_disc = NaiveBayesLaplace(alpha=1.0, feature_type="discrete")
    nb_disc.fit(x_disc, y_disc)

    # Make predictions
    nb_disc.predict(x_disc)
    probabilities = nb_disc.predict_proba(x_disc)

    print(f"Training accuracy: {nb_disc.score(x_disc, y_disc):.4f}")
    print(f"Sample probabilities: {probabilities[:5]}")

    # Test with unseen feature values
    x_unseen = np.array([[5, 6, 7], [8, 9, 10]])  # Unseen values
    predictions_unseen = nb_disc.predict(x_unseen)
    print(f"Predictions on unseen data: {predictions_unseen}")

    print("\n=== Continuous Features Example ===")

    # Generate continuous data
    x_cont, y_cont = generate_continuous_data(n_samples=100, n_features=2, n_classes=2)

    print(f"Data shape: {x_cont.shape}")
    print(f"Classes: {np.unique(y_cont)}")

    # Train model
    nb_cont = NaiveBayesLaplace(alpha=1.0, feature_type="continuous")
    nb_cont.fit(x_cont, y_cont)

    # Make predictions
    nb_cont.predict(x_cont)
    probabilities_cont = nb_cont.predict_proba(x_cont)

    print(f"Training accuracy: {nb_cont.score(x_cont, y_cont):.4f}")
    print(f"Sample probabilities: {probabilities_cont[:5]}")

    print("\n=== Comparison with Scikit-learn ===")
    compare_with_sklearn()


if __name__ == "__main__":
    doctest.testmod()
    main()
