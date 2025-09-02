# RBF Neural Network (RBFNN) on Iris Dataset
# ------------------------------------------------------
# This script implements a Radial Basis Function Neural Network (RBFNN)
# for classification tasks, using the Iris dataset as an example.
#
# Features:
# - Uses KMeans to determine RBF centers.
# - Applies Gaussian radial basis function as hidden layer activation.
# - Trains output weights using least-squares fitting.
#
# Includes:
# - Full training and prediction pipeline.
# - Evaluation using classification accuracy.
# ------------------------------------------------------

import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler


class RBFNN:
    def __init__(self, num_centers, gamma):
        # Initialize with number of RBF centers and spread parameter (gamma)
        self.num_centers = num_centers
        self.gamma = gamma
        self.centers = None
        self.weights = None

    def _rbf(self, x, centers):
        # Compute Gaussian RBF activations for inputs x given the centers
        dist = cdist(x, centers, "euclidean")  # Compute Euclidean distance to centers
        return np.exp(-self.gamma * (dist**2))  # Apply Gaussian function

    def train(self, x_data, y_data):
        # Train the RBFNN
        # Step 1: Use KMeans to find cluster centers for RBFs
        kmeans = KMeans(n_clusters=self.num_centers, random_state=0).fit(x_data)
        self.centers = kmeans.cluster_centers_

        # Step 2: Compute RBF activations
        rbf_activations = self._rbf(x_data, self.centers)

        # Step 3: Solve output weights using least squares
        self.weights = np.linalg.pinv(rbf_activations).dot(y_data)

    def predict(self, x):
        # Predict using learned weights and RBF activations
        rbf_activations = self._rbf(x, self.centers)
        return rbf_activations.dot(self.weights)


if __name__ == "__main__":
    # Load and preprocess Iris dataset
    iris = load_iris()
    x = iris.data  # Feature matrix
    y = iris.target.reshape(-1, 1)  # Labels

    # Standardize features
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)

    # One-hot encode target labels for multi-class classification
    encoder = OneHotEncoder(sparse_output=False)
    y_encoded = encoder.fit_transform(y)

    # Split data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(
        x_scaled, y_encoded, test_size=0.2, random_state=42
    )

    # Initialize and train the RBF Neural Network
    rbfnn = RBFNN(num_centers=10, gamma=1.0)
    rbfnn.train(x_train, y_train)

    # Predict on test set
    y_pred_probs = rbfnn.predict(x_test)
    y_pred = np.argmax(y_pred_probs, axis=1)
    y_true = np.argmax(y_test, axis=1)

    # Evaluate accuracy
    accuracy = accuracy_score(y_true, y_pred)
    print(f"Classification Accuracy: {accuracy:.4f}")
