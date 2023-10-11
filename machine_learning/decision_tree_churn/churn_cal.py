from pathlib import Path

import numpy as np
import pandas as pd
from sklearn import model_selection, tree


def calculate_churn_rate(filename: str = "churn_modelling.csv") -> np.ndarray:
    """
    Calculate the churn rate of customers using a decision tree classifier.

    >>> calculate_churn_rate()
    array([0, 0, 0, 0, 1])
    """

    churn_md = pd.read_csv(Path(__file__).with_name(filename).absolute())

    # Sort the dependent and independent values
    x = churn_md[
        [
            "CreditScore",
            "Age",
            "Tenure",
            "Balance",
            "NumOfProducts",
            "HasCrCard",
            "IsActiveMember",
            "EstimatedSalary",
        ]
    ].values
    y = churn_md["Exited"]

    # Split the dataset into training and testing data
    x_test, x_train, y_test, y_train = model_selection.train_test_split(
        x, y, test_size=0.3, random_state=3
    )

    # Create the decision tree classifier
    decision_tree = tree.DecisionTreeClassifier(criterion="entropy", max_depth=4)
    decision_tree.fit(x_train, y_train)

    # Returning the predicted values
    return decision_tree.predict(x_test)


if __name__ == "__main__":
    from doctest import testmod

    doctest.testmod()
    print(f"{calculate_churn_rate('churn_modelling.csv') = }")
