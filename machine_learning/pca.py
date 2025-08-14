# Author: https://github.com/satori1995
"""
Principal Component Analysis (PCA) is primarily used for data dimensionality reduction.
Its working principle involves mapping high-dimensional data to a lower-dimensional
space through linear transformation while preserving the main information in the data.

For example, if a sample has n features and n is very large, the training time
will be severely impacted.
However, in real-world situations, not all of these n features play a decisive role
in determining the sample classification - some features have negligible impact.
In such cases, PCA can be used for dimensionality reduction.

Note: At this point, you might think that PCA simply filters features by
selecting the most important ones. But that's not the case.
What PCA actually does is create new features (principal components).
These principal components are linear combinations of the original features,
are orthogonal to each other (uncorrelated),
and are arranged in descending order according to the maximum variance
they capture in the data.

Based on practical requirements, we only need the first k principal components
to achieve the desired effect.
As for the exact value of k, we can set a variance explanation ratio
threshold (such as 95%) and select the minimum number of principal components that
can explain this proportion of variance.
In any case, k must be less than n.

- The first few principal components usually capture most of the variability
  in the data.
  In many real-world datasets, the first 10~20% of principal components can explain
  more than 90% of the data variance.
- The later principal components often capture only small amounts of data variability,
  with some primarily reflecting noise rather than useful information.

Therefore, PCA is more powerful than simple feature selection because it can create
new features(principal components) that are more effective than the original features
while preserving the data structure.
Each principal component is a weighted combination of all original features,
just with different weights.
This enables PCA to preserve the main patterns and structures of the original data
while reducing dimensionality.

Now you should understand what PCA is. Its characteristics are as follows:
- Comprehensive information utilization: Each principal component integrates
  information from all original features, just with different weights assigned.
  This means that even if a feature's contribution is small, the useful information
  it contains can still be preserved in the principal components.
- Uncorrelatedness: Through orthogonal transformation, principal components
  are uncorrelated with each other, eliminating redundant information and
  multicollinearity problems that may exist between original features.
- Noise filtering: Low-variance principal components often represent noise.
  Discarding these components can improve the signal-to-noise ratio.
- Data structure preservation: Although the dimensionality is reduced,
  the main data structures and patterns are still preserved by
  the first few high-variance principal components.

In subsequent calculations and modeling,
we use these principal components (the newly created features).
Since the first k principal components already contain sufficient information
from the original features (where k<n), we achieve dimensionality reduction.
The benefits include faster training speed and lower memory consumption.

So principal components are new features created by linearly
combining the original features.
These new features synthesize the information from the original features
but represent the data in a more effective and streamlined way.
Moreover, each principal component is orthogonal to the others - they extract
information from the original features in mutually independent directions.
The benefit of this approach is that it avoids information redundancy, with each
principal component providing information that other principal components
do not contain.

These principal components are then arranged in descending order according to
the amount of data variance they capture:
- The first principal component is the new feature with the maximum variance.
- The second principal component is the new feature with maximum variance in
  the direction orthogonal to the first principal component.
- And so on...

For example, if a sample has 100 features, 100 principal components will be created.
However, in practical scenarios, the first 10 principal components may already retain
95% of the information from the original features.
If this level of accuracy is acceptable, then we can select only the first
10 principal components.
This reduces the data from 100 dimensions to 10 dimensions, resulting in a
significant speed improvement during training.
"""

import doctest

import numpy as np


class PCA:
    def __init__(self, n_components=None):
        """
        Parameters
        ----------
        n_components : int or float, default=None
            if n >= 1, Number of components to keep.

            if n < 1, select the number of components such that the amount of
            variance that needs to be explained is greater than the percentage
            specified by n_components.

            if n is None, keep min(n_samples, n_features) components.
        """
        self.n_components = n_components
        self.components_ = None
        self.explained_variance_ = None
        self.explained_variance_ratio_ = None

    def fit(self, x: np.ndarray):
        # Zero-mean
        x = x - np.mean(x, axis=0)
        # calculate eigenvalues and eigenvectors
        # the eigenvectors are the corresponding principal components
        # the eigenvalues are the amount of variance that the corresponding principal
        # components can explain
        eigenvalues, eigenvectors = np.linalg.eig(x @ x.T)
        # order by eigenvalues
        sorted_indices = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[sorted_indices]
        eigenvectors = eigenvectors[:, sorted_indices]

        # Matrix SVD, solve U, Σ, V
        u = eigenvectors
        singular_values = np.sqrt(np.where(eigenvalues > 0, eigenvalues, 0))
        sigma = np.diag(singular_values)
        sigma_inv = np.linalg.pinv(sigma)
        v = x.T @ u @ sigma_inv

        component_array = np.real(v.T[np.argsort(singular_values)[::-1]])
        explained_variance_array = np.real(
            np.sort(singular_values**2 / (len(x) - 1))[::-1]
        )
        explained_variance_ratio_array = explained_variance_array / np.sum(
            explained_variance_array
        )

        if self.n_components is None:
            n_components = min(x.shape)
        elif self.n_components >= 1:
            n_components = self.n_components
        elif self.n_components < 1:
            current_explained_variance_ratio = 0
            i = 0
            for i in range(len(explained_variance_ratio_array)):
                current_explained_variance_ratio += explained_variance_ratio_array[i]
                if current_explained_variance_ratio >= self.n_components:
                    break
            n_components = i + 1
        else:
            raise ValueError("n_components must be a number or None")

        self.components_ = component_array[:n_components]
        self.explained_variance_ = explained_variance_array[:n_components]
        self.explained_variance_ratio_ = explained_variance_ratio_array[:n_components]

    def transform(self, x: np.ndarray) -> np.ndarray:
        # Project the centered data onto the selected principal components
        return (x - np.mean(x, axis=0)) @ self.components_.T


def main():
    import time

    from sklearn.datasets import load_digits
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier

    data = load_digits()
    x = data.data
    y = data.target
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=520)
    print(x_train.shape, y_train.shape)  # (1347, 64) (1347,)

    knn_clf = KNeighborsClassifier()
    # Use all features
    knn_clf.fit(x_train, y_train)
    start = time.perf_counter()
    print("score:", knn_clf.score(x_test, y_test))  # score: 0.9822222222222222
    end = time.perf_counter()
    print("costs:", end - start)  # costs: 0.13106690000131493

    # decomposition
    pca = PCA(n_components=0.95)
    pca.fit(x_train)
    x_train_reduction = pca.transform(x_train)
    x_test_reduction = pca.transform(x_test)
    print(x_train_reduction.shape)  # (1347, 28)
    print("n_features:", x_train_reduction.shape[1])  # n_features: 28
    knn_clf = KNeighborsClassifier()
    knn_clf.fit(x_train_reduction, y_train)
    start = time.perf_counter()
    print(
        "score:", knn_clf.score(x_test_reduction, y_test)
    )  # score: 0.9888888888888889
    end = time.perf_counter()
    print("costs:", end - start)  # costs: 0.010363900000811554


if __name__ == "__main__":
    doctest.testmod()
    main()
