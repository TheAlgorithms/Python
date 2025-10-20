"""
Implementation of a basic regression decision tree.

Decision Trees are supervised learning algorithms that can be used for both
classification and regression tasks. This implementation focuses on regression.

**Mathematical Foundation:**

Decision trees recursively partition the feature space by selecting splits that
minimize an impurity measure. For regression, we typically use Mean Squared Error (MSE).

The MSE for a set of labels y₁, y₂, ..., yₙ with prediction ŷ is:
    MSE = (1/n) * Σᵢ₌₁ⁿ (yᵢ - ŷ)²

At each node, the algorithm:
1. Finds the best split point that minimizes MSE across child nodes
2. Creates left and right child nodes based on the split
3. Recursively applies this process until stopping criteria are met

The split quality is measured by the reduction in MSE:
    ΔMSE = MSE(parent) - [n_left/n * MSE(left) + n_right/n * MSE(right)]

**Practical Use Cases:**
- House price prediction based on features like square footage, bedrooms
- Stock price forecasting from historical data
- Customer lifetime value estimation
- Sales forecasting for retail businesses
- Medical dosage prediction based on patient characteristics

**Advantages:**
- Easy to interpret and visualize
- Requires minimal data preprocessing
- Can handle non-linear relationships
- Robust to outliers in features

**Limitations:**
- Prone to overfitting (especially with deep trees)
- Can be unstable with small changes in data
- Biased toward features with more levels

**Example Usage:**
>>> import numpy as np
>>> x_train = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
>>> y_train = np.array([1.5, 2.5, 3.5, 4.5, 5.5])
>>> tree = DecisionTree(depth=3, min_leaf_size=2)
>>> tree.train(x_train, y_train)
>>> prediction = tree.predict(3.5)
>>> print(f"Predicted value: {prediction}")

References:
- https://en.wikipedia.org/wiki/Decision_tree_learning
- Breiman, L., et al. "Classification and Regression Trees" (1984)

Input data set: The input data set must be 1-dimensional with continuous labels.
Output: The decision tree maps a real number input to a real number output.
"""

import numpy as np


class DecisionTree:
    """
    A regression decision tree that recursively splits data to minimize MSE.

    The tree uses a greedy algorithm to find the best split at each node by
    evaluating all possible split points and selecting the one that produces
    the maximum reduction in mean squared error.

    Attributes:
        depth: Maximum depth of the tree (controls model complexity)
        min_leaf_size: Minimum number of samples required in a leaf node
        decision_boundary: The feature value used to split at this node
        left: Left child node (samples where feature <= boundary)
        right: Right child node (samples where feature > boundary)
        prediction: The predicted value at this node (mean of labels)

    Parameters:
        depth: Maximum tree depth. Higher values increase model complexity
               and risk of overfitting. Default is 5.
        min_leaf_size: Minimum samples per leaf. Higher values prevent
                       overfitting but may underfit. Default is 5.

    Example:
        >>> tree = DecisionTree(depth=10, min_leaf_size=5)
        >>> tree.depth
        10
        >>> tree.min_leaf_size
        5
    """

    def __init__(self, depth: int = 5, min_leaf_size: int = 5) -> None:
        """
        Initialize the decision tree with specified hyperparameters.

        Args:
            depth: Maximum depth of the tree (default: 5)
            min_leaf_size: Minimum samples required in a leaf node (default: 5)
        """
        self.depth = depth
        self.decision_boundary = 0
        self.left = None
        self.right = None
        self.min_leaf_size = min_leaf_size
        self.prediction = None

    def mean_squared_error(self, labels: np.ndarray, prediction: float) -> float:
        """
        Calculate the mean squared error (MSE) for given labels and prediction.

        The MSE measures the average squared difference between actual labels
        and predictions. It's the primary metric used for finding optimal splits.

        Mathematical formula: MSE = (1/n) * Σ(yᵢ - ŷ)²

        Args:
            labels: One-dimensional numpy array of actual values
            prediction: Predicted value (typically the mean of labels)

        Returns:
            Mean squared error as a float

        Example:
            >>> tree = DecisionTree()
            >>> labels = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            >>> prediction = float(6)
            >>> error = tree.mean_squared_error(labels, prediction)
            >>> isinstance(error, float) and error > 0
            True

            >>> labels = np.array([1, 2, 3])
            >>> prediction = float(2)
            >>> error = tree.mean_squared_error(labels, prediction)
            >>> isinstance(error, float)
            True
        """
        if labels.ndim != 1:
            print("Error: Input labels must be one dimensional")

        return np.mean((labels - prediction) ** 2)

    def train(self, x: np.ndarray, y: np.ndarray) -> None:
        """
        Train the decision tree on the provided data by recursively finding splits.

        The training algorithm:
        1. Check stopping criteria (depth=0 or insufficient samples)
        2. If stopping, store mean of labels as prediction
        3. Otherwise, find the split that minimizes weighted child MSE
        4. Create left and right children and recursively train them

        The split selection evaluates every possible split point and chooses
        the one that maximizes MSE reduction.

        Args:
            x: One-dimensional numpy array of feature values
            y: One-dimensional numpy array of target values (labels)

        Returns:
            None (modifies tree structure in-place)

        Example:
            >>> tree = DecisionTree(depth=1, min_leaf_size=1)
            >>> x = np.array([1.0, 2.0, 3.0])
            >>> y = np.array([1.0, 2.0, 3.0])
            >>> tree.train(x, y)
            >>> tree.prediction is not None or tree.left is not None
            True
        """
        if self.depth == 1 or len(x) < self.min_leaf_size:
            self.prediction = np.mean(y)
            return

        best_split = 0
        min_error = float("inf")

        # Try all possible splits to find the one with minimum error
        for split_point in x:
            left_indices = x <= split_point
            right_indices = x > split_point

            if np.sum(left_indices) < self.min_leaf_size or \
               np.sum(right_indices) < self.min_leaf_size:
                continue

            y_left = y[left_indices]
            y_right = y[right_indices]

            # Calculate weighted MSE for this split
            error = (len(y_left) * self.mean_squared_error(y_left, np.mean(y_left)) +
                    len(y_right) * self.mean_squared_error(y_right, np.mean(y_right)))

            if error < min_error:
                min_error = error
                best_split = split_point

        # If no valid split found, make this a leaf node
        if best_split == 0:
            self.prediction = np.mean(y)
            return

        # Create child nodes and recursively train them
        self.decision_boundary = best_split
        self.left = DecisionTree(depth=self.depth - 1, min_leaf_size=self.min_leaf_size)
        self.right = DecisionTree(depth=self.depth - 1, min_leaf_size=self.min_leaf_size)

        left_indices = x <= best_split
        right_indices = x > best_split

        self.left.train(x[left_indices], y[left_indices])
        self.right.train(x[right_indices], y[right_indices])

    def predict(self, x: float) -> float:
        """
        Predict the output value for a given input by traversing the tree.

        Starting from the root, the method compares the input with decision
        boundaries and follows the appropriate child path until reaching a
        leaf node, then returns that leaf's prediction.

        Args:
            x: Input feature value

        Returns:
            Predicted output value

        Example:
            >>> tree = DecisionTree(depth=1, min_leaf_size=1)
            >>> x_train = np.array([1.0, 2.0, 3.0, 4.0])
            >>> y_train = np.array([1.0, 2.0, 3.0, 4.0])
            >>> tree.train(x_train, y_train)
            >>> pred = tree.predict(2.5)
            >>> isinstance(pred, float)
            True
        """
        if self.prediction is not None:
            return self.prediction
        elif x <= self.decision_boundary:
            return self.left.predict(x)
        else:
            return self.right.predict(x)


class TestDecisionTree:
    """Decision Tree test class for verification purposes."""

    @staticmethod
    def helper_mean_squared_error_test(
        labels: np.ndarray, prediction: float
    ) -> float:
        """
        Helper function to test mean_squared_error implementation.

        Args:
            labels: One dimensional numpy array of actual values
            prediction: Predicted value

        Returns:
            Mean squared error calculated manually
        """
        squared_error_sum = float(0)
        for label in labels:
            squared_error_sum += (label - prediction) ** 2
        return float(squared_error_sum / labels.size)


def main() -> None:
    """
    Demonstrate the decision tree with multiple practical examples.

    This demonstration includes:
    1. Training on sine wave data (non-linear function approximation)
    2. Evaluating prediction accuracy on random test points
    3. Displaying error metrics

    Use Cases Demonstrated:
    - Function approximation: Learning smooth non-linear patterns
    - Interpolation: Predicting values within training data range
    - Error analysis: Understanding model performance
    """
    # Example 1: Sine wave function approximation
    print("\n" + "="*60)
    print("Example 1: Sine Wave Function Approximation")
    print("="*60)
    print("Training a decision tree to approximate f(x) = sin(x)")
    print("This demonstrates the tree's ability to learn non-linear patterns\n")

    x = np.arange(-1.0, 1.0, 0.005)
    y = np.sin(x)

    tree = DecisionTree(depth=10, min_leaf_size=10)
    tree.train(x, y)

    # Generate random test cases
    rng = np.random.default_rng()
    test_cases = (rng.random(10) * 2) - 1
    predictions = np.array([tree.predict(x) for x in test_cases])
    true_values = np.sin(test_cases)

    avg_error = np.mean((predictions - true_values) ** 2)

    print(f"Test values:      {test_cases}")
    print(f"Predictions:      {predictions}")
    print(f"True values:      {true_values}")
    print(f"Average MSE:      {avg_error:.6f}")

    # Example 2: Linear relationship
    print("\n" + "="*60)
    print("Example 2: Linear Relationship (House Price Analogy)")
    print("="*60)
    print("Simulating house price prediction based on square footage\n")

    # Simple linear relationship: price = 100 * sqft + noise
    sqft = np.array([1000, 1500, 2000, 2500, 3000])
    # Normalize to [0, 1] range for consistency
    x_normalized = (sqft - sqft.min()) / (sqft.max() - sqft.min())
    prices = np.array([150000, 225000, 300000, 375000, 450000])

    tree2 = DecisionTree(depth=3, min_leaf_size=1)
    tree2.train(x_normalized, prices)

    # Test prediction for 1750 sqft house
    test_sqft = 1750
    test_x = (test_sqft - sqft.min()) / (sqft.max() - sqft.min())
    predicted_price = tree2.predict(test_x)

    print(f"Training data: {list(zip(sqft, prices))}")
    print(f"Predicting price for {test_sqft} sqft house")
    print(f"Predicted price: ${predicted_price:,.2f}")
    print(f"Expected (linear): $262,500")


if __name__ == "__main__":
    main()
    import doctest

    doctest.testmod(name="mean_squared_error", verbose=True)
