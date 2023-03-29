import copy
import logging
import numpy as np
import scipy

def column_reshape(input_array: np.ndarray) -> np.ndarray:
    """Function to reshape a row Numpy array into a column Numpy array"""

    return input_array.reshape((input_array.size, 1))


def covariance_within_classes(features: np.ndarray, labels: np.ndarray, classes: int) -> np.ndarray:
    """Function to compute the covariance matrix inside each class"""

    covariance_sum = None
    for i in range(classes):
        data = features[:, labels == i]
        data_mean = data.mean(1)
        # Centralize the data of class i
        centered_data = data - column_reshape(data_mean)
        if covariance_sum:
            # If covariance_sum is not None
            covariance_sum += np.dot(centered_data, centered_data.T)
        else:
            # If covariance_sum is None (i.e. first loop)
            covariance_sum = np.dot(centered_data, centered_data.T)

    return covariance_sum / features.shape[1]


def covariance_between_classes(features: np.ndarray, labels: np.ndarray, classes: int) -> np.ndarray:
    """Function to compute the covariance matrix between multiple classes"""

    general_data_mean = features.mean(1)
    covariance_sum = None
    for i in range(classes):
        data = features[:, labels == i]
        device_data = data.shape[1]
        data_mean = data.mean(1)
        if covariance_sum:
            # If covariance_sum is not None
            covariance_sum += device_data * np.dot((column_reshape(data_mean) - column_reshape(general_data_mean),
                                                    (column_reshape(data_mean) - column_reshape(general_data_mean)).T))
        else:
            # If covariance_sum is None (i.e. first loop)
            covariance_sum = device_data * np.dot((column_reshape(data_mean) - column_reshape(general_data_mean),
                                                   (column_reshape(data_mean) - column_reshape(general_data_mean)).T))

    return covariance_sum / features.shape[1]


class DimensionalityReduction:
    """Class to apply PCA and LDA techniques for the dataset dimensionality reduction.\n
    The data structures used are: \n
    * self._features: contains the features for each object as a matrix \n
    * self._class_labels:  contains the labels associated with each object \n
    * self._classes:  the number of classes in the dataset \n
    * self._features_after_PCA: will contain the features mapped in a new space after PCA"""

    def __init__(self, features: np.ndarray, class_labels: np.ndarray, classes: int):
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        self._features = features
        self._class_labels = class_labels
        self._classes = classes
        self._features_after_PCA = None

    def PCA(self, dimensions: int) -> np.ndarray:
        """Principal Component Analysis with a certain filter parameter"""

        try:
            # Check if the features have been loaded
            assert any(self._features) is True
            data_mean = self._features.mean(1)
            # Center the dataset
            centered_data = self._features - np.reshape(data_mean, (data_mean.size, 1))
            covariance_matrix = np.dot(centered_data, centered_data.T) / self._features.shape[1]
            _, eigenvectors = np.linalg.eigh(covariance_matrix)
            # Take all the columns in the reverse order (-1), and then takes only the first columns
            filtered_eigenvectors = eigenvectors[:, ::-1][:, 0:dimensions]
            # Project the database on the new space
            projected_data = np.dot(filtered_eigenvectors.T, self._features)
            self._features_after_PCA = copy.deepcopy(projected_data)
            logging.info("Principal Component Analysis computed")
        except AssertionError:
            logging.basicConfig(level=logging.ERROR, format='%(message)s', force=True)
            logging.error("Feature array is empty")
            raise AssertionError

        return projected_data

    def LDA(self, dimensions: int, pca_features=False) -> np.ndarray:
        """Linear Discriminant Analysis with a certain filter parameter"""

        try:
            if not pca_features:
                # Check if features have been already loaded
                assert any(self._features) is True
                _, eigenvectors = scipy.linalg.eigh(
                    covariance_between_classes(self._features, self._class_labels, self._classes),
                    covariance_within_classes(self._features, self._class_labels, self._classes))
                filtered_eigenvectors = eigenvectors[:, ::-1][:, :dimensions]
                svd_matrix, _, _ = np.linalg.svd(filtered_eigenvectors)
                filtered_svd_matrix = svd_matrix[:, 0:dimensions]
                projected_data = np.dot(filtered_svd_matrix.T, self._features)
                logging.info("Linear Discriminant Analysis computed on original features")
            else:
                # Check if features mapped on PCA have been already loaded
                assert self._features_after_PCA is not None
                _, eigenvectors = scipy.linalg.eigh(
                    covariance_between_classes(self._features_after_PCA, self._class_labels, self._classes),
                    covariance_within_classes(self._features_after_PCA, self._class_labels, self._classes))
                filtered_eigenvectors = eigenvectors[:, ::-1][:, :dimensions]
                svd_matrix, _, _ = np.linalg.svd(filtered_eigenvectors)
                svd_matrix_filtered = svd_matrix[:, 0:dimensions]
                # Project the database on the new space
                projected_data = np.dot(svd_matrix_filtered.T, self._features)
                logging.info("Linear Discriminant Analysis computed on features pre-processed with PCA")
        except AssertionError:
            logging.basicConfig(level=logging.ERROR, format='%(message)s', force=True)
            logging.error("Features array is empty!")
            raise AssertionError

        return projected_data
