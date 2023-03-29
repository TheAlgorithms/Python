"""
Implementation of a basic regression decision tree.
Input data set: The input data set must be 1-dimensional with continuous labels.
Output: The decision tree maps a real number input to a real number output.
"""
import numpy as np
import logging


class DecisionTree:
    def __init__(self, depth=5, min_leaf_size=5):
        self.depth = depth
        self.decision_boundary = 0
        self.left = None
        self.right = None
        self.min_leaf_size = min_leaf_size
        self.prediction = None

    def mean_squared_error(self, labels, prediction):
        """
        Calculates the mean squared error if prediction is used to estimate the labels.
        :param labels: a one dimensional numpy array
        :param prediction: a floating point value
        :return: mean squared error
        """
        if labels.ndim != 1:
            logging.error("Input labels must be one dimensional")
            return None

        return np.mean((labels - prediction) ** 2)

    def train(self, x, y):
        """
        Trains the decision tree using the input data x and y.
        :param x: a one dimensional numpy array
        :param y: a one dimensional numpy array. The contents of y are the labels for the corresponding X values
        :return: None
        """
        # Validate input data
        if x.ndim != 1:
            logging.error("Input data set must be one dimensional")
            return
        if len(x) != len(y):
            logging.error("X and y have different lengths")
            return
        if y.ndim != 1:
            logging.error("Data set labels must be one dimensional")
            return

        # Check if leaf node
        if len(x) < 2 * self.min_leaf_size or self.depth == 1:
            self.prediction = np.mean(y)
            return

        # Find the best split
        best_split = 0
        min_error = self.mean_squared_error(x, np.mean(y)) * 2

        for i in range(len(x)):
            if len(x[:i]) < self.min_leaf_size or len(x[i:]) < self.min_leaf_size:
                continue

            error_left = self.mean_squared_error(x[:i], np.mean(y[:i]))
            error_right = self.mean_squared_error(x[i:], np.mean(y[i:]))
            error = error_left + error_right

            if error < min_error:
                best_split = i
                min_error = error

        # Create child nodes
        if best_split != 0:
            left_x = x[:best_split]
            left_y = y[:best_split]
            right_x = x[best_split:]
            right_y = y[best_split:]

            self.decision_boundary = x[best_split]
            self.left = DecisionTree(
                depth=self.depth - 1, min_leaf_size=self.min_leaf_size
            )
            self.right = DecisionTree(

                depth=self.depth - 1, min_leaf_size=self.min_leaf_size
            )
            self.left.train(left_x, left_y)
            self.right.train(right_x, right_y)
        else:
            self.prediction = np.mean(y)

        return

    def predict(self, x):
        """
        predict:
        @param x: a floating point value to predict the label of
        the prediction function works by recursively calling the predict function
        of the appropriate subtrees based on the tree's decision boundary
        """
        if self.prediction is not None:
            return self.prediction
        elif self.left or self.right is not None:
            if x >= self.decision_boundary:
                return self.right.predict(x)
            else:
                return self.left.predict(x)
        else:
            print("Error: Decision tree not yet trained")
            return None


class TestDecisionTree:
    """Decision Tres test class"""

    @staticmethod
    def helper_mean_squared_error_test(labels, prediction):
        """
        helper_mean_squared_error_test:
        @param labels: a one dimensional numpy array
        @param prediction: a floating point value
        return value: helper_mean_squared_error_test calculates the mean squared error
        """
        squared_error_sum = float(0)
        for label in labels:
            squared_error_sum += (label - prediction) ** 2

        return float(squared_error_sum / labels.size)


def main():
    """
    In this demonstration we're generating a sample data set from the sin function in
    numpy.  We then train a decision tree on the data set and use the decision tree to
    predict the label of 10 different test values. Then the mean squared error over
    this test is displayed.
    """
    x = np.arange(-1.0, 1.0, 0.005)
    y = np.sin(x)

    tree = DecisionTree(depth=10, min_leaf_size=10)
    tree.train(x, y)

    test_cases = (np.random.rand(10) * 2) - 1
    predictions = np.array([tree.predict(x) for x in test_cases])
    avg_error = np.mean((predictions - test_cases) ** 2)

    print("Test values: " + str(test_cases))
    print("Predictions: " + str(predictions))
    print("Average error: " + str(avg_error))


if __name__ == "__main__":
    main()
    import doctest

    doctest.testmod(name="mean_squarred_error", verbose=True)
