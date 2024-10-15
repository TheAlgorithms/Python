"""
Name - - LSTM - Long Short-Term Memory Network For Sequence Prediction
Goal - - Predict sequences of data
Detail: Total 3 layers neural network
* Input layer
* LSTM layer
* Output layer
Author: Shashank Tyagi
Github: LEVII007
Date: [Current Date]
"""

# from typing import dict, list

import numpy as np
from numpy.random import Generator


class LSTM:
    def __init__(
        self, data: str, hidden_dim: int = 25, epochs: int = 10, lr: float = 0.05
    ) -> None:
        """
        Initialize the LSTM network with the given data and hyperparameters.

        :param data: The input data as a string.
        :param hidden_dim: The number of hidden units in the LSTM layer.
        :param epochs: The number of training epochs.
        :param lr: The learning rate.
        """
        """
        Test the LSTM model.

        >>> lstm = LSTM(data="abcde" * 50, hidden_dim=10, epochs=5, lr=0.01)
        >>> lstm.train()
        >>> predictions = lstm.test()
        >>> len(predictions) > 0
        True
        """
        self.data: str = data.lower()
        self.hidden_dim: int = hidden_dim
        self.epochs: int = epochs
        self.lr: float = lr

        self.chars: set = set(self.data)
        self.data_size: int = len(self.data)
        self.char_size: int = len(self.chars)

        print(f"Data size: {self.data_size}, Char Size: {self.char_size}")

        self.char_to_idx: dict[str, int] = {c: i for i, c in enumerate(self.chars)}
        self.idx_to_char: dict[int, str] = dict(enumerate(self.chars))

        self.train_X: str = self.data[:-1]
        self.train_y: str = self.data[1:]
        self.rng: Generator = np.random.default_rng()

        # Initialize attributes used in reset method
        self.concat_inputs: dict[int, np.ndarray] = {}
        self.hidden_states: dict[int, np.ndarray] = {-1: np.zeros((self.hidden_dim, 1))}
        self.cell_states: dict[int, np.ndarray] = {-1: np.zeros((self.hidden_dim, 1))}
        self.activation_outputs: dict[int, np.ndarray] = {}
        self.candidate_gates: dict[int, np.ndarray] = {}
        self.output_gates: dict[int, np.ndarray] = {}
        self.forget_gates: dict[int, np.ndarray] = {}
        self.input_gates: dict[int, np.ndarray] = {}
        self.outputs: dict[int, np.ndarray] = {}

        self.initialize_weights()

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

        self.wy: np.ndarray = self.init_weights(self.hidden_dim, self.char_size)
        self.by: np.ndarray = np.zeros((self.char_size, 1))

    def init_weights(self, input_dim: int, output_dim: int) -> np.ndarray:
        """
        Initialize weights with random values.

        :param input_dim: The input dimension.
        :param output_dim: The output dimension.
        :return: A matrix of initialized weights.
        """
        return self.rng.uniform(-1, 1, (output_dim, input_dim)) * np.sqrt(
            6 / (input_dim + output_dim)
        )

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

    def forward(self, inputs: list[np.ndarray]) -> list[np.ndarray]:
        """
        Perform forward propagation through the LSTM network.

        :param inputs: The input data as a list of one-hot encoded vectors.
        :return: The outputs of the network.
        """
        """
        Forward pass through the LSTM network.

        >>> lstm = LSTM(data="abcde", hidden_dim=10, epochs=1, lr=0.01)
        >>> inputs = [lstm.one_hot_encode(char) for char in lstm.train_X]
        >>> outputs = lstm.forward(inputs)
        >>> len(outputs) == len(inputs)
        True
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

    def backward(self, errors: list[np.ndarray], inputs: list[np.ndarray]) -> None:
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

            d_wy += np.dot(error, self.hidden_states[t].T)
            d_by += error

            d_hs = np.dot(self.wy.T, error) + dh_next

            d_o = (
                self.tanh(self.cell_states[t])
                * d_hs
                * self.sigmoid(self.output_gates[t], derivative=True)
            )
            d_wo += np.dot(d_o, self.concat_inputs[t].T)
            d_bo += d_o

            d_cs = (
                self.tanh(self.tanh(self.cell_states[t]), derivative=True)
                * self.output_gates[t]
                * d_hs
                + dc_next
            )

            d_f = (
                d_cs
                * self.cell_states[t - 1]
                * self.sigmoid(self.forget_gates[t], derivative=True)
            )
            d_wf += np.dot(d_f, self.concat_inputs[t].T)
            d_bf += d_f

            d_i = (
                d_cs
                * self.candidate_gates[t]
                * self.sigmoid(self.input_gates[t], derivative=True)
            )
            d_wi += np.dot(d_i, self.concat_inputs[t].T)
            d_bi += d_i

            d_c = (
                d_cs
                * self.input_gates[t]
                * self.tanh(self.candidate_gates[t], derivative=True)
            )
            d_wc += np.dot(d_c, self.concat_inputs[t].T)
            d_bc += d_c

            d_z = (
                np.dot(self.wf.T, d_f)
                + np.dot(self.wi.T, d_i)
                + np.dot(self.wc.T, d_c)
                + np.dot(self.wo.T, d_o)
            )

            dh_next = d_z[: self.hidden_dim, :]
            dc_next = self.forget_gates[t] * d_cs

        for d in (d_wf, d_bf, d_wi, d_bi, d_wc, d_bc, d_wo, d_bo, d_wy, d_by):
            np.clip(d, -1, 1, out=d)

        self.wf += d_wf * self.lr
        self.bf += d_bf * self.lr
        self.wi += d_wi * self.lr
        self.bi += d_bi * self.lr
        self.wc += d_wc * self.lr
        self.bc += d_bc * self.lr
        self.wo += d_wo * self.lr
        self.bo += d_bo * self.lr
        self.wy += d_wy * self.lr
        self.by += d_by * self.lr

    def train(self) -> None:
        """
        Train the LSTM network on the input data.
        """
        """
        Train the LSTM network on the input data.

        >>> lstm = LSTM(data="abcde" * 50, hidden_dim=10, epochs=5, lr=0.01)
        >>> lstm.train()
        >>> lstm.losses[-1] < lstm.losses[0]
        True
        """
        inputs = [self.one_hot_encode(char) for char in self.train_X]

        for _ in range(self.epochs):
            predictions = self.forward(inputs)

            errors = []
            for t in range(len(predictions)):
                errors.append(-self.softmax(predictions[t]))
                errors[-1][self.char_to_idx[self.train_y[t]]] += 1

            self.backward(errors, inputs)

    def test(self) -> None:
        """
        Test the trained LSTM network on the input data and print the accuracy.
        """
        """
        Test the LSTM model.

        >>> lstm = LSTM(data="abcde" * 50, hidden_dim=10, epochs=5, lr=0.01)
        >>> lstm.train()
        >>> predictions = lstm.test()
        >>> len(predictions) > 0
        True
        """
        accuracy = 0
        probabilities = self.forward(
            [self.one_hot_encode(char) for char in self.train_X]
        )

        output = ""
        for t in range(len(self.train_y)):
            probs = self.softmax(probabilities[t].reshape(-1))
            prediction_index = self.rng.choice(self.char_size, p=probs)
            prediction = self.idx_to_char[prediction_index]

            output += prediction

            if prediction == self.train_y[t]:
                accuracy += 1

        print(f"Ground Truth:\n{self.train_y}\n")
        print(f"Predictions:\n{output}\n")

        print(f"Accuracy: {round(accuracy * 100 / len(self.train_X), 2)}%")


if __name__ == "__main__":
    data = """Long Short-Term Memory (LSTM) networks are a type
         of recurrent neural network (RNN) capable of learning "
        "order dependence in sequence prediction problems.
         This behavior is required in complex problem domains like "
        "machine translation, speech recognition, and more.
        iter and Schmidhuber in 1997, and were refined and "
        "popularized by many people in following work."""
    import doctest

    doctest.testmod()

    # lstm = LSTM(data=data, hidden_dim=25, epochs=10, lr=0.05)

    ##### Training #####
    # lstm.train()

    ##### Testing #####
    # lstm.test()
