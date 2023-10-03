"""
    Principal Component Analysis (PCA) is an unsupervised learning
    algorithm that is used for the dimensionality reduction in machine
    learning. It  is a statistical procedure that uses an orthogonal
    transformation to convert a set of observations of possibly correlated
    variables into a set of values of linearly uncorrelated variables called
    principal components.

    Data: The data used for PCA is a set of 500 data points, each with 4
    features. The data is assumed to be in normal form.

    Reference: https://en.wikipedia.org/wiki/Principal_component_analysis

"""
import numpy as np


class PCA:
    def __init__(self, n_components: int) -> None:
        """
        Parameters:
        n_components: The number of components required after dimensionality reduction

        Create a PCA object with the given number of components
        """
        self.n = n_components
        self.mean = None
        self.components = None

    def fit(self, vector: np.ndarray[float]) -> None:
        """
        Parameters:
        vector: The data to be fitted

        Fit the PCA model to the given data
        The process of performing PCA involves the following steps:
        1. Normalize the data by subtracting the mean from each data point
        2. Calculate the covariance matrix of the normalized data
        3. Calculate the eigenvalues and eigenvectors of the covariance matrix
        4. Sort the eigenvalues and eigenvectors in descending order of the eigenvalues
        5. Choose the first n eigenvectors, where n is the number of components

        >>> test_data = np.array([
        ... [1.2, 2.3, 3.4], [4.5, 5.6, 6.7], [7.8, 8.9, 9.0], [10.1, 11.2, 12.3]
        ... ])
        >>> test_pca = PCA(2)
        >>> test_pca.fit(test_data)
        """
        self.mean = np.mean(vector, axis=0)
        vector = vector - self.mean

        cov = np.cov(vector.T)

        eigen_vector, eigen_value = np.linalg.eig(cov)
        eigen_vector = eigen_vector.T

        indexes = np.argsort(eigen_value)[::-1]
        eigen_vector = eigen_vector[indexes]

        self.components = eigen_vector[: self.n]

    def transform(self, vector: np.ndarray[float]) -> np.ndarray[float]:
        """
        Parameters:
        vector: The data to be transformed

        Transform the given data using the fitted PCA model

        >>> test_data = np.array([
        ... [1.2, 2.3, 3.4], [4.5, 5.6, 6.7], [7.8, 8.9, 9.0], [10.1, 11.2, 12.3]
        ... ])
        >>> test_pca = PCA(2)
        >>> test_pca.fit(test_data)
        >>> test_pca.transform(test_data)
        array([[-208.09344033, -208.13166667],
               [ -61.95844033,  -61.99666667],
               [  84.02365433,   84.13833333],
               [ 186.02822633,  185.99      ]])
        """
        vector = vector - self.mean
        return np.dot(vector, np.transpose(self.components))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    X1 = np.random.normal(0, 1, 500)
    X2 = np.random.normal(0, 1, 500)
    X3 = np.random.normal(0, 1, 500)
    X4 = np.random.normal(0, 1, 500)

    data = np.column_stack((X1, X2, X3, X4))

    pca = PCA(2)
    pca.fit(data)
    post_pca_data = pca.transform(data)

    print("Shape of X (Data Points) is: ", data.shape)
    print("Shape of X after PCA is: ", post_pca_data.shape)
