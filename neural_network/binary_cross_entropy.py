# Given a list Y containing 1s and 0s indicating the target values and a list P containing the probability whether the target is 1 or not.
# We can find the cross entropy using the formula.

import numpy as np 
def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -1*np.sum(Y*np.log(P)+ (1-Y)*np.log(1-P))

Y = [1,1,0,0]
P = [0.8,0.6,0.3,0.1]



print(cross_entropy(Y,P))
