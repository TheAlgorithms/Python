# -*- coding: utf-8 -*-
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
- class Matrix
- squareZeroMatrix(N)
"""


import math


class Vector(object):
    """
        This class represents a vector of arbitray size.
        You need to give the vector components. 
        
        Overview about the methods:
        
        constructor(components : list) : init the vector
        set(components : list) : changes the vector components.
        __str__() : toString method
        component(i : int): gets the i-th component (start by 0)
        size() : gets the size of the vector (number of components)
        euclidLength() : returns the eulidean length of the vector.
        operator + : vector addition
        operator - : vector subtraction
        operator * : scalar multiplication and dot product
        copy() : copies this vector and returns it.
        changeComponent(pos,value) : changes the specified component.
        TODO: compare-operator
    """
    def __init__(self,components):
        """
            input: components or nothing
            simple constructor for init the vector
        """
        self.__components = components
    def set(self,components):
        """
            input: new components
            changes the components of the vector.
            replace the components with newer one.
        """
        if len(components) > 0:
            self.__components = components
        else:
            raise Exception("please give any vector")
    def __str__(self):
        """
            returns a string representation of the vector
        """
        ans = "("
        length = len(self.__components)
        for i in range(length):
            if i != length-1:
                ans += str(self.__components[i]) + ","
            else:
                ans += str(self.__components[i]) + ")"
        if len(ans) == 1:
            ans += ")"
        return ans
    def component(self,i):
        """
            input: index (start at 0)
            output: the i-th component of the vector.
        """
        if i < len(self.__components) and i >= 0:
            return self.__components[i]
        else:
            raise Exception("index out of range")
    def size(self):
        """
            returns the size of the vector
        """
        return len(self.__components)
    def eulidLength(self):
        """
            returns the eulidean length of the vector
        """
        summe = 0
        for c in self.__components:
            summe += c**2
        return math.sqrt(summe)
    def __add__(self,other):
        """
            input: other vector
            assumes: other vector has the same size
            returns a new vector that represents the sum.
        """
        size = self.size()
        result = []
        if size == other.size():
            for i in range(size):
                result.append(self.__components[i] + other.component(i))
        else:
            raise Exception("must have the same size")
        return Vector(result)
    def __sub__(self,other):
        """
            input: other vector
            assumes: other vector has the same size
            returns a new vector that represents the differenz.
        """
        size = self.size()
        result = []
        if size == other.size():
            for i in range(size):
                result.append(self.__components[i] - other.component(i))
        else: # error case
            raise Exception("must have the same size")
        return Vector(result)
    def __mul__(self,other):
        """
            mul implements the scalar multiplication 
            and the dot-product
        """
        ans = []
        if isinstance(other,float) or isinstance(other,int):
            for c in self.__components:
                ans.append(c*other)
        elif (isinstance(other,Vector) and (self.size() == other.size())):
            size = self.size()
            summe = 0
            for i in range(size):
                summe += self.__components[i] * other.component(i)
            return summe
        else: # error case
            raise Exception("invalide operand!")
        return Vector(ans)
    def copy(self):
        """
            copies this vector and returns it.
        """
        components = [x for x in self.__components]
        return Vector(components)
    def changeComponent(self,pos,value):
        """
            input: an index (pos) and a value
            changes the specified component (pos) with the
            'value'
        """
        #precondition
        assert (pos >= 0 and pos < len(self.__components))
        self.__components[pos] = value
    
def zeroVector(dimension):
    """
        returns a zero-vector of size 'dimension'
    """        
    #precondition
    assert(isinstance(dimension,int))
    ans = []
    for i in range(dimension):
        ans.append(0)
    return Vector(ans)


def unitBasisVector(dimension,pos):
    """
        returns a unit basis vector with a One 
        at index 'pos' (indexing at 0)
    """
    #precondition
    assert(isinstance(dimension,int) and (isinstance(pos,int)))
    ans = []
    for i in range(dimension):
        if i != pos:
            ans.append(0)
        else:
            ans.append(1)
    return Vector(ans)
        

def axpy(scalar,x,y):
    """
        input: a 'scalar' and two vectors 'x' and 'y'
        output: a vector
        computes the axpy operation
    """
    # precondition
    assert(isinstance(x,Vector) and (isinstance(y,Vector)) \
    and (isinstance(scalar,int) or isinstance(scalar,float)))
    return (x*scalar + y)
    

class Matrix(object):
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
    def __init__(self,matrix,w,h):
        """
            simple constructor for initialzes 
            the matrix with components.
        """
        self.__matrix = matrix
        self.__width = w
        self.__height = h
    def __str__(self):
        """
            returns a string representation of this
            matrix.
        """
        ans = ""
        for i in range(self.__height):
            ans += "|"
            for j in range(self.__width):
                if j < self.__width -1:
                    ans += str(self.__matrix[i][j]) + ","
                else:
                    ans += str(self.__matrix[i][j]) + "|\n"
        return ans
    def changeComponent(self,x,y, value):
        """
            changes the x-y component of this matrix
        """
        if x >= 0 and x < self.__height and y >= 0 and y < self.__width:
            self.__matrix[x][y] = value
        else:
            raise Exception ("changeComponent: indices out of bounds")
    def component(self,x,y):
        """
            returns the specified (x,y) component
        """
        if x >= 0 and x < self.__height and y >= 0 and y < self.__width:
            return self.__matrix[x][y]
        else:
            raise Exception ("changeComponent: indices out of bounds")
    def width(self):
        """
            getter for the width
        """
        return self.__width
    def height(self):
        """
            getter for the height
        """
        return self.__height
    def __mul__(self,other):
        """
            implements the matrix-vector multiplication.
            implements the matrix-scalar multiplication
        """
        if isinstance(other, Vector): # vector-matrix 
            if (other.size() == self.__width):
                ans = zeroVector(self.__height)
                for i in range(self.__height):
                    summe = 0
                    for j in range(self.__width):
                        summe += other.component(j) * self.__matrix[i][j]
                    ans.changeComponent(i,summe)
                    summe = 0
                return ans
            else:
                raise Exception("vector must have the same size as the "
                + "number of columns of the matrix!")
        elif isinstance(other,int) or isinstance(other,float): # matrix-scalar
            matrix = []
            for i in range(self.__height):
                row = []
                for j in range(self.__width):
                    row.append(self.__matrix[i][j] * other)
                matrix.append(row)
            return Matrix(matrix,self.__width,self.__height)
    def __add__(self,other):
        """
            implements the matrix-addition.
        """
        if (self.__width == other.width() and self.__height == other.height()):
            matrix = []
            for i in range(self.__height):
                row = []
                for j in range(self.__width):
                    row.append(self.__matrix[i][j] + other.component(i,j))
                matrix.append(row)
            return Matrix(matrix,self.__width,self.__height)
        else:
            raise Exception("matrix must have the same dimension!")
    def __sub__(self,other):
        """
            implements the matrix-subtraction.
        """
        if (self.__width == other.width() and self.__height == other.height()):
            matrix = []
            for i in range(self.__height):
                row = []
                for j in range(self.__width):
                    row.append(self.__matrix[i][j] - other.component(i,j))
                matrix.append(row)
            return Matrix(matrix,self.__width,self.__height)
        else:
            raise Exception("matrix must have the same dimension!")
    

def squareZeroMatrix(N):
    """
        returns a square zero-matrix of dimension NxN
    """
    ans = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(0)
        ans.append(row)
    return Matrix(ans,N,N)
            
        