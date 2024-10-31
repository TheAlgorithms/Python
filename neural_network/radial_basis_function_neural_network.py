"""
 - - - - - -- - - - - - - - - - - - - - - - - - - - - - - 
Name - - RBFNN - Radial Basis Function Neural Network
Goal - - Recognize Patterns in Data
Detail: Total 3 layers neural network
        * Input layer
        * Hidden layer with RBF activation
        * Output layer
Author: Your Name
Github: your_email@example.com
Date: 2024.10.31
- - - - - -- - - - - - - - - - - - - - - - - - - - - - - 
"""

import numpy as np  # For numerical operations

class RBFNN:
    def __init__(self, input_size, hidden_size, output_size):
        """
        Initialize the RBFNN parameters.
        
        :param input_size: Number of input features
        :param hidden_size: Number of hidden units in the RBF layer
        :param output_size: Number of output classes
        """
        self.input_size = input_size  # Size of input layer
        self.hidden_size = hidden_size  # Size of hidden layer
        self.output_size = output_size  # Size of output layer
        
        rng = np.random.default_rng()  # Create a random number generator
        # Initialize centers and spread of the RBF neurons
        self.centers = rng.random((hidden_size, input_size))  # Centers for RBF
        self.spread = rng.random(hidden_size)  # Spread for each RBF

        # Initialize weights for the output layer
        self.weights = rng.random((hidden_size, output_size))  # Weights for output layer

    def rbf(self, x, center, spread):
        """ Radial Basis Function (Gaussian). """
        return np.exp(-np.linalg.norm(x - center) ** 2 / (2 * spread ** 2))

    def forward(self, x):
        """ Forward pass through the network. """
        hidden_outputs = np.zeros(self.hidden_size)  # Outputs of hidden layer
        for i in range(self.hidden_size):
            hidden_outputs[i] = self.rbf(x, self.centers[i], self.spread[i])  # Compute RBF outputs

        output = np.dot(hidden_outputs, self.weights)  # Compute final output
        return output

    def train(self, x_train, y_train, epochs, learning_rate):
        """
        Train the RBFNN model.
        
        :param x_train: Input data
        :param y_train: Target output
        :param epochs: Number of training iterations
        :param learning_rate: Learning rate for weight updates
        """
        for _ in range(epochs):  # Use underscore for unused loop variable
            for i in range(len(x_train)):
                x_i = x_train[i]
                y_i = y_train[i]

                # Forward pass
                hidden_outputs = np.zeros(self.hidden_size)
                for j in range(self.hidden_size):
                    hidden_outputs[j] = self.rbf(x_i, self.centers[j], self.spread[j])

                output = np.dot(hidden_outputs, self.weights)  # Output layer
                
                # Calculate the error
                error = y_i - output
                
                # Update weights
                self.weights += learning_rate * hidden_outputs.reshape(-1, 1) * error

    def predict(self, x_test):
        """
        Predict outputs for given input data.
        
        :param x_test: Input data
        :return: Predicted outputs
        """
        predictions = []
        for x in x_test:
            output = self.forward(x)  # Forward pass to get prediction
            predictions.append(output)
        return np.array(predictions)
