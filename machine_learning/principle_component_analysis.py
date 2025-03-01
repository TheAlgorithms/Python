"""
Principal Component Analysis (PCA) is a dimensionality reduction technique
commonly used in machine learning. It transforms high-dimensional data into
lower dimensions while retaining most of the information.

Here,we use a dataset (Iris dataset) and apply PCA to reduce the
dimensionality. We compute the principal components and transform the dataset
into a lower-dimensional space.

We reduce the number of columns form 4 to 2

"""

import numpy as np
import requests
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris


def collect_dataset():
    """Collect dataset (Iris dataset)
    :return: Feature matrix and target values
    """
    data = load_iris()
    return np.array(data.data), np.array(data.target)


def apply_pca(data_x, n_components):
    """Apply Principal Component Analysis (PCA)
    :param data_x: Original dataset
    :param n_components: Number of principal components
    :return: Transformed dataset and explained variance
    """
    # Standardizing the features
    scaler = StandardScaler()
    data_x_scaled = scaler.fit_transform(data_x)

    # Applying PCA
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(data_x_scaled)

    # Explained variance ratio
    explained_variance = pca.explained_variance_ratio_

    return principal_components, explained_variance


def main():
    """Driver function"""
    data_x, data_y = collect_dataset()
    # Set number of principal components
    n_components = 3

    # Apply PCA
    transformed_data, variance_ratio = apply_pca(data_x, n_components)

    print("Transformed Dataset (First 5 rows):")
    print(transformed_data[:5])

    print("\nExplained Variance Ratio:")
    print(variance_ratio)


if __name__ == "__main__":
    main()
