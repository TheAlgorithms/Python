import numpy as np
import matplotlib.pyplot as plt


v = np.linspace(0, 10, 100)  # Velocity range from 0 to 10

# Define constants for the Bernoulli equation
pressure_constant = 1.0  # A constant for simplicity

# Calculate pressure using the Bernoulli equation
pressure = pressure_constant - 0.5 * v**2

# Create a plot
plt.figure(figsize=(8, 6))
plt.plot(v, pressure)
plt.title("Bernoulli Principle Visualization")
plt.xlabel("Velocity")
plt.ylabel("Pressure")
plt.grid(True)

# Show the plot
plt.show()
