import numpy as np
import matplotlib.pyplot as plt

# Define your polynomial coefficients
# You can change these coefficients as per your needs
coefficients = [-2, 0, 1]  # Enter the polynomial coefficients from lowest to highest degree

# Function to evaluate the polynomial
def evaluate_polynomial(x_value: float) -> float:
    """
    Evaluate a polynomial with the given coefficients at a specific x value.

    Args:
        x_value (float): The value of x at which to evaluate the polynomial.

    Returns:
        float: The result of evaluating the polynomial at the given x value.

    Example:
        >>> evaluate_polynomial(2)
        2.0
    """
    result = 0
    for i, coef in enumerate(coefficients):
        result += coef * (x_value ** i)
    return result


# Create an array of x-values using np.linspace
x_values = np.linspace(-10, 10, 400)  # Adjust the range and number of points as needed

# Evaluate the polynomial for the x-values
y_values = evaluate_polynomial(x_values)

# Create the matplotlib plot
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label="Polynomial Visualizer", color='blue')
plt.axhline(0, color='red', linewidth=1)
plt.axvline(0, color='red', linewidth=1)

# Set the axis limits
plt.xlim(-50, 50)
plt.ylim(-50, 50)  # Adjust the y-axis limits as needed

# Add labels and a legend
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
