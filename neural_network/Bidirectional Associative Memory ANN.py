import numpy as np

# Define two pairs of vectors

X1 = np.array([1, 1, 1, 0, 0])
X2 = np.array([0, 0, 1, 1, 1])
Y1 = np.array([1, 0, 0])
Y2 = np.array([0, 1, 0])

# Define the weight matrix

W = np.zeros((len(X1), len(Y1)))
for i in range(len(X1)):
    for j in range(len(Y1)):
        W[i][j] = X1[i] * Y1[j] + X2[i] * Y2[j]
print(W)


# Define the BAM function

def BAM(input_vector):
    output_vector = np.zeros(len(Y1))
    for j in range(len(Y1)):
        sum = 0
        for i in range(len(X1)):
            sum += input_vector[i] * W[i][j]
        output_vector[j] = sum
    return output_vector

# Test the BAM function with the input vector X1

input_vector = X1
output_vector = BAM(input_vector)
print("Input vector", input_vector)
print("Output vector", output_vector)