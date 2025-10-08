"""
Principal Component Analysis (PCA) implemented from scratch using NumPy.

PCA is a dimensionality reduction technique that transforms high-dimensional data
into a lower-dimensional representation while retaining as much variance as possible.

This implementation includes:
- Data standardization (mean centering and scaling)
- Covariance matrix computation
- Eigenvalue decomposition to find principal components
- Dimensionality reduction with explained variance calculation
- Comparison with scikit-learn implementation

Reference: https://en.wikipedia.org/wiki/Principal_component_analysis
"""

import doctest

import numpy as np


class PCAFromScratch:
    """
    Principal Component Analysis implementation from scratch using NumPy.

    This class provides a complete PCA implementation without external ML libraries,
    demonstrating the mathematical foundations of the algorithm.
    """

    def __init__(self, n_components: int | None = None) -> None:
        """
        Initialize PCA with specified number of components.

        Args:
            n_components: Number of principal components to retain.
                         If None, all components are retained.

        >>> pca = PCAFromScratch(n_components=2)
        >>> pca.n_components
        2
        """
        self.n_components = n_components
        self.components_: np.ndarray | None = None
        self.explained_variance_: np.ndarray | None = None
        self.explained_variance_ratio_: np.ndarray | None = None
        self.mean_: np.ndarray | None = None
        self.std_: np.ndarray | None = None

    def _standardize_data(self, x: np.ndarray) -> np.ndarray:
        """
        Standardize the data by mean centering and scaling to unit variance.

        Args:
            x: Input data matrix of shape (n_samples, n_features)

        Returns:
            Standardized data matrix

        >>> pca = PCAFromScratch()
        >>> X = np.array([[1, 2], [3, 4], [5, 6]])
        >>> X_std = pca._standardize_data(X)
        >>> np.allclose(X_std.mean(axis=0), 0, atol=1e-15)
        True
        >>> np.allclose(X_std.std(axis=0), 1, atol=1e-10)
        True
        """
        # Calculate mean and standard deviation
        self.mean_ = np.mean(x, axis=0)
        self.std_ = np.std(x, axis=0, ddof=0)  # ddof=0 for population std

        # Avoid division by zero for constant features
        self.std_[self.std_ == 0] = 1.0

        # Standardize the data
        x_standardized = (x - self.mean_) / self.std_

        return x_standardized

    def _compute_covariance_matrix(self, x: np.ndarray) -> np.ndarray:
        """
        Compute the covariance matrix of the standardized data.

        Args:
            x: Standardized data matrix of shape (n_samples, n_features)

        Returns:
            Covariance matrix of shape (n_features, n_features)

        >>> pca = PCAFromScratch()
        >>> X = np.array([[1, 2], [2, 3], [3, 4]])
        >>> X_std = pca._standardize_data(X)
        >>> cov_matrix = pca._compute_covariance_matrix(X_std)
        >>> cov_matrix.shape
        (2, 2)
        >>> np.allclose(cov_matrix, cov_matrix.T)  # Symmetric matrix
        True
        """
        n_samples = x.shape[0]
        # Covariance matrix = (X^T * X) / (n_samples - 1)
        covariance_matrix = np.dot(x.T, x) / (n_samples - 1)
        return covariance_matrix

    def _eigenvalue_decomposition(
        self, covariance_matrix: np.ndarray
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        Perform eigenvalue decomposition on the covariance matrix.

        Args:
            covariance_matrix: Covariance matrix of shape (n_features, n_features)

        Returns:
            Tuple of (eigenvalues, eigenvectors)

        >>> pca = PCAFromScratch()
        >>> cov_matrix = np.array([[2, 1], [1, 2]])
        >>> eigenvalues, eigenvectors = pca._eigenvalue_decomposition(cov_matrix)
        >>> eigenvalues.shape
        (2,)
        >>> eigenvectors.shape
        (2, 2)
        """
        # Compute eigenvalues and eigenvectors
        eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)

        # Sort eigenvalues and eigenvectors in descending order
        idx = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]

        return eigenvalues, eigenvectors

    def fit(self, x: np.ndarray) -> "PCAFromScratch":
        """
        Fit PCA to the data.

        Args:
            x: Input data matrix of shape (n_samples, n_features)

        Returns:
            Self for method chaining

        >>> pca = PCAFromScratch(n_components=2)
        >>> X = np.random.randn(100, 4)
        >>> fitted = pca.fit(X)
        >>> isinstance(fitted, PCAFromScratch)
        True
        """
        if x.ndim != 2:
            raise ValueError("Input data must be 2-dimensional")

        n_samples, n_features = x.shape

        # Set default number of components
        if self.n_components is None:
            self.n_components = min(n_samples, n_features)
        elif self.n_components > min(n_samples, n_features):
            msg = (
                f"n_components={self.n_components} cannot be larger than "
                f"min(n_samples, n_features)={min(n_samples, n_features)}"
            )
            raise ValueError(msg)

        # Standardize the data
        x_standardized = self._standardize_data(x)

        # Compute covariance matrix
        covariance_matrix = self._compute_covariance_matrix(x_standardized)

        # Perform eigenvalue decomposition
        eigenvalues, eigenvectors = self._eigenvalue_decomposition(covariance_matrix)

        # Select the top n_components
        self.components_ = eigenvectors[:, : self.n_components]
        self.explained_variance_ = eigenvalues[: self.n_components]

        # Calculate explained variance ratio
        total_variance = np.sum(eigenvalues)
        self.explained_variance_ratio_ = self.explained_variance_ / total_variance

        return self

    def transform(self, x: np.ndarray) -> np.ndarray:
        """
        Transform data using the fitted PCA.

        Args:
            x: Input data matrix of shape (n_samples, n_features)

        Returns:
            Transformed data matrix of shape (n_samples, n_components)

        >>> pca = PCAFromScratch(n_components=2)
        >>> X = np.random.randn(50, 4)
        >>> fitted = pca.fit(X)
        >>> X_transformed = pca.transform(X)
        >>> X_transformed.shape
        (50, 2)
        """
        if self.components_ is None:
            raise ValueError("PCA must be fitted before transform")

        # Standardize the input data using the same parameters as during fit
        x_standardized = (x - self.mean_) / self.std_

        # Project data onto principal components
        x_transformed = np.dot(x_standardized, self.components_)

        return x_transformed

    def fit_transform(self, x: np.ndarray) -> np.ndarray:
        """
        Fit PCA and transform data in one step.

        Args:
            x: Input data matrix of shape (n_samples, n_features)

        Returns:
            Transformed data matrix of shape (n_samples, n_components)

        >>> pca = PCAFromScratch(n_components=2)
        >>> X = np.random.randn(50, 4)
        >>> X_transformed = pca.fit_transform(X)
        >>> X_transformed.shape
        (50, 2)
        """
        return self.fit(x).transform(x)

    def inverse_transform(self, x_transformed: np.ndarray) -> np.ndarray:
        """
        Transform data back to original space.

        Args:
            x_transformed: Transformed data matrix of shape (n_samples, n_components)

        Returns:
            Data in original space of shape (n_samples, n_features)

        >>> pca = PCAFromScratch(n_components=2)
        >>> X = np.random.randn(50, 4)
        >>> X_transformed = pca.fit_transform(X)
        >>> X_reconstructed = pca.inverse_transform(X_transformed)
        >>> X_reconstructed.shape
        (50, 4)
        """
        if self.components_ is None or self.mean_ is None or self.std_ is None:
            raise ValueError("PCA must be fitted before inverse_transform")

        # Transform back to standardized space
        x_standardized = np.dot(x_transformed, self.components_.T)

        # Denormalize to original space
        x_original = (x_standardized * self.std_) + self.mean_

        return x_original


def compare_with_sklearn() -> None:
    """
    Compare our PCA implementation with scikit-learn's PCA.

    This function demonstrates that our implementation produces results
    very close to the scikit-learn implementation.
    """
    from sklearn.datasets import make_blobs
    from sklearn.decomposition import PCA

    # Generate sample data
    x, _ = make_blobs(n_samples=100, centers=3, n_features=4, random_state=42)

    # Our implementation
    pca_ours = PCAFromScratch(n_components=2)
    x_transformed_ours = pca_ours.fit_transform(x)

    # Scikit-learn implementation
    pca_sklearn = PCA(n_components=2, random_state=42)
    x_transformed_sklearn = pca_sklearn.fit_transform(x)

    # Compare results (should be very similar, possibly with different signs)
    print("Our PCA - First 5 rows:")
    print(x_transformed_ours[:5])
    print("\nScikit-learn PCA - First 5 rows:")
    print(x_transformed_sklearn[:5])

    print(f"\nOur explained variance ratio: {pca_ours.explained_variance_ratio_}")
    print(f"Sklearn explained variance ratio: {pca_sklearn.explained_variance_ratio_}")

    # Check if results are similar (within tolerance)
    correlation = np.corrcoef(
        x_transformed_ours.flatten(), x_transformed_sklearn.flatten()
    )[0, 1]
    print(f"\nCorrelation between implementations: {correlation:.6f}")


def main() -> None:
    """
    Demonstrate PCA from scratch implementation.
    """
    # Generate sample data
    rng = np.random.default_rng(42)
    n_samples, n_features = 100, 4
    x = rng.standard_normal((n_samples, n_features))

    print("Original data shape:", x.shape)
    print("Original data (first 5 rows):")
    print(x[:5])

    # Apply PCA
    pca = PCAFromScratch(n_components=2)
    x_transformed = pca.fit_transform(x)

    print(f"\nTransformed data shape: {x_transformed.shape}")
    print("Transformed data (first 5 rows):")
    print(x_transformed[:5])

    print(f"\nExplained variance ratio: {pca.explained_variance_ratio_}")
    print(f"Total variance explained: {np.sum(pca.explained_variance_ratio_):.4f}")

    # Demonstrate inverse transform
    x_reconstructed = pca.inverse_transform(x_transformed)
    reconstruction_error = np.mean((x - x_reconstructed) ** 2)
    print(f"\nReconstruction error (MSE): {reconstruction_error:.6f}")

    # Compare with sklearn
    print("\n" + "=" * 50)
    print("Comparison with scikit-learn:")
    compare_with_sklearn()


if __name__ == "__main__":
    doctest.testmod()
    main()
