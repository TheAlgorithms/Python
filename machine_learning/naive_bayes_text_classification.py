"""
Naive Bayes text classification using a multinomial event model.

The implementation in this module is intentionally educational and keeps the
logic explicit: token counting, prior probabilities, and posterior scoring in
log-space.

References:
- https://en.wikipedia.org/wiki/Naive_Bayes_classifier
- https://scikit-learn.org/stable/modules/naive_bayes.html
"""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from math import exp, log


class NaiveBayesTextClassifier:
    """
    Multinomial Naive Bayes classifier for short text documents.

    Args:
        alpha: Additive (Laplace) smoothing parameter. Must be greater than 0.

    >>> NaiveBayesTextClassifier(alpha=0)
    Traceback (most recent call last):
    ...
    ValueError: alpha must be greater than 0.
    """

    def __init__(self, alpha: float = 1.0) -> None:
        if alpha <= 0:
            raise ValueError("alpha must be greater than 0.")

        self.alpha = alpha
        self.classes_: list[str] = []
        self.vocabulary_: set[str] = set()
        self.class_document_counts_: Counter[str] = Counter()
        self.class_token_counts_: dict[str, Counter[str]] = defaultdict(Counter)
        self.class_total_tokens_: Counter[str] = Counter()
        self.class_log_prior_: dict[str, float] = {}
        self.is_fitted_ = False

    @staticmethod
    def _tokenize(text: str) -> list[str]:
        """
        Split text into lowercase alphanumeric tokens.

        >>> NaiveBayesTextClassifier._tokenize("Hello, NLP world!")
        ['hello', 'nlp', 'world']
        """
        return re.findall(r"[a-z0-9']+", text.lower())

    def fit(self, texts: list[str], labels: list[str]) -> None:
        """
        Fit the classifier from labeled training texts.

        >>> model = NaiveBayesTextClassifier()
        >>> model.fit(["cheap meds", "project meeting"], ["spam", "ham"])
        >>> sorted(model.classes_)
        ['ham', 'spam']

        >>> model.fit(["only one text"], ["ham", "spam"])
        Traceback (most recent call last):
        ...
        ValueError: texts and labels must have the same length.

        >>> model.fit([], [])
        Traceback (most recent call last):
        ...
        ValueError: training data must not be empty.
        """
        if not texts:
            raise ValueError("training data must not be empty.")
        if len(texts) != len(labels):
            raise ValueError("texts and labels must have the same length.")

        self.classes_ = sorted(set(labels))
        self.vocabulary_.clear()
        self.class_document_counts_.clear()
        self.class_token_counts_ = defaultdict(Counter)
        self.class_total_tokens_.clear()
        self.class_log_prior_.clear()

        for text, label in zip(texts, labels):
            if not isinstance(text, str) or not isinstance(label, str):
                raise TypeError("texts and labels must contain strings only.")

            tokens = self._tokenize(text)
            self.class_document_counts_[label] += 1
            self.class_token_counts_[label].update(tokens)
            self.class_total_tokens_[label] += len(tokens)
            self.vocabulary_.update(tokens)

        total_documents = len(texts)
        self.class_log_prior_ = {
            label: log(self.class_document_counts_[label] / total_documents)
            for label in self.classes_
        }
        self.is_fitted_ = True

    def predict_proba(self, text: str) -> dict[str, float]:
        """
        Return posterior probabilities for every class.

        >>> train_texts, train_labels = build_toy_dataset()
        >>> model = NaiveBayesTextClassifier()
        >>> model.fit(train_texts, train_labels)
        >>> probs = model.predict_proba("cheap meds available now")
        >>> round(sum(probs.values()), 6)
        1.0
        >>> probs['spam'] > probs['ham']
        True

        An empty input text has no tokens, so predictions fall back to class priors.
        >>> empty_probs = model.predict_proba("")
        >>> round(empty_probs['spam'], 3), round(empty_probs['ham'], 3)
        (0.5, 0.5)

        >>> NaiveBayesTextClassifier().predict_proba("hello")
        Traceback (most recent call last):
        ...
        ValueError: model has not been fitted yet.
        """
        if not self.is_fitted_:
            raise ValueError("model has not been fitted yet.")
        if not isinstance(text, str):
            raise TypeError("text must be a string.")

        tokens = self._tokenize(text)
        vocabulary_size = len(self.vocabulary_)
        log_posteriors: dict[str, float] = {}

        for label in self.classes_:
            log_prob = self.class_log_prior_[label]
            token_counts = self.class_token_counts_[label]
            denominator = self.class_total_tokens_[label] + self.alpha * vocabulary_size

            for token in tokens:
                count = token_counts[token]
                log_prob += log((count + self.alpha) / denominator)

            log_posteriors[label] = log_prob

        max_log = max(log_posteriors.values())
        exp_scores = {
            label: exp(score - max_log) for label, score in log_posteriors.items()
        }
        normalizer = sum(exp_scores.values())
        return {label: score / normalizer for label, score in exp_scores.items()}

    def predict(self, text: str) -> str:
        """
        Predict the most likely class label for a text.

        >>> train_texts, train_labels = build_toy_dataset()
        >>> model = NaiveBayesTextClassifier(alpha=1.0)
        >>> model.fit(train_texts, train_labels)
        >>> model.predict("free cheap meds")
        'spam'
        >>> model.predict("project meeting schedule")
        'ham'
        """
        probabilities = self.predict_proba(text)
        return max(probabilities, key=lambda label: probabilities[label])


def build_toy_dataset() -> tuple[list[str], list[str]]:
    """
    Build a tiny text dataset for examples and quick local testing.

    >>> texts, labels = build_toy_dataset()
    >>> len(texts), len(labels)
    (6, 6)
    >>> sorted(set(labels))
    ['ham', 'spam']
    """
    texts = [
        "buy cheap meds now",
        "cheap meds available online",
        "win cash prizes now",
        "project meeting schedule attached",
        "let us discuss the project timeline",
        "team meeting moved to monday",
    ]
    labels = ["spam", "spam", "spam", "ham", "ham", "ham"]
    return texts, labels


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    sample_texts, sample_labels = build_toy_dataset()
    classifier = NaiveBayesTextClassifier(alpha=1.0)
    classifier.fit(sample_texts, sample_labels)

    print("Prediction:",classifier.predict("cheap prizes available now"))
    print("Prediction:",classifier.predict("team meeting about project timeline"))
