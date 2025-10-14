"""
Example: Using pandas and matplotlib together

This script demonstrates how to:
1. Create a DataFrame using pandas
2. Perform a simple transformation
3. Visualize the results using matplotlib

Requirements:
    pip install pandas matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a sample DataFrame
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [250, 300, 280, 350, 400, 380]
}
df = pd.DataFrame(data)

# Step 2: Add a moving average column
df["Moving_Avg"] = df["Sales"].rolling(window=2).mean()

# Step 3: Plot the data
plt.figure(figsize=(8, 5))
plt.plot(df["Month"], df["Sales"], marker='o', label="Sales", color="blue")
plt.plot(df["Month"], df["Moving_Avg"], marker='s', label="Moving Avg", linestyle="--", color="orange")

plt.title("Monthly Sales with Moving Average")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

# Optional: Print the DataFrame for reference
print(df)
