import numpy as np

# Define two pairs of vectors

x1 = np.array([1, 1, 1, 0, 0])
x2 = np.array([0, 0, 1, 1, 1])
y1 = np.array([1, 0, 0])
y2 = np.array([0, 1, 0])

# Define the weight matrix

w = np.zeros((len(x1), len(y1)))
for i in range(len(x1)):
    for j in range(len(y1)):
        w[i][j] = x1[i] * y1[j] + x2[i] * y2[j]
print(w)


# Define the bam function


def bam(input_vector):
    output_vector = np.zeros(len(y1))
    for j in range(len(y1)):
        sum = 0
        for i in range(len(x1)):
            sum += input_vector[i] * w[i][j]
        output_vector[j] = sum
    return output_vector


# test the bam function with the input vector x1

input_vector = x1
output_vector = bam(input_vector)
print("Input vector", input_vector)
print("Output vector", output_vector)
