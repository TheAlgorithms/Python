# Predicting Customer Churn rate using Decision Tree
# Dataset from Kaggle: https://www.kaggle.com/code/korfanakis/predicting-customer-churn-with-machine-learning/input
import pandas as pd
from sklearn import metrics, model_selection, tree

df = pd.read_csv("churn_modelling.csv")

# prints the first 5 rows of the dataset
# print(df.head())

# Sorting the dependent and independent values
x = df[
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
y = df["Exited"]

# Splitting the dataset into training and testing data
x_test, x_train, y_test, y_train = model_selection.train_test_split(
    x, y, test_size=0.3, random_state=3
)

# Creating the decision tree classifier
decision_tree = tree.DecisionTreeClassifier(criterion="entropy", max_depth=4)
decision_tree.fit(x_train, y_train)

# Predicting the values
pred_tree = decision_tree.predict(x_test)
print("Accuracy of the model: ", metrics.accuracy_score(y_test, pred_tree))

# Comparing the first five predicted and actual values
print("Predicted values: ", pred_tree[0:5])
print("Actual values: \n", y_test[0:5])

# Error rate
print("Error rate: ", metrics.mean_squared_error(y_test, pred_tree))
# Visualizing the decision tree
# tree.plot_tree(decision_tree)
# plt.show()
