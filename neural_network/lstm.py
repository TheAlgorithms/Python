import numpy as np
from numpy.random import Generator

"""
Author : Shashank Tyagi
Email : tyagishashank118@gmail.com
Description : This is a simple implementation of Long Short-Term Memory (LSTM)
networks in Python.
"""


class LongShortTermMemory:
    def __init__(
        self,
        input_data: str,
        hidden_layer_size: int = 25,
        training_epochs: int = 100,
        learning_rate: float = 0.05,
    ) -> None:
        """
        Initialize the LSTM network with the given data and hyperparameters.

        :param input_data: The input data as a string.
        :param hidden_layer_size: The number of hidden units in the LSTM layer.
        :param training_epochs: The number of training epochs.
        :param learning_rate: The learning rate.

        >>> lstm = LongShortTermMemory("abcde", hidden_layer_size=10, training_epochs=5,
        ... learning_rate=0.01)
        >>> isinstance(lstm, LongShortTermMemory)
        True
        >>> lstm.hidden_layer_size
        10
        >>> lstm.training_epochs
        5
        >>> lstm.learning_rate
        0.01
        """

        self.input_data: str = input_data.lower()
        self.hidden_layer_size: int = hidden_layer_size
        self.training_epochs: int = training_epochs
        self.learning_rate: float = learning_rate

        self.unique_chars: set = set(self.input_data)
        self.data_length: int = len(self.input_data)
        self.vocabulary_size: int = len(self.unique_chars)

        # print(
        #    f"Data length: {self.data_length}, Vocabulary size: {self.vocabulary_size}"
        # )

        self.char_to_index: dict[str, int] = {
            c: i for i, c in enumerate(self.unique_chars)
        }
        self.index_to_char: dict[int, str] = dict(enumerate(self.unique_chars))

        self.input_sequence: str = self.input_data[:-1]
        self.target_sequence: str = self.input_data[1:]
        self.random_generator: Generator = np.random.default_rng()

        # Initialize attributes used in reset method
        self.combined_inputs: dict[int, np.ndarray] = {}
        self.hidden_states: dict[int, np.ndarray] = {
            -1: np.zeros((self.hidden_layer_size, 1))
        }
        self.cell_states: dict[int, np.ndarray] = {
            -1: np.zeros((self.hidden_layer_size, 1))
        }
        self.forget_gate_activations: dict[int, np.ndarray] = {}
        self.input_gate_activations: dict[int, np.ndarray] = {}
        self.cell_state_candidates: dict[int, np.ndarray] = {}
        self.output_gate_activations: dict[int, np.ndarray] = {}
        self.network_outputs: dict[int, np.ndarray] = {}

        self.initialize_weights()

    def one_hot_encode(self, char: str) -> np.ndarray:
        """
        One-hot encode a character.

        :param char: The character to encode.
        :return: A one-hot encoded vector.

        >>> lstm = LongShortTermMemory("abcde" * 50, hidden_layer_size=10)
        >>> output = lstm.one_hot_encode('a')
        >>> isinstance(output, np.ndarray)
        True
        >>> output.shape
        (5, 1)
        >>> output = lstm.one_hot_encode('c')
        >>> isinstance(output, np.ndarray)
        True
        >>> output.shape
        (5, 1)
        """
        vector = np.zeros((self.vocabulary_size, 1))
        vector[self.char_to_index[char]] = 1
        return vector

    def initialize_weights(self) -> None:
        """
        Initialize the weights and biases for the LSTM network.

        This method initializes the forget gate, input gate,
        cell candidate, and output gate weights
        and biases, as well as the output layer weights and biases.
        It ensures that the weights
        and biases have the correct shapes.

        >>> lstm = LongShortTermMemory("abcde" * 50, hidden_layer_size=10)

        # Check the shapes of the weights and biases after initialization
        >>> lstm.initialize_weights()

        # Forget gate weights and bias
        >>> lstm.forget_gate_weights.shape
        (10, 15)
        >>> lstm.forget_gate_bias.shape
        (10, 1)

        # Input gate weights and bias
        >>> lstm.input_gate_weights.shape
        (10, 15)
        >>> lstm.input_gate_bias.shape
        (10, 1)

        # Cell candidate weights and bias
        >>> lstm.cell_candidate_weights.shape
        (10, 15)
        >>> lstm.cell_candidate_bias.shape
        (10, 1)

        # Output gate weights and bias
        >>> lstm.output_gate_weights.shape
        (10, 15)
        >>> lstm.output_gate_bias.shape
        (10, 1)

        # Output layer weights and bias
        >>> lstm.output_layer_weights.shape
        (5, 10)
        >>> lstm.output_layer_bias.shape
        (5, 1)
        """
        self.forget_gate_weights = self.init_weights(
            self.vocabulary_size + self.hidden_layer_size, self.hidden_layer_size
        )
        self.forget_gate_bias = np.zeros((self.hidden_layer_size, 1))

        self.input_gate_weights = self.init_weights(
            self.vocabulary_size + self.hidden_layer_size, self.hidden_layer_size
        )
        self.input_gate_bias = np.zeros((self.hidden_layer_size, 1))

        self.cell_candidate_weights = self.init_weights(
            self.vocabulary_size + self.hidden_layer_size, self.hidden_layer_size
        )
        self.cell_candidate_bias = np.zeros((self.hidden_layer_size, 1))

        self.output_gate_weights = self.init_weights(
            self.vocabulary_size + self.hidden_layer_size, self.hidden_layer_size
        )
        self.output_gate_bias = np.zeros((self.hidden_layer_size, 1))

        self.output_layer_weights = self.init_weights(
            self.hidden_layer_size, self.vocabulary_size
        )
        self.output_layer_bias = np.zeros((self.vocabulary_size, 1))

    def init_weights(self, input_dim: int, output_dim: int) -> np.ndarray:
        """
        Initialize weights with random values.

        :param input_dim: The input dimension.
        :param output_dim: The output dimension.
        :return: A matrix of initialized weights.

        Example:
        >>> lstm = LongShortTermMemory("abcde" * 50, hidden_layer_size=10)
        >>> weights = lstm.init_weights(5, 10)
        >>> isinstance(weights, np.ndarray)
        True
        >>> weights.shape
        (10, 5)
        """
        return self.random_generator.uniform(-1, 1, (output_dim, input_dim)) * np.sqrt(
            6 / (input_dim + output_dim)
        )

    def sigmoid(self, input_array: np.ndarray, derivative: bool = False) -> np.ndarray:
        """
        Sigmoid activation function.

        :param x: The input array.
        :param derivative: Whether to compute the derivative.
        :return: The sigmoid activation or its derivative.

        >>> lstm = LongShortTermMemory("abcde" * 50, hidden_layer_size=10)
        >>> output = lstm.sigmoid(np.array([[1, 2, 3]]))
        >>> isinstance(output, np.ndarray)
        True
        >>> np.round(output, 3)
        array([[0.731, 0.881, 0.953]])
        >>> derivative_output = lstm.sigmoid(output, derivative=True)
        >>> np.round(derivative_output, 3)
        array([[0.197, 0.105, 0.045]])
        """
        if derivative:
            return input_array * (1 - input_array)
        return 1 / (1 + np.exp(-input_array))

    def tanh(self, input_array: np.ndarray, derivative: bool = False) -> np.ndarray:
        """
        Tanh activation function.

        :param x: The input array.
        :param derivative: Whether to compute the derivative.
        :return: The tanh activation or its derivative.

        >>> lstm = LongShortTermMemory("abcde" * 50, hidden_layer_size=10)
        >>> output = lstm.tanh(np.array([[1, 2, 3]]))
        >>> isinstance(output, np.ndarray)
        True
        >>> np.round(output, 3)
        array([[0.762, 0.964, 0.995]])
        >>> derivative_output = lstm.tanh(output, derivative=True)
        >>> np.round(derivative_output, 3)
        array([[0.42 , 0.071, 0.01 ]])
        """
        if derivative:
            return 1 - input_array**2
        return np.tanh(input_array)

    def softmax(self, input_array: np.ndarray) -> np.ndarray:
        """
        Softmax activation function.

        :param x: The input array.
        :return: The softmax activation.

        >>> lstm = LongShortTermMemory("abcde" * 50, hidden_layer_size=10)
        >>> output = lstm.softmax(np.array([1, 2, 3]))
        >>> isinstance(output, np.ndarray)
        True
        >>> np.round(output, 3)
        array([0.09 , 0.245, 0.665])
        """
        exp_x = np.exp(input_array - np.max(input_array))
        return exp_x / exp_x.sum(axis=0)

    def reset_network_state(self) -> None:
        """
        Reset the LSTM network states.

        Resets the internal states of the LSTM network, including the combined inputs,
        hidden states, cell states, gate activations, and network outputs.

        >>> lstm = LongShortTermMemory("abcde" * 50, hidden_layer_size=10)
        >>> lstm.reset_network_state()
        >>> lstm.hidden_states[-1].shape == (10, 1)
        True
        >>> lstm.cell_states[-1].shape == (10, 1)
        True
        >>> lstm.combined_inputs == {}
        True
        >>> lstm.network_outputs == {}
        True
        """
        self.combined_inputs = {}
        self.hidden_states = {-1: np.zeros((self.hidden_layer_size, 1))}
        self.cell_states = {-1: np.zeros((self.hidden_layer_size, 1))}
        self.forget_gate_activations = {}
        self.input_gate_activations = {}
        self.cell_state_candidates = {}
        self.output_gate_activations = {}
        self.network_outputs = {}

    def forward_pass(self, inputs: list[np.ndarray]) -> list[np.ndarray]:
        """
        Perform a forward pass through the LSTM network for the given inputs.

        :param inputs: A list of input arrays (sequences).
        :return: A list of network outputs.

        Example:
        >>> lstm = LongShortTermMemory("abcde" * 50, hidden_layer_size=10)
        >>> inputs = [np.random.rand(5, 1) for _ in range(5)]
        >>> outputs = lstm.forward_pass(inputs)
        >>> len(outputs) == len(inputs)
        True
        """
        self.reset_network_state()

        outputs = []
        for t in range(len(inputs)):
            self.combined_inputs[t] = np.concatenate(
                (self.hidden_states[t - 1], inputs[t])
            )

            self.forget_gate_activations[t] = self.sigmoid(
                np.dot(self.forget_gate_weights, self.combined_inputs[t])
                + self.forget_gate_bias
            )
            self.input_gate_activations[t] = self.sigmoid(
                np.dot(self.input_gate_weights, self.combined_inputs[t])
                + self.input_gate_bias
            )
            self.cell_state_candidates[t] = self.tanh(
                np.dot(self.cell_candidate_weights, self.combined_inputs[t])
                + self.cell_candidate_bias
            )
            self.output_gate_activations[t] = self.sigmoid(
                np.dot(self.output_gate_weights, self.combined_inputs[t])
                + self.output_gate_bias
            )

            self.cell_states[t] = (
                self.forget_gate_activations[t] * self.cell_states[t - 1]
                + self.input_gate_activations[t] * self.cell_state_candidates[t]
            )
            self.hidden_states[t] = self.output_gate_activations[t] * self.tanh(
                self.cell_states[t]
            )

            outputs.append(
                np.dot(self.output_layer_weights, self.hidden_states[t])
                + self.output_layer_bias
            )

        return outputs

    def backward_pass(self, errors: list[np.ndarray], inputs: list[np.ndarray]) -> None:
        """
        Perform the backward pass for the LSTM model, adjusting weights and biases.

        :param errors: A list of errors computed from the output layer.
        :param inputs: A list of input one-hot encoded vectors.

        Example:
        >>> lstm = LongShortTermMemory("abcde" * 50, hidden_layer_size=10)
        >>> inputs = [lstm.one_hot_encode(char) for char in lstm.input_sequence]
        >>> predictions = lstm.forward_pass(inputs)
        >>> errors = [-lstm.softmax(predictions[t]) for t in range(len(predictions))]
        >>> for t in range(len(predictions)):
        ...     errors[t][lstm.char_to_index[lstm.target_sequence[t]]] += 1
        >>> lstm.backward_pass(errors, inputs)  # Should run without any errors
        """
        d_forget_gate_weights, d_forget_gate_bias = 0, 0
        d_input_gate_weights, d_input_gate_bias = 0, 0
        d_cell_candidate_weights, d_cell_candidate_bias = 0, 0
        d_output_gate_weights, d_output_gate_bias = 0, 0
        d_output_layer_weights, d_output_layer_bias = 0, 0

        d_next_hidden, d_next_cell = (
            np.zeros_like(self.hidden_states[0]),
            np.zeros_like(self.cell_states[0]),
        )

        for t in reversed(range(len(inputs))):
            error = errors[t]

            d_output_layer_weights += np.dot(error, self.hidden_states[t].T)
            d_output_layer_bias += error

            d_hidden = np.dot(self.output_layer_weights.T, error) + d_next_hidden

            d_output_gate = (
                self.tanh(self.cell_states[t])
                * d_hidden
                * self.sigmoid(self.output_gate_activations[t], derivative=True)
            )
            d_output_gate_weights += np.dot(d_output_gate, self.combined_inputs[t].T)
            d_output_gate_bias += d_output_gate

            d_cell = (
                self.tanh(self.tanh(self.cell_states[t]), derivative=True)
                * self.output_gate_activations[t]
                * d_hidden
                + d_next_cell
            )

            d_forget_gate = (
                d_cell
                * self.cell_states[t - 1]
                * self.sigmoid(self.forget_gate_activations[t], derivative=True)
            )
            d_forget_gate_weights += np.dot(d_forget_gate, self.combined_inputs[t].T)
            d_forget_gate_bias += d_forget_gate

            d_input_gate = (
                d_cell
                * self.cell_state_candidates[t]
                * self.sigmoid(self.input_gate_activations[t], derivative=True)
            )
            d_input_gate_weights += np.dot(d_input_gate, self.combined_inputs[t].T)
            d_input_gate_bias += d_input_gate

            d_cell_candidate = (
                d_cell
                * self.input_gate_activations[t]
                * self.tanh(self.cell_state_candidates[t], derivative=True)
            )
            d_cell_candidate_weights += np.dot(
                d_cell_candidate, self.combined_inputs[t].T
            )
            d_cell_candidate_bias += d_cell_candidate

            d_combined_input = (
                np.dot(self.forget_gate_weights.T, d_forget_gate)
                + np.dot(self.input_gate_weights.T, d_input_gate)
                + np.dot(self.cell_candidate_weights.T, d_cell_candidate)
                + np.dot(self.output_gate_weights.T, d_output_gate)
            )

            d_next_hidden = d_combined_input[: self.hidden_layer_size, :]
            d_next_cell = self.forget_gate_activations[t] * d_cell

        for d in (
            d_forget_gate_weights,
            d_forget_gate_bias,
            d_input_gate_weights,
            d_input_gate_bias,
            d_cell_candidate_weights,
            d_cell_candidate_bias,
            d_output_gate_weights,
            d_output_gate_bias,
            d_output_layer_weights,
            d_output_layer_bias,
        ):
            np.clip(d, -1, 1, out=d)

        self.forget_gate_weights += d_forget_gate_weights * self.learning_rate
        self.forget_gate_bias += d_forget_gate_bias * self.learning_rate
        self.input_gate_weights += d_input_gate_weights * self.learning_rate
        self.input_gate_bias += d_input_gate_bias * self.learning_rate
        self.cell_candidate_weights += d_cell_candidate_weights * self.learning_rate
        self.cell_candidate_bias += d_cell_candidate_bias * self.learning_rate
        self.output_gate_weights += d_output_gate_weights * self.learning_rate
        self.output_gate_bias += d_output_gate_bias * self.learning_rate
        self.output_layer_weights += d_output_layer_weights * self.learning_rate
        self.output_layer_bias += d_output_layer_bias * self.learning_rate

    def train(self) -> None:
        """
        Train the LSTM model.

        Example:
        >>> lstm = LongShortTermMemory("abcde" * 50, hidden_layer_size=10)
        >>> lstm.train()
        """
        inputs = [self.one_hot_encode(char) for char in self.input_sequence]

        for _ in range(self.training_epochs):
            predictions = self.forward_pass(inputs)

            errors = []
            for t in range(len(predictions)):
                errors.append(-self.softmax(predictions[t]))
                errors[-1][self.char_to_index[self.target_sequence[t]]] += 1

            self.backward_pass(errors, inputs)

    def test(self) -> str:
        """
        Test the LSTM model.

        Returns:
            str: The output predictions.

        Example:
        >>> lstm = LongShortTermMemory("abcde" * 50, hidden_layer_size=10)
        >>> output = lstm.test()
        >>> isinstance(output, str)
        True
        >>> len(output) == len(lstm.input_sequence)
        True
        """
        accuracy = 0
        probabilities = self.forward_pass(
            [self.one_hot_encode(char) for char in self.input_sequence]
        )

        output = ""
        for t in range(len(self.target_sequence)):
            # Apply softmax to get probabilities for predictions
            probs = self.softmax(probabilities[t].reshape(-1))
            prediction_index = self.random_generator.choice(
                self.vocabulary_size, p=probs
            )
            prediction = self.index_to_char[prediction_index]

            output += prediction

            # Calculate accuracy
            if prediction == self.target_sequence[t]:
                accuracy += 1

        # print(f"Ground Truth:\n{self.target_sequence}\n")
        # print(f"Predictions:\n{output}\n")
        # print(f"Accuracy: {round(accuracy * 100 / len(self.input_sequence), 2)}%")

        return output


if __name__ == "__main__":
    sample_data = """Long Short-Term Memory (LSTM) networks are a type
         of recurrent neural network (RNN) capable of learning "
        "order dependence in sequence prediction problems.
         This behavior is required in complex problem domains like "
        "machine translation, speech recognition, and more.
        LSTMs were introduced by Hochreiter and Schmidhuber in 1997, and were
        refined and "
        "popularized by many people in following work."""
    import doctest

    doctest.testmod()

    # lstm_model = LongShortTermMemory(
    #     input_data=sample_data,
    #     hidden_layer_size=25,
    #     training_epochs=100,
    #     learning_rate=0.05,
    # )

    # #### Training #####
    # lstm_model.train()

    # #### Testing #####
    # lstm_model.test()
