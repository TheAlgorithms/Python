
# Import required package
import numpy as np

# Inverses of several matrices can
# be computed at once
A = np.array([[[1., 2.], [3., 4.]],
			[[1, 3], [3, 5]]])

# Calculating the inverse of the matrix
print(np.linalg.inv(A))

