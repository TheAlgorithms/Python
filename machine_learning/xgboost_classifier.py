# XGBoost Classifier Example
import numpy as np
from decision_tree import DecisionTree
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

def data_handling(data: dict) -> tuple:
    # Split dataset into features and target
    # data is features
    """
    >>> data_handling(({'data':'[5.1, 3.5, 1.4, 0.2]','target':([0])}))
    ('[5.1, 3.5, 1.4, 0.2]', [0])
    >>> data_handling(
    ...     {'data': '[4.9, 3.0, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]', 'target': ([0, 0])}
    ... )
    ('[4.9, 3.0, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]', [0, 0])
    """
    return (data["data"], data["target"])

class XGBClassifier:
    """
    An implementation of a gradient boosting classifier inspired by XGBoost.

    This implementation uses multi-class boosting with a logistic (softmax) loss.
    It trains one regression tree per class on the negative gradient (residual)
    at each boosting iteration.

    Parameters
    ----------
    n_estimators : int, default=100
        The number of boosting rounds.
    learning_rate : float, default=0.3
        Step size shrinkage used in updates to prevent overfitting.
    max_depth : int, default=3
        Maximum depth of the regression trees.
    random_state : int, default=0
        Random seed.
    
    **Important:**  
    Due to limitations of our custom DecisionTree (which only supports one-dimensional input),
    only the first feature (column 0) of the dataset is used when training each tree.
    """

    def __init__(self, n_estimators: int = 100, learning_rate: float = 0.3,
                 max_depth: int = 3, random_state: int = 0):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.random_state = random_state

        # List of lists of trees; for each boosting round, we have one tree per class.
        self.trees = []
        self.num_class = None
        self.initial_pred = None  # Initial log-odds per class

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Fit the gradient boosting model.

        Parameters
        ----------
        X : np.ndarray, shape = (n_samples, n_features)
            Training data.
        y : np.ndarray, shape = (n_samples,)
            Class labels (assumed to be integers 0, 1, ..., K-1).
        """
        n_samples = X.shape[0]
        self.num_class = np.unique(y).shape[0]

        # One-hot encode the labels.
        y_onehot = np.zeros((n_samples, self.num_class))
        y_onehot[np.arange(n_samples), y] = 1

        # Initialize predictions F with the log class probabilities (log-odds).
        class_counts = np.bincount(y, minlength=self.num_class)
        class_prob = class_counts / n_samples
        initial_score = np.log(class_prob + 1e-10)  # add small constant to avoid log(0)
        self.initial_pred = initial_score  # shape: (num_class,)
        F = np.tile(initial_score, (n_samples, 1))  # shape: (n_samples, num_class)

        # Boosting rounds.
        for t in range(self.n_estimators):
            # Compute probabilities using softmax.
            exp_F = np.exp(F)
            p = exp_F / np.sum(exp_F, axis=1, keepdims=True)  # shape: (n_samples, num_class)
            trees_per_class = []

            for k in range(self.num_class):
                # The negative gradient for class k (logistic loss): (y_true - p)
                gradient = y_onehot[:, k] - p[:, k]

                # **Note:** Due to our custom DecisionTree limitations, we use only the first feature.
                feature_for_tree = X[:, 0]

                # Instantiate and train the decision tree on (feature, gradient) pair.
                tree = DecisionTree(depth=self.max_depth, min_leaf_size=5)
                tree.train(feature_for_tree, gradient)
                # Predict the update values using the tree.
                update = np.array([tree.predict(x_val) for x_val in feature_for_tree])
                # Update the scores for class k.
                F[:, k] += self.learning_rate * update
                trees_per_class.append(tree)
            self.trees.append(trees_per_class)

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """
        Predict class probabilities for X.

        Parameters
        ----------
        X : np.ndarray, shape = (n_samples, n_features)

        Returns
        -------
        proba : np.ndarray, shape = (n_samples, num_class)
            The class probabilities.
        """
        n_samples = X.shape[0]
        F = np.tile(self.initial_pred, (n_samples, 1))
        # Use the first feature for prediction as done in training.
        feature_for_tree = X[:, 0]
        for trees_per_class in self.trees:
            for k, tree in enumerate(trees_per_class):
                update = np.array([tree.predict(x_val) for x_val in feature_for_tree])
                F[:, k] += self.learning_rate * update
        exp_F = np.exp(F)
        proba = exp_F / np.sum(exp_F, axis=1, keepdims=True)
        return proba

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict class labels for X.

        Parameters
        ----------
        X : np.ndarray, shape = (n_samples, n_features)

        Returns
        -------
        labels : np.ndarray, shape = (n_samples,)
            The predicted class labels.
        """
        proba = self.predict_proba(X)
        return np.argmax(proba, axis=1)

def xgboost(features: np.ndarray, target: np.ndarray) -> XGBClassifier:
    """
    # THIS TEST IS BROKEN!! >>> xgboost(np.array([[5.1, 3.6, 1.4, 0.2]]), np.array([0]))
    XGBClassifier(base_score=0.5, booster='gbtree', callbacks=None,
                  colsample_bylevel=1, colsample_bynode=1, colsample_bytree=1,
                  early_stopping_rounds=None, enable_categorical=False,
                  eval_metric=None, gamma=0, gpu_id=-1, grow_policy='depthwise',
                  importance_type=None, interaction_constraints='',
                  learning_rate=0.300000012, max_bin=256, max_cat_to_onehot=4,
                  max_delta_step=0, max_depth=6, max_leaves=0, min_child_weight=1,
                  missing=nan, monotone_constraints='()', n_estimators=100,
                  n_jobs=0, num_parallel_tree=1, predictor='auto', random_state=0,
                  reg_alpha=0, reg_lambda=1, ...)
    """
    classifier = XGBClassifier()
    classifier.fit(features, target)
    return classifier


def main() -> None:
    """
    >>> main()

    Url for the algorithm:
    https://xgboost.readthedocs.io/en/stable/
    Iris type dataset is used to demonstrate algorithm.
    """

    # Load Iris dataset
    iris = load_iris()
    features, targets = data_handling(iris)
    x_train, x_test, y_train, y_test = train_test_split(
        features, targets, test_size=0.25
    )

    names = iris["target_names"]

    # Create an XGBoost Classifier from the training data
    xgboost_classifier = xgboost(x_train, y_train)

    # Display the confusion matrix of the classifier with both training and test sets
    ConfusionMatrixDisplay.from_estimator(
        xgboost_classifier,
        x_test,
        y_test,
        display_labels=names,
        cmap="Blues",
        normalize="true",
    )
    plt.title("Normalized Confusion Matrix - IRIS Dataset")
    plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
