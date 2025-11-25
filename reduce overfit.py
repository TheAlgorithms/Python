from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = load_iris()
X, y = data.data, data.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

# Decision Tree with Overfitting Controls
model = DecisionTreeClassifier(
    max_depth=3,              # limit depth of tree
    min_samples_split=4,      # minimum samples to split a node
    min_samples_leaf=2,       # minimum samples in each leaf
    ccp_alpha=0.01,           # pruning parameter (cost-complexity pruning)
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Depth of Tree:", model.get_depth())
print("Number of Leaves:", model.get_n_leaves())
