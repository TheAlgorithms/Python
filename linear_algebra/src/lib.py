"""
Created on Mon Feb 26 14:29:11 2018

@author: Christian Bender
@license: MIT-license

This module contains some useful classes and functions for dealing
with linear algebra in python.

Overview:

- class Vector
- function zero_vector(dimension)
- function unit_basis_vector(dimension, pos)
- function axpy(scalar, vector1, vector2)
- function random_vector(N, a, b)
- class Matrix
- function square_zero_matrix(N)
- function random_matrix(W, H, a, b)
"""
from __future__ import annotations

import math
import random
from collections.abc import Collection
from typing import overload


class Vector:
    """
    This class represents a vector of arbitrary size.
    You need to give the vector components.

    Overview of the methods:

        __init__(components: Collection[float] | None): init the vector
        __len__(): gets the size of the vector (number of components)
        __str__(): returns a string representation
        __add__(other: Vector): vector addition
        __sub__(other: Vector): vector subtraction
        __mul__(other: float): scalar multiplication
        __mul__(other: Vector): dot product
        copy(): copies this vector and returns it
        component(i): gets the i-th component (0-indexed)
        change_component(pos: int, value: float): changes specified component
        euclidean_length(): returns the euclidean length of the vector
        angle(other: Vector, deg: bool): returns the angle between two vectors
        TODO: compare-operator
    """

    def __init__(self, components: Collection[float] | None = None) -> None:
        """
        input: components or nothing
        simple constructor for init the vector
        """
        if components is None:
            components = []
        self.__components = list(components)

    def __len__(self) -> int:
        """
        returns the size of the vector
        """
        return len(self.__components)

    def __str__(self) -> str:
        """
        returns a string representation of the vector
        """
        return "(" + ",".join(map(str, self.__components)) + ")"

    def __add__(self, other: Vector) -> Vector:
        """
        input: other vector
        assumes: other vector has the same size
        returns a new vector that represents the sum.
        """
        size = len(self)
        if size == len(other):
            result = [self.__components[i] + other.component(i) for i in range(size)]
            return Vector(result)
        else:
            raise Exception("must have the same size")

    def __sub__(self, other: Vector) -> Vector:
        """
        input: other vector
        assumes: other vector has the same size
        returns a new vector that represents the difference.
        """
        size = len(self)
        if size == len(other):
            result = [self.__components[i] - other.component(i) for i in range(size)]
            return Vector(result)
        else:  # error case
            raise Exception("must have the same size")

    @overload
    def __mul__(self, other: float) -> Vector:
        ...

    @overload
    def __mul__(self, other: Vector) -> float:
        ...

    def __mul__(self, other: float | Vector) -> float | Vector:
        """
        mul implements the scalar multiplication
        and the dot-product
        """
        if isinstance(other, (float, int)):
            ans = [c * other for c in self.__components]
            return Vector(ans)
        elif isinstance(other, Vector) and len(self) == len(other):
            size = len(self)
            prods = [self.__components[i] * other.component(i) for i in range(size)]
            return sum(prods)
        else:  # error case
            raise Exception("invalid operand!")

    def copy(self) -> Vector:
        """
        copies this vector and returns it.
        """
        return Vector(self.__components)

    def component(self, i: int) -> float:
        """
        input: index (0-indexed)
        output: the i-th component of the vector.
        """
        if isinstance(i, int) and -len(self.__components) <= i < len(self.__components):
            return self.__components[i]
        else:
            raise Exception("index out of range")

    def change_component(self, pos: int, value: float) -> None:
        """
        input: an index (pos) and a value
        changes the specified component (pos) with the
        'value'
        """
        # precondition
        assert -len(self.__components) <= pos < len(self.__components)
        self.__components[pos] = value

    def euclidean_length(self) -> float:
        """
        returns the euclidean length of the vector

        >>> Vector([2, 3, 4]).euclidean_length()
        5.385164807134504
        >>> Vector([1]).euclidean_length()
        1.0
        >>> Vector([0, -1, -2, -3, 4, 5, 6]).euclidean_length()
        9.539392014169456
        >>> Vector([]).euclidean_length()
        Traceback (most recent call last):
            ...
        Exception: Vector is empty
        """
        if len(self.__components) == 0:
            raise Exception("Vector is empty")
        squares = [c**2 for c in self.__components]
        return math.sqrt(sum(squares))

    def angle(self, other: Vector, deg: bool = False) -> float:
        """
        find angle between two Vector (self, Vector)

        >>> Vector([3, 4, -1]).angle(Vector([2, -1, 1]))
        1.4906464636572374
        >>> Vector([3, 4, -1]).angle(Vector([2, -1, 1]), deg = True)
        85.40775111366095
        >>> Vector([3, 4, -1]).angle(Vector([2, -1]))
        Traceback (most recent call last):
            ...
        Exception: invalid operand!
        """
        num = self * other
        den = self.euclidean_length() * other.euclidean_length()
        if deg:
            return math.degrees(math.acos(num / den))
        else:
            return math.acos(num / den)


def zero_vector(dimension: int) -> Vector:
    """
    returns a zero-vector of size 'dimension'
    """
    # precondition
    assert isinstance(dimension, int)
    return Vector([0] * dimension)


def unit_basis_vector(dimension: int, pos: int) -> Vector:
    """
    returns a unit basis vector with a One
    at index 'pos' (indexing at 0)
    """
    # precondition
    assert isinstance(dimension, int)
    assert isinstance(pos, int)
    ans = [0] * dimension
    ans[pos] = 1
    return Vector(ans)


def axpy(scalar: float, x: Vector, y: Vector) -> Vector:
    """
    input: a 'scalar' and two vectors 'x' and 'y'
    output: a vector
    computes the axpy operation
    """
    # precondition
    assert isinstance(x, Vector)
    assert isinstance(y, Vector)
    assert isinstance(scalar, (int, float))
    return x * scalar + y


def random_vector(n: int, a: int, b: int) -> Vector:
    """
    input: size (N) of the vector.
           random range (a,b)
    output: returns a random vector of size N, with
            random integer components between 'a' and 'b'.
    """
    random.seed(None)
    ans = [random.randint(a, b) for _ in range(n)]
    return Vector(ans)


class Matrix:
    """
    class: Matrix
    This class represents an arbitrary matrix.

    Overview of the methods:

        __init__():
        __str__(): returns a string representation
        __add__(other: Matrix): matrix addition
        __sub__(other: Matrix): matrix subtraction
        __mul__(other: float): scalar multiplication
        __mul__(other: Vector): vector multiplication
        height() : returns height
        width() : returns width
        component(x: int, y: int): returns specified component
        change_component(x: int, y: int, value: float): changes specified component
        minor(x: int, y: int): returns minor along (x, y)
        cofactor(x: int, y: int): returns cofactor along (x, y)
        determinant() : returns determinant
    """

    def __init__(self, matrix: list[list[float]], w: int, h: int) -> None:
        """
        simple constructor for initializing the matrix with components.
        """
        self.__matrix = matrix
        self.__width = w
        self.__height = h

    def __str__(self) -> str:
        """
        returns a string representation of this matrix.
        """
        ans = ""
        for i in range(self.__height):
            ans += "|"
            for j in range(self.__width):
                if j < self.__width - 1:
                    ans += str(self.__matrix[i][j]) + ","
                else:
                    ans += str(self.__matrix[i][j]) + "|\n"
        return ans

    def __add__(self, other: Matrix) -> Matrix:
        """
        implements matrix addition.
        """
        if self.__width == other.width() and self.__height == other.height():
            matrix = []
            for i in range(self.__height):
                row = [
                    self.__matrix[i][j] + other.component(i, j)
                    for j in range(self.__width)
                ]
                matrix.append(row)
            return Matrix(matrix, self.__width, self.__height)
        else:
            raise Exception("matrix must have the same dimension!")

    def __sub__(self, other: Matrix) -> Matrix:
        """
        implements matrix subtraction.
        """
        if self.__width == other.width() and self.__height == other.height():
            matrix = []
            for i in range(self.__height):
                row = [
                    self.__matrix[i][j] - other.component(i, j)
                    for j in range(self.__width)
                ]
                matrix.append(row)
            return Matrix(matrix, self.__width, self.__height)
        else:
            raise Exception("matrices must have the same dimension!")

    @overload
    def __mul__(self, other: float) -> Matrix:
        ...

    @overload
    def __mul__(self, other: Vector) -> Vector:
        ...

    def __mul__(self, other: float | Vector) -> Vector | Matrix:
        """
        implements the matrix-vector multiplication.
        implements the matrix-scalar multiplication
        """
        if isinstance(other, Vector):  # matrix-vector
            if len(other) == self.__width:
                ans = zero_vector(self.__height)
                for i in range(self.__height):
                    prods = [
                        self.__matrix[i][j] * other.component(j)
                        for j in range(self.__width)
                    ]
                    ans.change_component(i, sum(prods))
                return ans
            else:
                raise Exception(
                    "vector must have the same size as the "
                    "number of columns of the matrix!"
                )
        elif isinstance(other, (int, float)):  # matrix-scalar
            matrix = [
                [self.__matrix[i][j] * other for j in range(self.__width)]
                for i in range(self.__height)
            ]
            return Matrix(matrix, self.__width, self.__height)
        return None

    def height(self) -> int:
        """
        getter for the height
        """
        return self.__height

    def width(self) -> int:
        """
        getter for the width
        """
        return self.__width

    def component(self, x: int, y: int) -> float:
        """
        returns the specified (x,y) component
        """
        if 0 <= x < self.__height and 0 <= y < self.__width:
            return self.__matrix[x][y]
        else:
            raise Exception("change_component: indices out of bounds")

    def change_component(self, x: int, y: int, value: float) -> None:
        """
        changes the x-y component of this matrix
        """
        if 0 <= x < self.__height and 0 <= y < self.__width:
            self.__matrix[x][y] = value
        else:
            raise Exception("change_component: indices out of bounds")

    def minor(self, x: int, y: int) -> float:
        """
        returns the minor along (x, y)
        """
        if self.__height != self.__width:
            raise Exception("Matrix is not square")
        minor = self.__matrix[:x] + self.__matrix[x + 1 :]
        for i in range(len(minor)):
            minor[i] = minor[i][:y] + minor[i][y + 1 :]
        return Matrix(minor, self.__width - 1, self.__height - 1).determinant()

    def cofactor(self, x: int, y: int) -> float:
        """
        returns the cofactor (signed minor) along (x, y)
        """
        if self.__height != self.__width:
            raise Exception("Matrix is not square")
        if 0 <= x < self.__height and 0 <= y < self.__width:
            return (-1) ** (x + y) * self.minor(x, y)
        else:
            raise Exception("Indices out of bounds")

    def determinant(self) -> float:
        """
        returns the determinant of an nxn matrix using Laplace expansion
        """
        if self.__height != self.__width:
            raise Exception("Matrix is not square")
        if self.__height < 1:
            raise Exception("Matrix has no element")
        elif self.__height == 1:
            return self.__matrix[0][0]
        elif self.__height == 2:
            return (
                self.__matrix[0][0] * self.__matrix[1][1]
                - self.__matrix[0][1] * self.__matrix[1][0]
            )
        else:
            cofactor_prods = [
                self.__matrix[0][y] * self.cofactor(0, y) for y in range(self.__width)
            ]
            return sum(cofactor_prods)


def square_zero_matrix(n: int) -> Matrix:
    """
    returns a square zero-matrix of dimension NxN
    """
    ans: list[list[float]] = [[0] * n for _ in range(n)]
    return Matrix(ans, n, n)


def random_matrix(width: int, height: int, a: int, b: int) -> Matrix:
    """
    returns a random matrix WxH with integer components
    between 'a' and 'b'
    """
    random.seed(None)
    matrix: list[list[float]] = [
        [random.randint(a, b) for _ in range(width)] for _ in range(height)
    ]
    return Matrix(matrix, width, height)
