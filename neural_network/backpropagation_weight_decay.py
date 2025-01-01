import warnings

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler

warnings.filterwarnings("ignore", category=DeprecationWarning)


def train_network(
    neurons: int, x_train: np.array, y_train: np.array, epochs: int
) -> tuple:
    """
    Code the backpropagation algorithm with the technique of regularization
    weight decay.
    The chosen network architecture consists of 3 layers
    (the input layer, the hidden layer and the output layer).

    Explanation here (Available just in Spanish):
    https://drive.google.com/file/d/1QTEbRVgevfK8QJ30tWcEbaNbBaKnvGWv/view?usp=sharing

    >>> import numpy as np
    >>> x_train = np.array([[0.1, 0.2], [0.4, 0.6]])
    >>> y_train = np.array([[1], [0]])
    >>> neurons = 2
    >>> epochs = 10
    >>> result = train_network(neurons, x_train, y_train, epochs)
    >>> all(part is not None for part in result)
    True
    """
    mu = 0.2
    lambda_ = 1e-4
    factor_scale = 0.001
    inputs = np.shape(x_train)[1]
    outputs = np.shape(y_train)[1]
    # initialization of weights and bias randomly in very small values
    rng = np.random.default_rng(seed=42)
    w_co = rng.random((int(inputs), int(neurons))) * factor_scale
    bias_co = rng.random((1, int(neurons))) * factor_scale
    w_cs = rng.random((int(neurons), int(outputs))) * factor_scale
    bias_cs = rng.random((1, int(outputs))) * factor_scale
    error = np.zeros(epochs)
    # iterative process
    k = 0
    while k < epochs:
        y = np.zeros(np.shape(y_train))
        for j in np.arange(0, len(x_train), 1):
            x = x_train[j]
            t = y_train[j]
            # forward step: calcul of aj, ak ,zj y zk
            aj = np.dot(x, w_co) + bias_co
            zj = relu(aj)
            ak = np.dot(zj, w_cs) + bias_cs
            zk = sigmoid(ak)
            y[j] = np.round(zk)

            # backward step: Error gradient estimation
            g2p = d_sigmoid(ak)  # for the weights and bias of the output layer neuron
            d_w_cs = g2p * zj.T
            d_bias_cs = g2p * 1
            grad_w_cs = (zk - t) * d_w_cs + lambda_ * w_cs
            grad_bias_cs = (zk - t) * d_bias_cs + lambda_ * bias_cs

            g1p = d_relu(aj)  # for the weights and bias of occult layer neurons
            d_w_co = np.zeros(np.shape(w_co))
            d_bias_co = np.zeros(np.shape(bias_co))
            for i in np.arange(0, np.shape(d_w_co)[1], 1):
                d_w_co[:, i] = g2p * w_cs[i] * g1p.T[i] * x.T
                d_bias_co[0, i] = g2p * w_cs[i] * g1p.T[i] * 1
            grad_w_co = (zk - t) * d_w_co + lambda_ * w_co
            grad_bias_co = (zk - t) * d_bias_co + lambda_ * bias_co

            # Weight and bias update with regularization weight decay
            w_cs = (1 - mu * lambda_) * w_cs - mu * grad_w_cs
            bias_cs = (1 - mu * lambda_) * bias_cs - mu * grad_bias_cs
            w_co = (1 - mu * lambda_) * w_co - mu * grad_w_co
            bias_co = (1 - mu * lambda_) * bias_co - mu * grad_bias_co
        error[k] = 0.5 * np.sum((y - y_train) ** 2)
        k += 1
    return w_co, bias_co, w_cs, bias_cs, error


def relu(input_: np.array) -> np.array:
    """
    Relu activation function
    Hidden Layer due to it is less susceptible to vanish gradient

    >>> relu(np.array([[0, -1, 2, 3, 0], [0, -1, -2, -3, 5]]))
    array([[0, 0, 2, 3, 0],
           [0, 0, 0, 0, 5]])
    """
    return np.maximum(input_, 0)


def d_relu(input_: np.array) -> np.array:
    """
    Relu Activation derivate function
    >>> d_relu(np.array([[0, -1, 2, 3, 0], [0, -1, -2, -3, 5]]))
    array([[1, 0, 1, 1, 1],
           [1, 0, 0, 0, 1]])
    """
    for i in np.arange(0, len(input_)):
        for j in np.arange(0, len(input_[i])):
            if input_[i, j] >= 0:
                input_[i, j] = 1
            else:
                input_[i, j] = 0
    return input_


def sigmoid(input_: float) -> float:
    """
    Sigmoid activation function
    Output layer
    >>> import numpy as np
    >>> sigmoid(0) is not None
    True
    """
    return 1 / (1 + np.exp(-input_))


def d_sigmoid(input_: float) -> float:
    """
    Sigmoid activation derivate
    >>> import numpy as np
    >>> d_sigmoid(0) is not None
    True
    """
    return sigmoid(input_) ** 2 * np.exp(-input_)


def main() -> None:
    """
    Import load_breast_cancer dataset
    It is a binary classification problem with 569 samples and 30 attributes
    Categorical value output [0 1]

    The date is split 70% / 30% in train and test sets

    Before train the neural network, the data is normalized to [0 1] interval

    The function train_network() returns the weight and bias matrix to apply the
    transfer function to predict the output
    """

    inputs = load_breast_cancer()["data"]
    target = load_breast_cancer()["target"]
    target = target.reshape(np.shape(target)[0], 1)

    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(inputs)

    train = int(np.round(np.shape(normalized_data)[0] * 0.7))
    x_train = normalized_data[0:train, :]
    x_test = normalized_data[train:, :]

    y_train = target[0:train]
    y_test = target[train:]

    # play with epochs and neuron numbers
    epochs = 5
    neurons = 5
    w_co, bias_co, w_cs, bias_cs, error = train_network(
        neurons, x_train, y_train, epochs
    )

    # find the labels with the weights obtained ( apply network transfer function )
    yp_test = np.round(
        sigmoid(np.dot(relu(np.dot(x_test, w_co) + bias_co), w_cs) + bias_cs)
    )

    print(f"accuracy: {accuracy_score(y_test, yp_test)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
