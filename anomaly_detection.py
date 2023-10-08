import numpy as np
from sklearn.ensemble import IsolationForest

# Generate sample data (replace this with your own dataset)
np.random.seed(42)
data = np.random.randn(1000, 2)

# Create an Isolation Forest model
model = IsolationForest(contamination=0.05)  # Contamination is an estimate of the proportion of outliers

# Fit the model to your data
model.fit(data)

# Predict anomaly scores for the data points
anomaly_scores = model.decision_function(data)

# Define a threshold for identifying anomalies
threshold = -0.2  # You can adjust this threshold based on your requirements

# Find the indices of anomalies
anomalies_indices = np.where(anomaly_scores < threshold)[0]

# Print the indices of anomalous data points
print("Anomalous Data Points Indices:")
print(anomalies_indices)
