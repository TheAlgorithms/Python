'''
Principal Component Analysis (PCA) is a linear dimensionality reduction technique used 
commonly as a data preprocessing step in unsupervised and supervised machine learning pipelines. 
The principle behind PCA is the reduction in the number of variables in the dataset, while 
preserving as much as information as possible. 

Here, the  principal components represent the directions of the data that explain a 
maximal amount of variance. Here, the data is projected onto a new coordinate system 
such that the direction cqpturing the largest variation in data can be easily identified. 

This implementation of PCA consists of the following steps:
1. Data Standardization (Z-score Normalization): This step involved the centering of the
data by subtracting the mean and dividing it by the standard deviation 
so that it has unit variance.

2. Covariance Matrix Calculation: This step involved the calculation of the covariance matrix 
of the standardized data. The covariance matrix allows us to measure how different 
features vary together, capturing the relationships between them.

3. Singular Value Decomposition: In this step, we use Singular Value Decomposition or SVD to 
Decomposes the covariance matrix into its singular eignvectors and singular eigenvalues,
 which help identify the principal components.

4. Selection of Principal Components: Here, we choose the top k principal components 
that explain the most variance in the data.

5. Projection of Data: Here, we transform the original standardized data into 
the new lower-dimensional space defined by the selected principal components.

REFERENCE: en.wikipedia.org/wiki/Principal_component_analysis
'''

import numpy as np


def svd(matrix):
    """
    Perform Singular Value Decomposition (SVD) on the given matrix.
    Args:
        matrix (np.ndarray): The input matrix.
    Returns:
        tuple: The U, S, and VT matrices from SVD.
    >>> matrix = np.array([[1, 2], [3, 4]])
    >>> u, s, vt = svd(matrix)
    >>> np.allclose(np.dot(u, np.dot(s, vt)), matrix)
    True
    """
    m, n = matrix.shape
    u = np.zeros((m, m))
    s = np.zeros((m, n))
    vt = np.zeros((n, n))
    eigvals, eigvecs = np.linalg.eig(np.dot(matrix.T, matrix))
    vt = eigvecs.T

    singular_values = np.sqrt(eigvals)
    s[:n, :n] = np.diag(singular_values)

    for i in range(n):
        u[:, i] = np.dot(matrix, vt[i, :]) / singular_values[i]

    return u, s, vt

def main(data: list[int], k:int):
    """
    Perform Principal Component Analysis (PCA) on the given data.

    Args:
        data (list[int]): The input data.
        k (int): The number of principal components to retain.

    Returns:
        np.ndarray: The transformed data with reduced dimensionality.

    >>> data = np.array([[1, 2], [3, 4], [5, 6]])
    >>> main(data, 1)
    array([[-2.82842712],
           [ 0.        ],
           [ 2.82842712]])
    """
    z_score = (data - data.mean(axis=0) / data.std(axis=0))
    cov_matrix = np.cov(z_score, ddof=1, rowvar=False)

    u, s, vt = svd(cov_matrix)
    principal_components = vt[:k]
    transformed_data = np.dot(z_score, principal_components.T)
    return transformed_data

if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.datasets import make_blobs

    data, _ = make_blobs(n_samples=100, n_features=4, centers=5, random_state=42)
    k = 2

    transformed_data = main(data, k)
    print("Transformed Data:")
    print(transformed_data)

    assert transformed_data.shape == (data.shape[0], k), "The transformed data does not have the expected shape."

    # Visualize the original data and the transformed data
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.scatter(data[:, 0], data[:, 1], c='blue', edgecolor='k', s=50)
    plt.title("Original Data")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")

    plt.subplot(1, 2, 2)
    plt.scatter(transformed_data, np.zeros_like(transformed_data), c='red', edgecolor='k', s=50)
    plt.title("Transformed Data")
    plt.xlabel("Principal Component 1")
    plt.yticks([])

    plt.tight_layout()
    plt.show()

    print("All tests passed.")