import numpy as np


def grid_search_cv(model, param_grid, X, y, cv=5):
    best_score = None
    best_params = None

    # Generate all possible parameter combinations
    param_combinations = np.array(np.meshgrid(*param_grid.values())).T.reshape(
        -1, len(param_grid)
    )

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
