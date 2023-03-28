import logging
import numpy as np
import scipy


def column_reshape(input_array: np.ndarray) -> np.ndarray:
    """Function to reshape a row Numpy array into a column Numpy array."""

    return v.reshape((input_array.size, 1))


def covariance_within_classes(features: np.ndarray, labels: np.ndarray, classes: int) -> np.ndarray:
    """Function to compute the covariance matrix inside each class."""

    covariance_sum = None
    for i in range(classes):
        data = features[:, labels == i]
        data_mean = data.mean(1)
        centered_data = data - column_reshape(data_mean)
        if covariance_sum:
            covariance_sum += + np.dot(centered_data, centered_data.T)
        else:
            covariance_sum = np.dot(centered_data, centered_data.T)

    return convariance_sum / features.shape[1]


def covariance_between_classes(features: np.ndarray, labels: np.ndarray, classes: int) -> np.ndarray:
    """Function to compute the covariance matrix between multiple classes."""

    general_data_mean = features.mean(1)
    covariance_sum = None
    for i in range(classes):
        data = features[:, labels == i]
        device_data = data.shape[1]
        data_mean = data.mean(1)
        if covariance_sum:
            covariance_sum += device_data * np.dot((column_reshape(data_mean) - column_reshape(general_data_mean),
                                                     (column_reshape(data_mean) - column_reshape(general_data_mean)).T)
        else:
            covariance_sum = device_data * np.dot((column_reshape(data_mean) - column_reshape(general_data_mean),
                                             (column_reshape(data_mean) - column_reshape(general_data_mean)).T)

    return covariance_sum / features.shape[1]


class DimensionalityReduction:
    """Class to apply PCA and LDA techniques for the dataset dimensionality reduction.\n
    The data structures used are: \n
    * self._features: a list of lists that contains all the packets features, where each packet has a list of features. \n
    * self._labels: a list that contains the category labels (i.e. device labels) of each list of packet features. \n
    * self._devices_number: an int value that specifies how many device models there are in the dataset. \n
    * self._features_PCA: a Numpy array with the features mapped with PCA. \n
    * self._features_LDA: a Numpy array with the features mapped with LDA."""

    def __init__(self, features: np.ndarray, class_labels: np.ndarray, classes: int):
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        self._features = features
        self._class_labels = class_labels
        self._classes = classes

    def PCA(self, dimensions: int) -> np.ndarray:
        """Principal Component Analysis with default filter parameter equal to 10."""

        try:
            assert any(self._features) is True
            data = np.array(self._features)
            mu = data.mean(1)
            centered_data = self._features - np.reshape(mu, (mu.size, 1))
            covariance_matrix = np.dot(centered_data, centered_data.T) / data.shape[1]
            s, U = np.linalg.eigh(covariance_matrix)
            # Take all the columns in the reverse order (-1), and then takes only the first columns
            P = U[:, ::-1][:, 0:m]
            projected_data = np.dot(P.T, self._features)
            logging.info("Principal Component Analysis computed.")
        except AssertionError:
            logging.basicConfig(level=logging.ERROR, format='%(message)s', force=True)
            logging.error("The features must be a not-empty list")
            raise AssertionError

        return projected_data

    def LDA(self, dimensions: int) -> np.ndarray:
        """Linear Discriminant Analysis with default filter parameter equal to 8."""

        try:
            assert self._features_PCA is not None
            data = np.array(self._features_PCA)
            labels = np.array(self._labels)
            s, U = scipy.linalg.eigh(covariance_between_classes(data, labels, self._devices_number),
                                     covariance_within_classes(data, labels, self._devices_number))
            W = U[:, ::-1][:, :m]
            UW, _, _ = np.linalg.svd(W)
            U = UW[:, 0:m]
            projected_data = np.dot(U.T, self._features_PCA)
            logging.info("Linear Discriminant Analysis computed.")
        except AssertionError:
            logging.basicConfig(level=logging.ERROR, format='%(message)s', force=True)
            logging.error("The features must be passed in PCA algorithm before!")
            raise AssertionError

        return projected_data