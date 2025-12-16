"""
README, Author - Md Ruman Islam (mailto:ruman23.github.io)
Requirements:
  - numpy
  - matplotlib
Python:
  - 3.8+
Inputs:
  - data : a 2D numpy array of features.
  - n_components : number of Gaussian distributions (clusters) to fit.
  - max_iter : maximum number of EM iterations.
  - tol : convergence tolerance.
Usage:
  1. define 'n_components' value and 'data' features array
  2. initialize model:
        gmm = GaussianMixture(n_components=3, max_iter=100)
  3. fit model to data:
        gmm.fit(data)
  4. get cluster predictions:
        labels = gmm.predict(data)
  5. visualize results:
        gmm.plot_results(data)
"""

import warnings

import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray
from scipy.stats import multivariate_normal

warnings.filterwarnings("ignore")

TAG = "GAUSSIAN-MIXTURE/ "


class GaussianMixture:
    """
    Gaussian Mixture Model implemented using the Expectation-Maximization algorithm.
    """

    def __init__(
        self,
        n_components: int = 2,
        max_iter: int = 100,
        tol: float = 1e-4,
        seed: int | None = None,
    ) -> None:
        self.n_components: int = n_components
        self.max_iter: int = max_iter
        self.tol: float = tol
        self.seed: int | None = seed

        # parameters
        self.weights_: NDArray[np.float64] | None = None
        self.means_: NDArray[np.float64] | None = None
        self.covariances_: NDArray[np.float64] | None = None
        self.log_likelihoods_: list[float] = []

    def _initialize_parameters(self, data: NDArray[np.float64]) -> None:
        """Randomly initialize means, covariances, and mixture weights.

        Examples
        --------
        >>> sample = np.array(
        ...     [[0.0, 0.5], [1.0, 1.5], [2.0, 2.5], [3.0, 3.5]]
        ... )
        >>> model = GaussianMixture(n_components=2, seed=0)
        >>> model._initialize_parameters(sample)
        >>> model.means_.shape
        (2, 2)
        >>> bool(np.isclose(model.weights_.sum(), 1.0))
        True
        """
        rng = np.random.default_rng(self.seed)
        n_samples, _ = data.shape

        indices = rng.choice(n_samples, self.n_components, replace=False)
        self.means_ = data[indices]

        identity = np.eye(data.shape[1]) * 1e-6
        self.covariances_ = np.array(
            [np.cov(data, rowvar=False) + identity for _ in range(self.n_components)]
        )
        self.weights_ = np.ones(self.n_components) / self.n_components

    def _e_step(self, data: NDArray[np.float64]) -> NDArray[np.float64]:
        """Compute responsibilities (posterior probabilities).

        Examples
        --------
        >>> sample = np.array(
        ...     [[0.0, 0.5], [1.0, 1.5], [2.0, 2.5], [3.0, 3.5]]
        ... )
        >>> model = GaussianMixture(n_components=2, seed=0)
        >>> model._initialize_parameters(sample)
        >>> resp = model._e_step(sample)
        >>> resp.shape
        (4, 2)
        >>> bool(np.allclose(resp.sum(axis=1), 1.0))
        True
        """
        if self.weights_ is None or self.means_ is None or self.covariances_ is None:
            raise ValueError(
                "Model parameters must be initialized before running the E-step."
            )

        n_samples = data.shape[0]
        responsibilities = np.zeros((n_samples, self.n_components))
        weights = self.weights_
        means = self.means_
        covariances = self.covariances_

        for k in range(self.n_components):
            rv = multivariate_normal(
                mean=means[k], cov=covariances[k], allow_singular=True
            )
            responsibilities[:, k] = weights[k] * rv.pdf(data)

        # Normalize to get probabilities
        responsibilities /= responsibilities.sum(axis=1, keepdims=True)
        return responsibilities

    def _m_step(
        self,
        data: NDArray[np.float64],
        responsibilities: NDArray[np.float64],
    ) -> None:
        """Update weights, means, and covariances.

        Note: assumes the model parameters are already initialized.

        Examples
        --------
        >>> sample = np.array(
        ...     [[0.0, 0.5], [1.0, 1.5], [2.0, 2.5], [3.0, 3.5]]
        ... )
        >>> model = GaussianMixture(n_components=2, seed=0)
        >>> model._initialize_parameters(sample)
        >>> resp = model._e_step(sample)
        >>> model._m_step(sample, resp)
        >>> bool(np.isclose(model.weights_.sum(), 1.0))
        True
        """
        n_samples, n_features = data.shape
        component_counts = responsibilities.sum(axis=0)

        self.weights_ = component_counts / n_samples
        self.means_ = (responsibilities.T @ data) / component_counts[:, np.newaxis]

        if self.covariances_ is None or self.means_ is None:
            raise ValueError(
                "Model parameters must be initialized before running the M-step."
            )

        covariances = self.covariances_
        means = self.means_

        for k in range(self.n_components):
            diff = data - means[k]
            covariances[k] = (responsibilities[:, k][:, np.newaxis] * diff).T @ diff
            covariances[k] /= component_counts[k]
            # Add small regularization term for numerical stability
            covariances[k] += np.eye(n_features) * 1e-6

    def _compute_log_likelihood(self, data: NDArray[np.float64]) -> float:
        """Compute total log-likelihood of the model.

        Note: assumes the model parameters are already initialized.

        Examples
        --------
        >>> sample = np.array(
        ...     [[0.0, 0.5], [1.0, 1.5], [2.0, 2.5], [3.0, 3.5]]
        ... )
        >>> model = GaussianMixture(n_components=2, seed=0)
        >>> model._initialize_parameters(sample)
        >>> bool(np.isfinite(model._compute_log_likelihood(sample)))
        True
        """
        if self.weights_ is None or self.means_ is None or self.covariances_ is None:
            raise ValueError(
                "Model parameters must be initialized before computing likelihood."
            )

        n_samples = data.shape[0]
        total_pdf = np.zeros((n_samples, self.n_components))
        weights = self.weights_
        means = self.means_
        covariances = self.covariances_

        for k in range(self.n_components):
            rv = multivariate_normal(
                mean=means[k], cov=covariances[k], allow_singular=True
            )
            total_pdf[:, k] = weights[k] * rv.pdf(data)

        log_likelihood = np.sum(np.log(np.sum(total_pdf, axis=1) + 1e-12))
        return log_likelihood

    def fit(self, data: NDArray[np.float64]) -> None:
        """Fit the Gaussian Mixture Model to data using the EM algorithm.

        Examples
        --------
        >>> sample = np.array(
        ...     [[0.0, 0.5], [1.0, 1.5], [2.0, 2.5], [3.0, 3.5]]
        ... )
        >>> model = GaussianMixture(n_components=2, max_iter=5, tol=1e-3, seed=0)
        >>> model.fit(sample)  # doctest: +ELLIPSIS
        GAUSSIAN-MIXTURE/ ...
        >>> len(model.log_likelihoods_) > 0
        True
        """
        self._initialize_parameters(data)

        prev_log_likelihood = None

        for i in range(self.max_iter):
            # E-step
            responsibilities = self._e_step(data)

            # M-step
            self._m_step(data, responsibilities)

            # Log-likelihood
            log_likelihood = self._compute_log_likelihood(data)
            self.log_likelihoods_.append(log_likelihood)

            if (
                prev_log_likelihood is not None
                and abs(log_likelihood - prev_log_likelihood) < self.tol
            ):
                print(f"{TAG}Converged at iteration {i}.")
                break
            prev_log_likelihood = log_likelihood

        print(f"{TAG}Training complete. Final log-likelihood: {log_likelihood:.4f}")

    def predict(self, data: NDArray[np.float64]) -> NDArray[np.int_]:
        """Predict cluster assignment for each data point.

        Note: assumes the model parameters are already initialized.

        Examples
        --------
        >>> sample = np.array(
        ...     [[0.0, 0.5], [1.0, 1.5], [2.0, 2.5], [3.0, 3.5]]
        ... )
        >>> model = GaussianMixture(n_components=2, max_iter=5, tol=1e-3, seed=0)
        >>> model.fit(sample)  # doctest: +ELLIPSIS
        GAUSSIAN-MIXTURE/ ...
        >>> labels = model.predict(sample)
        >>> labels.shape
        (4,)
        """
        responsibilities = self._e_step(data)
        return np.argmax(responsibilities, axis=1)

    def plot_results(self, data: NDArray[np.float64]) -> None:
        """Visualize GMM clustering results (2D only).

        Note: This method assumes self.means_ is initialized.

        Examples
        --------
        >>> sample = np.ones((3, 3))
        >>> model = GaussianMixture()
        >>> model.plot_results(sample)
        GAUSSIAN-MIXTURE/ Plotting only supported for 2D data.
        """
        if data.shape[1] != 2:
            print(f"{TAG}Plotting only supported for 2D data.")
            return

        labels = self.predict(data)
        if self.means_ is None:
            raise ValueError("Model means must be initialized before plotting.")
        plt.scatter(data[:, 0], data[:, 1], c=labels, cmap="viridis", s=30)
        plt.scatter(self.means_[:, 0], self.means_[:, 1], c="red", s=100, marker="x")
        plt.title("Gaussian Mixture Model Clustering")
        plt.xlabel("Feature 1")
        plt.ylabel("Feature 2")
        plt.show()


# Mock test
if __name__ == "__main__":
    from sklearn.datasets import make_blobs

    sample_data, _ = make_blobs(
        n_samples=300, centers=3, cluster_std=1.2, random_state=42
    )
    gmm = GaussianMixture(n_components=3, max_iter=100, seed=42)
    gmm.fit(sample_data)
    labels = gmm.predict(sample_data)
    gmm.plot_results(sample_data)
