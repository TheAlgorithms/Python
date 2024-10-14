##### Explanation #####
# This script implements a Long Short-Term Memory (LSTM) network to learn and predict sequences of characters.
# It uses numpy for numerical operations and tqdm for progress visualization.

# The data is a paragraph about LSTM, converted to lowercase and split into characters.
# Each character is one-hot encoded for training.

# The LSTM class initializes weights and biases for the forget, input, candidate, and output gates.
# It also initializes weights and biases for the final output layer.

# The forward method performs forward propagation through the LSTM network, computing hidden and cell states.
# It uses sigmoid and tanh activation functions for the gates and cell states.

# The backward method performs backpropagation through time, computing gradients for the weights and biases.
# It updates the weights and biases using the computed gradients and the learning rate.

# The train method trains the LSTM network on the input data for a specified number of epochs.
# It uses one-hot encoded inputs and computes errors using the softmax function.

# The test method evaluates the trained LSTM network on the input data, computing accuracy based on predictions.

# The script initializes the LSTM network with specified hyperparameters and trains it on the input data.
# Finally, it tests the trained network and prints the accuracy of the predictions.

##### Data #####

##### Imports #####
from tqdm import tqdm
import numpy as np

class LSTM:
    def __init__(self, data, hidden_dim=25, epochs=1000, lr=0.05):
        self.data = data.lower()
        self.hidden_dim = hidden_dim
        self.epochs = epochs
        self.lr = lr

        self.chars = set(self.data)
        self.data_size, self.char_size = len(self.data), len(self.chars)

        print(f'Data size: {self.data_size}, Char Size: {self.char_size}')

        self.char_to_idx = {c: i for i, c in enumerate(self.chars)}
        self.idx_to_char = {i: c for i, c in enumerate(self.chars)}

        self.train_X, self.train_y = self.data[:-1], self.data[1:]

        self.initialize_weights()

    ##### Helper Functions #####
    def one_hot_encode(self, char):
        vector = np.zeros((self.char_size, 1))
        vector[self.char_to_idx[char]] = 1
        return vector

    def initialize_weights(self):
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

    def init_weights(self, input_dim, output_dim):
        return np.random.uniform(-1, 1, (output_dim, input_dim)) * np.sqrt(6 / (input_dim + output_dim))

    ##### Activation Functions #####
    def sigmoid(self, x, derivative=False):
        if derivative:
            return x * (1 - x)
        return 1 / (1 + np.exp(-x))

    def tanh(self, x, derivative=False):
        if derivative:
            return 1 - x ** 2
        return np.tanh(x)

    def softmax(self, x):
        exp_x = np.exp(x - np.max(x))
        return exp_x / exp_x.sum(axis=0)

    ##### LSTM Network Methods #####
    def reset(self):
        self.concat_inputs = {}

        self.hidden_states = {-1: np.zeros((self.hidden_dim, 1))}
        self.cell_states = {-1: np.zeros((self.hidden_dim, 1))}

        self.activation_outputs = {}
        self.candidate_gates = {}
        self.output_gates = {}
        self.forget_gates = {}
        self.input_gates = {}
        self.outputs = {}

    def forward(self, inputs):
        self.reset()

        outputs = []
        for t in range(len(inputs)):
            self.concat_inputs[t] = np.concatenate((self.hidden_states[t - 1], inputs[t]))

            self.forget_gates[t] = self.sigmoid(np.dot(self.wf, self.concat_inputs[t]) + self.bf)
            self.input_gates[t] = self.sigmoid(np.dot(self.wi, self.concat_inputs[t]) + self.bi)
            self.candidate_gates[t] = self.tanh(np.dot(self.wc, self.concat_inputs[t]) + self.bc)
            self.output_gates[t] = self.sigmoid(np.dot(self.wo, self.concat_inputs[t]) + self.bo)

            self.cell_states[t] = self.forget_gates[t] * self.cell_states[t - 1] + self.input_gates[t] * self.candidate_gates[t]
            self.hidden_states[t] = self.output_gates[t] * self.tanh(self.cell_states[t])

            outputs.append(np.dot(self.wy, self.hidden_states[t]) + self.by)

        return outputs

    def backward(self, errors, inputs):
        d_wf, d_bf = 0, 0
        d_wi, d_bi = 0, 0
        d_wc, d_bc = 0, 0
        d_wo, d_bo = 0, 0
        d_wy, d_by = 0, 0

        dh_next, dc_next = np.zeros_like(self.hidden_states[0]), np.zeros_like(self.cell_states[0])
        for t in reversed(range(len(inputs))):
            error = errors[t]

            # Final Gate Weights and Biases Errors
            d_wy += np.dot(error, self.hidden_states[t].T)
            d_by += error

            # Hidden State Error
            d_hs = np.dot(self.wy.T, error) + dh_next

            # Output Gate Weights and Biases Errors
            d_o = self.tanh(self.cell_states[t]) * d_hs * self.sigmoid(self.output_gates[t], derivative=True)
            d_wo += np.dot(d_o, inputs[t].T)
            d_bo += d_o

            # Cell State Error
            d_cs = self.tanh(self.tanh(self.cell_states[t]), derivative=True) * self.output_gates[t] * d_hs + dc_next

            # Forget Gate Weights and Biases Errors
            d_f = d_cs * self.cell_states[t - 1] * self.sigmoid(self.forget_gates[t], derivative=True)
            d_wf += np.dot(d_f, inputs[t].T)
            d_bf += d_f

            # Input Gate Weights and Biases Errors
            d_i = d_cs * self.candidate_gates[t] * self.sigmoid(self.input_gates[t], derivative=True)
            d_wi += np.dot(d_i, inputs[t].T)
            d_bi += d_i
            
            # Candidate Gate Weights and Biases Errors
            d_c = d_cs * self.input_gates[t] * self.tanh(self.candidate_gates[t], derivative=True)
            d_wc += np.dot(d_c, inputs[t].T)
            d_bc += d_c

            # Concatenated Input Error (Sum of Error at Each Gate!)
            d_z = np.dot(self.wf.T, d_f) + np.dot(self.wi.T, d_i) + np.dot(self.wc.T, d_c) + np.dot(self.wo.T, d_o)

            # Error of Hidden State and Cell State at Next Time Step
            dh_next = d_z[:self.hidden_dim, :]
            dc_next = self.forget_gates[t] * d_cs

        for d_ in (d_wf, d_bf, d_wi, d_bi, d_wc, d_bc, d_wo, d_bo, d_wy, d_by):
            np.clip(d_, -1, 1, out=d_)

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

    def train(self):
        inputs = [self.one_hot_encode(char) for char in self.train_X]

        for _ in tqdm(range(self.epochs)):
            predictions = self.forward(inputs)

            errors = []
            for t in range(len(predictions)):
                errors.append(-self.softmax(predictions[t]))
                errors[-1][self.char_to_idx[self.train_y[t]]] += 1

            self.backward(errors, self.concat_inputs)
    
    def test(self):
        accuracy = 0
        probabilities = self.forward([self.one_hot_encode(char) for char in self.train_X])

        output = ''
        for t in range(len(self.train_y)):
            prediction = self.idx_to_char[np.random.choice(range(self.char_size), p=self.softmax(probabilities[t].reshape(-1)))]

            output += prediction

            if prediction == self.train_y[t]:
                accuracy += 1

        print(f'Ground Truth:\n{self.train_y}\n')
        print(f'Predictions:\n{output}\n')
        
        print(f'Accuracy: {round(accuracy * 100 / len(self.train_X), 2)}%')

##### Data #####
data = """Long Short-Term Memory (LSTM) networks are a type of recurrent neural network (RNN) capable of learning order dependence in sequence prediction problems. This behavior is required in complex problem domains like machine translation, speech recognition, and more. LSTMs are well-suited to classifying, processing, and making predictions based on time series data, since there can be lags of unknown duration between important events in a time series. LSTMs were introduced by Hochreiter and Schmidhuber in 1997, and were refined and popularized by many people in following work. They work by maintaining a cell state that is updated by gates: the forget gate, the input gate, and the output gate. These gates control the flow of information, allowing the network to remember or forget information as needed."""

# Initialize Network
lstm = LSTM(data=data, hidden_dim=25, epochs=1000, lr=0.05)

##### Training #####
lstm.train()

##### Testing #####
lstm.test()