import os

import matplotlib.pyplot as plt

# https://xgboost.readthedocs.io/en/stable/
import numpy as np
import pandas as pd
import seaborn as sns
from xgboost import XGBRegressor

for dirname, _, filenames in os.walk("/kaggle/input"):
    for filename in filenames:
        print(os.path.join(dirname, filename))

train_ames = pd.read_csv("/kaggle/input/ames-housing-dataset/AmesHousing.csv")
test = pd.read_csv("/kaggle/input/house-prices-advanced-regression-techniques/test.csv")
train = pd.read_csv(
    "/kaggle/input/house-prices-advanced-regression-techniques/train.csv"
)

train_ames.columns = train_ames.columns.str.replace(" ", "")
train_ames = train_ames.rename(columns={"YearRemod/Add": "YearRemodAdd"})

data = pd.concat([train_ames, train, test], axis=0, sort=False)
print("Size of the Housing Dataset", len(data))
useless = ["Id", "PID", "Order", "SalePrice"]
data = data.drop(useless, axis=1)
duplicate = data[data.duplicated(keep="last")].index
len(duplicate)

duplicate = duplicate[0:390]
train_ames = train_ames.drop(duplicate, axis=0)

training = pd.concat([train_ames, train], axis=0, sort=False)
useless = ["Id", "PID", "Order"]
training = training.drop(useless, axis=1)

# Separating Target and Features

target = training["SalePrice"]
test_id = test["Id"]
test = test.drop(["Id"], axis=1)
training2 = training.drop(["SalePrice"], axis=1)


# Concatenating train & test set

train_test = pd.concat([training2, test], axis=0, sort=False)

# Filling Categorical NaN (That we know how to fill due to the description file )

train_test["Functional"] = train_test["Functional"].fillna("Typ")
train_test["Electrical"] = train_test["Electrical"].fillna("SBrkr")
train_test["KitchenQual"] = train_test["KitchenQual"].fillna("TA")
train_test["Exterior1st"] = train_test["Exterior1st"].fillna(
    train_test["Exterior1st"].mode()[0]
)
train_test["Exterior2nd"] = train_test["Exterior2nd"].fillna(
    train_test["Exterior2nd"].mode()[0]
)
train_test["SaleType"] = train_test["SaleType"].fillna(train_test["SaleType"].mode()[0])
train_test["PoolQC"] = train_test["PoolQC"].fillna("None")
train_test["Alley"] = train_test["Alley"].fillna("None")
train_test["FireplaceQu"] = train_test["FireplaceQu"].fillna("None")
train_test["Fence"] = train_test["Fence"].fillna("None")
train_test["MiscFeature"] = train_test["MiscFeature"].fillna("None")
for col in ("GarageArea", "GarageCars"):
    train_test[col] = train_test[col].fillna(0)

for col in ["GarageType", "GarageFinish", "GarageQual", "GarageCond"]:
    train_test[col] = train_test[col].fillna("None")

for col in ("BsmtQual", "BsmtCond", "BsmtExposure", "BsmtFinType1", "BsmtFinType2"):
    train_test[col] = train_test[col].fillna("None")

for col in (
    "BsmtFinSF1",
    "BsmtFinSF2",
    "BsmtFullBath",
    "BsmtHalfBath",
    "MasVnrArea",
    "BsmtUnfSF",
    "TotalBsmtSF",
):
    train_test[col] = train_test[col].fillna(0)

train_test["LotFrontage"] = train_test["LotFrontage"].fillna(
    train["LotFrontage"].median()
)

# Checking the features with NaN remained out

for col in train_test:
    if train_test[col].isna().sum() > 0:
        print(train_test[col][1])

# Converting non-numeric predictors stored as numbers into string

train_test["MSSubClass"] = train_test["MSSubClass"].apply(str)
train_test["YrSold"] = train_test["YrSold"].apply(str)
train_test["MoSold"] = train_test["MoSold"].apply(str)
train_test["OverallQual"] = train_test["OverallQual"].apply(str)
train_test["OverallCond"] = train_test["OverallCond"].apply(str)
train_test["SqFtPerRoom"] = train_test["GrLivArea"] / (
    train_test["TotRmsAbvGrd"]
    + train_test["FullBath"]
    + train_test["HalfBath"]
    + train_test["KitchenAbvGr"]
)

train_test["Total_Home_Quality"] = train_test["OverallQual"] + train_test["OverallCond"]

train_test["Total_Bathrooms"] = (
    train_test["FullBath"]
    + (0.5 * train_test["HalfBath"])
    + train_test["BsmtFullBath"]
    + (0.5 * train_test["BsmtHalfBath"])
)

train_test["HighQualSF"] = train_test["1stFlrSF"] + train_test["2ndFlrSF"]
train_test["renovated"] = train_test["YearRemodAdd"] + train_test["YearBuilt"]

# Removing the useless variables

useless = ["GarageYrBlt", "YearRemodAdd"]
train_test = train_test.drop(useless, axis=1)
# Creating dummy variables from categorical features

from scipy.stats import skew

train_test_dummy = pd.get_dummies(train_test)

numeric_features = train_test_dummy.dtypes[train_test_dummy.dtypes != object].index
skewed_features = (
    train_test_dummy[numeric_features]
    .apply(lambda skewed: skew(skewed))
    .sort_values(ascending=False)
)
high_skew = skewed_features[skewed_features > 0.5]
skew_index = high_skew.index

# Normalize skewed features using log_transformation

for i in skew_index:
    train_test_dummy[i] = np.log1p(train_test_dummy[i])

target_log = np.log1p(target)

from xgboost import XGBRegressor

# Train-Test separation

x_train = train_test_dummy[0:4000]
x_test = train_test_dummy[4000:]

xgb = XGBRegressor()
xgb.fit(x_train, target_log)

test_pred = xgb.predict(x_test)
submission = pd.DataFrame(test_id, columns=["Id"])
test_pred = np.expm1(test_pred)
submission["SalePrice"] = test_pred
submission.head()
submission.to_csv("xgb.csv", index=False, header=True)
