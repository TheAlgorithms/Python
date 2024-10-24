"""
Doctest for RidgeRegression class

Tests include:
- feature_scaling
- fit
- predict
- mean_absolute_error

To run these tests, use the following command:
    python -m doctest test_ridge_regression.py -v
"""

import numpy as np  # noqa: F401

from machine_learning.ridge_regression.ridge_regression import (
    RidgeRegression,  # noqa: F401
)


def test_feature_scaling():
    """
       Tests the feature_scaling function of RidgeRegression.
    --------
       >>> model = RidgeRegression()
       >>> features = np.array([[1, 2], [2, 3], [3, 4]])
       >>> features_scaled, mean, std = model.feature_scaling(features)
       >>> np.round(features_scaled, 2)
       array([[-1.22, -1.22],
              [ 0.  ,  0.  ],
              [ 1.22,  1.22]])
       >>> np.round(mean, 2)
       array([2., 3.])
       >>> np.round(std, 2)
       array([0.82, 0.82])
    """


def test_fit():
    """
    Tests the fit function of RidgeRegression
    --------
    >>> model = RidgeRegression(alpha=0.01,
    ...                          regularization_param=0.1,
    ...                          num_iterations=1000)
    >>> features = np.array([[1], [2], [3]])
    >>> target = np.array([2, 3, 4])

    # Adding a bias term
    >>> features = np.c_[np.ones(features.shape[0]), features]

    # Fit the model
    >>> model.fit(features, target)

    # Check if the weights have been updated
    >>> np.round(model.theta, decimals=2)
    array([0.  , 0.79])
    """


def test_predict():
    """
    Tests the predict function of RidgeRegression
    --------
    >>> model = RidgeRegression(alpha=0.01,
    ...                          regularization_param=0.1,
    ...                          num_iterations=1000)
    >>> features = np.array([[1], [2], [3]])
    >>> target = np.array([2, 3, 4])

    # Adding a bias term
    >>> features = np.c_[np.ones(features.shape[0]), features]

    # Fit the model
    >>> model.fit(features, target)

    # Predict with the model
    >>> predictions = model.predict(features)
    >>> np.round(predictions, decimals=2)
    array([-0.97,  0.  ,  0.97])
    """


def test_mean_absolute_error():
    """
    Tests the mean_absolute_error function of RidgeRegression
    --------
    >>> model = RidgeRegression()
    >>> target = np.array([2, 3, 4])
    >>> predictions = np.array([2.1, 3.0, 3.9])
    >>> mae = model.mean_absolute_error(target, predictions)
    >>> float(np.round(mae, 2))
    0.07
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
