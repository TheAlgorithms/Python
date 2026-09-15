import numpy as np
import pytest

from machine_learning import RidgeRegression, mean_absolute_error


def test_fit_perfect_linear_no_regularization():
    x = np.array([[1.0], [2.0], [3.0]])
    y = np.array([2.0, 4.0, 6.0])

    model = RidgeRegression(learning_rate=0.1, lambda_=0.0, epochs=2000)
    model.fit(x, y)

    # bias ~ 0, slope ~ 2
    assert pytest.approx(0.0, abs=1e-2) == model.weights[0]
    assert pytest.approx(2.0, abs=1e-2) == model.weights[1]


def test_regularization_reduces_weight_norm():
    rng = np.random.default_rng(0)
    x = rng.normal(size=(200, 2))
    true_w = np.array([0.0, 5.0, -3.0])
    y = x @ true_w[1:] + true_w[0] + rng.normal(scale=0.1, size=200)

    no_reg = RidgeRegression(learning_rate=0.01, lambda_=0.0, epochs=5000)
    no_reg.fit(x, y)

    strong_reg = RidgeRegression(learning_rate=0.01, lambda_=10.0, epochs=5000)
    strong_reg.fit(x, y)

    norm_no_reg = np.linalg.norm(no_reg.weights[1:])
    norm_strong_reg = np.linalg.norm(strong_reg.weights[1:])

    assert norm_strong_reg < norm_no_reg


def test_predict_and_mae():
    x = np.array([[1.0], [2.0]])
    y = np.array([3.0, 5.0])
    model = RidgeRegression(learning_rate=0.1, lambda_=0.0, epochs=1000)
    model.fit(x, y)

    preds = model.predict(x)
    assert preds.shape == (2,)
    assert mean_absolute_error(preds, y) < 1e-2


def test_input_validation():
    model = RidgeRegression()
    with pytest.raises(ValueError):
        model.fit(np.array([1, 2, 3]), np.array([1, 2, 3]))


def test_accepts_numpy_matrix():
    from machine_learning.ridge_regression import collect_dataset

    data = collect_dataset()
    x = np.c_[data[:, 0].astype(float)]  # numpy.matrix
    y = np.ravel(data[:, 1].astype(float))

    model = RidgeRegression(learning_rate=0.0002, lambda_=0.01, epochs=500)
    model.fit(x, y)
    preds = model.predict(x)
    assert preds.shape == (y.shape[0],)
    assert mean_absolute_error(preds, y) >= 0.0
