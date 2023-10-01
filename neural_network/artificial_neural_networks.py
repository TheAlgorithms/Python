"""
Title: Simplified Implementation of Artificial Neural Networks

Description: This Python code offers a straightforward approach to utilizing Artificial Neural Networks for tasks involving both classification and regression.
"""

import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras

class ANN_classifier:
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
        self.optimizer = opt
        self.loss = lo
        self.ann.compile(optimizer=self.optimizer, loss=self.loss, metrics=['accuracy'])

    def train(self, X_train: np.ndarray, y_train: np.ndarray) -> None:
        self.ann.fit(X_train, y_train, batch_size=32, epochs=100)

    def predict(self, X_test: np.ndarray) -> np.ndarray:
        predicted = self.ann.predict(X_test)
        return predicted

    def add_layer(self, unit: int, activate: str) -> None:
        self.params.insert(len(self.params)-1, keras.layers.Dense(units=unit, activation=activate))
        self.ann.compile(optimizer=self.optimizer, loss=self.loss, metrics=['accuracy'])

    def update_neurons(self, new_no: int, u: int = 6, activate: str = 'sigmoid') -> None:
        self.params[new_no-1] = keras.layers.Dense(units=u, activation=activate)
        self.ann.compile(optimizer=self.optimizer, loss=self.loss, metrics=['accuracy'])

class ANN_regressor:
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
        self.ann.fit(X_train, y_train, batch_size=32, epochs=100)

    def predict(self, X_test: np.ndarray) -> np.ndarray:
        predicted = self.ann.predict(X_test)
        return predicted

    def add_layer(self, unit: int, activate: str) -> None:
        return self.params.append(keras.layers.Dense(units=unit, activation=activate))

if __name__ == "__main__":
    # Dummy data for demonstration
    X_train = np.random.rand(100, 10)
    y_train = np.random.randint(0, 2, size=(100,))
    X_test = np.random.rand(10, 10)

    obj = ANN_classifier(3)

    # Train the classifier
    obj.train(X_train, y_train)

    # Predict using the trained classifier
    predictions = obj.predict(X_test)

    print(predictions)

    # Dummy data for regression
    y_train_regressor = np.random.rand(100, 1)
    X_test_regressor = np.random.rand(10, 10)

    obj_regressor = ANN_regressor(1)

    # Train the regressor
    obj_regressor.train(X_train, y_train_regressor)

    # Predict using the trained regressor
    predictions_regressor = obj_regressor.predict(X_test_regressor)

    print(predictions_regressor)

