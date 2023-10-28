from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# Generate a random dataset
X, y = make_classification(
    n_samples=1000, n_features=20, n_informative=10, n_redundant=5, random_state=42
)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Define the parameter grid to search over
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [5, 10, 20],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4],
}

# Create a random forest classifier object
rf_clf = RandomForestClassifier(random_state=42)

# Create a grid search object
grid_search = GridSearchCV(rf_clf, param_grid=param_grid, cv=5)

# Fit the grid search object to the training data
grid_search.fit(X_train, y_train)

# Print the best hyperparameters found by the grid search
print(f"Best hyperparameters: {grid_search.best_params_}")

# Evaluate the performance of the classifier on the testing set using the best hyperparameters found by the grid search
accuracy = grid_search.score(X_test, y_test)
print(f"Accuracy: {accuracy:.2f}")
