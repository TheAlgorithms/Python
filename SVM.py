from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Load the iris dataset
iris = load_iris()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Create an SVM classifier object
svm_clf = SVC(kernel='linear', C=1)

# Train the SVM classifier on the training set
svm_clf.fit(X_train, y_train)

# Evaluate the performance of the classifier on the testing set
accuracy = svm_clf.score(X_test, y_test)
print(f"Accuracy: {accuracy:.2f}")
