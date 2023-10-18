import numpy as np
import matplotlib.pyplot as plt

# Constants
magnetic_flux = 0.0  # Initial magnetic flux (Weber)
magnetic_field_strength = 1.0  # Magnetic field strength (Tesla)
area = 0.01  # Area of the coil (square meters)
velocity = 0.1  # Velocity of the magnet (m/s)
time = np.linspace(0, 2, num=100)  # Time values from 0 to 2 seconds

# Lists to store data for plotting
flux_values = []
current_values = []

# Simulate the change in magnetic flux over time
for t in time:
    # Calculate the change in magnetic flux
    delta_flux = -velocity * magnetic_field_strength * area * t

    # Calculate the induced EMF and current using Lenz's Law
    induced_emf = -delta_flux / t
    induced_current = induced_emf / area

    flux_values.append(magnetic_flux + delta_flux)
    current_values.append(induced_current)

# Plot the change in magnetic flux and induced current
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(time, flux_values, lw=2)
plt.title("Change in Magnetic Flux vs. Time")
plt.xlabel("Time (s)")
plt.ylabel("Change in Magnetic Flux (Wb)")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(time, current_values, lw=2, color='orange')
plt.title("Induced Current vs. Time")
plt.xlabel("Time (s)")
plt.ylabel("Induced Current (A)")
plt.grid(True)

plt.tight_layout()
plt.show()
