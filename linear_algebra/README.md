# Linear algebra library for Python  

This module contains classes and functions for doing linear algebra.  

---

## Overview  

### class Vector  
-
    - This class represents a vector of arbitrary size and related operations.  

    **Overview about the methods:**    
        
    - constructor(components : list) : init the vector  
    - set(components : list) : changes the vector components.  
    - \_\_str\_\_() : toString method  
    - component(i : int): gets the i-th component (start by 0)  
    - \_\_len\_\_() : gets the size / length of the vector (number of components)  
    - euclidLength() : returns the eulidean length of the vector.  
    - operator + : vector addition  
    - operator - : vector subtraction  
    - operator * : scalar multiplication and dot product  
    - copy() : copies this vector and returns it.  
    - changeComponent(pos,value) : changes the specified component.  

- function zeroVector(dimension)  
    - returns a zero vector of 'dimension'  
- function unitBasisVector(dimension,pos)  
    - returns a unit basis vector with a One at index 'pos' (indexing at 0)  
- function axpy(scalar,vector1,vector2)  
    - computes the axpy operation  
- function randomVector(N,a,b)
    - returns a random vector of size N, with random integer components between 'a' and 'b'.

### class Matrix
-
    - This class represents a matrix of arbitrary size and operations on it.

    **Overview about the methods:**  
    
    -  \_\_str\_\_() : returns a string representation  
    - operator * : implements the matrix vector multiplication  
                   implements the matrix-scalar multiplication.  
    - changeComponent(x,y,value) : changes the specified component.  
    - component(x,y) : returns the specified component.  
    - width() : returns the width of the matrix  
    - height() : returns the height of the matrix
    - determinate() : returns the determinate of the matrix if it is square 
    - operator + : implements the matrix-addition.  
    - operator - _ implements the matrix-subtraction  

- function squareZeroMatrix(N)  
    - returns a square zero-matrix of dimension NxN  
- function randomMatrix(W,H,a,b)  
    - returns a random matrix WxH with integer components between 'a' and 'b'  
---

## Documentation  

This module uses docstrings to enable the use of Python's in-built `help(...)` function.
For instance, try `help(Vector)`, `help(unitBasisVector)`, and `help(CLASSNAME.METHODNAME)`.

---

## Usage  

Import the module `lib.py` from the **src** directory into your project.
Alternatively, you can directly use the Python bytecode file `lib.pyc`.   

---

## Tests  

`src/tests.py` contains Python unit tests which can be run with `python3 -m unittest -v`.
