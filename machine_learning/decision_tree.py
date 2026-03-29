"""
Implementation of a basic regression decision tree.
Input data set: The input data set must be 1-dimensional with continuous labels.
Output: The decision tree maps a real number input to a real number output.
"""

import numpy as np
from collections import Counter


class DecisionTree:
    def __init__(self, depth=5, min_leaf_size=5, task="regression", criterion="gini"):
        self.depth = depth
        self.decision_boundary = 0
        self.left = None
        self.right = None
        self.min_leaf_size = min_leaf_size
        self.prediction = None
        self.task = task
        self.criterion = criterion
        
    def mean_squared_error(self, labels, prediction):
        """
        mean_squared_error:
        @param labels: a one-dimensional numpy array
        @param prediction: a floating point value
        return value: mean_squared_error calculates the error if prediction is used to
            estimate the labels
        >>> tester = DecisionTree()
        >>> test_labels = np.array([1,2,3,4,5,6,7,8,9,10])
        >>> test_prediction = float(6)
        >>> bool(tester.mean_squared_error(test_labels, test_prediction) == (
        ...     TestDecisionTree.helper_mean_squared_error_test(test_labels,
        ...         test_prediction)))
        True
        >>> test_labels = np.array([1,2,3])
        >>> test_prediction = float(2)
        >>> bool(tester.mean_squared_error(test_labels, test_prediction) == (
        ...     TestDecisionTree.helper_mean_squared_error_test(test_labels,
        ...         test_prediction)))
        True
        """
        if labels.ndim != 1:
            raise ValueError("Input labels must be one dimensional")
        return np.mean((labels - prediction) ** 2)

    def gini(self, y):
        """
        Computes the Gini impurity for a set of labels.
        Gini impurity measures how often a randomly chosen element
        would be incorrectly classified.
        Formula: Gini = 1 - sum(p_i^2)
        where p_i is the probability of class i.
    
        Lower Gini value indicates better purity (best split).
        """
        classes, counts = np.unique(y, return_counts=True)
        prob = counts / counts.sum()
        return 1 - np.sum(prob ** 2)

    def entropy(self, y):
        """
        Computes the entropy (impurity) of a set of labels.
        Entropy measures the randomness or disorder in the data.
        Formula: Entropy = - sum(p_i * log2(p_i))
        where p_i is the probability of class i.
    
        Lower entropy means higher purity.
        """
        classes, counts = np.unique(y, return_counts=True)
        prob = counts / counts.sum()
        return -np.sum(prob * np.log2(prob + 1e-9))

    def information_gain(self, parent, left, right):
        """
        Computes the information gain from splitting a dataset.
        Information gain represents the reduction in impurity
        after a dataset is split into left and right subsets.
        Formula: IG = Impurity(parent) - [weighted impurity(left) + weighted impurity(right)]
    
        Higher information gain indicates a better split.
        """
        if self.criterion == "gini":
            func = self.gini
        elif self.criterion == "entropy":
            func = self.entropy
        else:
            raise ValueError("Invalid criterion")

        weight_l = len(left) / len(parent)
        weight_r = len(right) / len(parent)

        return func(parent) - (
            weight_l * func(left) + weight_r * func(right)
        )

    def most_common_label(self, y):
        return Counter(y).most_common(1)[0][0]

    def train(self, x, y):
        """
        train:
        @param x: a one-dimensional numpy array
        @param y: a one-dimensional numpy array.
        The contents of y are the labels for the corresponding X values

        train() does not have a return value

        Examples:
        1. Try to train when x & y are of same length & 1 dimensions (No errors)
        >>> dt = DecisionTree()
        >>> dt.train(np.array([10,20,30,40,50]),np.array([0,0,0,1,1]))

        2. Try to train when x is 2 dimensions
        >>> dt = DecisionTree()
        >>> dt.train(np.array([[1,2,3,4,5],[1,2,3,4,5]]),np.array([0,0,0,1,1]))
        Traceback (most recent call last):
            ...
        ValueError: Input data set must be one-dimensional

        3. Try to train when x and y are not of the same length
        >>> dt = DecisionTree()
        >>> dt.train(np.array([1,2,3,4,5]),np.array([[0,0,0,1,1],[0,0,0,1,1]]))
        Traceback (most recent call last):
            ...
        ValueError: x and y have different lengths

        4. Try to train when x & y are of the same length but different dimensions
        >>> dt = DecisionTree()
        >>> dt.train(np.array([1,2,3,4,5]),np.array([[1],[2],[3],[4],[5]]))
        Traceback (most recent call last):
            ...
        ValueError: Data set labels must be one-dimensional

        This section is to check that the inputs conform to our dimensionality
        constraints
        """
        if x.ndim != 1:
            raise ValueError("Input data set must be one-dimensional")
        if len(x) != len(y):
            raise ValueError("x and y have different lengths")
        if y.ndim != 1:
            raise ValueError("Data set labels must be one-dimensional")

        if len(x) < 2 * self.min_leaf_size or self.depth == 1:
            if self.task == "regression":
                self.prediction = np.mean(y)
            else:
                self.prediction = self.most_common_label(y)
            return

        best_split = 0
        
        """
        loop over all possible splits for the decision tree. find the best split.
        if no split exists that is less than 2 * error for the entire array
        then the data set is not split and the average for the entire array is used as
        the predictor
        """
        if self.task == "regression":
            best_score = float("inf")
        else:
            best_score = -float("inf")

        for i in range(len(x)):
            if len(x[:i]) < self.min_leaf_size:
                continue
            if len(x[i:]) < self.min_leaf_size:
                continue

            left_y = y[:i]
            right_y = y[i:]

            if self.task == "regression":
                error_left = self.mean_squared_error(left_y, np.mean(left_y))
                error_right = self.mean_squared_error(right_y, np.mean(right_y))
                score = error_left + error_right

                if score < best_score:
                    best_score = score
                    best_split = i

            else:  
                gain = self.information_gain(y, left_y, right_y)

                if gain > best_score:
                    best_score = gain
                    best_split = i

        if best_split != 0:
            left_x = x[:best_split]
            left_y = y[:best_split]
            right_x = x[best_split:]
            right_y = y[best_split:]

            self.decision_boundary = x[best_split]

            self.left = DecisionTree(
                depth=self.depth - 1,
                min_leaf_size=self.min_leaf_size,
                task=self.task,
                criterion=self.criterion,
            )
            self.right = DecisionTree(
                depth=self.depth - 1,
                min_leaf_size=self.min_leaf_size,
                task=self.task,
                criterion=self.criterion,
            )

            self.left.train(left_x, left_y)
            self.right.train(right_x, right_y)

        else:
            if self.task == "regression":
                self.prediction = np.mean(y)
            else:
                self.prediction = self.most_common_label(y)

    def predict(self, x):
        """
        predict:
        @param x: a floating point value to predict the label of
        the prediction function works by recursively calling the predict function
        of the appropriate subtrees based on the tree's decision boundary
        """
        if self.prediction is not None:
            return self.prediction
        if self.left is not None and self.right is not None:
            if x >= self.decision_boundary:
                return self.right.predict(x)
            else:
                return self.left.predict(x)

        raise ValueError("Decision tree not yet trained")

        
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

    tree = DecisionTree(depth=10, min_leaf_size=10, task="regression")
    tree.train(x, y)

    print("Regression prediction:", tree.predict(0.5))
    x_cls = np.array([1, 2, 3, 4, 5, 6])
    y_cls = np.array([0, 0, 0, 1, 1, 1])

    clf = DecisionTree(depth=3, min_leaf_size=1, task="classification", criterion="gini")
    clf.train(x_cls, y_cls)

    print("Classification prediction (2):", clf.predict(2)) 
    print("Classification prediction (5):", clf.predict(5))  


if __name__ == "__main__":
    main()
    import doctest

    doctest.testmod(name="mean_squared_error", verbose=True)