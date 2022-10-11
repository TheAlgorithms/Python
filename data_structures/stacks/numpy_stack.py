import numpy as np
 
# input array
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
 
# Stacking 2 1-d arrays
c = np.stack((a, b),axis=0)
print(c)
