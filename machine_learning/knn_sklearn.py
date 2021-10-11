from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

# Load iris file
iris = load_iris()
iris.keys()


print(f"Target names: \n {iris.target_names} ")
print(f"\n Features: \n {iris.feature_names}")

# Train set and Test set
X_train, X_test, y_train, y_test = train_test_split(
    iris["data"], iris["target"], random_state=4
)

# KNN
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
y_predict=knn.predict(X_test)

#Accuracy
print(metrics.accuracy_score(y_test, y_predict))
#Accuracy = 94.73%(approx)

# new array sample to test
sample = [[1, 2, 1, 4], [2, 3, 4, 5]]
prediction = knn.predict(sample)

print(
    f"\nNew array: \n {sample}\n\nTarget Names Prediction: \n"
    f" {iris['target_names'][prediction]}"
)

# one more array sample to test
sample2 = [[2,3,4,5], [3,4,5,6]]
prediction2 = knn.predict(samples)

print(
    f"\nNew array: \n {sample2}\n\nTarget Names Prediction: \n"
    f" {iris['target_names'][prediction2]}"
)
