import numpy as np
from sklearn.datasets import make_blobs 
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split

def isolation_forest(features: np.ndarray, test_features: np.ndarray) -> np.ndarray:
    """
    This function trains an Isolation Forest algorithm and predicts anomalies.

    More on Isolation Forest:
    https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html
    https://en.wikipedia.org/wiki/Isolation_forest
    
    Parameters:
    features (np.ndarray): The training data (features) on which the Isolation Forest model will be trained.
    test_features (np.ndarray): The test data (features) to predict whether they are anomalies or not.

    Returns:
    np.ndarray: Array of predictions where -1 indicates an anomaly.

    Raises:
    ValueError: If `features` or `test_features` are not two-dimensional arrays or have mismatched feature sizes.

    Examples:
    >>> features, _ = make_blobs(n_samples=100, centers=3, cluster_std=0.60, random_state=0)
    >>> test_features = np.array([[0, 0], [10, 10], [-1, -1]])  # Adjusted to ensure variability
    >>> predictions = isolation_forest(features, test_features)
    >>> np.unique(predictions)
    array([-1,  1])  # Expecting some normal points and some anomalies

    >>> isolation_forest(np.array([[1, 2]]), np.array([[1]]))  # Test for ValueError
    Traceback (most recent call last):
        ...
    ValueError: `features` and `test_features` must have the same number of features.
    """
    # Validate input shapes
    if features.ndim != 2 or test_features.ndim != 2:
        raise ValueError("`features` and `test_features` must be two-dimensional arrays.")
    if features.shape[1] != test_features.shape[1]:
        raise ValueError("`features` and `test_features` must have the same number of features.")
    
    iso_forest = IsolationForest(n_estimators=100, random_state=42)    
    iso_forest.fit(features)
    
    predictions = iso_forest.predict(test_features)
    return predictions

def main() -> None:
    """
    Main function to demonstrate the use of Isolation Forest on a synthetic dataset.
    """
    features, _ = make_blobs(n_samples=100, centers=3, cluster_std=0.60, random_state=0)
    x_train, x_test = train_test_split(features, test_size=0.2, random_state=42)
    
    test_features = np.array([[1, 1], [5, 5], [10, 10], [6, 6], [-1, -1]])
    predictions = isolation_forest(x_train, test_features)

if __name__ == "__main__":
  import doctest

  doctest.testmod(verbose=True)
  main()