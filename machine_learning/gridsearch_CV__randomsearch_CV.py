import typing
import random


def grid_search_cv(
    model: typing.Callable,
    params: typing.Dict[str, typing.List[typing.Any]],
    X_train: typing.List[typing.List[float]],
    y_train: typing.List[int],
    cv: int = 5,
) -> typing.Dict[str, typing.Any]:
    best_params = {}
    best_score = float("-inf")

    param_combinations = get_param_combinations(params)

    for p in param_combinations:
        # K-fold cross-validation
        kfold = KFold(n_splits=cv)
        fold_scores = cross_val_score(
            model, X_train, y_train, cv=kfold, scoring="accuracy"
        )
        mean_score = fold_scores.mean()

        if mean_score > best_score:
            best_score = mean_score
            best_params = p

    return best_params


def get_param_combinations(params):
    # Generate parameter combinations
    pass


def random_search_cv(
    model: typing.Callable,
    params: typing.Dict[str, typing.List[typing.Any]],
    X_train: typing.List[typing.List[float]],
    y_train: typing.List[int],
    n_iter: int = 10,
    cv: int = 5,
) -> typing.Dict[str, typing.Any]:
    best_params = {}
    best_score = float("-inf")

    for i in range(n_iter):
        # Sample random hyperparameters
        sample_params = sample_params(params)

        # Cross-validate
        kfold = KFold(n_splits=cv)
        cv_scores = cross_val_score(
            model, X_train, y_train, cv=kfold, scoring="accuracy"
        )
        mean_score = cv_scores.mean()

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
