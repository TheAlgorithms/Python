
import numpy as np

# Simple ARIMA (AutoRegressive Integrated Moving Average) implementation
# Only AR and differencing parts are implemented (no MA part)
class ARIMA:
    def __init__(self, p=1, d=0, q=0):
        # p: AR order, d: differencing order, q: MA order (not used here)
        self.p = p
        self.d = d
        self.q = q
        self.coef_ = None

    def difference(self, series, d):
        # Apply differencing d times to make series stationary
        for _ in range(d):
            series = np.diff(series)
        return series

    def fit(self, y):
        # Fit AR(p) model to differenced series
        y = np.asarray(y)
        y_diff = self.difference(y, self.d)
        # Build lagged feature matrix
        X = np.column_stack([np.roll(y_diff, i) for i in range(1, self.p + 1)])
        X = X[self.p:]
        y_target = y_diff[self.p:]
        # Add intercept
        X = np.hstack([np.ones((X.shape[0], 1)), X])
        # Solve least squares for AR coefficients
        self.coef_ = np.linalg.lstsq(X, y_target, rcond=None)[0]
        self.resid_ = y_target - X @ self.coef_
        return self

    def predict(self, y, n_periods=1):
        # Forecast n_periods ahead given observed y
        y = np.asarray(y)
        y_pred = list(y[-self.p:])
        for _ in range(n_periods):
            # Build feature vector for prediction
            X = [1] + y_pred[-self.p:][::-1]
            next_val = np.dot(X, self.coef_)
            y_pred.append(next_val)
        return np.array(y_pred[self.p:])
