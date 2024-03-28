"""
References:
    - http://neuralnetworksanddeeplearning.com/chap2.html (Backpropagation)
    - https://en.wikipedia.org/wiki/Sigmoid_function (Sigmoid activation function)
    - https://en.wikipedia.org/wiki/Feedforward_neural_network (Feedforward)
"""

import numpy


class TwoHiddenLayerNeuralNetwork:
    def __init__(self, input_array: numpy.ndarray, output_array: numpy.ndarray) -> None:
        """
        This function initializes the TwoHiddenLayerNeuralNetwork class with random
        weights for every layer and initializes predicted output with zeroes.

        input_array : input values for training the neural network (i.e training data) .
        output_array : expected output values of the given inputs.
        """

        # Input values provided for training the model.
        self.input_array = input_array

        # Random initial weights are assigned where first argument is the
        # number of nodes in previous layer and second argument is the
        # number of nodes in the next layer.

        # Random initial weights are assigned.
        # self.input_array.shape[1] is used to represent number of nodes in input layer.
        # First hidden layer consists of 4 nodes.
        self.input_layer_and_first_hidden_layer_weights = numpy.random.rand(
            self.input_array.shape[1], 4
        )

        # Random initial values for the first hidden layer.
        # First hidden layer has 4 nodes.
        # Second hidden layer has 3 nodes.
        self.first_hidden_layer_and_second_hidden_layer_weights = numpy.random.rand(
            4, 3
        )

        # Random initial values for the second hidden layer.
        # Second hidden layer has 3 nodes.
        # Output layer has 1 node.
        self.second_hidden_layer_and_output_layer_weights = numpy.random.rand(3, 1)

        # Real output values provided.
        self.output_array = output_array

        # Predicted output values by the neural network.
        # Predicted_output array initially consists of zeroes.
        self.predicted_output = numpy.zeros(output_array.shape)

    def feedforward(self) -> numpy.ndarray:
        """
        The information moves in only one direction i.e. forward from the input nodes,
        through the two hidden nodes and to the output nodes.
        There are no cycles or loops in the network.

        Return layer_between_second_hidden_layer_and_output
            (i.e the last layer of the neural network).

        >>> input_val = numpy.array(([0, 0, 0], [0, 0, 0], [0, 0, 0]), dtype=float)
        >>> output_val = numpy.array(([0], [0], [0]), dtype=float)
        >>> nn = TwoHiddenLayerNeuralNetwork(input_val, output_val)
        >>> res = nn.feedforward()
        >>> array_sum = numpy.sum(res)
        >>> numpy.isnan(array_sum)
        False
        """
        # Layer_between_input_and_first_hidden_layer is the layer connecting the
        # input nodes with the first hidden layer nodes.
        self.layer_between_input_and_first_hidden_layer = sigmoid(
            numpy.dot(self.input_array, self.input_layer_and_first_hidden_layer_weights)
        )

        # layer_between_first_hidden_layer_and_second_hidden_layer is the layer
        # connecting the first hidden set of nodes with the second hidden set of nodes.
        self.layer_between_first_hidden_layer_and_second_hidden_layer = sigmoid(
            numpy.dot(
                self.layer_between_input_and_first_hidden_layer,
                self.first_hidden_layer_and_second_hidden_layer_weights,
            )
        )

        # layer_between_second_hidden_layer_and_output is the layer connecting
        # second hidden layer with the output node.
        self.layer_between_second_hidden_layer_and_output = sigmoid(
            numpy.dot(
                self.layer_between_first_hidden_layer_and_second_hidden_layer,
                self.second_hidden_layer_and_output_layer_weights,
            )
        )

        return self.layer_between_second_hidden_layer_and_output

    def back_propagation(self) -> None:
        """
        Function for fine-tuning the weights of the neural net based on the
        error rate obtained in the previous epoch (i.e., iteration).
        Updation is done using derivative of sogmoid activation function.

        >>> input_val = numpy.array(([0, 0, 0], [0, 0, 0], [0, 0, 0]), dtype=float)
        >>> output_val = numpy.array(([0], [0], [0]), dtype=float)
        >>> nn = TwoHiddenLayerNeuralNetwork(input_val, output_val)
        >>> res = nn.feedforward()
        >>> nn.back_propagation()
        >>> updated_weights = nn.second_hidden_layer_and_output_layer_weights
        >>> (res == updated_weights).all()
        False
        """

        updated_second_hidden_layer_and_output_layer_weights = numpy.dot(
            self.layer_between_first_hidden_layer_and_second_hidden_layer.T,
            2
            * (self.output_array - self.predicted_output)
            * sigmoid_derivative(self.predicted_output),
        )
        updated_first_hidden_layer_and_second_hidden_layer_weights = numpy.dot(
            self.layer_between_input_and_first_hidden_layer.T,
            numpy.dot(
                2
                * (self.output_array - self.predicted_output)
                * sigmoid_derivative(self.predicted_output),
                self.second_hidden_layer_and_output_layer_weights.T,
            )
            * sigmoid_derivative(
                self.layer_between_first_hidden_layer_and_second_hidden_layer
            ),
        )
        updated_input_layer_and_first_hidden_layer_weights = numpy.dot(
            self.input_array.T,
            numpy.dot(
                numpy.dot(
                    2
                    * (self.output_array - self.predicted_output)
                    * sigmoid_derivative(self.predicted_output),
                    self.second_hidden_layer_and_output_layer_weights.T,
                )
                * sigmoid_derivative(
                    self.layer_between_first_hidden_layer_and_second_hidden_layer
                ),
                self.first_hidden_layer_and_second_hidden_layer_weights.T,
            )
            * sigmoid_derivative(self.layer_between_input_and_first_hidden_layer),
        )

        self.input_layer_and_first_hidden_layer_weights += (
            updated_input_layer_and_first_hidden_layer_weights
        )
        self.first_hidden_layer_and_second_hidden_layer_weights += (
            updated_first_hidden_layer_and_second_hidden_layer_weights
        )
        self.second_hidden_layer_and_output_layer_weights += (
            updated_second_hidden_layer_and_output_layer_weights
        )

    def train(self, output: numpy.ndarray, iterations: int, give_loss: bool) -> None:
        """
        Performs the feedforwarding and back propagation process for the
        given number of iterations.
        Every iteration will update the weights of neural network.

        output : real output values,required for calculating loss.
        iterations : number of times the weights are to be updated.
        give_loss : boolean value, If True then prints loss for each iteration,
                    If False then nothing is printed

        >>> input_val = numpy.array(([0, 0, 0], [0, 1, 0], [0, 0, 1]), dtype=float)
        >>> output_val = numpy.array(([0], [1], [1]), dtype=float)
        >>> nn = TwoHiddenLayerNeuralNetwork(input_val, output_val)
        >>> first_iteration_weights = nn.feedforward()
        >>> nn.back_propagation()
        >>> updated_weights = nn.second_hidden_layer_and_output_layer_weights
        >>> (first_iteration_weights == updated_weights).all()
        False
        """
        for iteration in range(1, iterations + 1):
            self.output = self.feedforward()
            self.back_propagation()
            if give_loss:
                loss = numpy.mean(numpy.square(output - self.feedforward()))
                print(f"Iteration {iteration} Loss: {loss}")

    def predict(self, input_arr: numpy.ndarray) -> int:
        """
        Predict's the output for the given input values using
        the trained neural network.

        The output value given by the model ranges in-between 0 and 1.
        The predict function returns 1 if the model value is greater
        than the threshold value else returns 0,
        as the real output values are in binary.

        >>> input_val = numpy.array(([0, 0, 0], [0, 1, 0], [0, 0, 1]), dtype=float)
        >>> output_val = numpy.array(([0], [1], [1]), dtype=float)
        >>> nn = TwoHiddenLayerNeuralNetwork(input_val, output_val)
        >>> nn.train(output_val, 1000, False)
        >>> nn.predict([0, 1, 0]) in (0, 1)
        True
        """

        # Input values for which the predictions are to be made.
        self.array = input_arr

        self.layer_between_input_and_first_hidden_layer = sigmoid(
            numpy.dot(self.array, self.input_layer_and_first_hidden_layer_weights)
        )

        self.layer_between_first_hidden_layer_and_second_hidden_layer = sigmoid(
            numpy.dot(
                self.layer_between_input_and_first_hidden_layer,
                self.first_hidden_layer_and_second_hidden_layer_weights,
            )
        )

        self.layer_between_second_hidden_layer_and_output = sigmoid(
            numpy.dot(
                self.layer_between_first_hidden_layer_and_second_hidden_layer,
                self.second_hidden_layer_and_output_layer_weights,
            )
        )

        return int((self.layer_between_second_hidden_layer_and_output > 0.6)[0])


def sigmoid(value: numpy.ndarray) -> numpy.ndarray:
    """
    Applies sigmoid activation function.

    return normalized values

    >>> sigmoid(numpy.array(([1, 0, 2], [1, 0, 0]), dtype=numpy.float64))
    array([[0.73105858, 0.5       , 0.88079708],
           [0.73105858, 0.5       , 0.5       ]])
    """
    return 1 / (1 + numpy.exp(-value))


def sigmoid_derivative(value: numpy.ndarray) -> numpy.ndarray:
    """
    Provides the derivative value of the sigmoid function.

    returns derivative of the sigmoid value

    >>> sigmoid_derivative(numpy.array(([1, 0, 2], [1, 0, 0]), dtype=numpy.float64))
    array([[ 0.,  0., -2.],
           [ 0.,  0.,  0.]])
    """
    return (value) * (1 - (value))


def example() -> int:
    """
    Example for "how to use the neural network class and use the
    respected methods for the desired output".
    Calls the TwoHiddenLayerNeuralNetwork class and
    provides the fixed input output values to the model.
    Model is trained for a fixed amount of iterations then the predict method is called.
    In this example the output is divided into 2 classes i.e. binary classification,
    the two classes are represented by '0' and '1'.

    >>> example() in (0, 1)
    True
    """
    # Input values.
    test_input = numpy.array(
        (
            [0, 0, 0],
            [0, 0, 1],
            [0, 1, 0],
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 1],
            [1, 1, 0],
            [1, 1, 1],
        ),
        dtype=numpy.float64,
    )

    # True output values for the given input values.
    output = numpy.array(([0], [1], [1], [0], [1], [0], [0], [1]), dtype=numpy.float64)

    # Calling neural network class.
    neural_network = TwoHiddenLayerNeuralNetwork(
        input_array=test_input, output_array=output
    )

    # Calling training function.
    # Set give_loss to True if you want to see loss in every iteration.
    neural_network.train(output=output, iterations=10, give_loss=False)

    return neural_network.predict(numpy.array(([1, 1, 1]), dtype=numpy.float64))


if __name__ == "__main__":
    example()
