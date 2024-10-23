import numpy as np

"""# Ridge Regression Class
class RidgeRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000, regularization_param=0.1):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.regularization_param = regularization_param
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        
        # initializing weights and bias
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # gradient descent
        for _ in range(self.num_iterations):
            y_predicted = np.dot(X, self.weights) + self.bias
            
            # gradients for weights and bias
            dw = (1/n_samples) * np.dot(X.T, (y_predicted - y)) + (self.regularization_param / n_samples) * self.weights
            db = (1/n_samples) * np.sum(y_predicted - y)
            
            # updating weights and bias
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

    def mean_absolute_error(self, y_true, y_pred):
        return np.mean(np.abs(y_true - y_pred))

# Load Data Function
def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file.readlines()[1:]:  
            features = line.strip().split(',')
            data.append([float(f) for f in features])
    return np.array(data)

# Example usage
if __name__ == "__main__":
    
    data = load_data('ADRvsRating.csv')
    X = data[:, 0].reshape(-1, 1)  # independent features
    y = data[:, 1]  # dependent variable
    
    # initializing and training Ridge Regression model
    model = RidgeRegression(learning_rate=0.001, num_iterations=1000, regularization_param=0.1)
    model.fit(X, y)
    
    # predictions
    predictions = model.predict(X)
    
    # mean absolute error
    mae = model.mean_absolute_error(y, predictions)
    print(f"Mean Absolute Error: {mae}")
    
    # final output weights and bias
    print(f"Optimized Weights: {model.weights}")
    print(f"Bias: {model.bias}")"""

import pandas as pd
class RidgeRegression:
    def __init__(self, alpha=0.001, lambda_=0.1, iterations=1000):
        self.alpha = alpha
        self.lambda_ = lambda_
        self.iterations = iterations
        self.theta = None

    def feature_scaling(self, X):
        mean = np.mean(X, axis=0)
        std = np.std(X, axis=0)
        # avoid division by zero for constant features (std = 0)
        std[std == 0] = 1  # set std=1 for constant features to avoid NaN
        X_scaled = (X - mean) / std
        return X_scaled, mean, std
    
    def fit(self, X, y):
        X_scaled, mean, std = self.feature_scaling(X)
        m, n = X_scaled.shape
        self.theta = np.zeros(n)  # initializing weights to zeros
        for i in range(self.iterations):
            predictions = X_scaled.dot(self.theta)
            error = predictions - y
            # computing gradient with L2 regularization
            gradient = (X_scaled.T.dot(error) + self.lambda_ * self.theta) / m
            self.theta -= self.alpha * gradient  # updating weights

    def predict(self, X):
        X_scaled, _, _ = self.feature_scaling(X)
        return X_scaled.dot(self.theta)
    
    def compute_cost(self, X, y):
        X_scaled, _, _ = self.feature_scaling(X)  
        m = len(y)
        predictions = X_scaled.dot(self.theta)
        cost = (1 / (2 * m)) * np.sum((predictions - y) ** 2) + (
            self.lambda_ / (2 * m)
        ) * np.sum(self.theta**2)
        return cost
    
    def mean_absolute_error(self, y_true, y_pred):
        return np.mean(np.abs(y_true - y_pred))
# Example usage
if __name__ == "__main__":
    df = pd.read_csv("ADRvsRating.csv")
    X = df[["Rating"]].values
    y = df["ADR"].values
    y = (y - np.mean(y)) / np.std(y)

    # Add bias term (intercept) to the feature matrix
    X = np.c_[np.ones(X.shape[0]), X] 

    # initialize and train the Ridge Regression model
    model = RidgeRegression(alpha=0.01, lambda_=0.1, iterations=1000)
    model.fit(X, y)

    # predictions
    predictions = model.predict(X)

    # results
    print("Optimized Weights:", model.theta)
    print("Cost:", model.compute_cost(X, y))
    print("Mean Absolute Error:", model.mean_absolute_error(y, predictions))