"""
Kalman Filter in Python

This script demonstrates the implementation of a one-dimensional Kalman
filter using the 'filterpy' library.
The Kalman filter is used for estimating the state of a linear
dynamic system that is subject to Gaussian noise.

The steps involved in the Kalman filter algorithm are as follows:
1. Initialization of the state and covariance.
2. Prediction of the next state and covariance based on the state
transition matrix and process noise covariance.
3. Update of the state estimate based on the measurement
received and the measurement noise covariance.
"""

import numpy as np
from filterpy.kalman import KalmanFilter

# Create a one-dimensional Kalman filter
kf = KalmanFilter(dim_x=1, dim_z=1)

# Define the state transition matrix
kf.F = np.array([[1.0]])

# Define the measurement function
kf.H = np.array([[1.0]])

# Define the measurement noise covariance
kf.R = 1

# Define the process noise covariance
kf.Q = 0.001

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
