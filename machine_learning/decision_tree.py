"""
Implementation of a basic regression decision tree.
Input data set: The input data set must be 1-dimensional with continuous labels.
Output: The decision tree maps a real number input to a real number output.
"""
import numpy as np

class Decision_Tree:
    def __init__(self, depth = 5, min_leaf_size = 5):
        self.depth = depth
        self.decision_boundary = 0
        self.left = None
        self.right = None
        self.min_leaf_size = min_leaf_size
        self.prediction = None

    def mean_squared_error(self, labels, prediction):
        """
        mean_squared_error:
        @param labels: a one dimensional numpy array
        @param prediction: a floating point value
        return value: mean_squared_error calculates the error if prediction is used to estimate the labels
        """
        if labels.ndim != 1:
            print("Error: Input labels must be one dimensional")

        return np.mean((labels - prediction) ** 2)

    def train(self, X, y):
        """
        train:
        @param X: a one dimensional numpy array
        @param y: a one dimensional numpy array.
        The contents of y are the labels for the corresponding X values

        train does not have a return value
        """

        """
        this section is to check that the inputs conform to our dimensionality constraints
        """
        if X.ndim != 1:
            print("Error: Input data set must be one dimensional")
            return
        if len(X) != len(y):
            print("Error: X and y have different lengths")
            return
        if y.ndim != 1:
            print("Error: Data set labels must be one dimensional")
            return

        if len(X) < 2 * self.min_leaf_size:
            self.prediction = np.mean(y)
            return

        if self.depth == 1:
            self.prediction = np.mean(y)
            return

        best_split = 0
        min_error = self.mean_squared_error(X,np.mean(y)) * 2


        """
        loop over all possible splits for the decision tree. find the best split.
        if no split exists that is less than 2 * error for the entire array
        then the data set is not split and the average for the entire array is used as the predictor
        """
        for i in range(len(X)):
            if len(X[:i]) < self.min_leaf_size:
                continue
            elif len(X[i:]) < self.min_leaf_size:
                continue
            else:
                error_left = self.mean_squared_error(X[:i], np.mean(y[:i]))
                error_right = self.mean_squared_error(X[i:], np.mean(y[i:]))
                error = error_left + error_right
                if error < min_error:
                    best_split = i
                    min_error = error

        if best_split != 0:
            left_X = X[:best_split]
            left_y = y[:best_split]
            right_X = X[best_split:]
            right_y = y[best_split:]

            self.decision_boundary = X[best_split]
            self.left = Decision_Tree(depth = self.depth - 1, min_leaf_size = self.min_leaf_size)
            self.right = Decision_Tree(depth = self.depth - 1, min_leaf_size = self.min_leaf_size)
            self.left.train(left_X, left_y)
            self.right.train(right_X, right_y)
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

def main():
    """
    In this demonstration we're generating a sample data set from the sin function in numpy.
    We then train a decision tree on the data set and use the decision tree to predict the
    label of 10 different test values. Then the mean squared error over this test is displayed.
    """
    X = np.arange(-1., 1., 0.005)
    y = np.sin(X)

    tree = Decision_Tree(depth = 10, min_leaf_size = 10)
    tree.train(X,y)

    test_cases = (np.random.rand(10) * 2) - 1
    predictions = np.array([tree.predict(x) for x in test_cases])
    avg_error = np.mean((predictions - test_cases) ** 2)

    print("Test values: " + str(test_cases))
    print("Predictions: " + str(predictions))
    print("Average error: " + str(avg_error))


if __name__ == '__main__':
    main()