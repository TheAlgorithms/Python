"""
Delta Encoding
--------------

Delta encoding is a lossless data compression method that stores the difference
(delta) between sequential values instead of the absolute values themselves.

For example:
    Input:  [100, 103, 105, 108]
    Output: [100, 3, 2, 3]

The first element is stored as-is; each subsequent value is replaced
by the difference from its predecessor.

This is useful for compressing data that changes gradually, such as
sensor readings, time series data, or pixel values in images.

Reference:
https://en.wikipedia.org/wiki/Delta_encoding
"""


def delta_encode(data: list[int]) -> list[int]:
    """
    Encodes a list of integers using delta encoding.

    Args:
        data (list[int]): A list of integers.

    Returns:
        list[int]: Delta-encoded list.

    Example:
        >>> delta_encode([100, 103, 105, 108])
        [100, 3, 2, 3]
    """
    if not data:
        return []

    deltas = [data[0]]
    for i in range(1, len(data)):
        deltas.append(data[i] - data[i - 1])
    return deltas


def delta_decode(encoded: list[int]) -> list[int]:
    """
    Decodes a delta-encoded list back to the original sequence.

    Args:
        encoded (list[int]): Delta-encoded list.

    Returns:
        list[int]: Decoded list of integers.

    Example:
        >>> delta_decode([100, 3, 2, 3])
        [100, 103, 105, 108]
    """
    if not encoded:
        return []

    decoded = [encoded[0]]
    for i in range(1, len(encoded)):
        decoded.append(decoded[-1] + encoded[i])
    return decoded


if __name__ == "__main__":
    # Example run
    data = [100, 103, 105, 108]
    encoded = delta_encode(data)
    decoded = delta_decode(encoded)

    print(f"Original data: {data}")
    print(f"Delta Encoded: {encoded}")
    print(f"Delta Decoded: {decoded}")
