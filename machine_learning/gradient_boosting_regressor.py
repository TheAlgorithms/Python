"""Implementation of GradientBoostingRegressor in sklearn using the
diabetes dataset, a popular regression problem used to predict
disease progression one year after baseline.

Note: this example previously used the Boston house-price dataset,
which was removed from scikit-learn (>=1.2) for ethical reasons.
``load_diabetes`` is a drop-in bundled alternative that ships with
scikit-learn, so the example runs offline.
"""

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def main():
    # loading the dataset from sklearn
    df = load_diabetes()
    print(df.keys())
    # now let's construct a data frame
    df_data = pd.DataFrame(df.data, columns=df.feature_names)
    # let's add the target to the dataframe
    df_data["Target"] = df.target
    # print the first five rows using the head function
    print(df_data.head())
    # Summary statistics
    print(df_data.describe().T)
    # Feature selection

    x = df_data.iloc[:, :-1]
    y = df_data.iloc[:, -1]  # target variable
    # split the data with 75% train and 25% test sets.
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, random_state=0, test_size=0.25
    )

    model = GradientBoostingRegressor(
        n_estimators=500, max_depth=5, min_samples_split=4, learning_rate=0.01
    )
    # training the model
    model.fit(x_train, y_train)
    # to see how good the model fit the data
    training_score = model.score(x_train, y_train).round(3)
    test_score = model.score(x_test, y_test).round(3)
    print("Training score of GradientBoosting is :", training_score)
    print("The test score of GradientBoosting is :", test_score)
    # Let us evaluate the model by finding the errors
    y_pred = model.predict(x_test)

    # The mean squared error
    print(f"Mean squared error: {mean_squared_error(y_test, y_pred):.2f}")
    # Explained variance score: 1 is perfect prediction
    print(f"Test Variance score: {r2_score(y_test, y_pred):.2f}")

    # So let's run the model against the test data
    _fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred, edgecolors=(0, 0, 0))
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "k--", lw=4)
    ax.set_xlabel("Actual")
    ax.set_ylabel("Predicted")
    ax.set_title("Truth vs Predicted")
    # this show function will display the plotting
    plt.show()


if __name__ == "__main__":
    main()
