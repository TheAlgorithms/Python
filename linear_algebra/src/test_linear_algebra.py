"""
Created on Mon Feb 26 15:40:07 2018

@author: Christian Bender
@license: MIT-license

This file contains the test-suite for the linear algebra library.
"""
import unittest

import pytest

from .lib import (
    Matrix,
    Vector,
    axpy,
    square_zero_matrix,
    unit_basis_vector,
    zero_vector,
)


class Test(unittest.TestCase):
    def test_component(self) -> None:
        """
        test for method component()
        """
        x = Vector([1, 2, 3])
        assert x.component(0) == 1
        assert x.component(2) == 3
        _ = Vector()

    def test_str(self) -> None:
        """
        test for method toString()
        """
        x = Vector([0, 0, 0, 0, 0, 1])
        assert str(x) == "(0,0,0,0,0,1)"

    def test_size(self) -> None:
        """
        test for method size()
        """
        x = Vector([1, 2, 3, 4])
        assert len(x) == 4

    def test_euclidean_length(self) -> None:
        """
        test for method euclidean_length()
        """
        x = Vector([1, 2])
        y = Vector([1, 2, 3, 4, 5])
        z = Vector([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        w = Vector([1, -1, 1, -1, 2, -3, 4, -5])
        assert x.euclidean_length() == pytest.approx(2.236, abs=1e-3)
        assert y.euclidean_length() == pytest.approx(7.416, abs=1e-3)
        assert z.euclidean_length() == 0
        assert w.euclidean_length() == pytest.approx(7.616, abs=1e-3)

    def test_add(self) -> None:
        """
        test for + operator
        """
        x = Vector([1, 2, 3])
        y = Vector([1, 1, 1])
        assert (x + y).component(0) == 2
        assert (x + y).component(1) == 3
        assert (x + y).component(2) == 4

    def test_sub(self) -> None:
        """
        test for - operator
        """
        x = Vector([1, 2, 3])
        y = Vector([1, 1, 1])
        assert (x - y).component(0) == 0
        assert (x - y).component(1) == 1
        assert (x - y).component(2) == 2

    def test_mul(self) -> None:
        """
        test for * operator
        """
        x = Vector([1, 2, 3])
        a = Vector([2, -1, 4])  # for test of dot product
        b = Vector([1, -2, -1])
        assert str(x * 3.0) == "(3.0,6.0,9.0)"
        assert a * b == 0

    def test_zero_vector(self) -> None:
        """
        test for global function zero_vector()
        """
        assert str(zero_vector(10)).count("0") == 10

    def test_unit_basis_vector(self) -> None:
        """
        test for global function unit_basis_vector()
        """
        assert str(unit_basis_vector(3, 1)) == "(0,1,0)"

    def test_axpy(self) -> None:
        """
        test for global function axpy() (operation)
        """
        x = Vector([1, 2, 3])
        y = Vector([1, 0, 1])
        assert str(axpy(2, x, y)) == "(3,4,7)"

    def test_copy(self) -> None:
        """
        test for method copy()
        """
        x = Vector([1, 0, 0, 0, 0, 0])
        y = x.copy()
        assert str(x) == str(y)

    def test_change_component(self) -> None:
        """
        test for method change_component()
        """
        x = Vector([1, 0, 0])
        x.change_component(0, 0)
        x.change_component(1, 1)
        assert str(x) == "(0,1,0)"

    def test_str_matrix(self) -> None:
        """
        test for Matrix method str()
        """
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        assert str(a) == "|1,2,3|\n|2,4,5|\n|6,7,8|\n"

    def test_minor(self) -> None:
        """
        test for Matrix method minor()
        """
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        minors = [[-3, -14, -10], [-5, -10, -5], [-2, -1, 0]]
        for x in range(a.height()):
            for y in range(a.width()):
                assert minors[x][y] == a.minor(x, y)

    def test_cofactor(self) -> None:
        """
        test for Matrix method cofactor()
        """
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        cofactors = [[-3, 14, -10], [5, -10, 5], [-2, 1, 0]]
        for x in range(a.height()):
            for y in range(a.width()):
                assert cofactors[x][y] == a.cofactor(x, y)

    def test_determinant(self) -> None:
        """
        test for Matrix method determinant()
        """
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        assert a.determinant() == -5

    def test__mul__matrix(self) -> None:
        """
        test for Matrix * operator
        """
        a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3)
        x = Vector([1, 2, 3])
        assert str(a * x) == "(14,32,50)"
        assert str(a * 2) == "|2,4,6|\n|8,10,12|\n|14,16,18|\n"

    def test_change_component_matrix(self) -> None:
        """
        test for Matrix method change_component()
        """
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        a.change_component(0, 2, 5)
        assert str(a) == "|1,2,5|\n|2,4,5|\n|6,7,8|\n"

    def test_component_matrix(self) -> None:
        """
        test for Matrix method component()
        """
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        assert a.component(2, 1) == 7, 0.01

    def test__add__matrix(self) -> None:
        """
        test for Matrix + operator
        """
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        b = Matrix([[1, 2, 7], [2, 4, 5], [6, 7, 10]], 3, 3)
        assert str(a + b) == "|2,4,10|\n|4,8,10|\n|12,14,18|\n"

    def test__sub__matrix(self) -> None:
        """
        test for Matrix - operator
        """
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        b = Matrix([[1, 2, 7], [2, 4, 5], [6, 7, 10]], 3, 3)
        assert str(a - b) == "|0,0,-4|\n|0,0,0|\n|0,0,-2|\n"

    def test_square_zero_matrix(self) -> None:
        """
        test for global function square_zero_matrix()
        """
        assert str(square_zero_matrix(5)) == (
            "|0,0,0,0,0|\n|0,0,0,0,0|\n|0,0,0,0,0|\n|0,0,0,0,0|\n|0,0,0,0,0|\n"
        )


if __name__ == "__main__":
    unittest.main()
