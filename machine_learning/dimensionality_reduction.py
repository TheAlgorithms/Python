import copy
import logging
import numpy as np
import scipy


def column_reshape(input_array: np.ndarray) -> np.ndarray:
    """Function to reshape a row Numpy array into a column Numpy array."""

    return input_array.reshape((input_array.size, 1))


def covariance_within_classes(features: np.ndarray, labels: np.ndarray, classes: int) -> np.ndarray:
    """Function to compute the covariance matrix inside each class."""

    covariance_sum = None
    for i in range(classes):
        data = features[:, labels == i]
        data_mean = data.mean(1)
        centered_data = data - column_reshape(data_mean)
        if covariance_sum:
            covariance_sum += np.dot(centered_data, centered_data.T)
        else:
            covariance_sum = np.dot(centered_data, centered_data.T)

    return covariance_sum / features.shape[1]


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
                                                     (column_reshape(data_mean) - column_reshape(general_data_mean)).T))
        else:
            covariance_sum = device_data * np.dot((column_reshape(data_mean) - column_reshape(general_data_mean),
                                             (column_reshape(data_mean) - column_reshape(general_data_mean)).T))

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
        self._features_after_PCA = None

    def PCA(self, dimensions: int) -> np.ndarray:
        """Principal Component Analysis with default filter parameter equal to 10."""

        try:
            assert any(self._features) is True
            data_mean = self._features.mean(1)
            centered_data = self._features - np.reshape(data_mean, (data_mean.size, 1))
            covariance_matrix = np.dot(centered_data, centered_data.T) / self._features.shape[1]
            s, U = np.linalg.eigh(covariance_matrix)
            # Take all the columns in the reverse order (-1), and then takes only the first columns
            P = U[:, ::-1][:, 0:dimensions]
            projected_data = np.dot(P.T, self._features)
            self._features_after_PCA = copy.deepcopy(projected_data)
            logging.info("Principal Component Analysis computed")
        except AssertionError:
            logging.basicConfig(level=logging.ERROR, format='%(message)s', force=True)
            logging.error("Feature array is empty")
            raise AssertionError

        return projected_data

    def LDA(self, dimensions: int, pca_features=False) -> np.ndarray:
        """Linear Discriminant Analysis with default filter parameter equal to 8."""

        try:
            if not pca_features:
                assert any(self._features) is True
                s, U = scipy.linalg.eigh(covariance_between_classes(self._features, self._class_labels, self._classes),
                                         covariance_within_classes(self._features, self._class_labels, self._classes))
                W = U[:, ::-1][:, :dimensions]
                UW, _, _ = np.linalg.svd(W)
                U = UW[:, 0:dimensions]
                projected_data = np.dot(U.T, self._features)
                logging.info("Linear Discriminant Analysis computed on original features")
            else:
                assert self._features_after_PCA is not None
                s, U = scipy.linalg.eigh(covariance_between_classes(self._features_after_PCA, self._class_labels, self._classes),
                                         covariance_within_classes(self._features_after_PCA, self._class_labels, self._classes))
                W = U[:, ::-1][:, :dimensions]
                UW, _, _ = np.linalg.svd(W)
                U = UW[:, 0:dimensions]
                projected_data = np.dot(U.T, self._features)
                logging.info("Linear Discriminant Analysis computed on features pre-processed with PCA")
        except AssertionError:
            logging.basicConfig(level=logging.ERROR, format='%(message)s', force=True)
            logging.error("Features array is empty!")
            raise AssertionError

        return projected_data
