import numpy as np


def hilbert_sort(data: list) -> list:
    """
    Imagine you have a bunch of balls, each with a different number on it. To sort the balls, you first throw them up in the air. As each ball falls back down, it follows a unique path based on its number.
    As the balls fall back down and land, they come to rest at a location in 2D space.
    To sort the balls based on their 2D coordinates, you can imagine lining up the balls along a winding road (Hilbert curve) based on their location. The balls that are close together along the road are also close together in 2D space.
    Finally, you can read off the sorted order of the balls by simply following the order in which they appear along the winding road. This is similar to reading a book by following the order of the words on the page.
    In this analogy the balls would start in 1D space and be transposed into 2D space, the 3rd dimension is mostly analogy.
    """
    data = np.array(data)

    # Map each number in the input array to a point in 2D space using the Hilbert curve
    # Step 1: Convert each number to binary using zfill to ensure each binary string is 16 bits long
    binary_array = np.array([list(bin(n)[2:].zfill(16)) for n in data], dtype=int)

    # Step 2: Generate the coordinates for each binary string using the Hilbert curve
    coords_array = np.zeros((len(data), 32))

    # Step 2a: Compute the odd-indexed coordinates using the cumulative sum of the product of the binary values and powers of 2
    coords_array[:, 1::2] = np.cumsum(
        (-1) ** binary_array[:, ::-1] * 2 ** np.arange(16), axis=1
    )[:, ::-1]

    # Step 2b: Compute the even-indexed coordinates using a cumulative product of the binary values, reversed and shifted by 1
    # We reverse the binary values so that the most significant bit is at the end of the array, making it easier to compute the cumulative product
    # We shift the array by 1 so that we don't include the value for the current index in the product
    # We use np.cumprod to compute the cumulative product of the binary values, which are either -1 or 1
    # We reverse the result again and concatenate a column of zeros to obtain the even-indexed coordinates
    coords_array[:, ::2] = np.concatenate(
        (
            np.zeros((len(data), 1)),
            np.cumprod((-1) ** binary_array[:, ::-1][:, :-1], axis=1)[:, ::-1],
        ),
        axis=1,
    )

    # Step 2c: Compute the cumulative sum of the coordinates to obtain the final Hilbert curve coordinates
    np.add.accumulate(coords_array, axis=1, out=coords_array)

    # Step 3: Sort the data array based on the Hilbert curve coordinates
    sorted_indices = np.lexsort(coords_array.T)
    return data[sorted_indices].tolist()[::-1]
