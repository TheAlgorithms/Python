import doctest

import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

""""
Implementation of basic AdaBoost classifier on iris dataset.
The following classifier uses a pre-built DecisionTreeClassifier
from scikit-learn as a weak learner.

AdaBoost (Adaptive Boosting) is an ensemble learning technique 
used for classification problems. It combines multiple weak learners 
(in this case, decision trees with maximum depth 1) to create a strong classifier. 
The key idea behind AdaBoost is to give more weight to the training instances that 
are misclassified by the previous weak learners, 
so that subsequent weak learners focus more on these misclassified instances.
"""

class AdaBoost:
    def __init__(self, n_estimators=50):
        self.n_estimators = n_estimators
        self.alphas = []  # List to store alpha values
        self.models = []  # List to store individual decision tree models

    def train(self, X, y):
        n_samples, _ = X.shape
        w = np.full(n_samples, 1 / n_samples)  # Initialize sample weights

        for _ in range(self.n_estimators):
            model = DecisionTreeClassifier(max_depth=1)  # Create a decision tree model
            model.fit(X, y, sample_weight=w)  # Fit the model using weighted samples
            y_pred = model.predict(X)  # Predict labels with the current model

            err = np.dot(w, y_pred != y) / np.sum(w)  # Calculate the weighted error

            alpha = 0.5 * np.log((1 - err) / max(err, 1e-10))  # Calculate alpha for the model
            w = w * np.exp(-alpha * y * y_pred)  # Update sample weights
            w /= np.sum(w)  # Normalize the weights

            self.alphas.append(alpha)  # Store the alpha value for this model
            self.models.append(model)  # Store the model itself

    def predict(self, X):
        n_samples, _ = X.shape
        results = np.zeros(n_samples)  # Initialize results array

        for alpha, model in zip(self.alphas, self.models):
            results += alpha * model.predict(X)  # Weighted combination of model predictions

        return np.sign(results)  # Convert results into binary classification

def main():
    # Generate a sample dataset
    np.random.seed(0)
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Train AdaBoost
    adaboost = AdaBoost(n_estimators=50)
    adaboost.train(X, y)

    # Make predictions
    predictions = adaboost.predict(X)

    # Calculate accuracy
    accuracy = np.mean(predictions == y)
    print(f'Accuracy: {accuracy}')

if __name__ == "__main__":
    doctest.testmod(verbose=True)  # Run doctests for documentation
    main()  # Execute the AdaBoost algorithm and display accuracy
