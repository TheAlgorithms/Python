"""
Implementation from scratch of a Multinomial Naive Bayes Classifier.
The algorithm is trained and tested on the twenty_newsgroup dataset from sklearn to perform text classification
"""


import numpy as np
import doctest
from scipy import sparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups
from sklearn.metrics import accuracy_score


def group_indices_by_target(targets):
    """
    Associates to each target label the indices of the examples with that label

    Parameters
    ----------
    targets : array-like of shape (n_samples,)
              Target labels

    Returns
    ----------
    grouped_indices : dict of (label : list)
                      Maps each target label to the list of indices of the examples with that label

    Example
    ----------
    >>> y = np.array([1, 2, 3, 1, 2, 5])
    >>> group_indices_by_target(y)
    {1: [0, 3], 2: [1, 4], 3: [2], 5: [5]}
    """
    grouped_indices = {}
    for i, y in enumerate(targets):
        if y not in grouped_indices:
            grouped_indices[y] = []
        grouped_indices[y].append(i)
    return grouped_indices


class MultinomialNBClassifier:
    def __init__(self, alpha=1):
        self.classes = None
        self.features_probs = None
        self.priors = None
        self.alpha = alpha

    def _check_X(self, X):
        if not sparse.issparse(X):
            raise ValueError("Matrix X must be an instance of scipy.sparse.csr_matrix")

    def _check_X_y(self, X, y):
        self._check_X(X)
        if X.shape[0] != len(y):
            raise ValueError(
                "The expected shape for array y is (" + str(X.shape[0]) + ",), but got (" + str(len(y)) + ",)")

    def fit(self, X, y):
        """
        Parameters
        ----------
        X : scipy.sparse.csr_matrix of shape (n_samples, n_features)
            Multinomial training examples

        y : array-like of shape (n_samples,)
            Target labels
        """
        self._check_X_y(X, y)
        n_examples, n_features = X.shape
        grouped_indices = group_indices_by_target(y)
        self.classes = list(grouped_indices.keys())
        self.priors = np.zeros(shape=len(self.classes))
        self.features_probs = np.zeros(shape=(len(self.classes), n_features))

        for i, class_i in enumerate(self.classes):
            data_class_i = X[grouped_indices[class_i]]
            prior_class_i = data_class_i.shape[0] / n_examples
            self.priors[i] = prior_class_i
            tot_features_count = data_class_i.sum()   # count of all features in class_i
            features_count = np.array(data_class_i.sum(axis=0))[0]   # count of each feature x_j in class_i
            for j, n_j in enumerate(features_count):
                self.features_probs[i][j] = (self.alpha + n_j) / (tot_features_count + self.alpha * n_features)

    def predict(self, X):
        """
        Parameters
        ----------
        X : scipy.sparse.csr_matrix of shape (n_samples, n_features)
            Multinomial test examples

        Returns
        ----------
        y_pred : ndarray of shape (n_samples,)
                 Predicted target labels of test examples

        Example
        ----------
        Let's test the function following an example taken from the documentation of the MultinomialNB model
        from sklearn
        >>> rng = np.random.RandomState(1)
        >>> X = rng.randint(5, size=(6, 100))
        >>> X = sparse.csr_matrix(X)
        >>> y = np.array([1, 2, 3, 4, 5, 6])
        >>> model = MultinomialNBClassifier()
        >>> model.fit(X, y)
        >>> model.predict(X[2:3])
        array([3])
        """
        self._check_X(X)
        y_pred = []
        log_features_probs = np.log(self.features_probs)
        log_priors = np.log(self.priors)
        for instance in X:
            theta = instance.multiply(log_features_probs).sum(axis=1)
            likelihood = [log_prior_class_i + theta[i] for i, log_prior_class_i in enumerate(log_priors)]
            y_pred.append(self.classes[np.argmax(likelihood)])
        return np.array(y_pred)


def main():
    newsgroups_train = fetch_20newsgroups(subset='train')
    newsgroups_test = fetch_20newsgroups(subset='test')
    X_train = newsgroups_train['data']
    y_train = newsgroups_train['target']
    X_test = newsgroups_test['data']
    y_test = newsgroups_test['target']
    vectorizer = TfidfVectorizer(stop_words='english')
    X_train = vectorizer.fit_transform(X_train)
    X_test = vectorizer.transform(X_test)

    model = MultinomialNBClassifier()
    print("Start training")
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Accuracy of naive bayes text classifier: " + str(accuracy_score(y_test, y_pred)))


if __name__ == "__main__":
    main()
    doctest.testmod()

