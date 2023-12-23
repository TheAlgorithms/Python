import numpy as np


class MLP:
    """
    A simple Multi-Layer Perceptron with one hidden layer.
    """

    def __init__(self, num_inputs, num_hidden, num_outputs):
        """
        Initialize the weights and biases of the network.
        Weights are initialized randomly using numpy's random rand function.
        Biases are initialized to zero.
        """
        self.weights1 = np.random.rand(num_inputs, num_hidden)
        self.biases1 = np.zeros(num_hidden)
        self.weights2 = np.random.rand(num_hidden, num_outputs)
        self.biases2 = np.zeros(num_outputs)

    def forward(self, inputs):
        """
        Perform the forward pass of the MLP.

        Parameters:
        inputs (np.ndarray): Input data

        Returns:
        np.ndarray: Outputs from the MLP
        """

        # Calculate the outputs from the first hidden layer
        z1 = inputs.dot(self.weights1) + self.biases1
        a1 = np.tanh(z1)

        # Calculate the outputs from the second output layer
        z2 = a1.dot(self.weights2) + self.biases2
        return z2

    def fit(self, inputs, labels, epochs, learning_rate):
        """
        Train the MLP using backpropagation.

        Parameters:
        inputs (np.ndarray): Input data
        labels (np.ndarray): Target outputs
        epochs (int): Number of training iterations
        learning_rate (float): Learning rate for weight updates
        """

        for _ in range(epochs):
            # Perform the forward pass
            outputs = self.forward(inputs)

            # Calculate the gradients via backpropagation
            dz2 = 2 * (outputs - labels)
            dw2 = np.dot(self.a1.T, dz2)
            db2 = dz2.sum(axis=0)

            da1 = np.dot(dz2, self.weights2.T)
            dz1 = da1 * (1 - np.power(self.a1, 2))
            dw1 = np.dot(inputs.T, dz1)
            db1 = dz1.sum(axis=0)

            # Update the weights and biases
            self.weights1 -= learning_rate * dw1
            self.biases1 -= learning_rate * db1
            self.weights2 -= learning_rate * dw2
            self.biases2 -= learning_rate * db2
