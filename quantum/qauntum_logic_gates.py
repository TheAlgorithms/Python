"""
Quantum Logic Gates which are implemented mathematically
and can be used as functions to build complex calculations
and implement different operations. The input taken is a real value
and imaginary value of the number and the result is output after computation.

References :
https://en.wikipedia.org/wiki/Quantum_logic_gate

Book : Mathematics Of Quantum Computing An Introduction by Wolfgang Scherer
"""

import cmath
import math

import numpy as np


def paulix_gate(input_realvalue: float, input_imaginaryvalue: float) -> list[float]:
    """
    Glossary :
    input_realvalue : the magnitude of the real part of the input complex number.
    input_imaginaryvalue : the magnitude of the imaginary part
    of the input complex number.
    In cases which require 2 inputs the input is named with a suffix of 1 and 2
    (Eg. input_realvalue_1)

    Usage :
    >>> paulix_gate(2,3)
    array([3, 2])
    """
    paulix_matrix = np.array([[0, 1], [1, 0]])
    complex_input = np.array([input_realvalue, input_imaginaryvalue])
    result = np.dot(paulix_matrix, complex_input)
    return result


def pauliy_gate(input_realvalue: float, input_imaginaryvalue: float) -> list[float]:
    """
    Glossary :
    input_realvalue : the magnitude of the real part of the input complex number.
    input_imaginaryvalue : the magnitude of the imaginary part
    of the input complex number.
    In cases which require 2 inputs the input is named with a suffix of 1 and 2
    (Eg. input_realvalue_1)

    Usage :
    >>> pauliy_gate(5,8)
    array([0.+8.j, 0.-5.j])
    """
    i = complex(0, 1)
    pauliy_matrix = [[0, i], [-1 * i, 0]]
    complex_input = np.array([input_realvalue, input_imaginaryvalue])
    result = np.dot(pauliy_matrix, complex_input)
    return result


def pauliz_gate(input_realvalue: float, input_imaginaryvalue: float) -> list[float]:
    """
    Glossary :
    input_realvalue : the magnitude of the real part of the input complex number.
    input_imaginaryvalue : the magnitude
    of the imaginary part of the input complex number.
    In cases which require 2 inputs the input is named with a suffix of 1 and 2
    (Eg. input_realvalue_1)

    Usage :
    >>> pauliz_gate(4,1)
    array([ 4, -1])
    """
    pauliz_matrix = np.array([[1, 0], [0, -1]])
    complex_input = np.array([input_realvalue, input_imaginaryvalue])
    result = np.dot(pauliz_matrix, complex_input)
    return result


def identity_gate(input_realvalue: float, input_imaginaryvalue: float) -> float:
    """
    Glossary :
    input_realvalue : the magnitude of the real part of the input complex number.
    input_imaginaryvalue : the magnitude of the imaginary part
    of the input complex number.
    In cases which require 2 inputs the input is named with a suffix of 1 and 2
    (Eg. input_realvalue_1)

    Usage :
    >>> identity_gate(7,2)
    9
    """
    identiy_matrix = np.diag([[1, 0], [0, 1]])
    complex_input = np.array([input_realvalue, input_imaginaryvalue])
    result = np.dot(identiy_matrix, complex_input)
    return result


def phasefactor_of_input(
    input_realvalue: float, input_imaginaryvalue: float, alpha: float
) -> list[float]:
    """
    Glossary :
    alpha : angle of rotation as represented by the block sphere.
    iota : The exponential complex of alpha value.
    input_realvalue : the magnitude of the real part of the input complex number.
    input_imaginaryvalue : the magnitude of the imaginary part
    of the input complex number.
    In cases which require 2 inputs the input is named with a suffix of 1 and 2
    (Eg. input_realvalue_1)

    Usage :
    >>> phasefactor_of_input(4,7,45)
    array([1.39737084e+20+0.j, 2.44539897e+20+0.j])
    """
    iota = cmath.exp(alpha)
    phasefactor = [[iota, 0], [0, iota]]
    complex_input = np.array([input_realvalue, input_imaginaryvalue])
    result = np.dot(phasefactor, complex_input)
    return result


def phaseshift_of_input(
    input_realvalue: float, input_imaginaryvalue: float, alpha: float
) -> list[float]:
    """
    Glossary :
    alpha : angle of rotation as represented by the block sphere.
    iota : The exponential complex of alpha value.
    input_realvalue : the magnitude of the real part of the input complex number.
    input_imaginaryvalue : the magnitude of the imaginary part
    of the input complex number.
    In cases which require 2 inputs the input is named with a suffix of 1 and 2
    (Eg. input_realvalue_1)

    Usage :
    >>> phaseshift_of_input(3,9,30)
    array([3.00000000e+00+0.j, 9.61782712e+13+0.j])
    """
    iota = cmath.exp(alpha)
    phase = [[1, 0], [0, iota]]
    complex_input = np.array([input_realvalue, input_imaginaryvalue])
    result = np.dot(phase, complex_input)
    return result


def hadamard_gate(input_realvalue: float, input_imaginaryvalue: float) -> list[float]:
    """
    Glossary :
    input_realvalue : the magnitude of the real part of the input complex number.
    input_imaginaryvalue : the magnitude of the imaginary part
    of the input complex number.
    In cases which require 2 inputs the input is named with a suffix of 1 and 2
    (Eg. input_realvalue_1)

    Usage :
    >>> hadamard_gate(5,9)
    array([ 9.89949494, -2.82842712])
    """
    root_of_2 = 1.0 / math.sqrt(2)
    hadamard_gate_matrix = np.array(
        [[root_of_2, root_of_2], [root_of_2, -1 * root_of_2]]
    )
    complex_input = np.array([input_realvalue, input_imaginaryvalue])
    result = np.dot(hadamard_gate_matrix, complex_input)
    return result


def controlled_not_gate_in_0ket(
    input_realvalue_1: float,
    input_imaginaryvalue_1: float,
    input_realvalue_2: float,
    input_imaginaryvalue_2: float,
) -> list[float]:
    """
    Glossary :
    input_realvalue : the magnitude of the real part of the input complex number.
    input_imaginaryvalue : the magnitude of the imaginary part
    of the input complex number.
    In cases which require 2 inputs the input is named with a suffix of 1 and 2
    (Eg. input_realvalue_1)

    Usage :
    >>> controlled_not_gate_in_0ket(1,7,4,8)
    [1 7 4 8]
    array([7, 1, 4, 8])
    """
    controlled_not_gate_0ket_matrix = np.array(
        [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    )
    complex_input = np.array(
        [
            input_realvalue_1,
            input_imaginaryvalue_1,
            input_realvalue_2,
            input_imaginaryvalue_2,
        ]
    )
    print(complex_input)
    result = np.dot(controlled_not_gate_0ket_matrix, complex_input)
    return result


def controlled_not_gate(
    input_realvalue_1: float,
    input_imaginaryvalue_1: float,
    input_realvalue_2: float,
    input_imaginaryvalue_2: float,
) -> list[float]:
    """
    Glossary :
    input_realvalue : the magnitude of the real part of the input complex number.
    input_imaginaryvalue : the magnitude of the imaginary part
    of the input complex number.
    In cases which require 2 inputs the input is named with a suffix of 1 and 2
    (Eg. input_realvalue_1)

    Usage :
    >>> controlled_not_gate(6,3,7,5)
    array([6, 3, 5, 7])
    """
    controlled_not_gate_matrix = np.array(
        [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
    )
    complex_input = np.array(
        [
            input_realvalue_1,
            input_imaginaryvalue_1,
            input_realvalue_2,
            input_imaginaryvalue_2,
        ]
    )
    result = np.dot(controlled_not_gate_matrix, complex_input)
    return result


def inverted_controlled_not_gate(
    input_realvalue_1: float,
    input_imaginaryvalue_1: float,
    input_realvalue_2: float,
    input_imaginaryvalue_2: float,
) -> list[float]:
    """
    Glossary :
    input_realvalue : the magnitude of the real part of the input complex number.
    input_imaginaryvalue : the magnitude of the imaginary part
    of the input complex number.
    In cases which require 2 inputs the input is named with a suffix of 1 and 2
    (Eg. input_realvalue_1)

    Usage :
    >>> inverted_controlled_not_gate(8,4,9,6)
    array([8, 6, 9, 4])
    """
    inverted_controlled_not_gate_matrix = np.array(
        [[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]]
    )
    complex_input = np.array(
        [
            input_realvalue_1,
            input_imaginaryvalue_1,
            input_realvalue_2,
            input_imaginaryvalue_2,
        ]
    )
    result = np.dot(inverted_controlled_not_gate_matrix, complex_input)
    return result


def controlled_phase_multiplication(
    input_realvalue_1: float,
    input_imaginaryvalue_1: float,
    input_realvalue_2: float,
    input_imaginaryvalue_2: float,
    alpha: float,
) -> list[float]:
    """
    Glossary :
    alpha : angle of rotation as represented by the block sphere.
    iota : The exponential complex of alpha value.
    input_realvalue : the magnitude of the real part of the input complex number.
    input_imaginaryvalue : the magnitude of the imaginary part
    of the input complex number.
    In cases which require 2 inputs the input is named with a suffix of 1 and 2
    (Eg. input_realvalue_1)

    Usage :
    >>> controlled_phase_multiplication(3,2,5,1,10)
    array([3.00000000e+00+0.j, 2.00000000e+00+0.j, 1.10132329e+05+0.j,
           2.20264658e+04+0.j])
    """
    iota = cmath.exp(alpha)
    controlled_phase_multiplication_matrix = np.array(
        [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, iota, 0], [0, 0, 0, iota]]
    )
    complex_input = np.array(
        [
            input_realvalue_1,
            input_imaginaryvalue_1,
            input_realvalue_2,
            input_imaginaryvalue_2,
        ]
    )
    result = np.dot(controlled_phase_multiplication_matrix, complex_input)
    return result


def swap_gate(
    input_realvalue_1: float,
    input_imaginaryvalue_1: float,
    input_realvalue_2: float,
    input_imaginaryvalue_2: float,
) -> list[float]:
    """
    Glossary :
    input_realvalue : the magnitude of the real part of the input complex number.
    input_imaginaryvalue : the magnitude of the imaginary part
    of the input complex number.
    In cases which require 2 inputs the input is named with a suffix of 1 and 2
    (Eg. input_realvalue_1)

    Usage :
    >>> swap_gate(5,1,3,7)
    array([5, 3, 1, 7])
    """
    swap_gate_matrix = np.array(
        [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]
    )
    complex_input = np.array(
        [
            input_realvalue_1,
            input_imaginaryvalue_1,
            input_realvalue_2,
            input_imaginaryvalue_2,
        ]
    )
    result = np.dot(swap_gate_matrix, complex_input)
    return result


def spin_of_input(
    input_realvalue: float,
    input_imaginaryvalue: float,
    alpha_value: float,
    nx_value: float,
    ny_value: float,
    nz_value: float,
) -> list[float]:
    """
    Glossary :
    alpha : angle of rotation as represented by the block sphere.
    iota : The exponential complex of alpha value.
    nx_value : value of vector in X axis as represented by Hilbert space.
    nx_value : value of vector in Y axis as represented by Hilbert space.
    nx_value : value of vector in Z axis as represented by Hilbert space.

    * The nx,ny and nz values can also be considered as values of vectors along
    the respective axes on the bloch sphere.

    Usage :
    >>> spin_of_input(6,3,45,1,8,3)
    array([-16.93201614+10.23066476j, -50.61991392 -1.46152354j])
    """
    i = complex(0, 1)
    spin_matrix = [
        [
            (math.cos(alpha_value / 2.0))
            - (i * math.sin(alpha_value / 2.0) * nz_value),
            (-1 * i * math.sin(alpha_value / 2.0) * (nx_value + i * ny_value)),
        ],
        [
            -1 * i * (math.sin(alpha_value / 2.0) * nx_value - i * ny_value),
            math.cos(alpha_value / 2.0) + (i * math.sin(alpha_value / 2.0) * nz_value),
        ],
    ]
    complex_input = np.array([input_realvalue, input_imaginaryvalue])
    result = np.dot(spin_matrix, complex_input)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
