#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Correlation-based Feature Selection (CFS):
Wikipedia Reference: Feature Selection - https://en.wikipedia.org/wiki/Feature_selection#Correlation-Based_Feature_Selection_(CFS)

Chi-squared (χ²) Test:
Wikipedia Reference: https://en.wikipedia.org/wiki/Chi-squared_test

Recursive Feature Elimination (RFE):
Wikipedia Reference: https://en.wikipedia.org/wiki/Feature_selection#Recursive_feature_elimination_(RFE)

Gravitational Search Algorithm (GSA):
Reference: https://link.springer.com/article/10.1007/s11042-020-09831-4#:~:text=
Gravitational%20search%20algorithm%20is%20a,efficiently%20solve%20complex%20optimization%20problems.
"""


import numpy as np
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, f_classif, chi2
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def cfs_feature_selection(X, y, k=2):
    """
    Perform Correlation-based Feature Selection (CFS).

    @params:
        X: Input feature matrix.
        y: Target variable.
        k: Number of top features to select (default is 2).

    @returns:
        X_selected: Feature matrix with selected features.
    """
    selector = SelectKBest(score_func=f_classif, k=k)
    X_selected = selector.fit_transform(X, y)
    return X_selected


def chi2_feature_selection(X, y, k=2):
    """
    Perform feature selection using the Chi-squared (χ²) Test.

    @params:
        X: Input feature matrix.
        y: Target variable.
        k: Number of top features to select (default is 2).

    @returns:
        X_selected: Feature matrix with selected features.
    """
    selector = SelectKBest(score_func=chi2, k=k)
    X_selected = selector.fit_transform(X, y)
    return X_selected


def rfe_feature_selection(X, y, num_features=2):
    """
    Perform Recursive Feature Elimination (RFE) with Logistic Regression.

    @params:
        X: Input feature matrix.
        y: Target variable.
        num_features: Number of features to select (default is 2).

    @returns:
        X_selected: Feature matrix with selected features.
    """
    model = LogisticRegression()
    rfe = RFE(model, num_features)
    X_selected = rfe.fit_transform(X, y)
    return X_selected


def gsa_feature_selection(X, y, population_size=50, max_iterations=100):
    """
    Perform feature selection using the Gravitational Search Algorithm (GSA).

    @params:
        X: Input feature matrix.
        y: Target variable.
        population_size: Size of the population in GSA (default is 50).
        max_iterations: Maximum number of GSA iterations (default is 100).

    @returns:
        best_solution: The optimal subset of features.
        best_fitness: The fitness (accuracy) of the best solution.
    """

    def fitness_function(selected_features):
        clf = RandomForestClassifier(random_state=42)
        clf.fit(X_train[:, selected_features], y_train)
        accuracy = clf.score(X_test[:, selected_features], y_test)
        return accuracy

    # Initialize GSA parameters
    population = np.random.choice(
        [0, 1], size=(population_size, X.shape[1]), replace=True
    )
    best_solution = None
    best_fitness = 0

    for iteration in range(max_iterations):
        # Calculate fitness for each solution in the population
        fitness_values = [
            fitness_function(selected_features) for selected_features in population
        ]

        # Find the best solution
        best_index = np.argmax(fitness_values)
        current_best_fitness = fitness_values[best_index]

        if current_best_fitness > best_fitness:
            best_solution = population[best_index]
            best_fitness = current_best_fitness

        # Update positions using gravitational forces (simplified example)
        # You can implement the GSA gravitational force calculation here

        # Apply mass redistribution (optional)

    return best_solution, best_fitness


# Example usage:
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

X_cfs = cfs_feature_selection(X, y, k=2)
X_chi2 = chi2_feature_selection(X, y, k=2)
X_rfe = rfe_feature_selection(X, y, num_features=2)
best_gsa_solution, best_gsa_fitness = gsa_feature_selection(
    X, y, population_size=50, max_iterations=100
)

print("CFS Selected Features:", X_cfs.shape[1])
print("Chi-squared Selected Features:", X_chi2.shape[1])
print("RFE Selected Features:", X_rfe.shape[1])
print("Best GSA Subset of Features:", best_gsa_solution)
print("Best GSA Fitness (Accuracy):", best_gsa_fitness)
