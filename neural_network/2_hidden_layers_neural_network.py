import numpy


class NeuralNetwork:
    def __init__(self, input_array: numpy.array, output_array: numpy.array):
        """
        input_array : input values for training the neural network.
        output_array : expected output values of the given inputs.
        """
        self.input = input_array
        # Initial weights are assigned randomly where first argument is the number
        # of nodes in previous layer and second argument is the
        # number of nodes in the next layer.

        # random initial weights for the input layer
        # self.input.shape[1] is used to represent number of nodes in input layer
        # first hidden layer consists of 4 nodes
        self.weights1 = numpy.random.rand(self.input.shape[1], 4)

        # random initial weights for the first hidden layer
        # first hidden layer has 4 nodes
        # second hidden layer has 3 nodes
        self.weights2 = numpy.random.rand(4, 3)

        # random initial weights for the second hidden layer
        # second hidden layer has 3 nodes
        # output layer has 1 node
        self.weights3 = numpy.random.rand(3, 1)

        self.y = output_array
        self.output = numpy.zeros(output_array.shape)

    def feedforward(self):
        """
        feedforward propagation using sigmoid activation function between layers
        return the last layer of the neural network
        """
        # layer1 is the layer connecting the input nodes with
        # the first hidden layer nodes
        self.layer1 = sigmoid(numpy.dot(self.input, self.weights1))

        # layer2 is the layer connecting the first hidden set of nodes
        # with the second hidden set of nodes
        self.layer2 = sigmoid(numpy.dot(self.layer1, self.weights2))

        # layer3 is the layer connecting second hidden layer with the output node
        self.layer3 = sigmoid(numpy.dot(self.layer2, self.weights3))

        return self.layer3

    def back_propagation(self):
        """
        backpropagating between the layers using sigmoid derivative and
        loss between layers
        updates the weights between the layers
        """

        updated_weights3 = numpy.dot(
            self.layer2.T, 2 * (self.y - self.output) * sigmoid_derivative(self.output)
        )
        updated_weights2 = numpy.dot(
            self.layer1.T,
            numpy.dot(
                2 * (self.y - self.output) * sigmoid_derivative(self.output),
                self.weights3.T,
            )
            * sigmoid_derivative(self.layer2),
        )
        updated_weights1 = numpy.dot(
            self.input.T,
            numpy.dot(
                numpy.dot(
                    2 * (self.y - self.output) * sigmoid_derivative(self.output),
                    self.weights3.T,
                )
                * sigmoid_derivative(self.layer2),
                self.weights2.T,
            )
            * sigmoid_derivative(self.layer1),
        )

        self.weights1 += updated_weights1
        self.weights2 += updated_weights2
        self.weights3 += updated_weights3

    def train(self, output: numpy.array, iterations: int):
        """
        output : required for calculating loss
        performs the feeding and back propagation process for the
        given number of iterations
        every iteration will update the weights of neural network
        """
        for iteration in range(1, iterations + 1):
            self.output = self.feedforward()
            self.back_propagation()
            print(
                "Iteration %s " % iteration,
                "Loss: " + str(numpy.mean(numpy.square(output - self.feedforward()))),
            )

    def predict(self, input: list) -> int:
        """
        predict's output for the given input values
        """
        self.array = numpy.array((input), dtype=float)
        self.layer1 = sigmoid(numpy.dot(self.array, self.weights1))
        self.layer2 = sigmoid(numpy.dot(self.layer1, self.weights2))
        self.layer3 = sigmoid(numpy.dot(self.layer2, self.weights3))
        if self.layer3 >= 0.5:
            return 1
        else:
            return 0


def sigmoid(value: float) -> float:
    """
    applies sigmoid activation function
    return normalized values

    >>> sigmoid(2)
    0.8807970779778823

    >>> sigmoid(0)
    0.5
    """
    return 1 / (1 + numpy.exp(-value))


def sigmoid_derivative(value: float) -> float:
    """
    returns derivative of the sigmoid value

    >>> sigmoid_derivative(0.7)
    0.22171287329310904
    """
    return sigmoid(value) * (1 - sigmoid(value))


def example():
    # input values
    input = numpy.array(
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
        dtype=float,
    )

    # true output for the given input values
    output = numpy.array(([0], [1], [1], [0], [1], [0], [0], [1]), dtype=float)

    # calling neural network class
    Neural_Network = NeuralNetwork(input_array=input, output_array=output)

    # calling training function
    Neural_Network.train(output=output, iterations=1000)
    print(Neural_Network.predict([0, 1, 1]))


if __name__ == "__main__":
    example()
