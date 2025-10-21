"""
Assumption:
    - The values to compress are assumed to be comparable,
      values can be sorted and compared with '<' and '>' operators.
"""


class CoordinateCompressor:
    """
    A class for coordinate compression.

    This class allows you to compress and decompress a list of values.

    Mapping:
    In addition to compression and decompression, this class maintains a mapping
    between original values and their compressed counterparts using two data
    structures: a dictionary `coordinate_map` and a list `reverse_map`:
    - `coordinate_map`: A dictionary that maps original values to compressed
      coordinates.
    - `reverse_map`: A list used for reverse mapping, where each index corresponds
      to a compressed coordinate, and the value at that index is the original value.

    Example of mapping:
    Original: 10, Compressed: 0
    Original: 52, Compressed: 1
    Original: 83, Compressed: 2
    Original: 100, Compressed: 3
    """

    def __init__(self, arr: list[int | float | str]) -> None:
        """
        Initialize the CoordinateCompressor with a list.

        Args:
        arr: The list of values to be compressed.

        >>> arr = [100, 10, 52, 83]
        >>> cc = CoordinateCompressor(arr)
        >>> cc.compress(100)
        3
        >>> cc.compress(52)
        1
        >>> cc.decompress(1)
        52
        """
        self.coordinate_map: dict[int | float | str, int] = {}
        self.reverse_map: list[int | float | str] = [-1] * len(arr)
        self.arr = sorted(arr)
        self.n = len(arr)
        self.compress_coordinates()

    def compress_coordinates(self) -> None:
        """
        Compress the coordinates in the input list.

        >>> arr = [100, 10, 52, 83]
        >>> cc = CoordinateCompressor(arr)
        >>> cc.coordinate_map[83]
        2
        >>> cc.reverse_map[2]
        83
        """
        key = 0
        for val in self.arr:
            if val not in self.coordinate_map:
                self.coordinate_map[val] = key
                self.reverse_map[key] = val
                key += 1

    def compress(self, original: float | str) -> int:
        """
        Compress a single value.

        Args:
        original: The value to compress.

        Returns:
        The compressed integer.

        Raises:
        ValueError if the value is not in the original list.

        >>> arr = [100, 10, 52, 83]
        >>> cc = CoordinateCompressor(arr)
        >>> cc.compress(100)
        3
        >>> cc.compress(7)
        Traceback (most recent call last):
        ...
        ValueError: Value 7 not found in coordinate map.
        """
        if original not in self.coordinate_map:
            raise ValueError(f"Value {original} not found in coordinate map.")
        return self.coordinate_map[original]

    def decompress(self, num: int) -> int | float | str:
        """
        Decompress a single integer.

        Args:
        num: The compressed integer to decompress.

        Returns:
        The original value.

        Raises:
        ValueError if the compressed coordinate is out of range.

        >>> arr = [100, 10, 52, 83]
        >>> cc = CoordinateCompressor(arr)
        >>> cc.decompress(0)
        10
        >>> cc.decompress(5)
        Traceback (most recent call last):
        ...
        ValueError: Index 5 out of range.
        """
        if 0 <= num < len(self.reverse_map):
            return self.reverse_map[num]
        raise ValueError(f"Index {num} out of range.")


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    arr: list[int | float | str] = [100, 10, 52, 83]
    cc = CoordinateCompressor(arr)

    for original in arr:
        compressed = cc.compress(original)
        decompressed = cc.decompress(compressed)
        print(f"Original: {decompressed}, Compressed: {compressed}")
