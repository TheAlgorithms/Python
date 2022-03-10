# Linear algebra library for Python

This module contains classes and functions for doing linear algebra.

---

## Overview

### class Vector
-
    - This class represents a vector of arbitrary size and related operations.

    **Overview of the methods:**

    - constructor(components) : init the vector
    - set(components) : changes the vector components.
    - \_\_str\_\_() : toString method
    - component(i): gets the i-th component (0-indexed)
    - \_\_len\_\_() : gets the size / length of the vector (number of components)
    - euclidean_length() : returns the eulidean length of the vector
    - operator + : vector addition
    - operator - : vector subtraction
    - operator * : scalar multiplication and dot product
    - copy() : copies this vector and returns it
    - change_component(pos,value) : changes the specified component

- function zero_vector(dimension)
    - returns a zero vector of 'dimension'
- function unit_basis_vector(dimension, pos)
    - returns a unit basis vector with a one at index 'pos' (0-indexed)
- function axpy(scalar, vector1, vector2)
    - computes the axpy operation
- function random_vector(N, a, b)
    - returns a random vector of size N, with random integer components between 'a' and 'b' inclusive

### class Matrix
-
    - This class represents a matrix of arbitrary size and operations on it.

    **Overview of the methods:**

    -  \_\_str\_\_() : returns a string representation
    - operator * : implements the matrix vector multiplication
                   implements the matrix-scalar multiplication.
    - change_component(x, y, value) : changes the specified component.
    - component(x, y) : returns the specified component.
    - width() : returns the width of the matrix
    - height() : returns the height of the matrix
    - determinant() : returns the determinant of the matrix if it is square
    - operator + : implements the matrix-addition.
    - operator - : implements the matrix-subtraction

- function square_zero_matrix(N)
    - returns a square zero-matrix of dimension NxN
- function random_matrix(W, H, a, b)
    - returns a random matrix WxH with integer components between 'a' and 'b' inclusive
---

## Documentation

This module uses docstrings to enable the use of Python's in-built `help(...)` function.
For instance, try `help(Vector)`, `help(unit_basis_vector)`, and `help(CLASSNAME.METHODNAME)`.

---

## Usage

Import the module `lib.py` from the **src** directory into your project.
Alternatively, you can directly use the Python bytecode file `lib.pyc`.

---

## Tests

`src/tests.py` contains Python unit tests which can be run with `python3 -m unittest -v`.
