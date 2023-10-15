# https://en.wikipedia.org/wiki/Joint_probability_distribution
# Function to calculate the joint probability distribution
def calculate_joint_probability(
    x_values: list, y_values: list, x_probabilities: list, y_probabilities: list
) -> dict:
    """
    Examples:
    >>>calculate_joint_probability([1],[1],[1],[1])
    {(1,1):1}
    >>>calculate_joint_probability([1][1,2][0.5][0.1,0.5])
    {(1,1):0.05 , (1,2):0.25}

    """
    joint_distribution = {}

    # Calculate the joint probability for all combinations of (X, Y)
    for x, x_prob in zip(x_values, x_probabilities):
        for y, y_prob in zip(y_values, y_probabilities):
            joint_prob = x_prob * y_prob
            joint_distribution[(x, y)] = joint_prob
    return joint_distribution


# Function to calculate the expectation (mean)
def expectation(values: list, probabilities: list) -> float:
    """
    Examples:
    >>>expectation([1,2],[0.7,0.3])
    1.2999999999999999999999
    >>>expectation([-2,5,8],[0.3,0.5,0.2])
    3.5

    """
    return sum(x * p for x, p in zip(values, probabilities))


# Function to calculate the variance
def variance(values: list, probabilities: list) -> float:
    """
    Examples:
    >>>variance([1,2],[0.7,0.3])
    0.21000
    >>>variance([-2.5.8],[0.3,0.5,0.2])
    14.25
    """
    mean = expectation(values, probabilities)
    return sum((x - mean) ** 2 * p for x, p in zip(values, probabilities))


# Function to calculate the covariance
def covariance(
    x_values: list, y_values: list, x_probabilities: list, y_probabilities: list
) -> float:
    """
    Examples:
    >>>covariance([1,2],[-2,5 ,8],[0.7, 0.3],[0.3, 0.5, 0.2])
    0
    >>>covariance([1],[1],[1],[1])
    0

    """
    mean_x = expectation(x_values, x_probabilities)
    mean_y = expectation(y_values, y_probabilities)
    return sum(
        (x - mean_x) * (y - mean_y) * px * py
        for x, px in zip(x_values, x_probabilities)
        for y, py in zip(y_values, y_probabilities)
    )


# Function to calculate the standard deviation
def standard_deviation(variance: list) -> float:
    """
    Examples
    >>>standard_deviation(4)
    2
    >>>standard_deviation(9)
    3

    """
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
joint_distribution = calculate_joint_probability(
    x_values, y_values, x_probabilities, y_probabilities
)

# Print the joint probability distribution
for (x, y), probability in joint_distribution.items():
    print(f"P(X={x}, Y={y}) = {probability}")


# Calculate the joint probability distribution
joint_distribution = calculate_joint_probability(
    x_values, y_values, x_probabilities, y_probabilities
)

# Print the joint probability distribution
for (x, y), probability in joint_distribution.items():
    print(f"P(X={x}, Y={y}) = {probability}")

# Calculate the statistics
mean_x = expectation(x_values, x_probabilities)
mean_y = expectation(y_values, y_probabilities)
mean_xy = expectation(
    [x * y for x in x_values for y in y_values],
    [px * py for px in x_probabilities for py in y_probabilities],
)
variance_x = variance(x_values, x_probabilities)
variance_y = variance(y_values, y_probabilities)
cov_xy = covariance(x_values, y_values, x_probabilities, y_probabilities)
stddev_x = standard_deviation(variance_x)
stddev_y = standard_deviation(variance_y)

# Print the results
print(f"Expectation (mean) of X: {expectation(x_values, x_probabilities)}")
print(f"Expectation (mean) of Y: {expectation(y_values, y_probabilities)}")
print(f"Expectation (mean) of XY: {expectation(
    [x * y for x in x_values for y in y_values],
    [px * py for px in x_probabilities for py in y_probabilities],
)}")
print(f"Variance of X: {variance(x_values, x_probabilities)}")
print(f"Variance of Y: {variance(y_values, y_probabilities)}")
print(f"Covariance between X and Y: {covariance(x_values, y_values, x_probabilities, y_probabilities)}")
print(f"Standard Deviation of X: {standard_deviation(variance_x)}")
print(f"Standard Deviation of Y: {standard_deviation(variance_y)}")
