"""
Simple Neural Network

https://machinelearningmastery.com/implement-backpropagation-algorithm-scratch-python/

"""
from random import seed
from random import random
from math import exp


# Initializing Network
def initialize_network(n_input, n_hidden, n_output):
    network = list()
    hidden_layer = [
        {"weights": [random() for i in range(n_input + 1)]} for i in range(n_hidden)
    ]
    network.append(hidden_layer)
    output_layer = [
        {"weights": [random() for i in range(n_hidden + 1)]} for i in range(n_output)
    ]
    network.append(output_layer)
    return network


# Forward Propagate
# 1.Neuron Activation.
# 2.Neuron Transfer.
# 3.Forward Propagation.


# Neuron activation is calculated as the weighted sum of the inputs
def activate(weights, inputs):
    activation = weights[-1]
    for i in range(len(weights) - 1):
        activation += weights[i] * inputs[i]
    return activation


def transfer(activation):
    return 1.0 / (1.0 + exp(-activation))


def forward_propogate(network, row):
    inputs = row
    for layer in network:
        new_inputs = []
        for neuron in layer:
            activation = activate(neuron["weights"], inputs)
            neuron["output"] = transfer(activation)
            new_inputs.append(neuron["output"])
        inputs = new_inputs

    return inputs


# Back Propagation
# 1.Transfer Derivative.
# 2.Error Backpropagation.
def transfer_derivative(output):
    return output * (1.0 - output)


def back_propogate_error(network, expected):
    for i in reversed(range(len(network))):
        layer = network[i]
        errors = list()

        if i != len(network) - 1:
            for j in range(len(layer)):
                error = 0.0
                for neuron in network[i + 1]:
                    error += neuron["weights"][j] * neuron["delta"]
                errors.append(error)
        else:
            for j in range(len(layer)):
                neuron = layer[j]
                errors.append(neuron["output"] - expected[j])

        for j in range(len(layer)):
            neuron = layer[j]
            neuron["delta"] = errors[j] * transfer_derivative(neuron["output"])


# Once errors are calculated for each neuron in the network via the back propagation method above,
#  they can be used to update weights.
def update_weights(network, row, l_rate):
    for i in range(len(network)):
        inputs = row[:-1]
        if i != 0:
            inputs = [neuron["output"] for neuron in network[i - 1]]
        for neuron in network[i]:
            for j in range(len(inputs)):
                neuron["weights"][j] -= l_rate * neuron["delta"] * inputs[j]
            neuron["weights"][-1] -= l_rate * neuron["delta"]


##Training


def train_network(network, train, l_rate, n_epoch, n_outputs):
    for epoch in range(n_epoch):
        sum_error = 0
        for row in train:
            outputs = forward_propogate(network, row)
            expected = [0 for i in range(n_outputs)]
            expected[row[-1]] = 1
            sum_error += sum(
                [(expected[i] - outputs[i]) ** 2 for i in range(len(expected))]
            )
            back_propogate_error(network, expected)
            update_weights(network, row, l_rate)
        print(">epoch=%d, lrate=%.3f, error=%.3f" % (epoch, l_rate, sum_error))


seed(1)
dataset = [
    [2.7810836, 2.550537003, 0],
    [1.465489372, 2.362125076, 0],
    [3.396561688, 4.400293529, 0],
    [1.38807019, 1.850220317, 0],
    [3.06407232, 3.005305973, 0],
    [7.627531214, 2.759262235, 1],
    [5.332441248, 2.088626775, 1],
    [6.922596716, 1.77106367, 1],
    [8.675418651, -0.242068655, 1],
    [7.673756466, 3.508563011, 1],
]
n_inputs = len(dataset[0]) - 1
n_outputs = len(set([row[-1] for row in dataset]))
network = initialize_network(n_inputs, 2, n_outputs)
train_network(network, dataset, 0.7, 30, n_outputs)
for layer in network:
    print(layer)
