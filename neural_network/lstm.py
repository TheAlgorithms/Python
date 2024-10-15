"""
Name - - LSTM - Long Short-Term Memory Network For Sequence Prediction
Goal - - Predict sequences of data
Detail: Total 3 layers neural network
* Input layer
* LSTM layer
* Output layer
Author: Shashank Tyagi
Github: LEVII007
link : https://www.kaggle.com/code/navjindervirdee/lstm-neural-network-from-scratch
"""

##### Explanation #####
# This script implements a Long Short-Term Memory (LSTM) network to learn
# and predict sequences of characters.
# It uses numpy for numerical operations and tqdm for progress visualization.

# The data is a paragraph about LSTM, converted to lowercase and split into
# characters. Each character is one-hot encoded for training.

# The LSTM class initializes weights and biases for the forget, input, candidate,
# and output gates. It also initializes weights and biases for the final output layer.

# The forward method performs forward propagation through the LSTM network,
# computing hidden and cell states. It uses sigmoid and tanh activation
# functions for the gates and cell states.

# The backward method performs backpropagation through time, computing gradients
# for the weights and biases. It updates the weights and biases using
# the computed gradients and the learning rate.

# The train method trains the LSTM network on the input data for a specified
# number of epochs. It uses one-hot encoded inputs and computes errors
# using the softmax function.

# The test method evaluates the trained LSTM network on the input data,
# computing accuracy based on predictions.

# The script initializes the LSTM network with specified hyperparameters
# and trains it on the input data. Finally, it tests the trained network
# and prints the accuracy of the predictions.

##### Imports #####
from tqdm import tqdm
import numpy as np


class LSTM:
    def __init__(
        self, data: str, hidden_dim: int = 25, epochs: int = 1000, lr: float = 0.05
    ) -> None:
        """
        Initialize the LSTM network with the given data and hyperparameters.

        :param data: The input data as a string.
        :param hidden_dim: The number of hidden units in the LSTM layer.
        :param epochs: The number of training epochs.
        :param lr: The learning rate.
        """
        self.data = data.lower()
        self.hidden_dim = hidden_dim
        self.epochs = epochs
        self.lr = lr

        self.chars = set(self.data)
        self.data_size, self.char_size = len(self.data), len(self.chars)

        print(f"Data size: {self.data_size}, Char Size: {self.char_size}")

        self.char_to_idx = {c: i for i, c in enumerate(self.chars)}
        self.idx_to_char = {i: c for i, c in enumerate(self.chars)}

        self.train_X, self.train_y = self.data[:-1], self.data[1:]

        self.initialize_weights()

    ##### Helper Functions #####
    def one_hot_encode(self, char: str) -> np.ndarray:
        """
        One-hot encode a character.

        :param char: The character to encode.
        :return: A one-hot encoded vector.
        """
        vector = np.zeros((self.char_size, 1))
        vector[self.char_to_idx[char]] = 1
        return vector

    def initialize_weights(self) -> None:
        """
        Initialize the weights and biases for the LSTM network.
        """
        self.wf = self.init_weights(self.char_size + self.hidden_dim, self.hidden_dim)
        self.bf = np.zeros((self.hidden_dim, 1))

        self.wi = self.init_weights(self.char_size + self.hidden_dim, self.hidden_dim)
        self.bi = np.zeros((self.hidden_dim, 1))

        self.wc = self.init_weights(self.char_size + self.hidden_dim, self.hidden_dim)
        self.bc = np.zeros((self.hidden_dim, 1))

        self.wo = self.init_weights(self.char_size + self.hidden_dim, self.hidden_dim)
        self.bo = np.zeros((self.hidden_dim, 1))

        self.wy = self.init_weights(self.hidden_dim, self.char_size)
        self.by = np.zeros((self.char_size, 1))

    def init_weights(self, input_dim: int, output_dim: int) -> np.ndarray:
        """
        Initialize weights with random values.

        :param input_dim: The input dimension.
        :param output_dim: The output dimension.
        :return: A matrix of initialized weights.
        """
        return np.random.uniform(-1, 1, (output_dim, input_dim)) * np.sqrt(
            6 / (input_dim + output_dim)
        )

    ##### Activation Functions #####
    def sigmoid(self, x: np.ndarray, derivative: bool = False) -> np.ndarray:
        """
        Sigmoid activation function.

        :param x: The input array.
        :param derivative: Whether to compute the derivative.
        :return: The sigmoid activation or its derivative.
        """
        if derivative:
            return x * (1 - x)
        return 1 / (1 + np.exp(-x))

    def tanh(self, x: np.ndarray, derivative: bool = False) -> np.ndarray:
        """
        Tanh activation function.

        :param x: The input array.
        :param derivative: Whether to compute the derivative.
        :return: The tanh activation or its derivative.
        """
        if derivative:
            return 1 - x**2
        return np.tanh(x)

    def softmax(self, x: np.ndarray) -> np.ndarray:
        """
        Softmax activation function.

        :param x: The input array.
        :return: The softmax activation.
        """
        exp_x = np.exp(x - np.max(x))
        return exp_x / exp_x.sum(axis=0)

    ##### LSTM Network Methods #####
    def reset(self) -> None:
        """
        Reset the LSTM network states.
        """
        self.concat_inputs = {}

        self.hidden_states = {-1: np.zeros((self.hidden_dim, 1))}
        self.cell_states = {-1: np.zeros((self.hidden_dim, 1))}

        self.activation_outputs = {}
        self.candidate_gates = {}
        self.output_gates = {}
        self.forget_gates = {}
        self.input_gates = {}
        self.outputs = {}

    def forward(self, inputs: list) -> list:
        """
        Perform forward propagation through the LSTM network.

        :param inputs: The input data as a list of one-hot encoded vectors.
        :return: The outputs of the network.
        """
        self.reset()

        outputs = []
        for t in range(len(inputs)):
            self.concat_inputs[t] = np.concatenate(
                (self.hidden_states[t - 1], inputs[t])
            )

            self.forget_gates[t] = self.sigmoid(
                np.dot(self.wf, self.concat_inputs[t]) + self.bf
            )
            self.input_gates[t] = self.sigmoid(
                np.dot(self.wi, self.concat_inputs[t]) + self.bi
            )
            self.candidate_gates[t] = self.tanh(
                np.dot(self.wc, self.concat_inputs[t]) + self.bc
            )
            self.output_gates[t] = self.sigmoid(
                np.dot(self.wo, self.concat_inputs[t]) + self.bo
            )

            self.cell_states[t] = (
                self.forget_gates[t] * self.cell_states[t - 1]
                + self.input_gates[t] * self.candidate_gates[t]
            )
            self.hidden_states[t] = self.output_gates[t] * self.tanh(
                self.cell_states[t]
            )

            outputs.append(np.dot(self.wy, self.hidden_states[t]) + self.by)

        return outputs

    def backward(self, errors: list, inputs: list) -> None:
        """
        Perform backpropagation through time to compute gradients and update weights.

        :param errors: The errors at each time step.
        :param inputs: The input data as a list of one-hot encoded vectors.
        """
        d_wf, d_bf = 0, 0
        d_wi, d_bi = 0, 0
        d_wc, d_bc = 0, 0
        d_wo, d_bo = 0, 0
        d_wy, d_by = 0, 0

        dh_next, dc_next = (
            np.zeros_like(self.hidden_states[0]),
            np.zeros_like(self.cell_states[0]),
        )
        for t in reversed(range(len(inputs))):
            error = errors[t]

            # Final Gate Weights and Biases Errors
            d_wy += np.dot(error, self.hidden_states[t].T)
            d_by += error

            # Hidden State Error
            d_hs = np.dot(self.wy.T, error) + dh_next

            # Output Gate Weights and Biases Errors
            d_o = (
                self.tanh(self.cell_states[t])
                * d_hs
                * self.sigmoid(self.output_gates[t], derivative=True)
            )
            d_wo += np.dot(d_o, inputs[t].T)
            d_bo += d_o

            # Cell State Error
            d_cs = (
                self.tanh(self.tanh(self.cell_states[t]), derivative=True)
                * self.output_gates[t]
                * d_hs
                + dc_next
            )

            # Forget Gate Weights and Biases Errors
            d_f = (
                d_cs
                * self.cell_states[t - 1]
                * self.sigmoid(self.forget_gates[t], derivative=True)
            )
            d_wf += np.dot(d_f, inputs[t].T)
            d_bf += d_f

            # Input Gate Weights and Biases Errors
            d_i = (
                d_cs
                * self.candidate_gates[t]
                * self.sigmoid(self.input_gates[t], derivative=True)
            )
            d_wi += np.dot(d_i, inputs[t].T)
            d_bi += d_i

            # Candidate Gate Weights and Biases Errors
            d_c = (
                d_cs
                * self.input_gates[t]
                * self.tanh(self.candidate_gates[t], derivative=True)
            )
            d_wc += np.dot(d_c, inputs[t].T)
            d_bc += d_c

            # Update the next hidden and cell state errors
            dh_next = (
                np.dot(self.wf.T, d_f)
                + np.dot(self.wi.T, d_i)
                + np.dot(self.wo.T, d_o)
                + np.dot(self.wc.T, d_c)
            )
            dc_next = d_cs * self.forget_gates[t]

        # Apply gradients to weights and biases
        for param, grad in zip(
            [self.wf, self.wi, self.wc, self.wo, self.wy],
            [d_wf, d_wi, d_wc, d_wo, d_wy],
        ):
            param -= self.lr * grad

        for param, grad in zip(
            [self.bf, self.bi, self.bc, self.bo, self.by],
            [d_bf, d_bi, d_bc, d_bo, d_by],
        ):
            param -= self.lr * grad

    def train(self) -> None:
        """
        Train the LSTM network on the input data for a specified number of epochs.
        """
        for epoch in tqdm(range(self.epochs)):
            inputs = [self.one_hot_encode(char) for char in self.train_X]
            targets = [self.one_hot_encode(char) for char in self.train_y]

            # Forward pass
            outputs = self.forward(inputs)

            # Compute error at each time step
            errors = [output - target for output, target in zip(outputs, targets)]

            # Backward pass and weight updates
            self.backward(errors, inputs)

    def predict(self, inputs: list) -> str:
        """
        Predict the next character in the sequence.

        :param inputs: The input data as a list of one-hot encoded vectors.
        :return: The predicted character.
        """
        output = self.forward(inputs)[-1]
        return self.idx_to_char[np.argmax(self.softmax(output))]

    def test(self) -> None:
        """
        Test the LSTM network on the input data and compute accuracy.
        """
        inputs = [self.one_hot_encode(char) for char in self.train_X]
        correct_predictions = sum(
            self.idx_to_char[np.argmax(self.softmax(output))] == target
            for output, target in zip(self.forward(inputs), self.train_y)
        )

        accuracy = (correct_predictions / len(self.train_y)) * 100
        print(f"Accuracy: {accuracy:.2f}%")


if __name__ == "__main__":
    # Define the input data and hyperparameters
    data = "LSTM Neural Networks are designed to handle sequences of data.This is just rantom test data"
    # hidden_dim = 50
    # epochs = 1000
    # lr = 0.01

    # # Initialize and train the LSTM network
    # lstm = LSTM(data, hidden_dim, epochs, lr)
    # lstm.train()

    # # Test the LSTM network and compute accuracy
    # lstm.test()
