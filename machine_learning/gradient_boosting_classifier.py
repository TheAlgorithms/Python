# Importing required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load the dataset
iris = load_iris()
x = iris.data
y = iris.target

# Step 2: Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Step 3: Preprocess the data (if required)
# No preprocessing needed for the Iris dataset in this case

# Step 4: Train the gradient boosting model
gb_model = GradientBoostingClassifier()
gb_model.fit(x_train, y_train)

# Step 5: Evaluate the model
y_pred = gb_model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
classification_report = classification_report(y_test, y_pred)

# Step 6: Make predictions on new data (if required)
# Here, we'll use the same test set for demonstration
new_data_predictions = gb_model.predict(x_test)

# Step 7: Print the results
print(f"Accuracy: {accuracy}")
print(f"Classification Report: \n{classification_report}\n")
print(f"Predictions on new data: \n{new_data_predictions}")
