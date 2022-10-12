import matplotlib.pyplot as plt

"""
The Url for the algorithm
https://xgboost.readthedocs.io/en/stable/
"""
import numpy as np
import pandas as pd
import seaborn as sns
from xgboost import XGBClassifier

 """
    You have to download the dataset from kaggle in order to run this
    https://www.kaggle.com/competitions/titanic/data
    This is the link from where you can get the data.
 """

training = pd.read_csv("../input/titanic/train.csv")
test = pd.read_csv("../input/titanic/test.csv")

# Commented out IPython magic to ensure Python compatibility.
training["train_test"] = 1
test["train_test"] = 0
test["Survived"] = np.NaN
all_data = pd.concat([training, test])
# %matplotlib inline
all_data.columns

all_data.describe()

all_data["cabin_mul"] = all_data.Cabin.apply(
    lambda cabin_class: 0 if pd.isna(cabin_class) else len(x.split(" "))
)
all_data["cabin_adv"] = all_data.Cabin.apply(lambda cabin_number: str(cabin_number)[0])
all_data["name_title"] = all_data.Name.apply(
    lambda name: name.split(",")[1].split(".")[0].strip()
)
all_data.Age = all_data.Age.fillna(training.Age.median())
all_data.Fare = all_data.Fare.fillna(training.Fare.median())
all_data.dropna(subset=["Embarked"], inplace=True)
all_data["norm_fare"] = np.log(all_data.Fare + 1)
all_data.Pclass = all_data.Pclass.astype(str)
all_data["Age"] = all_data["Age"].apply(np.int64)
all_dummies = pd.get_dummies(
    all_data[
        [
            "Pclass",
            "Sex",
            "Age",
            "SibSp",
            "Parch",
            "norm_fare",
            "Embarked",
            "cabin_adv",
            "cabin_mul",
            "name_title",
            "train_test",
        ]
    ]
)

from sklearn.preprocessing import StandardScaler

scale = StandardScaler()
all_dummies_scaled = all_dummies.copy()
all_dummies_scaled[["Age", "SibSp", "Parch", "norm_fare"]] = scale.fit_transform(
    all_dummies_scaled[["Age", "SibSp", "Parch", "norm_fare"]]
)
all_dummies_scaled.head()

x_train_scaled = all_dummies_scaled[all_dummies_scaled.train_test == 1].drop(
    ["train_test"], axis=1
)
x_test_scaled = all_dummies_scaled[all_dummies_scaled.train_test == 0].drop(
    ["train_test"], axis=1
)

y_train = all_data[all_data.train_test == 1].Survived

from xgboost import XGBClassifier

xgb = XGBClassifier()
xgb.fit(X_train_scaled, y_train)

y_hat_base_vc = xgb.predict(x_test_scaled).astype(int)
basic_submission = {"PassengerId": test.PassengerId, "Survived": y_hat_base_vc}
base_submission = pd.DataFrame(data=basic_submission)
base_submission.to_csv("xgb_submission.csv", index=False)
