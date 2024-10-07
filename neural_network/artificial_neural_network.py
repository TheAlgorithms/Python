import numpy as np


class SimpleANN:
    """
    Simple Artificial Neural Network (ANN)

    - Feedforward Neural Network with 1 hidden layer and Sigmoid activation.
    - Uses Gradient Descent for backpropagation and Mean Squared Error (MSE)
      as the loss function.
    - Example demonstrates solving the XOR problem.
    """

<<<<<<< HEAD
    def __init__(self, input_size: int, hidden_size: int, output_size: int,
                 learning_rate: float = 0.1) -> None:
=======
    def __init__(
        self,
        input_size: int,
        hidden_size: int,
        output_size: int,
        learning_rate: float = 0.1,
    ) -> None:
>>>>>>> 79fed0c49891c60d2134ee45c6f6592c19f4cef5
        """
        Initialize the neural network with random weights and biases.

        Args:
            input_size (int): Number of input features.
            hidden_size (int): Number of neurons in the hidden layer.
            output_size (int): Number of neurons in the output layer.
            learning_rate (float): Learning rate for gradient descent.

        Example:
        >>> ann = SimpleANN(2, 2, 1)
        >>> isinstance(ann, SimpleANN)
        True
        """
        rng = np.random.default_rng()
        self.weights_input_hidden = rng.standard_normal((input_size, hidden_size))
        self.weights_hidden_output = rng.standard_normal((hidden_size, output_size))
        self.bias_hidden = np.zeros((1, hidden_size))
        self.bias_output = np.zeros((1, output_size))
        self.learning_rate = learning_rate

    def sigmoid(self, value: np.ndarray) -> np.ndarray:
        """
        Sigmoid activation function.

        Args:
            value (ndarray): Input value for activation.

        Returns:
            ndarray: Activated output using sigmoid function.

        Example:
        >>> ann = SimpleANN(2, 2, 1)
        >>> ann.sigmoid(np.array([0]))
        array([0.5])
        """
        return 1 / (1 + np.exp(-value))

    def sigmoid_derivative(self, sigmoid_output: np.ndarray) -> np.ndarray:
        """
        Derivative of the sigmoid function.

        Args:
            sigmoid_output (ndarray): Output after applying the sigmoid function.

        Returns:
            ndarray: Derivative of the sigmoid function.

        Example:
        >>> ann = SimpleANN(2, 2, 1)
        >>> output = ann.sigmoid(np.array([0]))  # Use input 0 for testing
        >>> ann.sigmoid_derivative(output)
        array([0.25])
        """
        return sigmoid_output * (1 - sigmoid_output)

    def feedforward(self, inputs: np.ndarray) -> np.ndarray:
        """
        Perform forward propagation through the network.

        Args:
            inputs (ndarray): Input features for the network.

        Returns:
            ndarray: Output from the network after feedforward pass.

        Example:
        >>> ann = SimpleANN(2, 2, 1)
        >>> inputs = np.array([[0, 0], [1, 1]])
        >>> ann.feedforward(inputs).shape
        (2, 1)
        """
        self.hidden_input = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = self.sigmoid(self.hidden_input)
        self.final_input = (
            np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        )
        self.final_output = self.sigmoid(self.final_input)
        return self.final_output

<<<<<<< HEAD
    def backpropagation(self, inputs: np.ndarray, targets: np.ndarray,
                       outputs: np.ndarray) -> None:
=======
    def backpropagation(
        self, inputs: np.ndarray, targets: np.ndarray, outputs: np.ndarray
    ) -> None:
>>>>>>> 79fed0c49891c60d2134ee45c6f6592c19f4cef5
        """
        Perform backpropagation to adjust the weights and biases.

        Args:
            inputs (ndarray): Input features.
            targets (ndarray): True output labels.
            outputs (ndarray): Output predicted by the network.

        Example:
        >>> ann = SimpleANN(2, 2, 1)
        >>> inputs = np.array([[0, 0], [1, 1]])
        >>> outputs = ann.feedforward(inputs)
        >>> targets = np.array([[0], [1]])
        >>> ann.backpropagation(inputs, targets, outputs)
        """
        error = targets - outputs
        output_gradient = error * self.sigmoid_derivative(outputs)
        hidden_error = output_gradient.dot(self.weights_hidden_output.T)
        hidden_gradient = hidden_error * self.sigmoid_derivative(self.hidden_output)

        self.weights_hidden_output += (
            self.hidden_output.T.dot(output_gradient) * self.learning_rate
        )
        self.bias_output += (
            np.sum(output_gradient, axis=0, keepdims=True) * self.learning_rate
        )

<<<<<<< HEAD
        self.weights_input_hidden += (
            inputs.T.dot(hidden_gradient) * self.learning_rate
        )
=======
        self.weights_input_hidden += inputs.T.dot(hidden_gradient) * self.learning_rate
>>>>>>> 79fed0c49891c60d2134ee45c6f6592c19f4cef5
        self.bias_hidden += (
            np.sum(hidden_gradient, axis=0, keepdims=True) * self.learning_rate
        )

<<<<<<< HEAD
    def train(self, inputs: np.ndarray, targets: np.ndarray,
              epochs: int = 10000, verbose: bool = False) -> None:
=======
    def train(
        self, inputs: np.ndarray, targets: np.ndarray, epochs: int = 10000
    ) -> None:
>>>>>>> 79fed0c49891c60d2134ee45c6f6592c19f4cef5
        """
        Train the neural network on the given input and target data.

        Args:
            inputs (ndarray): Input features for training.
            targets (ndarray): True labels for training.
            epochs (int): Number of training iterations.
            verbose (bool): Whether to print loss every 1000 epochs.

        Example:
        >>> ann = SimpleANN(2, 2, 1)
        >>> inputs = np.array([[0, 0], [1, 1]])
        >>> targets = np.array([[0], [1]])
        >>> ann.train(inputs, targets, epochs=1, verbose=False)
        """
        for epoch in range(epochs):
            outputs = self.feedforward(inputs)
            self.backpropagation(inputs, targets, outputs)
            if verbose and epoch % 1000 == 0:
                loss = np.mean(np.square(targets - outputs))
                print(f"Epoch {epoch}, Loss: {loss}")

    def predict(self, inputs: np.ndarray) -> np.ndarray:
        """
        Predict the output for new input data.

        Args:
            inputs (ndarray): Input data for prediction.

        Returns:
            ndarray: Predicted output from the network.

        Example:
        >>> ann = SimpleANN(2, 2, 1)
        >>> inputs = np.array([[0, 0], [1, 1]])
        >>> ann.predict(inputs).shape
        (2, 1)
        """
        return self.feedforward(inputs)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
