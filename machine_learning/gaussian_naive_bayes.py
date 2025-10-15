"""
Gaussian Naive Bayes Classifier

Naive Bayes is a probabilistic classifier based on Bayes' theorem with the
"naive" assumption of conditional independence between features.

Gaussian Naive Bayes assumes that features follow a normal (Gaussian) distribution.

For each class, we calculate:
- Mean (μ) and variance (σ²) of each feature
- Prior probability P(class)

For prediction, we use Bayes theorem:
P(class|X) = P(X|class) * P(class)

Where P(X|class) is calculated using the Gaussian probability density function:
P(x|class) = (1 / sqrt(2 * pi * sigma^2)) * exp(-(x - mu)^2 / (2 * sigma^2))

Reference: https://en.wikipedia.org/wiki/Naive_Bayes_classifier
"""

import numpy as np


class GaussianNaiveBayes:
    """
    Gaussian Naive Bayes Classifier

    Parameters
    ----------
    None

    Attributes
    ----------
    classes_ : ndarray of shape (n_classes,)
        The unique class labels
    class_priors_ : ndarray of shape (n_classes,)
        Probability of each class P(class)
    mean_ : ndarray of shape (n_classes, n_features)
        Mean of each feature per class
    var_ : ndarray of shape (n_classes, n_features)
        Variance of each feature per class

    Examples
    --------
    >>> import numpy as np
    >>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    >>> y = np.array([0, 0, 0, 1, 1, 1])
    >>> clf = GaussianNaiveBayes()
    >>> _ = clf.fit(X, y)
    >>> clf.predict(np.array([[-0.8, -1]]))
    array([0])
    >>> clf.predict(np.array([[3, 2]]))
    array([1])
    """

    def __init__(self) -> None:
        self.classes_: np.ndarray = np.array([])
        self.class_priors_: np.ndarray = np.array([])
        self.mean_: np.ndarray = np.array([])
        self.var_: np.ndarray = np.array([])

    def fit(self, X: np.ndarray, y: np.ndarray) -> "GaussianNaiveBayes":  # noqa: N803
        """
        Fit Gaussian Naive Bayes classifier

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)
            Training data
        y : ndarray of shape (n_samples,)
            Target values

        Returns
        -------
        self : object
            Returns self
        """
        self.classes_ = np.unique(y)
        n_classes = len(self.classes_)
        n_features = X.shape[1]

        # Initialize arrays for mean, variance, and priors
        self.mean_ = np.zeros((n_classes, n_features))
        self.var_ = np.zeros((n_classes, n_features))
        self.class_priors_ = np.zeros(n_classes)

        # Calculate mean, variance, and prior for each class
        for idx, c in enumerate(self.classes_):
            X_c = X[y == c]  # noqa: N806
            self.mean_[idx] = X_c.mean(axis=0)
            self.var_[idx] = X_c.var(axis=0)
            self.class_priors_[idx] = X_c.shape[0] / X.shape[0]

        return self

    def _calculate_likelihood(self, class_idx: int, x: np.ndarray) -> float:
        """
        Calculate the Gaussian probability density function (likelihood)
        P(x|class) for all features

        Parameters
        ----------
        class_idx : int
            Index of the class
        x : ndarray of shape (n_features,)
            Input sample

        Returns
        -------
        likelihood : float
            Product of likelihoods for all features
        """
        mean = self.mean_[class_idx]
        var = self.var_[class_idx]

        # Gaussian probability density function
        # P(x|class) = (1 / sqrt(2 * pi * sigma^2)) * exp(-(x - mu)^2 / (2 * sigma^2))
        numerator = np.exp(-((x - mean) ** 2) / (2 * var))
        denominator = np.sqrt(2 * np.pi * var)

        # Calculate probability for each feature and return product
        # Using log probabilities to avoid numerical underflow
        return np.prod(numerator / denominator)

    def _calculate_posterior(self, x: np.ndarray) -> np.ndarray:
        """
        Calculate posterior probability for each class
        P(class|x) = P(x|class) * P(class)

        Parameters
        ----------
        x : ndarray of shape (n_features,)
            Input sample

        Returns
        -------
        posteriors : ndarray of shape (n_classes,)
            Posterior probability for each class
        """
        posteriors = []
        for idx in range(len(self.classes_)):
            prior = np.log(self.class_priors_[idx])
            likelihood = self._calculate_likelihood(idx, x)
            # Use log to avoid numerical underflow
            posterior = prior + np.sum(np.log(likelihood + 1e-10))
            posteriors.append(posterior)

        return np.array(posteriors)

    def predict(self, X: np.ndarray) -> np.ndarray:  # noqa: N803
        """
        Perform classification on an array of test vectors X

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)
            Test data

        Returns
        -------
        y_pred : ndarray of shape (n_samples,)
            Predicted target values for X
        """
        y_pred = [self._predict_single(x) for x in X]
        return np.array(y_pred)

    def _predict_single(self, x: np.ndarray) -> int:
        """
        Predict class for a single sample

        Parameters
        ----------
        x : ndarray of shape (n_features,)
            Input sample

        Returns
        -------
        prediction : int
            Predicted class label
        """
        posteriors = self._calculate_posterior(x)
        return self.classes_[np.argmax(posteriors)]

    def predict_proba(self, X: np.ndarray) -> np.ndarray:  # noqa: N803
        """
        Return probability estimates for the test vector X

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)
            Test data

        Returns
        -------
        probabilities : ndarray of shape (n_samples, n_classes)
            Returns the probability of the samples for each class
        """
        probabilities = []
        for x in X:
            posteriors = self._calculate_posterior(x)
            # Convert log probabilities to probabilities
            probs = np.exp(posteriors)
            # Normalize to sum to 1
            probs = probs / np.sum(probs)
            probabilities.append(probs)

        return np.array(probabilities)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example with Iris dataset
    from sklearn.datasets import load_iris
    from sklearn.metrics import accuracy_score, classification_report
    from sklearn.model_selection import train_test_split

    # Load dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Train the classifier
    clf = GaussianNaiveBayes()
    clf.fit(X_train, y_train)

    # Make predictions
    y_pred = clf.predict(X_test)

    # Evaluate
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2%}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))

    # Show probability predictions for first 5 samples
    probas = clf.predict_proba(X_test[:5])
    print("\nProbability predictions for first 5 samples:")
    for i, proba in enumerate(probas):
        print(f"Sample {i + 1}: {proba}")
