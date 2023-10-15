# https://en.wikipedia.org/wiki/Joint_probability_distribution
# Function to calculate the joint probability distribution
def calculate_joint_probability(x_values, y_values, x_probabilities, y_probabilities):
    joint_distribution = {}

    # Calculate the joint probability for all combinations of (X, Y)
    for x, x_prob in zip(x_values, x_probabilities):
        for y, y_prob in zip(y_values, y_probabilities):
            joint_prob = x_prob * y_prob
            joint_distribution[(x, y)] = joint_prob

    return joint_distribution

# Function to calculate the expectation (mean)
def expectation(values, probabilities):
    return sum(x * p for x, p in zip(values, probabilities))

# Function to calculate the variance
def variance(values, probabilities):
    mean = expectation(values, probabilities)
    return sum((x - mean)**2 * p for x, p in zip(values, probabilities))

# Function to calculate the covariance
def covariance(x_values, y_values, x_probabilities, y_probabilities):
    mean_x = expectation(x_values, x_probabilities)
    mean_y = expectation(y_values, y_probabilities)
    return sum((x - mean_x) * (y - mean_y) * px * py for x, px in zip(x_values, x_probabilities) for y, py in zip(y_values, y_probabilities))

# Function to calculate the standard deviation
def standard_deviation(variance):
    return variance**0.5


# Input values for X and Y
x_values = input("Enter values of X separated by spaces: ").split()
y_values = input("Enter values of Y separated by spaces: ").split()

# Convert input values to integers
x_values = [int(x) for x in x_values]
y_values = [int(y) for y in y_values]

# Input probabilities for X and Y
x_probabilities = input("Enter probabilities for X separated by spaces: ").split()
y_probabilities = input("Enter probabilities for Y separated by spaces: ").split()

# Convert input probabilities to floats
x_probabilities = [float(p) for p in x_probabilities]
y_probabilities = [float(p) for p in y_probabilities]

# Calculate the joint probability distribution
joint_distribution = calculate_joint_probability(x_values, y_values, x_probabilities, y_probabilities)

# Print the joint probability distribution
for (x, y), probability in joint_distribution.items():
    print(f'P(X={x}, Y={y}) = {probability}')




# Calculate the joint probability distribution
joint_distribution = calculate_joint_probability(x_values, y_values, x_probabilities, y_probabilities)

# Print the joint probability distribution
for (x, y), probability in joint_distribution.items():
    print(f'P(X={x}, Y={y}) = {probability}')

# Calculate the statistics
mean_x = expectation(x_values, x_probabilities)
mean_y = expectation(y_values, y_probabilities)
mean_xy = expectation([x * y for x in x_values for y in y_values], [px * py for px in x_probabilities for py in y_probabilities])
variance_x = variance(x_values, x_probabilities)
variance_y = variance(y_values, y_probabilities)
cov_xy = covariance(x_values, y_values, x_probabilities, y_probabilities)
stddev_x = standard_deviation(variance_x)
stddev_y = standard_deviation(variance_y)

# Print the results
print(f"Expectation (mean) of X: {mean_x}")
print(f"Expectation (mean) of Y: {mean_y}")
print(f"Expectation (mean) of XY: {mean_xy}")
print(f"Variance of X: {variance_x}")
print(f"Variance of Y: {variance_y}")
print(f"Covariance between X and Y: {cov_xy}")
print(f"Standard Deviation of X: {stddev_x}")
print(f"Standard Deviation of Y: {stddev_y}")
