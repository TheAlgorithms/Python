"""
Assumption:
    - The values to compress are assumed to be comparable,
    - values can be sorted and compared with '<' and '>' operators.
"""


class CoordinateCompressor:
    """
    A class for coordinate compression.

    This class allows you to compress and decompress a list of values.

    Mapping:
    In addition to compression and decompression, this class maintains a mapping
    between original values and their compressed counterparts using two data
    structures: a dictionary `coordinate_map` and a list `reverse_map`.

    - `coordinate_map`: A dictionary that maps original values to their compressed
      coordinates. Keys are original values, and values are compressed coordinates.

    - `reverse_map`: A list used for reverse mapping, where each index corresponds
      to a compressed coordinate, and the value at that index is the original value.

    Example mapping:

    Original: 10, Compressed: 0
    Original: 52, Compressed: 1
    Original: 83, Compressed: 2
    Original: 100, Compressed: 3

    This mapping allows for efficient compression and decompression of values within
    the list.
    """

    def __init__(self, arr):
        """
        Initialize the CoordinateCompressor with a list.

        Args:
        arr (list): The list of values to be compressed.

        >>> arr = [100, 10, 52, 83]
        >>> cc = CoordinateCompressor(arr)
        >>> cc.compress(100)
        3
        >>> cc.compress(52)
        1
        >>> cc.decompress(1)
        52

        """

        self.coordinate_map = {}  # A dictionary to store compressed coordinates
        self.reverse_map = [-1] * (len(arr))  # A list to store reverse mapping
        self.arr = sorted(arr)  # The input list
        self.n = len(arr)  # The length of the input list
        self.compress_coordinates()

    def compress_coordinates(self):
        """
        Compress the coordinates in the input list.
        """
        key = 0
        for val in self.arr:
            if val not in self.coordinate_map:
                self.coordinate_map[val] = key
                self.reverse_map[key] = val
                key += 1

    def compress(self, num):
        """
        Compress a single value.

        Args:
        num (any) : The value to compress.

        Returns:
        int: The compressed integer, or -1 if not found in the original list.

        >>> arr = [100, 10, 52, 83]
        >>> cc = CoordinateCompressor(arr)
        >>> cc.compress(100)
        3
        >>> cc.compress(7)  # Value not in the original list
        -1

        """
        return self.coordinate_map.get(num, -1)

    def decompress(self, num):
        """
        Decompress a single integer.

        Args:
        num (int): The compressed integer to decompress.

        Returns:
        original value (any) : The original value.

        >>> arr = [100, 10, 52, 83]
        >>> cc = CoordinateCompressor(arr)
        >>> cc.decompress(0)
        10
        >>> cc.decompress(5)  # Compressed coordinate out of range
        -1

        """
        return self.reverse_map[num] if num < len(self.reverse_map) else -1

    @staticmethod
    def how_to_use():
        """
        Example usage of CoordinateCompressor.
        """
        arr = [100, 10, 52, 83]
        cc = CoordinateCompressor(arr)
        compressed = [0] * len(arr)
        decompressed = [0] * len(arr)

        for i in range(len(arr)):
            compressed[i] = cc.compress(arr[i])
            decompressed[i] = cc.decompress(compressed[i])
            print(f"Original: {arr[i]}, Compressed: {compressed[i]}")


if __name__ == "__main__":
    from doctest import testmod

    testmod()
