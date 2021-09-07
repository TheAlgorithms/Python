"""
Created on Mon Feb 26 14:29:11 2018

@author: Christian Bender
@license: MIT-license

This module contains some useful classes and functions for dealing
with linear algebra in python.

Overview:

- class Vector
- function zeroVector(dimension)
- function unitBasisVector(dimension,pos)
- function axpy(scalar,vector1,vector2)
- function randomVector(N,a,b)
- class Matrix
- function squareZeroMatrix(N)
- function randomMatrix(W,H,a,b)
"""
from __future__ import annotations

import math
import random
from typing import Collection, overload


class Vector:
    """
    This class represents a vector of arbitrary size.
    You need to give the vector components.

    Overview about the methods:

    constructor(components : list) : init the vector
    set(components : list) : changes the vector components.
    __str__() : toString method
    component(i : int): gets the i-th component (start by 0)
    __len__() : gets the size of the vector (number of components)
    euclidLength() : returns the euclidean length of the vector.
    operator + : vector addition
    operator - : vector subtraction
    operator * : scalar multiplication and dot product
    copy() : copies this vector and returns it.
    changeComponent(pos,value) : changes the specified component.
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

    def set(self, components: Collection[float]) -> None:
        """
        input: new components
        changes the components of the vector.
        replace the components with newer one.
        """
        if len(components) > 0:
            self.__components = list(components)
        else:
            raise Exception("please give any vector")

    def __str__(self) -> str:
        """
        returns a string representation of the vector
        """
        return "(" + ",".join(map(str, self.__components)) + ")"

    def component(self, i: int) -> float:
        """
        input: index (start at 0)
        output: the i-th component of the vector.
        """
        if type(i) is int and -len(self.__components) <= i < len(self.__components):
            return self.__components[i]
        else:
            raise Exception("index out of range")

    def __len__(self) -> int:
        """
        returns the size of the vector
        """
        return len(self.__components)

    def euclidLength(self) -> float:
        """
        returns the euclidean length of the vector
        """
        summe: float = 0
        for c in self.__components:
            summe += c ** 2
        return math.sqrt(summe)

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
        if isinstance(other, float) or isinstance(other, int):
            ans = [c * other for c in self.__components]
            return Vector(ans)
        elif isinstance(other, Vector) and (len(self) == len(other)):
            size = len(self)
            summe: float = 0
            for i in range(size):
                summe += self.__components[i] * other.component(i)
            return summe
        else:  # error case
            raise Exception("invalid operand!")

    def copy(self) -> Vector:
        """
        copies this vector and returns it.
        """
        return Vector(self.__components)

    def changeComponent(self, pos: int, value: float) -> None:
        """
        input: an index (pos) and a value
        changes the specified component (pos) with the
        'value'
        """
        # precondition
        assert -len(self.__components) <= pos < len(self.__components)
        self.__components[pos] = value


def zeroVector(dimension: int) -> Vector:
    """
    returns a zero-vector of size 'dimension'
    """
    # precondition
    assert isinstance(dimension, int)
    return Vector([0] * dimension)


def unitBasisVector(dimension: int, pos: int) -> Vector:
    """
    returns a unit basis vector with a One
    at index 'pos' (indexing at 0)
    """
    # precondition
    assert isinstance(dimension, int) and (isinstance(pos, int))
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
    assert (
        isinstance(x, Vector)
        and (isinstance(y, Vector))
        and (isinstance(scalar, int) or isinstance(scalar, float))
    )
    return x * scalar + y


def randomVector(N: int, a: int, b: int) -> Vector:
    """
    input: size (N) of the vector.
           random range (a,b)
    output: returns a random vector of size N, with
            random integer components between 'a' and 'b'.
    """
    random.seed(None)
    ans = [random.randint(a, b) for _ in range(N)]
    return Vector(ans)


class Matrix:
    """
    class: Matrix
    This class represents a arbitrary matrix.

    Overview about the methods:

           __str__() : returns a string representation
           operator * : implements the matrix vector multiplication
                        implements the matrix-scalar multiplication.
           changeComponent(x,y,value) : changes the specified component.
           component(x,y) : returns the specified component.
           width() : returns the width of the matrix
           height() : returns the height of the matrix
           operator + : implements the matrix-addition.
           operator - _ implements the matrix-subtraction
    """

    def __init__(self, matrix: list[list[float]], w: int, h: int) -> None:
        """
        simple constructor for initializing
        the matrix with components.
        """
        self.__matrix = matrix
        self.__width = w
        self.__height = h

    def __str__(self) -> str:
        """
        returns a string representation of this
        matrix.
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

    def changeComponent(self, x: int, y: int, value: float) -> None:
        """
        changes the x-y component of this matrix
        """
        if 0 <= x < self.__height and 0 <= y < self.__width:
            self.__matrix[x][y] = value
        else:
            raise Exception("changeComponent: indices out of bounds")

    def component(self, x: int, y: int) -> float:
        """
        returns the specified (x,y) component
        """
        if 0 <= x < self.__height and 0 <= y < self.__width:
            return self.__matrix[x][y]
        else:
            raise Exception("changeComponent: indices out of bounds")

    def width(self) -> int:
        """
        getter for the width
        """
        return self.__width

    def height(self) -> int:
        """
        getter for the height
        """
        return self.__height

    def determinate(self) -> float:
        """
        returns the determinate of an nxn matrix using Laplace expansion
        """
        if self.__height == self.__width and self.__width >= 2:
            total = 0
            if self.__width > 2:
                for x in range(0, self.__width):
                    for y in range(0, self.__height):
                        total += (
                            self.__matrix[x][y]
                            * (-1) ** (x + y)
                            * Matrix(
                                self.__matrix[0:x] + self.__matrix[x + 1 :],
                                self.__width - 1,
                                self.__height - 1,
                            ).determinate()
                        )
            else:
                return (
                    self.__matrix[0][0] * self.__matrix[1][1]
                    - self.__matrix[0][1] * self.__matrix[1][0]
                )
            return total
        else:
            raise Exception("matrix is not square")

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
        if isinstance(other, Vector):  # vector-matrix
            if len(other) == self.__width:
                ans = zeroVector(self.__height)
                for i in range(self.__height):
                    summe: float = 0
                    for j in range(self.__width):
                        summe += other.component(j) * self.__matrix[i][j]
                    ans.changeComponent(i, summe)
                    summe = 0
                return ans
            else:
                raise Exception(
                    "vector must have the same size as the "
                    + "number of columns of the matrix!"
                )
        elif isinstance(other, int) or isinstance(other, float):  # matrix-scalar
            matrix = [
                [self.__matrix[i][j] * other for j in range(self.__width)]
                for i in range(self.__height)
            ]
            return Matrix(matrix, self.__width, self.__height)

    def __add__(self, other: Matrix) -> Matrix:
        """
        implements the matrix-addition.
        """
        if self.__width == other.width() and self.__height == other.height():
            matrix = []
            for i in range(self.__height):
                row = []
                for j in range(self.__width):
                    row.append(self.__matrix[i][j] + other.component(i, j))
                matrix.append(row)
            return Matrix(matrix, self.__width, self.__height)
        else:
            raise Exception("matrix must have the same dimension!")

    def __sub__(self, other: Matrix) -> Matrix:
        """
        implements the matrix-subtraction.
        """
        if self.__width == other.width() and self.__height == other.height():
            matrix = []
            for i in range(self.__height):
                row = []
                for j in range(self.__width):
                    row.append(self.__matrix[i][j] - other.component(i, j))
                matrix.append(row)
            return Matrix(matrix, self.__width, self.__height)
        else:
            raise Exception("matrix must have the same dimension!")


def squareZeroMatrix(N: int) -> Matrix:
    """
    returns a square zero-matrix of dimension NxN
    """
    ans: list[list[float]] = [[0] * N for _ in range(N)]
    return Matrix(ans, N, N)


def randomMatrix(W: int, H: int, a: int, b: int) -> Matrix:
    """
    returns a random matrix WxH with integer components
    between 'a' and 'b'
    """
    random.seed(None)
    matrix: list[list[float]] = [
        [random.randint(a, b) for _ in range(W)] for _ in range(H)
    ]
    return Matrix(matrix, W, H)
