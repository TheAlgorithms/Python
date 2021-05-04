"""Author Alexandre De Zotti

Draws Julia sets of quadratic polynomials and exponential maps. More specifically, this iterates the function a fixed number of times then plot whether the absolute value of the last iterate is greater than a fixed threshold (named "escape radius"). For  the exponential map this is not really an escape radius but rather a convenient way to approximate the Julia set with bounded orbits.

The examples presented here are:
- The Cauliflower Julia set, see e.g. https://en.wikipedia.org/wiki/File:Julia_z2%2B0,25.png
- Other examples from https://en.wikipedia.org/wiki/Julia_set
- An exponential map Julia set ambiantly homeomorphic to the examples from in http://www.math.univ-toulouse.fr/~cheritat/GalII/galery.html and https://ddd.uab.cat/pub/pubmat/02141493v43n1/02141493v43n1p27.pdf
"""

import warnings
from typing import Any, Callable, NewType, Union

import numpy
from matplotlib import pyplot

c_cauliflower = 0.25 + 0.0j
c_polynomial_1 = -0.4 + 0.6j
c_polynomial_2 = -0.7269 + 0.1889j
c_polynomial_2 = -0.1+0.651j 
c_exponential = -2.0
nb_iterations = 56
window_size = 2.0
nb_pixels = 666


def eval_exponential(c: complex, z: numpy.ndarray) -> numpy.ndarray:
    """
    >>> eval_exponential(0, 0)
    1.0
    """
    return numpy.exp(z) + c


def eval_quadratic_polynomial(c: complex, z: numpy.ndarray) -> numpy.ndarray:
    """
    >>> eval_quadratic_polynomial(0, 2)
    4
    >>> eval_quadratic_polynomial(-1, 1)
    0
    >>> eval_quadratic_polynomial(1.j, 0)
    1j
    """
    return z * z + c


def prepare_grid(window_size: float, nb_pixels: int) -> numpy.ndarray:
    """
    Create a grid of complex values of size nb_pixels*nb_pixels with real and
     imaginary parts ranging from -window_size to window_size (inclusive).
    Returns a numpy array.

    >>> prepare_grid(1,3)
    array([[-1.-1.j, -1.+0.j, -1.+1.j],
           [ 0.-1.j,  0.+0.j,  0.+1.j],
           [ 1.-1.j,  1.+0.j,  1.+1.j]])
    """
    x = numpy.linspace(-window_size, window_size, nb_pixels)
    x = x.reshape((nb_pixels, 1))
    y = numpy.linspace(-window_size, window_size, nb_pixels)
    y = y.reshape((1, nb_pixels))
    return x + 1.0j * y


# def iterate_function(eval_function, function_params, nb_iterations: int, z_0: numpy.array) -> numpy.array:
def iterate_function(
    eval_function: Callable[[Any, numpy.ndarray], numpy.ndarray],
    function_params: Any,
    nb_iterations: int,
    z_0: numpy.ndarray,
) -> numpy.ndarray:
    """
    Iterate the function "eval_function" exactly nb_iterations times.
    The first argument of the function is a parameter which is contained in
    function_params. The variable z_0 is an array that contains the initial
    values to iterate from.
    This function returns the final iterates.

    >>> iterate_function(eval_quadratic_polynomial, 0, 3, numpy.array([0,1,2]))
    array([  0,   1, 256])
    """

    z_n = z_0
    for i in range(nb_iterations):
        z_n = eval_function(function_params, z_n)
    return z_n


def show_results(
    function_label: str,
    function_params: Any,
    escape_radius: float,
    z_final: numpy.ndarray,
) -> None:
    """
    Plots of whether the absolute value of z_final is greater than
    the value of escape_radius. Adds the function_label and function_params to
    the title.
    
    >>> show_results('Test', 0, 1, numpy.array([[0,1,0.5],[0.4,2.,1.1],[.2,1.,1.3]]))
    """

    abs_z_final = (abs(z_final)).transpose()
    abs_z_final[:, :] = abs_z_final[::-1, :]
    pyplot.matshow(abs_z_final < escape_radius)
    pyplot.title(f"Julia set of {function_label}\n c={function_params}")
    pyplot.show()


if __name__ == "__main__":

    warnings.filterwarnings("ignore", category=RuntimeWarning)

    nb_iterations = 24
    z_0 = prepare_grid(window_size, nb_pixels)
    z_final = iterate_function(
        eval_quadratic_polynomial, c_cauliflower, nb_iterations, z_0
    )
    escape_radius = 2 * abs(c_cauliflower) + 1
    show_results("z²+c", c_cauliflower, escape_radius, z_final)

    nb_iterations = 64
    z_0 = prepare_grid(window_size, nb_pixels)
    z_final = iterate_function(
        eval_quadratic_polynomial, c_polynomial_1, nb_iterations, z_0
    )
    escape_radius = 2 * abs(c_polynomial_1) + 1
    show_results("z²+c", c_polynomial_1, escape_radius, z_final)

    nb_iterations = 161
    z_0 = prepare_grid(window_size, nb_pixels)
    z_final = iterate_function(
        eval_quadratic_polynomial, c_polynomial_2, nb_iterations, z_0
    )
    escape_radius = 2 * abs(c_polynomial_2) + 1
    show_results("z²+c", c_polynomial_2, escape_radius, z_final)

    nb_iterations = 12
    z_final = iterate_function(eval_exponential, c_exponential, nb_iterations, z_0 + 2)
    escape_radius = 10000.0
    show_results("exp(z)+c", c_exponential, escape_radius, z_final)
