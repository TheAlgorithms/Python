from __future__ import annotations

import random

import pytest

from machine_learning.gaussian_naive_bayes import GaussianNaiveBayes
from machine_learning.gradient_boosting_regressor import GradientBoostingRegressor
from machine_learning.random_forest_classifier import RandomForestClassifier
from machine_learning.random_forest_regressor import RandomForestRegressor
from neural_network.perceptron import Perceptron


def test_gaussian_naive_bayes_predicts_expected_clusters() -> None:
    features = [[1.0, 1.1], [1.1, 0.9], [5.0, 5.1], [5.2, 4.9]]
    labels = [0, 0, 1, 1]

    model = GaussianNaiveBayes().fit(features, labels)
    assert model.predict([[1.0, 1.0], [5.1, 5.0]]) == [0, 1]


@pytest.mark.parametrize(
    ("constructor", "kwargs"),
    [
        (RandomForestClassifier, {"num_trees": 0}),
        (RandomForestRegressor, {"num_trees": 0}),
        (GradientBoostingRegressor, {"num_estimators": 0}),
    ],
)
def test_invalid_constructor_arguments_raise_value_error(constructor, kwargs) -> None:
    with pytest.raises(ValueError):
        constructor(**kwargs)


def test_random_forest_classifier_handles_duplicates_and_empty_predict() -> None:
    x_train = [[0.0], [0.0], [1.0], [1.0], [1.1], [1.1]]
    y_train = [0, 0, 1, 1, 1, 1]
    model = RandomForestClassifier(num_trees=11, random_seed=1)
    model.fit(x_train, y_train)

    predictions = model.predict([[0.0], [1.0]])
    assert len(predictions) == 2
    assert set(predictions) <= {0, 1}

    assert model.predict([]) == []


def test_random_forest_regressor_preserves_monotonic_trend() -> None:
    x_train = [[float(i)] for i in range(50)]
    y_train = [float(i) for i in range(50)]
    model = RandomForestRegressor(num_trees=21, random_seed=2)
    model.fit(x_train, y_train)

    low, high = model.predict([[5.0], [45.0]])
    assert low < high


def test_gradient_boosting_regressor_reduces_absolute_error() -> None:
    x_train = [[float(i)] for i in range(30)]
    y_train = [2.0 * i + 1.0 for i in range(30)]

    model = GradientBoostingRegressor(num_estimators=60, learning_rate=0.05)
    model.fit(x_train, y_train)

    predictions = model.predict([[3.0], [10.0], [25.0]])
    expected = [7.0, 21.0, 51.0]
    avg_abs_error = sum(abs(pred - exp) for pred, exp in zip(predictions, expected)) / 3
    assert avg_abs_error < 10.0


def test_perceptron_predicts_and_functionality() -> None:
    data = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
    labels = [-1, -1, -1, 1]
    model = Perceptron(learning_rate=0.2, max_epochs=30)

    epochs_used = model.fit(data, labels)
    assert 1 <= epochs_used <= 30
    assert model.predict([1.0, 1.0]) == 1
    assert model.predict([0.0, 0.0]) == -1


def test_models_scale_to_larger_arrays() -> None:
    random.seed(42)
    x_train = [[float(i), float(i % 7)] for i in range(300)]
    y_clf = [1 if i > 150 else 0 for i in range(300)]
    y_reg = [0.5 * i + (i % 3) for i in range(300)]

    clf = RandomForestClassifier(num_trees=13, random_seed=42)
    clf.fit(x_train, y_clf)
    assert len(clf.predict(x_train[:25])) == 25

    reg = RandomForestRegressor(num_trees=13, random_seed=42)
    reg.fit(x_train, y_reg)
    assert len(reg.predict(x_train[:25])) == 25
