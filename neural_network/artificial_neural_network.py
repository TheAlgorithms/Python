"""
Simple Artificial Neural Network (ANN)
- Feedforward Neural Network with 1 hidden layer and Sigmoid activation.
- Uses Gradient Descent for backpropagation and Mean Squared Error (MSE)
  as the loss function.
- Example demonstrates solving the XOR problem.
"""

import numpy as np


class ANN:
    """
    Artificial Neural Network (ANN)

    - Feedforward Neural Network with 1 hidden layer
      and Sigmoid activation.
    - Uses Gradient Descent for backpropagation.
    - Example demonstrates solving the XOR problem.
    """

    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.1):
        # Initialize weights using np.random.Generator
        rng = np.random.default_rng()
        self.weights_input_hidden = rng.standard_normal((input_size, hidden_size))
        self.weights_hidden_output = rng.standard_normal((hidden_size, output_size))

        # Initialize biases
        self.bias_hidden = np.zeros((1, hidden_size))
        self.bias_output = np.zeros((1, output_size))

        # Learning rate
        self.learning_rate = learning_rate

    def sigmoid(self, x):
        """Sigmoid activation function."""
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        """Derivative of the sigmoid function."""
        return x * (1 - x)

    def feedforward(self, x):
        """Forward pass."""
        self.hidden_input = np.dot(x, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = self.sigmoid(self.hidden_input)
        self.final_input = (
            np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        )
        self.final_output = self.sigmoid(self.final_input)
        return self.final_output

    def backpropagation(self, x, y, output):
        """Backpropagation to adjust weights."""
        error = y - output
        output_gradient = error * self.sigmoid_derivative(output)
        hidden_error = output_gradient.dot(self.weights_hidden_output.T)
        hidden_gradient = hidden_error * self.sigmoid_derivative(self.hidden_output)

        self.weights_hidden_output += (
            self.hidden_output.T.dot(output_gradient) * self.learning_rate
        )
        self.bias_output += (
            np.sum(output_gradient, axis=0, keepdims=True) * self.learning_rate
        )

        self.weights_input_hidden += x.T.dot(hidden_gradient) * self.learning_rate
        self.bias_hidden += (
            np.sum(hidden_gradient, axis=0, keepdims=True) * self.learning_rate
        )

    def train(self, x, y, epochs=10000):
        """Train the network."""
        for epoch in range(epochs):
            output = self.feedforward(x)
            self.backpropagation(x, y, output)
            if epoch % 1000 == 0:
                loss = np.mean(np.square(y - output))
                print(f"Epoch {epoch}, Loss: {loss}")

    def predict(self, x):
        """Make predictions."""
        return self.feedforward(x)


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
