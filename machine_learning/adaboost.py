
import numpy as np

# AdaBoost implementation for binary classification
# Uses decision stumps (one-level trees) as weak learners
class AdaBoost:
    def __init__(self, n_estimators=50):
        # Number of boosting rounds
        self.n_estimators = n_estimators
        self.alphas = []  # Weights for each weak learner
        self.models = []  # List of weak learners (stumps)

    def fit(self, X, y):
        # X: (n_samples, n_features), y: (n_samples,) with labels 0 or 1
        n_samples, n_features = X.shape
        w = np.ones(n_samples) / n_samples  # Initialize sample weights
        self.models = []
        self.alphas = []
        y_ = np.where(y == 0, -1, 1)  # Convert labels to -1, 1
        for _ in range(self.n_estimators):
            # Train a decision stump with weighted samples
            stump = self._build_stump(X, y_, w)
            pred = stump['pred']
            err = stump['error']
            # Compute alpha (learner weight)
            alpha = 0.5 * np.log((1 - err) / (err + 1e-10))
            # Update sample weights
            w *= np.exp(-alpha * y_ * pred)
            w /= np.sum(w)
            self.models.append(stump)
            self.alphas.append(alpha)

    def predict(self, X):
        # Aggregate predictions from all weak learners
        clf_preds = np.zeros(X.shape[0])
        for alpha, stump in zip(self.alphas, self.models):
            pred = self._stump_predict(X, stump['feature'], stump['threshold'], stump['polarity'])
            clf_preds += alpha * pred
        # Return final prediction (majority vote)
        return np.where(clf_preds >= 0, 1, 0)

    def _build_stump(self, X, y, w):
        # Find the best decision stump for current weights
        n_samples, n_features = X.shape
        min_error = float('inf')
        best_stump = {}
        for feature in range(n_features):
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                for polarity in [1, -1]:
                    pred = self._stump_predict(X, feature, threshold, polarity)
                    error = np.sum(w * (pred != y))
                    if error < min_error:
                        min_error = error
                        best_stump = {
                            'feature': feature,
                            'threshold': threshold,
                            'polarity': polarity,
                            'error': error,
                            'pred': pred.copy()
                        }
        return best_stump

    def _stump_predict(self, X, feature, threshold, polarity):
        # Predict using a single decision stump
        pred = np.ones(X.shape[0])
        if polarity == 1:
            pred[X[:, feature] < threshold] = -1
        else:
            pred[X[:, feature] > threshold] = -1
        return pred
