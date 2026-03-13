"""
Implementation from scratch of a Multinomial Naive Bayes Classifier.
The algorithm is trained and tested on the twenty_newsgroup dataset
from sklearn to perform text classification

Here the Wikipedia page to understand the theory behind this kind
of probabilistic models:
https://en.wikipedia.org/wiki/Naive_Bayes_classifier
"""

import doctest

import numpy as np
import scipy
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score


def group_indices_by_target(targets: np.ndarray) -> dict[int, list[int]]:
    """
    Associates to each target label the indices of the examples with that label

    Parameters
    ----------
    targets : array-like of shape (n_samples,)
              Target labels

    Returns
    ----------
    grouped_indices : dict of (label : list)
                      Maps each target label to the list of indices of the
                      examples with that label

    Example
    ----------
    >>> y = np.array([1, 2, 3, 1, 2, 5])
    >>> group_indices_by_target(y)
    {1: [0, 3], 2: [1, 4], 3: [2], 5: [5]}
    """
    grouped_indices: dict[int, list[int]] = {}
    for i, y in enumerate(targets):
        if y not in grouped_indices:
            grouped_indices[y] = []
        grouped_indices[y].append(i)
    return grouped_indices


class MultinomialNBClassifier:
    def __init__(self, alpha: int = 1) -> None:
        self.classes: list[int] = []
        self.features_probs: np.ndarray = np.array([])
        self.priors: np.ndarray = np.array([])
        self.alpha = alpha

    def fit(self, data: scipy.sparse.csr_matrix, targets: np.ndarray) -> None:
        """
        Parameters
        ----------
        data : scipy.sparse.csr_matrix of shape (n_samples, n_features)
            Multinomial training examples

        targets : array-like of shape (n_samples,)
            Target labels

        Example
        ----------
        >>> from scipy import sparse
        >>> rng = np.random.RandomState(1)
        >>> data = rng.randint(5, size=(6, 100))
        >>> data = sparse.csr_matrix(data)
        >>> y = np.array([1, 2, 3, 4, 5, 6])
        >>> model = MultinomialNBClassifier()
        >>> print(model.fit(data, y))
        None
        """
        n_examples, n_features = data.shape
        grouped_indices = group_indices_by_target(targets)
        self.classes = list(grouped_indices.keys())
        self.priors = np.zeros(shape=len(self.classes))
        self.features_probs = np.zeros(shape=(len(self.classes), n_features))

        for i, class_i in enumerate(self.classes):
            data_class_i = data[grouped_indices[class_i]]
            prior_class_i = data_class_i.shape[0] / n_examples
            self.priors[i] = prior_class_i
            tot_features_count = data_class_i.sum()  # count of all features in class_i
            features_count = np.array(data_class_i.sum(axis=0))[0]
            for j, n_j in enumerate(features_count):
                self.features_probs[i][j] = (self.alpha + n_j) / (
                    tot_features_count + self.alpha * n_features
                )

    def predict(self, data: scipy.sparse.csr_matrix) -> np.ndarray:
        """
        Parameters
        ----------
        data : scipy.sparse.csr_matrix of shape (n_samples, n_features)
            Multinomial test examples

        Returns
        ----------
        y_pred : ndarray of shape (n_samples,)
                 Predicted target labels of test examples

        Example
        ----------
        >>> from scipy import sparse
        >>> rng = np.random.RandomState(1)
        >>> data = rng.randint(5, size=(6, 100))
        >>> data = sparse.csr_matrix(data)
        >>> y = np.array([1, 2, 3, 4, 5, 6])
        >>> model = MultinomialNBClassifier()
        >>> model.fit(data, y)
        >>> model.predict(data[2:3])
        array([3])
        """
        y_pred = []
        log_features_probs = np.log(self.features_probs)
        log_priors = np.log(self.priors)
        for instance in data:
            theta = instance.multiply(log_features_probs).sum(axis=1)
            likelihood = [
                log_prior_class_i + theta[i]
                for i, log_prior_class_i in enumerate(log_priors)
            ]
            y_pred.append(self.classes[np.argmax(likelihood)])
        return np.array(y_pred)


if __name__ == "__main__":
    newsgroups_train = fetch_20newsgroups(subset="train")
    newsgroups_test = fetch_20newsgroups(subset="test")
    x_train = newsgroups_train["data"]
    y_train = newsgroups_train["target"]
    x_test = newsgroups_test["data"]
    y_test = newsgroups_test["target"]
    vectorizer = TfidfVectorizer(stop_words="english")
    x_train = vectorizer.fit_transform(x_train)
    x_test = vectorizer.transform(x_test)

    model = MultinomialNBClassifier()
    print("Start training")
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    print(
        "Accuracy of naive bayes text classifier: "
        + str(accuracy_score(y_test, y_pred))
    )
    doctest.testmod()
