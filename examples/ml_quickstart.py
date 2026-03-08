"""Quick start examples for recently restored ML algorithms."""

from __future__ import annotations

import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from machine_learning.gaussian_naive_bayes import GaussianNaiveBayes
from machine_learning.gradient_boosting_regressor import GradientBoostingRegressor
from machine_learning.random_forest_classifier import RandomForestClassifier
from machine_learning.random_forest_regressor import RandomForestRegressor


def run_demo() -> None:
    gnb = GaussianNaiveBayes().fit([[1.0], [1.2], [3.9], [4.1]], [0, 0, 1, 1])
    print("GaussianNB:", gnb.predict([[1.1], [4.0]]))

    rf_clf = RandomForestClassifier(num_trees=21, random_seed=7)
    rf_clf.fit([[0.0], [0.2], [0.9], [1.0]], [0, 0, 1, 1])
    print("RandomForestClassifier:", rf_clf.predict([[0.1], [0.95]]))

    rf_reg = RandomForestRegressor(num_trees=21, random_seed=7)
    rf_reg.fit([[0.0], [1.0], [2.0], [3.0]], [0.0, 1.0, 2.0, 3.0])
    print(
        "RandomForestRegressor:", [round(v, 3) for v in rf_reg.predict([[0.5], [2.5]])]
    )

    gbr = GradientBoostingRegressor(num_estimators=50, learning_rate=0.05)
    gbr.fit([[0.0], [1.0], [2.0], [3.0]], [0.0, 1.0, 2.0, 3.0])
    print(
        "GradientBoostingRegressor:",
        [round(v, 3) for v in gbr.predict([[0.5], [2.5]])],
    )


if __name__ == "__main__":
    run_demo()
