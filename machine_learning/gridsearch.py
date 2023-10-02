import numpy as np

def grid_search_cv(model, param_grid, X, y, cv=5):
    best_score = None
    best_params = None
    
    # Generate all possible parameter combinations
    param_combinations = np.array(np.meshgrid(*param_grid.values())).T.reshape(-1, len(param_grid))
    
    for params in param_combinations:
        scores = []
        for train_idx, val_idx in cross_validate_indices(len(X), cv):
            X_train, X_val = X[train_idx], X[val_idx]
            y_train, y_val = y[train_idx], y[val_idx]
            
            # Fit the model with the current parameters
            model.set_params(**dict(zip(param_grid.keys(), params)))
            model.fit(X_train, y_train)
            
            # Evaluate the model on the validation set
            score = model.score(X_val, y_val)
            scores.append(score)
        
        # Calculate the mean score across folds
        mean_score = np.mean(scores)
        
        # Update the best score and parameters if necessary
        if best_score is None or mean_score > best_score:
            best_score = mean_score
            best_params = dict(zip(param_grid.keys(), params))
    
    return best_params, best_score

def cross_validate_indices(data_size, num_folds):
    indices = np.arange(data_size)
    fold_size = data_size // num_folds
    for i in range(num_folds):
        val_idx = indices[i * fold_size: (i + 1) * fold_size]
        train_idx = np.concatenate([indices[:i * fold_size], indices[(i + 1) * fold_size:]])
        yield train_idx, val_idx

# Example usage:
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Define the model and hyperparameter grid
model = LogisticRegression()
param_grid = {
    'C': [0.001, 0.01, 0.1, 1, 10],
    'solver': ['lbfgs', 'liblinear'],
}

# Perform GridSearchCV
best_params, best_score = grid_search_cv(model, param_grid, X, y, cv=5)
print("Best Parameters:", best_params)
print("Best Score:", best_score)
