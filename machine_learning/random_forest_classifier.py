"""Random Forest Classifier implementation from scratch.

This module implements a Random Forest Classifier using:
- Decision Tree base learners built from scratch
- Bootstrap sampling (bagging)
- Random feature selection at splits
- Majority voting for aggregation
"""

import numpy as np
from collections import Counter


class DecisionTreeClassifier:
    """A Decision Tree Classifier built from scratch.
    
    This tree uses information gain (entropy-based) for splitting decisions.
    
    Attributes:
        max_depth: Maximum depth of the tree
        min_samples_split: Minimum samples required to split a node
        n_features: Number of features to consider for best split
        tree: The built tree structure
    """

    def __init__(self, max_depth=10, min_samples_split=2, n_features=None):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.n_features = n_features
        self.tree = None

    def fit(self, X, y):
        """Build the decision tree.
        
        Args:
            X: Training features, shape (n_samples, n_features)
            y: Training labels, shape (n_samples,)
        """
        self.n_features = X.shape[1] if not self.n_features else min(self.n_features, X.shape[1])
        self.tree = self._grow_tree(X, y)

    def _grow_tree(self, X, y, depth=0):
        """Recursively grow the decision tree."""
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))

        # Stopping criteria
        if depth >= self.max_depth or n_labels == 1 or n_samples < self.min_samples_split:
            leaf_value = self._most_common_label(y)
            return {'leaf': True, 'value': leaf_value}

        # Find best split
        feat_idxs = np.random.choice(n_features, self.n_features, replace=False)
        best_feat, best_thresh = self._best_split(X, y, feat_idxs)

        if best_feat is None:
            leaf_value = self._most_common_label(y)
            return {'leaf': True, 'value': leaf_value}

        # Split the data
        left_idxs = X[:, best_feat] <= best_thresh
        right_idxs = ~left_idxs

        # Grow subtrees
        left = self._grow_tree(X[left_idxs], y[left_idxs], depth + 1)
        right = self._grow_tree(X[right_idxs], y[right_idxs], depth + 1)

        return {
            'leaf': False,
            'feature': best_feat,
            'threshold': best_thresh,
            'left': left,
            'right': right
        }

    def _best_split(self, X, y, feat_idxs):
        """Find the best feature and threshold to split on."""
        best_gain = -1
        split_idx, split_thresh = None, None

        for feat_idx in feat_idxs:
            X_column = X[:, feat_idx]
            thresholds = np.unique(X_column)

            for threshold in thresholds:
                gain = self._information_gain(y, X_column, threshold)

                if gain > best_gain:
                    best_gain = gain
                    split_idx = feat_idx
                    split_thresh = threshold

        return split_idx, split_thresh

    def _information_gain(self, y, X_column, threshold):
        """Calculate information gain from a split."""
        # Parent entropy
        parent_entropy = self._entropy(y)

        # Create children
        left_idxs = X_column <= threshold
        right_idxs = ~left_idxs

        if np.sum(left_idxs) == 0 or np.sum(right_idxs) == 0:
            return 0

        # Calculate weighted average entropy of children
        n = len(y)
        n_left, n_right = np.sum(left_idxs), np.sum(right_idxs)
        e_left, e_right = self._entropy(y[left_idxs]), self._entropy(y[right_idxs])
        child_entropy = (n_left / n) * e_left + (n_right / n) * e_right

        # Information gain
        ig = parent_entropy - child_entropy
        return ig

    def _entropy(self, y):
        """Calculate entropy of a label distribution."""
        hist = np.bincount(y)
        ps = hist / len(y)
        return -np.sum([p * np.log2(p) for p in ps if p > 0])

    def _most_common_label(self, y):
        """Return the most common label."""
        counter = Counter(y)
        return counter.most_common(1)[0][0]

    def predict(self, X):
        """Predict class labels for samples in X.
        
        Args:
            X: Features, shape (n_samples, n_features)
            
        Returns:
            Predicted labels, shape (n_samples,)
        """
        return np.array([self._traverse_tree(x, self.tree) for x in X])

    def _traverse_tree(self, x, node):
        """Traverse the tree to make a prediction for a single sample."""
        if node['leaf']:
            return node['value']

        if x[node['feature']] <= node['threshold']:
            return self._traverse_tree(x, node['left'])
        return self._traverse_tree(x, node['right'])


class RandomForestClassifier:
    """Random Forest Classifier built from scratch.
    
    Random Forest is an ensemble learning method that constructs multiple
    decision trees during training and outputs the mode of the classes
    (classification) of the individual trees.
    
    Features:
    - Bootstrap sampling (bagging) to create diverse trees
    - Random feature selection at each split
    - Majority voting for final predictions
    
    Attributes:
        n_estimators: Number of trees in the forest
        max_depth: Maximum depth of each tree
        min_samples_split: Minimum samples required to split a node
        n_features: Number of features to consider for best split
        trees: List of trained decision trees
    
    Example:
        >>> from sklearn.datasets import make_classification
        >>> from sklearn.model_selection import train_test_split
        >>> from sklearn.metrics import accuracy_score
        >>>
        >>> # Generate sample data
        >>> X, y = make_classification(n_samples=1000, n_features=20,
        ...                            n_informative=15, n_redundant=5,
        ...                            random_state=42)
        >>> X_train, X_test, y_train, y_test = train_test_split(
        ...     X, y, test_size=0.2, random_state=42)
        >>>
        >>> # Train Random Forest
        >>> rf = RandomForestClassifier(n_estimators=10, max_depth=10)
        >>> rf.fit(X_train, y_train)
        >>>
        >>> # Make predictions
        >>> y_pred = rf.predict(X_test)
        >>> print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    """

    def __init__(self, n_estimators=100, max_depth=10, min_samples_split=2, n_features=None):
        """Initialize Random Forest Classifier.
        
        Args:
            n_estimators: Number of trees in the forest (default: 100)
            max_depth: Maximum depth of each tree (default: 10)
            min_samples_split: Minimum samples required to split (default: 2)
            n_features: Number of features to consider for best split.
                       If None, uses sqrt(n_features) (default: None)
        """
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.n_features = n_features
        self.trees = []

    def fit(self, X, y):
        """Build a forest of trees from the training set (X, y).
        
        Args:
            X: Training features, shape (n_samples, n_features)
            y: Training labels, shape (n_samples,)
            
        Returns:
            self: Fitted classifier
        """
        self.trees = []
        n_features = X.shape[1]
        
        # Default to sqrt of total features if not specified
        if self.n_features is None:
            self.n_features = int(np.sqrt(n_features))

        for _ in range(self.n_estimators):
            tree = DecisionTreeClassifier(
                max_depth=self.max_depth,
                min_samples_split=self.min_samples_split,
                n_features=self.n_features
            )
            X_sample, y_sample = self._bootstrap_sample(X, y)
            tree.fit(X_sample, y_sample)
            self.trees.append(tree)
            
        return self

    def _bootstrap_sample(self, X, y):
        """Create a bootstrap sample from the dataset.
        
        Bootstrap sampling randomly samples with replacement from the dataset.
        This creates diverse training sets for each tree.
        
        Args:
            X: Features, shape (n_samples, n_features)
            y: Labels, shape (n_samples,)
            
        Returns:
            X_sample: Bootstrap sample of features
            y_sample: Bootstrap sample of labels
        """
        n_samples = X.shape[0]
        idxs = np.random.choice(n_samples, n_samples, replace=True)
        return X[idxs], y[idxs]

    def predict(self, X):
        """Predict class labels for samples in X.
        
        Uses majority voting: each tree votes for a class, and the
        class with the most votes becomes the final prediction.
        
        Args:
            X: Features, shape (n_samples, n_features)
            
        Returns:
            Predicted labels, shape (n_samples,)
        """
        # Get predictions from all trees
        tree_preds = np.array([tree.predict(X) for tree in self.trees])
        
        # Majority voting: transpose to get predictions per sample
        # then find most common prediction for each sample
        tree_preds = np.swapaxes(tree_preds, 0, 1)
        y_pred = [self._most_common_label(tree_pred) for tree_pred in tree_preds]
        return np.array(y_pred)

    def _most_common_label(self, y):
        """Return the most common label (majority vote)."""
        counter = Counter(y)
        return counter.most_common(1)[0][0]


if __name__ == "__main__":
    # Example usage with synthetic data
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, classification_report

    print("Random Forest Classifier - Example Usage")
    print("=" * 50)

    # Generate sample classification dataset
    X, y = make_classification(
        n_samples=1000,
        n_features=20,
        n_informative=15,
        n_redundant=5,
        random_state=42
    )

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print(f"Training samples: {X_train.shape[0]}")
    print(f"Test samples: {X_test.shape[0]}")
    print(f"Number of features: {X_train.shape[1]}")
    print()

    # Train Random Forest Classifier
    print("Training Random Forest Classifier...")
    rf_classifier = RandomForestClassifier(
        n_estimators=10,
        max_depth=10,
        min_samples_split=2
    )
    rf_classifier.fit(X_train, y_train)
    print("Training complete!")
    print()

    # Make predictions
    y_pred = rf_classifier.predict(X_test)

    # Evaluate
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f}")
    print()
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
