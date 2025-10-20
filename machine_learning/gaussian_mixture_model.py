"""
README, Author - Md Ruman Islam (mailto:ruman23.github.io)
Requirements:
  - numpy
  - matplotlib
Python:
  - 3.8+
Inputs:
  - X : a 2D numpy array of features.
  - n_components : number of Gaussian distributions (clusters) to fit.
  - max_iter : maximum number of EM iterations.
  - tol : convergence tolerance.
Usage:
  1. define 'n_components' value and 'X' features array
  2. initialize model:
        gmm = GaussianMixture(n_components=3, max_iter=100)
  3. fit model to data:
        gmm.fit(X)
  4. get cluster predictions:
        labels = gmm.predict(X)
  5. visualize results:
        gmm.plot_results(X)
"""

import warnings
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

warnings.filterwarnings("ignore")

TAG = "GAUSSIAN-MIXTURE/ "


class GaussianMixture:
    """
    Gaussian Mixture Model implemented using the Expectation-Maximization algorithm.
    """

    def __init__(self, n_components=2, max_iter=100, tol=1e-4, seed=None):
        self.n_components = n_components
        self.max_iter = max_iter
        self.tol = tol
        self.seed = seed

        # parameters
        self.weights_ = None
        self.means_ = None
        self.covariances_ = None
        self.log_likelihoods_ = []

    def _initialize_parameters(self, X):
        """Randomly initialize means, covariances, and mixture weights"""
        rng = np.random.default_rng(self.seed)
        n_samples, n_features = X.shape

        indices = rng.choice(n_samples, self.n_components, replace=False)
        self.means_ = X[indices]

        self.covariances_ = np.array(
            [np.cov(X, rowvar=False) for _ in range(self.n_components)]
        )
        self.weights_ = np.ones(self.n_components) / self.n_components

    def _e_step(self, X):
        """Compute responsibilities (posterior probabilities)"""
        n_samples = X.shape[0]
        responsibilities = np.zeros((n_samples, self.n_components))

        for k in range(self.n_components):
            rv = multivariate_normal(mean=self.means_[k], cov=self.covariances_[k])
            responsibilities[:, k] = self.weights_[k] * rv.pdf(X)

        # Normalize to get probabilities
        responsibilities /= responsibilities.sum(axis=1, keepdims=True)
        return responsibilities

    def _m_step(self, X, responsibilities):
        """Update weights, means, and covariances"""
        n_samples, n_features = X.shape
        Nk = responsibilities.sum(axis=0)

        self.weights_ = Nk / n_samples
        self.means_ = (responsibilities.T @ X) / Nk[:, np.newaxis]

        for k in range(self.n_components):
            diff = X - self.means_[k]
            self.covariances_[k] = (responsibilities[:, k][:, np.newaxis] * diff).T @ diff
            self.covariances_[k] /= Nk[k]
            # Add small regularization term for numerical stability
            self.covariances_[k] += np.eye(n_features) * 1e-6

    def _compute_log_likelihood(self, X):
        """Compute total log-likelihood of the model"""
        n_samples = X.shape[0]
        total_pdf = np.zeros((n_samples, self.n_components))

        for k in range(self.n_components):
            rv = multivariate_normal(mean=self.means_[k], cov=self.covariances_[k])
            total_pdf[:, k] = self.weights_[k] * rv.pdf(X)

        log_likelihood = np.sum(np.log(np.sum(total_pdf, axis=1) + 1e-12))
        return log_likelihood

    def fit(self, X):
        """Fit the Gaussian Mixture Model to data using the EM algorithm"""
        self._initialize_parameters(X)

        prev_log_likelihood = None

        for i in range(self.max_iter):
            # E-step
            responsibilities = self._e_step(X)

            # M-step
            self._m_step(X, responsibilities)

            # Log-likelihood
            log_likelihood = self._compute_log_likelihood(X)
            self.log_likelihoods_.append(log_likelihood)

            if prev_log_likelihood is not None:
                if abs(log_likelihood - prev_log_likelihood) < self.tol:
                    print(f"{TAG}Converged at iteration {i}.")
                    break
            prev_log_likelihood = log_likelihood

        print(f"{TAG}Training complete. Final log-likelihood: {log_likelihood:.4f}")

    def predict(self, X):
        """Predict cluster assignment for each data point"""
        responsibilities = self._e_step(X)
        return np.argmax(responsibilities, axis=1)

    def plot_results(self, X):
        """Visualize GMM clustering results (2D only)"""
        if X.shape[1] != 2:
            print(f"{TAG}Plotting only supported for 2D data.")
            return

        labels = self.predict(X)
        plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis", s=30)
        plt.scatter(self.means_[:, 0], self.means_[:, 1], c="red", s=100, marker="x")
        plt.title("Gaussian Mixture Model Clustering")
        plt.xlabel("Feature 1")
        plt.ylabel("Feature 2")
        plt.show()


# Mock test
if __name__ == "__main__":
    from sklearn.datasets import make_blobs

    X, _ = make_blobs(n_samples=300, centers=3, cluster_std=1.2, random_state=42)
    gmm = GaussianMixture(n_components=3, max_iter=100, seed=42)
    gmm.fit(X)
    labels = gmm.predict(X)
    gmm.plot_results(X)