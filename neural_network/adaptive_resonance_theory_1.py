"""
- - - - - -- - - - - - - - - - - - - - - - - - - - - - -
Name - - ART1 - Adaptive Resonance Theory 1
Goal - - Cluster Binary Data
Detail: Unsupervised clustering model using a vigilance parameter
        to control cluster formation in binary datasets.
        * Initialize with features and vigilance threshold
        * Train to form clusters based on input patterns
        * Predict for assigning new inputs to clusters
Author: Your Name
Github: your_email@example.com
Date: 2024.10.31
- - - - - -- - - - - - - - - - - - - - - - - - - - - - -
"""

import numpy as np


class ART1:
    def __init__(self, num_features, vigilance=0.8):
        """
        Initialize the ART1 model with the number of features and the vigilance parameter.

        Parameters:
        num_features (int): Number of features in input binary data.
        vigilance (float): Vigilance parameter to control cluster formation (0 < vigilance <= 1).
        """
        self.num_features = num_features
        self.vigilance = vigilance
        self.weights = []  # Stores the weights for clusters

    def _similarity(self, x, w):
        """
        Calculate similarity between input vector x and weight vector w.

        Parameters:
        x (np.array): Input binary vector.
        w (np.array): Cluster weight vector.

        Returns:
        float: Similarity value based on the intersection over the input length.
        """
        return np.sum(np.minimum(x, w)) / np.sum(x)

    def _weight_update(self, x, w):
        """
        Update weights for a cluster based on input vector.

        Parameters:
        x (np.array): Input binary vector.
        w (np.array): Cluster weight vector.

        Returns:
        np.array: Updated weight vector.
        """
        return np.minimum(x, w)

    def train(self, data):
        """
        Train the ART1 model to form clusters based on the vigilance parameter.

        Parameters:
        data (np.array): Binary dataset with each row as a sample.
        """
        for x in data:
            assigned = False
            for i, w in enumerate(self.weights):
                # Check similarity and update weights if similarity exceeds vigilance
                similarity = self._similarity(x, w)
                if similarity >= self.vigilance:
                    self.weights[i] = self._weight_update(x, w)
                    assigned = True
                    break
            if not assigned:
                self.weights.append(x.copy())

    def predict(self, x):
        """
        Predict the cluster for a new input vector or classify it as a new cluster.

        Parameters:
        x (np.array): Input binary vector.

        Returns:
        int: Cluster index for the input or -1 if classified as a new cluster.
        """
        for i, w in enumerate(self.weights):
            # Check similarity for prediction
            similarity = self._similarity(x, w)
            if similarity >= self.vigilance:
                return i
        return -1

    def get_weights(self):
        """
        Retrieve the weight vectors of the clusters.

        Returns:
        list: List of weight vectors for each cluster.
        """
        return self.weights
