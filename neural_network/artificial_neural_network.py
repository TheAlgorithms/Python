"""
Simple Artificial Neural Network (ANN)
- Feedforward Neural Network with 1 hidden layer and Sigmoid activation.
- Uses Gradient Descent for backpropagation and Mean Squared Error (MSE) as the loss function.
- Example demonstrates solving the XOR problem.
"""

import numpy as np


class ANN:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.1):
        # Initialize weights
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)
        # Initialize biases
        self.bias_hidden = np.zeros((1, hidden_size))
        self.bias_output = np.zeros((1, output_size))

        # Learning rate
        self.learning_rate = learning_rate

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def feedforward(self, X):
        # Hidden layer
        self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = self.sigmoid(self.hidden_input)

        # Output layer
        self.final_input = (
            np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        )
        self.final_output = self.sigmoid(self.final_input)

        return self.final_output

    def backpropagation(self, X, y, output):
        # Calculate the error (Mean Squared Error)
        error = y - output
        # Gradient for output layer
        output_gradient = error * self.sigmoid_derivative(output)
        # Error for hidden layer
        hidden_error = output_gradient.dot(self.weights_hidden_output.T)
        hidden_gradient = hidden_error * self.sigmoid_derivative(self.hidden_output)
        # Update weights and biases
        self.weights_hidden_output += (
            self.hidden_output.T.dot(output_gradient) * self.learning_rate
        )
        self.bias_output += (
            np.sum(output_gradient, axis=0, keepdims=True) * self.learning_rate
        )
        self.weights_input_hidden += X.T.dot(hidden_gradient) * self.learning_rate
        self.bias_hidden += (
            np.sum(hidden_gradient, axis=0, keepdims=True) * self.learning_rate
        )

    def train(self, X, y, epochs=10000):
        for epoch in range(epochs):
            output = self.feedforward(X)
            self.backpropagation(X, y, output)
            if epoch % 1000 == 0:
                loss = np.mean(np.square(y - output))
                print(f"Epoch {epoch}, Loss: {loss}")

    def predict(self, X):
        return self.feedforward(X)


if __name__ == "__main__":
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])
    # Initialize the neural network
    ann = ANN(input_size=2, hidden_size=2, output_size=1, learning_rate=0.1)
    # Train the neural network
    ann.train(X, y, epochs=100)
    # Predict
    predictions = ann.predict(X)
    print("Predictions:")
    print(predictions)
