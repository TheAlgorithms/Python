"""      Transpose of a Matrix

Following is a simpler code for Transpose
of a matrix using the NUMPY library of Python.

The transpose of a matrix swaps its rows and columns:

            [[a,b,c],
             [d,e,f]]
​
Would be written as :

            [[a,d],
             [b,e],
             [c,f]]

This comes in extensive use when we matrices in ML. """


import numpy as np

# We have imported the NUMPY library using above SYNTAX.

def Transpose(mat):

# Here we create a function Transpose.
    arr=np.array(mat)

    # We convert the incoming matrix in an array form using np.array() function.
    
    a=arr.T

    # Here we just use the inbuild function of the NUMPY library.
    return a

""" Let us declare a matrix and we will see the output

>>>mat=[[1,2,3],
        [4,5,6]]
>>>print(Transpose(mat))     

OUTPUT:
>>> 
[[1 4]
 [2 5]
 [3 6]]


>>>mat=[['a','b','c'],
        ['d','e','f']]
>>>print(Transpose(mat))

OUTPUT:
 >>> 
[['a' 'd']
 ['b' 'e']
 ['c' 'f']]
 """

