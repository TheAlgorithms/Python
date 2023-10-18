"""
Implementation of gradient descent algorithm for minimizing cost of a linear hypothesis
function.
"""
import numpy as np


def random_linear_function(x0: float, x1: float, x2: float) -> float:
    return -0.44562 * x0 + 1.07831 * x1 + 0.34078 * x2 - 0.60752


"""
This is the list of inputs and outputs.
Input shape: (3, m)
Output shape: (1, n)
Each column represents a single training example.
m is the number of training examples.
"""
train_x = np.array(
    [
        [0.013933, 0.18614919, 0.22363674, 0.18737055, 1.49787963, 1.24865476],
        [0.00972224, -0.51948611, -0.74649768, 0.38754526, 1.43271505, -1.74150751],
        [0.49624539, -1.66085244, 0.58543661, 2.47361057, -0.09029329, -0.64871002],
    ]
)

train_y = np.array(
    [[-0.43413473, -1.81662416, -1.31262783, 0.56983487, 0.2391357, -3.2628979]]
)

test_x = np.array(
    [[0.28367314, 2.60050588], [-0.20341425, -0.77734235], [1.07614145, 0.4527949]]
)

test_y = np.array([[-0.58654656, -2.45027001]])

m = train_x.shape[-1]

# Randomly initialize weights and biases
weights = np.random.randn(1, 3)
bias = np.random.randn(1, 1)


def predict(data_x: np.ndarray, weights: np.ndarray, bias: np.ndarray) -> np.ndarray:
    """
    Returns an array of predictions for an array of inputs.
    """
    return weights @ data_x + bias


def losses(y_true: np.ndarray, y_predicted: np.ndarray) -> np.ndarray:
    """
    Returns an array of losses for an array of inputs.
    """
    return np.square(y_true - y_predicted)


def cost(y_true: np.ndarray, y_predicted: np.ndarray) -> float:
    """
    Returns cost function for a model.
    Cost is the average of losses over the inputs.
    """
    return np.mean(losses(y_true, y_predicted))


def gradient_descent(
    input_x: np.ndarray,
    output_y: np.ndarray,
    weights: np.ndarray,
    bias: np.ndarray,
    learning_rate: float = 0.001,
    iterations: int = 10000,
) -> tuple:
    """
    Uses gradient descent to train the model.
    Returns final modified parameters as a tuple (weights, biases).
    Prints cost function every 1000 epochs.
    """
    for iteration in range(iterations):
        yhat = predict(input_x, weights, bias)
        dz = 2 * (yhat - output_y)
        dw = dz @ input_x.T / m
        db = np.mean(dz)
        weights -= learning_rate * dw
        bias -= learning_rate * db

        if iteration % 1000 == 0:
            print(f"Cost after {iteration} iterations: {cost(output_y, yhat)}")

    print(f"Final cost: {cost(output_y, yhat)}\n")
    return weights, bias


def test_gradient_descent() -> None:
    """
    Prints actual output and predicted output side by side for a model.
    """
    global weights, bias
    weights, bias = gradient_descent(
        train_x, train_y, weights, bias, learning_rate=0.001, iterations=10000
    )

    predictions = predict(test_x, weights, bias)
    print("Testing: ")
    for i in range(test_x.shape[-1]):
        print(
            f"Actual output value: {test_y[0, i]}\t\
              Predicted output value: {predictions[0, i]}"
        )
    print()


if __name__ == "__main__":
    # test_gradient_descent()
    import doctest

    doctest.testmod()
