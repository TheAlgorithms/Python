"""
This script demonstrates the implementation of the Softmax function.

It takes as input a vector of K real numbers and normalizes it into a
probability distribution consisting of K probabilities proportional
to the exponentials of the input numbers. After applying softmax,
the elements of the vector always sum up to 1.

Script inspired by its corresponding Wikipedia article:
https://en.wikipedia.org/wiki/Softmax_function
"""

import numpy as np
from numpy.exceptions import AxisError


def softmax(vector: np.ndarray, axis: int | None = -1) -> np.ndarray:
    """
    Compute the softmax of ``vector`` along ``axis`` in a numerically-stable way.

    Parameters:
        vector (np.ndarray | list | tuple): Input data (vector, matrix or
            higher-rank tensor). It is converted to a float ``np.ndarray``,
            so lists, tuples and integers are accepted too.
        axis (int | None, optional): Axis along which softmax is computed so
            that the probabilities sum to 1 along that axis. If ``None``, the
            softmax is computed over the flattened array (a single
            distribution). Default is ``-1`` (the last axis).

    Returns:
        np.ndarray: An array with the same shape as ``vector`` whose values
        along ``axis`` (or over the whole array when ``axis is None``) form a
        probability distribution that sums to 1.

    Raises:
        ValueError: If ``vector`` is empty or cannot be converted to a numeric
            float array (for example a string or a dict).
        numpy.exceptions.AxisError: If ``axis`` is out of bounds for the input.

    Note:
        If the input contains ``NaN`` or ``inf`` the result will contain
        ``NaN`` along the affected axis; softmax is only meaningful for finite
        real inputs.

    The softmax vector adds up to one. We need to ceil to mitigate precision.

    >>> float(np.ceil(np.sum(softmax([1, 2, 3, 4]))))
    1.0

    Identical logits map to a uniform distribution:

    >>> softmax(np.array([5, 5]))
    array([0.5, 0.5])

    A single element always maps to 1:

    >>> softmax([0])
    array([1.])

    It is numerically stable for large logits (no overflow):

    >>> softmax([1000.0, 1001.0, 1002.0])
    array([0.09003057, 0.24472847, 0.66524096])

    For a 2-D array the ``axis`` selects where probabilities sum to 1:

    >>> mat = np.array([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]])
    >>> np.round(softmax(mat, axis=-1), 3)
    array([[0.09 , 0.245, 0.665],
           [0.09 , 0.245, 0.665]])
    >>> np.round(softmax(mat, axis=0), 3)
    array([[0.5, 0.5, 0.5],
           [0.5, 0.5, 0.5]])

    With ``axis=None`` the whole array becomes one distribution that sums to 1:

    >>> float(np.round(np.sum(softmax(mat, axis=None)), 6))
    1.0

    Empty, non-numeric and out-of-bounds inputs raise clear errors:

    >>> softmax([])
    Traceback (most recent call last):
        ...
    ValueError: softmax input must be non-empty
    >>> softmax("not a number")
    Traceback (most recent call last):
        ...
    ValueError: softmax input must be numeric, got str
    >>> softmax([1, 2, 3], axis=3)
    Traceback (most recent call last):
        ...
    numpy.exceptions.AxisError: axis 3 is out of bounds for array of dimension 1
    """
    # Convert input to a float numpy array, turning numpy's terse conversion
    # errors into a clear message about the unsupported input type.
    try:
        vector = np.asarray(vector, dtype=float)
    except (ValueError, TypeError) as exc:
        error_message = f"softmax input must be numeric, got {type(vector).__name__}"
        raise ValueError(error_message) from exc

    # Handle empty input
    if vector.size == 0:
        raise ValueError("softmax input must be non-empty")

    # Validate axis (None means "treat the whole array as one distribution")
    if axis is not None:
        ndim = vector.ndim
        if axis >= ndim or axis < -ndim:
            error_message = (
                f"axis {axis} is out of bounds for array of dimension {ndim}"
            )
            raise AxisError(error_message)

    # Subtract max for numerical stability
    vector_max = np.max(vector, axis=axis, keepdims=True)
    exponent_vector = np.exp(vector - vector_max)

    # Sum of exponentials along the axis
    sum_of_exponents = np.sum(exponent_vector, axis=axis, keepdims=True)

    # Divide each exponent by the sum along the axis
    softmax_vector = exponent_vector / sum_of_exponents
    return softmax_vector


if __name__ == "__main__":
    # Single value
    print(softmax((0,)))
    # Vector
    print(softmax([1, 2, 3]))
    # Matrix along last axis
    mat = np.array([[1, 2, 3], [4, 5, 6]])
    print("Softmax along last axis:\n", softmax(mat))
    # Matrix along axis 0
    print("Softmax along axis 0:\n", softmax(mat, axis=0))
    # Whole-matrix distribution
    print("Softmax over the whole matrix:\n", softmax(mat, axis=None))
