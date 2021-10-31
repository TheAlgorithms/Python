# Random Forest Feature Importance Example
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def main() -> None:

    """
    Random Forest Feature Importance Example using sklearn function.
    Iris type dataset is used to demonstrate algorithm.
    https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html
    """

    # Load Iris dataset
    iris = load_iris()

    # Split dataset into train and test data
    X = iris["data"]
    Y = iris["target"]
    x_train, x_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.3, random_state=1
    )

    # Random Forest Classifier
    rand_for = RandomForestClassifier(random_state=42, n_estimators=100)
    rand_for.fit(x_train, y_train)

    # Average importances and standard deviations
    importances = rand_for.feature_importances_
    std = np.std([tree.feature_importances_ for tree in rand_for.estimators_], axis=0)

    # Plot
    forest_importances = pd.Series(importances, index=iris["feature_names"])
    fig, ax = plt.subplots()
    forest_importances.plot.bar(yerr=std, ax=ax)
    ax.set_title("Feature importances using MDI")
    ax.set_ylabel("Mean decrease in impurity")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    import doctest
    main()
    doctest.testmod()
