import numpy as np


def softmax(vector: np.ndarray | list | tuple, axis: int | None = -1) -> np.ndarray:
    """
    Compute the softmax of `vector` along `axis` in a numerically-stable way.

    Parameters
    ----------
    vector : array_like (np.ndarray, list, or tuple)
        Input data (vector, matrix, tensor). Will be converted to float ndarray.
    axis : int or None, optional
        Axis along which to compute softmax. If None, compute softmax over
        the flattened array (single distribution). Default is -1 (last axis).

    Returns
    -------
    np.ndarray
        Same shape as `vector`, with softmax applied along `axis`. Probabilities
        sum to 1 along `axis` (or to 1 overall if axis is None).

    Raises
    ------
    ValueError
        If input is empty or cannot be converted to a float ndarray.
    """
    try:
        vector = np.asarray(vector, dtype=float)
    except TypeError as e:
        msg = f"Could not convert input to float ndarray: {e}"
        raise ValueError(msg)

    if vector.size == 0:
        raise ValueError("softmax input must be non-empty")

    if axis is None:
        # flatten to single distribution
        vector_max = np.max(vector)
        e_vector = np.exp(vector - vector_max)
        return e_vector / e_vector.sum()

    # subtract max along axis with keepdims for numerical stability/broadcasting
    vector_max = np.max(vector, axis=axis, keepdims=True)
    e_vector = np.exp(vector - vector_max)
    denom = e_vector.sum(axis=axis, keepdims=True)
    return e_vector / denom


def _test_softmax():
    import numpy.testing as npt

    # Typical 1D input
    result = softmax([1, 2, 3])
    npt.assert_almost_equal(result.sum(), 1)

    # Typical 2D, axis=-1
    result = softmax([[1, 2, 3], [4, 5, 6]])
    npt.assert_almost_equal(result.sum(axis=-1).tolist(), [1, 1])

    # Scalar input
    result = softmax([0])
    npt.assert_almost_equal(result, [1.0])

    # Identical values
    result = softmax([5, 5])
    npt.assert_almost_equal(result, [0.5, 0.5])

    # Large values for numeric stability
    result = softmax([1000, 1001])
    npt.assert_almost_equal(result.sum(), 1)

    # axis=None flatten
    data = np.array([[1, 2], [3, 4]])
    flat_result = softmax(data, axis=None)
    npt.assert_almost_equal(flat_result.sum(), 1)

    # Empty input error
    try:
        softmax([])
        raise AssertionError("Expected ValueError for empty input")
    except ValueError:
        pass

    print("All tests passed.")


if __name__ == "__main__":
    print("Softmax demonstration:")

    print("softmax((0,)) =", softmax((0,)))

    print("softmax([1, 2, 3]) =", softmax([1, 2, 3]))

    print("softmax([[1, 2, 3], [4, 5, 6]]) =", softmax([[1, 2, 3], [4, 5, 6]]))

    _test_softmax()
