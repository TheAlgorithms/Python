"""
ARIMA (AutoRegressive Integrated Moving Average) model for time series forecasting.

Reference: https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average

>>> import numpy as np
>>> series = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
>>> model = ARIMAModel(p=2, d=1, q=0)
>>> model.fit(series)
ARIMAModel(...)
>>> model.predict(series, n_periods=2)
array([10.99999999, 12.00000001])
"""

import numpy as np
from typing import Optional


class ARIMAModel:
    def __init__(self, p: int = 1, d: int = 0, q: int = 0) -> None:
        """Initialize ARIMA model.
        Args:
            p: AR order
            d: Differencing order
            q: MA order (not used in this implementation)
        """
        self.p = p
        self.d = d
        self.q = q
        self.coef_: Optional[np.ndarray] = None
        self.resid_: Optional[np.ndarray] = None

    def difference(self, series: np.ndarray, order: int) -> np.ndarray:
        """Apply differencing to make series stationary."""
        for _ in range(order):
            series = np.diff(series)
        return series

    def fit(self, time_series: np.ndarray) -> "ARIMAModel":
        """Fit ARIMA model to the given time series.
        Args:
            time_series: 1D numpy array of time series values
        Returns:
            self
        >>> import numpy as np
        >>> series = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        >>> model = ARIMAModel(p=2, d=1, q=0)
        >>> model.fit(series)
        ARIMAModel(...)
        """
        y = np.asarray(time_series)
        y_diff = self.difference(y, self.d)
        # Build lagged feature matrix
        feature_matrix = np.column_stack(
            [np.roll(y_diff, i) for i in range(1, self.p + 1)]
        )
        feature_matrix = feature_matrix[self.p :]
        target = y_diff[self.p :]
        # Add intercept
        feature_matrix = np.hstack(
            [np.ones((feature_matrix.shape[0], 1)), feature_matrix]
        )
        # Solve least squares for AR coefficients
        self.coef_ = np.linalg.lstsq(feature_matrix, target, rcond=None)[0]
        self.resid_ = target - feature_matrix @ self.coef_
        return self

    def predict(self, time_series: np.ndarray, n_periods: int = 1) -> np.ndarray:
        """Forecast n_periods ahead given observed time_series.
        Args:
            time_series: 1D numpy array of observed values
            n_periods: Number of periods to forecast
        Returns:
            1D numpy array of forecasted values
        >>> import numpy as np
        >>> series = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        >>> model = ARIMAModel(p=2, d=1, q=0)
        >>> model.fit(series)
        ARIMAModel(...)
        >>> model.predict(series, n_periods=2)
        array([10.99999999, 12.00000001])
        """
        y = np.asarray(time_series)
        y_pred = list(y[-self.p :])
        for _ in range(n_periods):
            # Build feature vector for prediction
            features = [1] + y_pred[-self.p :][::-1]
            next_val = np.dot(features, self.coef_)
            y_pred.append(next_val)
        return np.array(y_pred[self.p :])
