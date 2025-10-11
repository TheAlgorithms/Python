import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray
from scipy.optimize import minimize

"""
This program implements an ARIMA (AutoRegressive Integrated Moving Average) model
from scratch in Python.

References:
Wikipedia page on ARIMA:
https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average
"""

class ARIMA:
    def __init__(self, p=1, d=1, q=1, lr=0.001, epochs=500) -> None:
        """
        Initializes the ARIMA model.

        Args:
            p: AR lag order (uses past y values).
            d: Differencing order (makes data stationary).
            q: MA lag order (uses past errors).
            lr: Learning rate for Gradient Descent.
            epochs: Number of training cycles.
        """
        # We need to make sure p, d, and q are sensible numbers (positive integers).
        if not all(isinstance(x, int) and x >= 0 for x in [p, d, q]):
            raise ValueError("p, d, and q must be non-negative integers")
        # Learning rate and epochs should also be positive.
        if lr <= 0 or epochs <= 0:
            raise ValueError("lr and epochs must be positive")

        self.p = p
        self.d = d
        self.q = q
        self.lr = lr
        self.epochs = epochs

        # These are the parameters our model will learn. We'll initialize them at zero.
        # phi -> The weights for the AR (past values) part.
        self.phi = np.zeros(p)
        # theta -> The weights for the MA (past errors) part.
        self.theta = np.zeros(q)
        # c -> A constant or intercept, like a baseline value.
        self.c = 0.0

        # Store info after model training
        self.is_fitted = False  # Flag for training status
        self.train_last = 0.0  # Last value from training data
        # Type hints for optional attributes
        self.diff_data: NDArray[np.float64] | None = None
        self.errors: NDArray[np.float64] | None = None
        self.n_train: int | None = None
        self.sigma_err: float | None = None

    def difference(self, data) -> NDArray[np.float64]:
        """
        Makes the time series stationary by differencing.

        Args:
            data: Original time series data.
        Returns:
            Differenced data.
        """
        diff = np.copy(data)
        # We loop 'd' times, applying the differencing each time.
        for _ in range(self.d):
            diff = np.diff(diff)  # np.diff is a handy function that does exactly this.
        return diff

    def inverse_difference(
        self, last_obs: float, diff_forecast: list[float]
    ) -> list[float]:
        """
        Converts differenced data back to the original scale.

        Args:
            last_obs: Last value from the original data.
            diff_forecast: Predictions on differenced data.
        Returns:
            Forecasts in the original scale.
        """
        forecast = []
        # We start with the last known value from the original data.
        prev = last_obs
        # For each predicted *change*, we add it to the last value to get the next one.
        for val in diff_forecast:
            next_val = prev + val
            forecast.append(next_val)
            # Store current value for next iteration
            prev = next_val
        return forecast

    def _compute_residuals(
        self, diff_data: NDArray[np.float64], phi: NDArray[np.float64],
        theta: NDArray[np.float64], c: float
    ) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
        """
        Computes residuals for given parameters.

        Args:
            diff_data: Differenced data.
            phi, theta, c: Model parameters.
        Returns:
            Tuple of predictions and residuals.
        """
        n = len(diff_data)
        # Need initial values to get started,we begin after the max of p or q.
        start = max(self.p, self.q)
        preds = np.zeros(n)
        errors = np.zeros(n)

        # Loop through the data from the starting point.
        for t in range(start, n):
            # AR part: a weighted sum of the last 'p' actual values.
            # We reverse the data slice [::-1] so that the most recent value is first.
            ar_term = (np.dot(phi, diff_data[t - self.p:t][::-1])
                      if self.p > 0 else 0.0)

            # MA part: a weighted sum of the last 'q' prediction errors.
            ma_term = (np.dot(theta, errors[t - self.q:t][::-1])
                      if self.q > 0 else 0.0)

            # Combine everything to make the one-step-ahead prediction.
            preds[t] = c + ar_term + ma_term
            # Calculate error
            errors[t] = diff_data[t] - preds[t]

        return preds, errors

    def fit(
        self, data: list[float] | NDArray[np.float64], method: str = "opt"
    ) -> 'ARIMA':
        """
        Trains the ARIMA model.

        Args:
            data: Time series data to train on.
            method: "opt" for optimization, "gd" for Gradient Descent.
        Returns:
            The fitted ARIMA model.
        """
        data = np.asarray(data, dtype=float)
        # Check if we have enough data to even build the model.
        if len(data) < max(self.p, self.q) + self.d + 5:
            raise ValueError("Not enough data to train. You need more samples.")

        # Store last value of the original data.We'll need it to forecast later.
        self.train_last = float(data[-1])

        # Step 1: Make the data stationary.
        diff_data = self.difference(data)
        n = len(diff_data)
        start = max(self.p, self.q)

        # Another check to make sure we have enough data AFTER differencing.
        if n <= start:
            raise ValueError("Not enough data after differencing. Try reducing 'd'.")

        # Step 2: Call the chosen training method to find the best parameters.
        if method == "gd":
            self._fit_gradient_descent(diff_data, start)
        elif method == "opt":
            self._fit_optimization(diff_data, start)
        else:
            raise ValueError("method must be 'opt' or 'gd'")

        # All done! Mark the model as fitted and ready to forecast.
        self.is_fitted = True
        self.diff_data = diff_data  # Ensure diff_data is assigned correctly
        self.errors = np.zeros(len(diff_data))  # Initialize errors as a numpy array
        self.n_train = len(diff_data)  # Assign n_train as an integer
        return self

    def _fit_gradient_descent(self, diff_data: NDArray[np.float64], start: int) -> None:
        """
        Trains the model using Gradient Descent.

        Args:
            diff_data: Differenced data.
            start: Starting index for training.
        """
        n = len(diff_data)
        errors = np.zeros(n)
        preds = np.zeros(n)
        m = max(1, n - start)  # Number of points we can calculate error on.

        # The main training loop. We repeat this 'epochs' times.
        for epoch in range(self.epochs):
            # First, calculate the predictions and errors with the current parameters.
            for t in range(start, n):
                ar_term = (np.dot(self.phi, diff_data[t - self.p:t][::-1])
                          if self.p > 0 else 0.0)
                ma_term = (np.dot(self.theta, errors[t - self.q:t][::-1])
                          if self.q > 0 else 0.0)
                preds[t] = self.c + ar_term + ma_term
                errors[t] = diff_data[t] - preds[t]

            # Calculate the "gradient"-which direction we should nudge our parameters
            # to reduce the error. It's based on the partial derivatives of the MSE.
            dc = -2 * np.sum(errors[start:]) / m
            dphi = np.zeros_like(self.phi)

            # Calculate AR gradients
            for i in range(self.p):
                err_idx = slice(start - i - 1, n - i - 1)
                error_term = errors[start:] * diff_data[err_idx]
                dphi[i] = -2 * np.sum(error_term) / m

            # Calculate MA gradients
            dtheta = np.zeros_like(self.theta)
            for j in range(self.q):
                err_idx = slice(start - j - 1, n - j - 1)
                error_term = errors[start:] * errors[err_idx]
                dtheta[j] = -2 * np.sum(error_term) / m

            # Update parameters by taking steps
            # in the opposite direction of the gradient.
            self.phi -= self.lr * dphi
            self.theta -= self.lr * dtheta
            self.c -= self.lr * dc

            if epoch % 100 == 0:
                mse = np.mean(errors[start:] ** 2)
                print(f"Epoch {epoch}: MSE={mse:.6f}, c={self.c:.6f}")

        # After training, store the final results.
        self.errors = errors  # Ensure errors is assigned correctly
        self.diff_data = diff_data  # Ensure diff_data is assigned correctly
        self.n_train = n  # Ensure n_train is assigned as an integer
        sigma_term = np.sum(self.errors[start:] ** 2) / m
        self.sigma_err = float(np.sqrt(sigma_term))
        msg=f"Fitted params (GD): phi={self.phi},theta={self.theta},c={self.c:.6f}\n"
        print(msg)

    def _fit_optimization(self, diff_data: NDArray[np.float64], start: int) -> None:
        """
        Trains the model using optimization.

        Args:
            diff_data: Differenced data.
            start: Starting index for training.
        """
        n = len(diff_data)

        # We need to define a "goal" for the optimizer. This function calculates
        # the total error (SSE) for any given set of parameters. The optimizer's
        # Must find 'params' that make output of this function as small as possible.
        def sse_objective(params):
            # Unpack the parameters from the single array the optimizer uses.
            phi = params[:self.p] if self.p > 0 else np.array([])
            theta = params[self.p:self.p + self.q] if self.q > 0 else np.array([])
            c = params[-1]

            # Calculate the errors for these parameters.
            _, errors = self._compute_residuals(diff_data, phi, theta, c)
            # Return the score: the sum of the squared errors.
            return np.sum(errors[start:] ** 2)

        # Give the optimizer a starting guess for the parameters.
        init_params = np.concatenate([self.phi, self.theta, np.array([self.c])])

        # Let the optimizer do its magic!
        result = minimize(
            sse_objective,
            init_params,
            method='L-BFGS-B',
            options={"maxiter": 5000, "ftol": 1e-9}
        )

        # Once it's done, unpack the best parameters it found.
        best_params = result.x
        self.phi = best_params[:self.p] if self.p > 0 else np.array([])
        self.theta = best_params[self.p:self.p + self.q] if self.q > 0 else np.array([])
        self.c = float(best_params[-1])

        # Recalculate final errors with these optimal parameters and store everything.
        _,final_errors=self._compute_residuals(diff_data,self.phi,self.theta,self.c)
        self.errors = final_errors  # Ensure errors is assigned correctly
        self.diff_data = diff_data  # Ensure diff_data is assigned correctly
        self.n_train = n  # Ensure n_train is assigned as an integer
        sigma_term = np.sum(self.errors[start:] ** 2)
        denom = max(1, n - start)
        self.sigma_err = float(np.sqrt(sigma_term / denom))

        # Format and print results
        params = {
            'phi': self.phi,
            'theta': self.theta,
            'c': f"{self.c:.6f}"
        }
        msg = "Fitted params (Opt): phi={phi}, theta={theta}, c={c}\n"
        print(msg.format(**params))

    def forecast(
        self, steps: int, simulate_errors: bool = False, random_state: int | None = None
    ) -> NDArray[np.float64]:
        """
        Generates future predictions.

        Args:
            steps: Number of steps to predict.
            simulate_errors: Adds randomness to forecasts if True.
            random_state: Seed for reproducibility.
        Returns:
            Forecasted values.
        """
        msg = "Model must be fitted before forecasting. Call fit() first."
        if not self.is_fitted:
            raise ValueError(msg)

        if self.diff_data is None or self.errors is None or self.sigma_err is None:
            raise ValueError(msg)

        # We'll be adding to these lists, so let's work on copies.
        diff_data = np.copy(self.diff_data)
        errors = np.copy(self.errors)
        forecasts_diff = []

        # A tool for generating random numbers if we need them.
        rng = np.random.default_rng(random_state)

        # Generate one forecast at a time.
        for _ in range(steps):
            # AR part: Use the last 'p' values (from previous y-values).
            ar_slice = slice(-self.p, None)
            ar_term = (np.dot(self.phi, diff_data[ar_slice][::-1])
                      if self.p > 0 else 0.0)
            # MA part:Use the last 'q' errors(from prediction errors).
            ma_slice = slice(-self.q, None)
            ma_term = (np.dot(self.theta, errors[ma_slice][::-1])
                      if self.q > 0 else 0.0)

            # The next predicted value (on the differenced scale).
            next_diff_forecast = self.c + ar_term + ma_term
            forecasts_diff.append(next_diff_forecast)

            # For the next loop, we need a value for the "next error".
            # If we're simulating, we draw a random error from a normal distribution
            # with the same standard deviation as our past errors.
            next_error = rng.normal(0.0, self.sigma_err) if simulate_errors else 0.0

            # Now, append our new prediction and error to the history.
            # This is crucial: our next forecast will use these values we just made up!
            diff_data = np.append(diff_data, next_diff_forecast)
            errors = np.append(errors, next_error)

        # Finally, "un-difference" the forecasts to get them back to the original scale.
        final_forecasts = self.inverse_difference(self.train_last, forecasts_diff)
        return np.array(final_forecasts, dtype=np.float64)


# This part of the code only runs if you execute this script directly.
if __name__ == "__main__":
    # Let's create some fake data that follows an ARIMA(2,1,2) pattern.
    rng = np.random.default_rng(42)  # Replace legacy np.random.seed
    n = 500
    ar_params = [0.5, -0.3]
    ma_params = [0.4, 0.2]

    # Start with some random noise.
    noise = rng.standard_normal(n)  # Replace np.random.randn
    data = np.zeros(n)

    # Build the ARMA part first.
    for t in range(2, n):
        data[t] = (
            ar_params[0] * data[t - 1]
            + ar_params[1] * data[t - 2]
            + noise[t]
            + ma_params[0] * noise[t - 1]
            + ma_params[1] * noise[t - 2]
        )
    # Now, "integrate" it by taking the cumulative sum.
    data = np.cumsum(data)

    # Train the model on the first 300 data points.
    train_end = 300
    model = ARIMA(p=3, d=2, q=3)
    model.fit(data[:train_end], method="opt")

    # Forecast the next 200 steps.
    forecast_steps = 200
    forecast = model.forecast(forecast_steps, simulate_errors=True)

    # Compare forecast to the actual data.
    true_future = data[train_end:train_end + forecast_steps]
    rmse = np.sqrt(np.mean((np.array(forecast) - true_future) ** 2))
    print(f"Forecast RMSE: {rmse:.6f}\n")

    # Visualize results.
    plt.figure(figsize=(14, 6))
    plt.plot(range(len(data)), data, label="Original Data", linewidth=1.5)
    plt.plot(
        range(train_end, train_end + forecast_steps),
        forecast,
        label="Forecast",
        color="red",
        linewidth=1.5,
    )
    split_label = "Split"
    plt.axvline(
        train_end - 1,
        color="gray",
        linestyle=":",
        alpha=0.7,
        label=f"Train/Test {split_label}"
    )
    plt.xlabel("Time Step")
    plt.ylabel("Value")
    plt.title("ARIMA(2,1,2) Model: Training Data and Forecast")
    plt.legend()
    plt.tight_layout()
    plt.show()
