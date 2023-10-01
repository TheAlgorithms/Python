# Import necessary libraries
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# Load a dataset (replace this with your dataset)
data = load_iris()
X = data.data
y = data.target

# Define the model you want to tune (replace with your own model)
model = RandomForestClassifier()

# Hyperparameters to tune
param_grid = {
    'n_estimators': [10, 50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Grid Search Cross-Validation
grid_search = GridSearchCV(model, param_grid, cv=5, n_jobs=-1)
grid_search.fit(X, y)

# Print the best hyperparameters and corresponding score
print("Grid Search Best Hyperparameters:", grid_search.best_params_)
print("Grid Search Best Score:", grid_search.best_score_)

# Random Search Cross-Validation
from scipy.stats import randint
param_dist = {
    'n_estimators': randint(10, 200),
    'max_depth': [None] + list(randint(10, 30, 4)),
    'min_samples_split': randint(2, 10),
    'min_samples_leaf': randint(1, 4)
}

random_search = RandomizedSearchCV(model, param_distributions=param_dist, n_iter=100, cv=5, n_jobs=-1)
random_search.fit(X, y)

# Print the best hyperparameters and corresponding score
print("Random Search Best Hyperparameters:", random_search.best_params_)
print("Random Search Best Score:", random_search.best_score_)
