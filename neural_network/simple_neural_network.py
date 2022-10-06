import nnfs
import numpy as np
from nnfs.datasets import spiral_data


class LayerDense:
    """
    Main layer dense function for creating layers.
    """

    def __init__(self, n_inputs: int, n_neurons: int) -> None:
        """
        Given number of neurons input and numbers of neurons
        return a numpy array of set of weights and biases.
        """
        self.weights = np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs: np.ndarray) -> np.ndarray:
        """
        Given neurons set of weights, inputs and biases return the dot
        product of the input and weights + biases to get the output of the
        neuron.
        """
        self.output = np.dot(inputs, self.weights) + self.biases


class ActivationReLU:
    """
    Class for creating the ReLU activation function.
    """

    def forward(self, inputs: np.ndarray) -> np.ndarray:
        """
        Given neuron inputs, preform ReLU activatoin function and
        return the output of it after applying the activation function.
        """
        self.output = np.maximum(0, inputs)


class ActivationSoftmax:
    """
    Class for creating the softmax activation function
    """

    def forward(self, inputs: np.ndarray) -> np.ndarray:
        """
        Given neuron inputs, apply the softmax activation function to it
        then return the output of the neuron after the softmax function.
        """
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))

        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)

        self.output = probabilities


class Loss:
    """Class for calculating the loss of the neuron network"""

    def calculate(self, output: np.ndarray, y: np.ndarray) -> np.ndarray:
        """
        Given the output of the neuron network, return the mean of the sample losses.
        """
        sample_losses = self.forward(output, y)
        data_loss = np.mean(sample_losses)

        return data_loss


class LossCategoricalCrossentropy(Loss):
    """Clas for calculating the loss categorical cross entropy of the neural network."""

    def forward(self, y_pred: np.ndarray, y_true: np.ndarray) -> np.ndarray:
        """
        Given predictions and ground truth values, calcualte the mean loss
        and return the negative loss likehoods.
        """
        y_pred_clipped = np.clip(y_pred, -1e-7, +1e-7)

        if len(y_true.shape) == 1:
            correct_confidences = y_pred_clipped[range(len(y_pred)), y_true]

        elif len(y_true.shape) == 2:
            correct_confidences = np.sum(y_pred_clipped * y_true, axis=1)

        negative_loss_likehoods = -np.log(correct_confidences)
        return negative_loss_likehoods


X, y = spiral_data(samples=100, classes=3)
dense1 = LayerDense(2, 3)

activation1 = ActivationReLU()

dense2 = LayerDense(3, 3)

activation2 = ActivationSoftmax()

loss_function = LossCategoricalCrossentropy()

dense1.forward(X)

activation1.forward(dense1.output)

dense2.forward(activation1.output)

activation2.forward(dense2.output)

print(f"Neural Network Output: {activation2.output}")
