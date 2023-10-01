import typing
import random

def grid_search_cv(
    model: typing.Callable,
    params: typing.Dict[str, typing.List[typing.Any]],
    X_train: typing.List[typing.List[float]],
    y_train: typing.List[int],
    cv: int = 5
) -> typing.Dict[str, typing.Any]:
    """
    Perform grid search cross-validation hyperparameters tuning.

    Args:
        model: Model function to tune
        params: Dictionary of hyperparameters to evaluate
        X_train: Training features
        y_train: Training labels
        cv: Number of cross-validation folds

    Returns:
        dict: Best hyperparameters
    """

    best_params = {}
    best_score = float('-inf')

    param_combinations = get_param_combinations(params)

    for p in param_combinations:

        # K-fold cross-validation
        fold_scores = []
        for _ in range(cv):
            X_train_split, X_val_split, y_train_split, y_val_split = split_data(X_train, y_train)

            model_clone = clone_model(model)
            model_clone.set_params(**p)
            model_clone.fit(X_train_split, y_train_split)

            val_score = evaluate(model_clone, X_val_split, y_val_split)
            fold_scores.append(val_score)

        mean_score = np.mean(fold_scores)

        if mean_score > best_score:
            best_score = mean_score
            best_params = p

    return best_params

# Helper functions
def get_param_combinations(params):
    keys = params.keys()
    combinations = [[]]

    for key in keys:
        values = params[key]
        new_combinations = []
        for combo in combinations:
            for value in values:
                new_combo = combo + [ (key, value) ]
                new_combinations.append(new_combo)
        combinations = new_combinations

    return combinations

def split_data(X, y, test_size=0.2):
    # Split X, y into train/validation splits
    pass

def clone_model(model):
    # Create a clone of model
    pass

def evaluate(model, X, y):
    # Evaluate model performance on X, y
    pass
```

```python
def random_search_cv(
    model: typing.Callable,
    params: typing.Dict[str, typing.List[typing.Any]],
    X_train: typing.List[typing.List[float]],
    y_train: typing.List[int],
    n_iter: int = 10,
    cv: int = 5
) -> typing.Dict[str, typing.Any]:
    """
    Perform random search cross-validation hyperparameters tuning.

    Args:
        model: Model function to tune
        params: Dictionary of hyperparameters to evaluate
        X_train: Training features
        y_train: Training labels
        n_iter: Number of iterations
        cv: Number of cross-validation folds

    Returns:
        dict: Best hyperparameters
    """

    best_params = {}
    best_score = float('-inf')

    for i in range(n_iter):

        # Sample random hyperparameters
        sample_params = sample_params(params)

        # Cross-validate
        cv_scores = cross_validate(model, sample_params, X_train, y_train, cv)

        mean_score = np.mean(cv_scores)

        if mean_score > best_score:
            best_score = mean_score
            best_params = sample_params

    return best_params

def sample_params(params):
    # Sample random hyperparameters
    pass

def cross_validate(model, params, X, y, cv):
    # Cross-validate model with k folds
    pass
