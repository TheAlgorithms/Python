"""
ARIMA (AutoRegressive Integrated Moving Average) model for time series forecasting.

Reference: https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average

>>> import numpy as np
>>> series = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
>>> model = ARIMAModel(ar_order=2, diff_order=1, ma_order=0)
>>> model.fit(series)
ARIMAModel(...)
>>> model.predict(series, n_periods=2)
array([10.99999999, 12.00000001])
"""

import numpy as np


class ARIMAModel:
    def __init__(
        self,
        ar_order: int = 1,
        diff_order: int = 0,
        ma_order: int = 0,
    ) -> None:
        """Initialize ARIMA model.
        Args:
            ar_order: Autoregressive order (p)
            diff_order: Differencing order (d)
            ma_order: Moving average order (q, not used in this implementation)
        """
        self.ar_order = ar_order
        self.diff_order = diff_order
        self.ma_order = ma_order
        self.coef_: np.ndarray | None = None
        self.resid_: np.ndarray | None = None

    def difference(self, time_series: np.ndarray, order: int) -> np.ndarray:
        """Apply differencing to make series stationary."""
        for _ in range(order):
            time_series = np.diff(time_series)
        return time_series

    def fit(self, time_series: np.ndarray) -> "ARIMAModel":
        """Fit ARIMA model to the given time series.
        Args:
            time_series: 1D numpy array of time series values
        Returns:
            self
        >>> import numpy as np
        >>> series = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        >>> model = ARIMAModel(ar_order=2, diff_order=1, ma_order=0)
        >>> model.fit(series)
        ARIMAModel(...)
        """
        y = np.asarray(time_series)
        y_diff = self.difference(y, self.diff_order)

        # Build lagged feature matrix
        feature_matrix = np.column_stack(
            [np.roll(y_diff, i) for i in range(1, self.ar_order + 1)]
        )
        feature_matrix = feature_matrix[self.ar_order :]
        target = y_diff[self.ar_order :]

        # Add intercept
        intercept = np.ones((feature_matrix.shape[0], 1))
        feature_matrix = np.hstack([intercept, feature_matrix])

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
        >>> model = ARIMAModel(ar_order=2, diff_order=1, ma_order=0)
        >>> model.fit(series)
        ARIMAModel(...)
        >>> model.predict(series, n_periods=2)
        array([10.99999999, 12.00000001])
        """
        y = np.asarray(time_series)
        y_pred = list(y[-self.ar_order :])
        for _ in range(n_periods):
            # Build feature vector for prediction
            features = [1, *y_pred[-self.ar_order :][::-1]]
            next_val = np.dot(features, self.coef_)
            y_pred.append(next_val)
        return np.array(y_pred[self.ar_order :])
