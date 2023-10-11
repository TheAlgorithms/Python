import pandas as pd
from sklearn import metrics, model_selection, tree

df = pd.read_csv("churn_modelling.csv")

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

x_test, x_train, y_test, y_train = model_selection.train_test_split(
    x, y, test_size=0.3, random_state=3
)

decision_tree = tree.DecisionTreeClassifier(criterion="entropy", max_depth=4)
decision_tree.fit(x_train, y_train)

pred_tree = decision_tree.predict(x_test)
print("Accuracy of the model: ", metrics.accuracy_score(y_test, pred_tree))

print("Predicted values: ", pred_tree[0:5])
print("Actual values: \n", y_test[0:5])

print("Error rate: ", metrics.mean_squared_error(y_test, pred_tree))
