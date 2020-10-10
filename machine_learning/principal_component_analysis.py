    """
    Principal Component Analysis, or PCA, is a dimensionality-reduction method
    that is often used to reduce the dimensionality of large data sets, 
    by transforming a large set of variables into a smaller one that still 
    contains most of the information in the large set. Reducing the number of variables 
    of a data set naturally comes at the expense of accuracy, but the trick in 
    dimensionality reduction is to trade a little accuracy for simplicity. 
    Because smaller data sets are easier to explore and visualize and make analyzing
    data much easier and faster for machine learning algorithms without extraneous 
    variables to process.
    """

    import numpy as np


    def center(data: np.ndarray) -> np.ndarray:
        """Center data by subtracting mean of each features
        :data   : a numpy array has shape of (observations, features)
        :return : a numpy array has shape of (observations, features)

        >>> center(np.array([[0.5, 1], [1,4]]))
        array([[-0.25, -1.5 ],
            [ 0.25,  1.5 ]])
        """
        N = data.shape[0]
        mean = np.sum(data, axis=0) / N
        X = data - mean
        return X


    def pca(data: np.ndarray, n_components=2) -> np.ndarray:
        """Perform PCA
        >>> data = np.array([[0.5, 1], [1,4]])
        >>> pca(data, 1)
        array([[-1.52069063],
            [ 1.52069063]])
        """
        X = center(data)  # center the data
        N = X.shape[0]  # number of observations
        cov = X.T.dot(X) / N  # compute covariance matrix
        eig_values, eig_vectors = np.linalg.eigh(cov)  # get eigenvalues and eigenvectors

        idx = np.argsort(eig_values)[::-1]  # sort eigenvalues and return index
        vec = eig_vectors[:, idx]  # get sorted eigenvectors with sorted eigenvalues index
        transformed = X.dot(
            vec[:, :n_components]
        )  # multiplying data with k sorted eigenvectors

        return transformed


    if __name__ == "__main__":
        import doctest

        doctest.testmod()
