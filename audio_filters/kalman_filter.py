import numpy as np
from filterpy.kalman import KalmanFilter

kf = KalmanFilter(dim_x=1, dim_z=1)

# Define the state transition matrix
kf.F = np.array([[1.0]])

# Define the measurement function
kf.H = np.array([[1.0]])

# Define the measurement noise covariance
kf.R = np.array([[1.0]])

# Define the process noise covariance
kf.Q = np.array([[0.001]])

# Initialize the state estimate
kf.x = np.array([0.0])

# Initialize the state covariance
kf.P = np.array([[1.0]])

# Simulate measurements
measurements = [1, 2, 3, 4, 5]

# Perform filtering
filtered_state_means = []
for z in measurements:
    kf.predict()
    kf.update(z)
    filtered_state_means.append(kf.x[0])

print("Filtered state means:", filtered_state_means)
