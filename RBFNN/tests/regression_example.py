import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from rbfnn.model import RBFNN

# Generate sine wave data
X = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
y = np.sin(X).ravel()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RBFNN(num_centers=10, gamma=1.0)
model.train(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Plot
plt.scatter(X_test, y_test, label="True")
plt.scatter(X_test, y_pred, label="Predicted", color="red", marker="x")
plt.title("RBFNN Regression - Sine Function")
plt.legend()
plt.show()
