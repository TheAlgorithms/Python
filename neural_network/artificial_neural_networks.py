"""
Title: Simplified Implementation of Artificial Neural Networks

Description: This Python code offers a straightforward approach to utilizing Artificial Neural Networks for tasks involving both classification and regression. For more information on multiclass classification, you can refer to [this Wikipedia page](https://en.wikipedia.org/wiki/Multiclass_classification).

"""

import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras

class ANN_classifier:

    """
    Implementation of an Artificial Neural Network for classification tasks.

    Attributes:
        params (list): List of Dense layers in the neural network.
        optimizer (str): The optimizer used for training.
        loss (str): The loss function used for training.
        ann (tensorflow.keras.Sequential): The neural network model.

    Methods:
        neuro_compile(opt='adam', lo='binary_crossentropy'): Set optimizer and loss.
        train(X_train: np.ndarray, y_train: np.ndarray): Train the classifier.
        predict(X_test: np.ndarray) -> np.ndarray: Make predictions on test data.
        add_layer(unit: int, activate: str): Add a new layer to the network.
        update_neurons(new_no: int, u: int = 6, activate: str = 'sigmoid'): Update a layer.

    >>> X_train = np.random.rand(100, 10)
    >>> y_train = np.random.randint(0, 2, size=(100,))
    >>> X_test = np.random.rand(10, 10)
    >>> obj = ANN_classifier(3)
    >>> obj.train(X_train, y_train)
    >>> predictions = obj.predict(X_test)
    >>> isinstance(predictions, np.ndarray)
    True
    """

    def __init__(self, no_of_classes: int) -> None:
        self.params = [
            keras.layers.Dense(units=6, activation='relu'),
            keras.layers.Dense(units=8, activation='relu'),
            keras.layers.Dense(units=10, activation='relu')
        ]
        self.optimizer: str = 'binary_crossentropy'
        self.loss: str = 'adam'
        self.ann = keras.Sequential(self.params)
        self.ann.add(keras.layers.Dense(units=no_of_classes, activation='sigmoid'))

        if no_of_classes > 1:
            self.ann.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        else:
            self.ann.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def neuro_compile(self, opt: str = 'adam', lo: str = 'binary_crossentropy') -> None:
        """
        Set the optimizer and loss for the neural network.

        Args:
            opt (str): Optimizer name.
            lo (str): Loss function name.

        Returns:
            None

        >>> obj = ANN_classifier(2)
        >>> obj.neuro_compile(opt='sgd', lo='mse')
        """
        self.optimizer = opt
        self.loss = lo
        self.ann.compile(optimizer=self.optimizer, loss=self.loss, metrics=['accuracy'])

    def train(self, X_train: np.ndarray, y_train: np.ndarray) -> None:
        """
        Train the classifier.

        Args:
            X_train (np.ndarray): Input data for training.
            y_train (np.ndarray): Target labels.

        Returns:
            None

        >>> X_train = np.random.rand(100, 10)
        >>> y_train = np.random.randint(0, 2, size=(100,))
        >>> obj = ANN_classifier(2)
        >>> obj.train(X_train, y_train)
        """
        self.ann.fit(X_train, y_train, batch_size=32, epochs=100)

    def predict(self, X_test: np.ndarray) -> np.ndarray:
        """
        Make predictions on test data.

        Args:
            X_test (np.ndarray): Input data for testing.

        Returns:
            np.ndarray: Predicted labels.

        >>> X_test = np.random.rand(10, 10)
        >>> obj = ANN_classifier(2)
        >>> obj.train(X_train, y_train)
        >>> predictions = obj.predict(X_test)
        >>> isinstance(predictions, np.ndarray)
        True
        """
        predicted = self.ann.predict(X_test)
        return predicted

    def add_layer(self, unit: int, activate: str) -> None:
        """
        Add a new layer to the network.

        Args:
            unit (int): Number of units in the Dense layer.
            activate (str): Activation function for the layer.

        Returns:
            None

        >>> obj = ANN_classifier(2)
        >>> obj.add_layer(unit=12, activate='relu')
        """
        self.params.insert(len(self.params)-1, keras.layers.Dense(units=unit, activation=activate))
        self.ann.compile(optimizer=self.optimizer, loss=self.loss, metrics=['accuracy'])

    def update_neurons(self, new_no: int, u: int = 6, activate: str = 'sigmoid') -> None:
        """
        Update a layer in the network.

        Args:
            new_no (int): Index of the layer to be updated.
            u (int): Number of units for the updated layer.
            activate (str): Activation function for the updated layer.

        Returns:
            None

        >>> obj = ANN_classifier(2)
        >>> obj.update_neurons(new_no=2, u=8, activate='relu')
        """
        self.params[new_no-1] = keras.layers.Dense(units=u, activation=activate)
        self.ann.compile(optimizer=self.optimizer, loss=self.loss, metrics=['accuracy'])

class ANN_regressor:
    """
    Implementation of an Artificial Neural Network for regression tasks.

    Attributes:
        params (list): List of Dense layers in the neural network.
        ann (tensorflow.keras.Sequential): The neural network model.

    Methods:
        train(X_train: np.ndarray, y_train: np.ndarray): Train the regressor.
        predict(X_test: np.ndarray) -> np.ndarray: Make predictions on test data.
        add_layer(unit: int, activate: str): Add a new layer to the network.

    >>> X_train = np.random.rand(100, 10)
    >>> y_train_regressor = np.random.rand(100, 1)
    >>> X_test_regressor = np.random.rand(10, 10)
    >>> obj = ANN_regressor(1)
    >>> obj.train(X_train, y_train_regressor)
    >>> predictions = obj.predict(X_test_regressor)
    >>> isinstance(predictions, np.ndarray)
    True
    """

    def __init__(self, no_of_classes: int) -> None:
        self.params = [
            keras.layers.Dense(units=6, activation='relu'),
            keras.layers.Dense(units=8, activation='relu'),
            keras.layers.Dense(units=10, activation='relu')
        ]
        self.ann = tf.keras.Sequential(self.params)
        self.ann.add(keras.layers.Dense(units=no_of_classes, activation='sigmoid'))
        self.ann.compile(optimizer='adam', loss='mean_squared_error')

    def train(self, X_train: np.ndarray, y_train: np.ndarray) -> None:
        """
        Train the regressor.

        Args:
            X_train (np.ndarray): Input data for training.
            y_train (np.ndarray): Target values.

        Returns:
            None

        >>> X_train = np.random.rand(100, 10)
        >>> y_train_regressor = np.random.rand(100, 1)
        >>> obj = ANN_regressor(1)
        >>> obj.train(X_train, y_train_regressor)
        """
        self.ann.fit(X_train, y_train, batch_size=32, epochs=100)

    def predict(self, X_test: np.ndarray) -> np.ndarray:
        """
        Make predictions on test data.

        Args:
            X_test (np.ndarray): Input data for testing.

        Returns:
            np.ndarray: Predicted values.

        >>> X_test_regressor = np.random.rand(10, 10)
        >>> obj = ANN_regressor(1)
        >>> obj.train(X_train, y_train_regressor)
        >>> predictions = obj.predict(X_test_regressor)
        >>> isinstance(predictions, np.ndarray)
        True
        """
        predicted = self.ann.predict(X_test)
        return predicted

    def add_layer(self, unit: int, activate: str) -> None:
        """
        Add a new layer to the network.

        Args:
            unit (int): Number of units in the Dense layer.
            activate (str): Activation function for the layer.

        Returns:
            None

        >>> obj = ANN_regressor(1)
        >>> obj.add_layer(unit=12, activate='relu')
        """
        return self.params.append(keras.layers.Dense(units=unit, activation=activate))

if __name__ == "__main__":
    # Dummy data for demonstration
    X_train = np.random.rand(100, 10)
    y_train = np.random.randint(0, 2, size=(100,))
    X_test = np.random.rand(10, 10)

    obj = ANN_classifier(3)
    obj.train(X_train, y_train)
    predictions = obj.predict(X_test)
    print(predictions)

    # Dummy data for regression
    y_train_regressor = np.random.rand(100, 1)
    X_test_regressor = np.random.rand(10, 10)

    obj_regressor = ANN_regressor(1)
    obj_regressor.train(X_train, y_train_regressor)
    predictions_regressor = obj_regressor.predict(X_test_regressor)
    print(predictions_regressor)
