"""
Coordinate Compression Utility
------------------------------

Fix for Issue #13226: Handles missing or invalid values (None, NaN)
to ensure consistent compression behavior.

This module provides a `CoordinateCompressor` class that safely compresses
and decompresses values from a list by mapping each unique valid value
to a unique integer index.

Invalid or non-comparable values (like None or NaN) are ignored during
compression mapping and return -1 when compressed.
"""

from __future__ import annotations

import math
from typing import Any


class CoordinateCompressor:
    """
    CoordinateCompressor compresses comparable values to integer ranks.

    Example:
    >>> arr = [100, 10, 52, 83]
    >>> cc = CoordinateCompressor(arr)
    >>> cc.compress(100)
    3
    >>> cc.compress(52)
    1
    >>> cc.decompress(1)
    52
    >>> cc.compress(None)
    -1
    """

    def __init__(self, arr: list[Any]) -> None:
        """
        Initialize the CoordinateCompressor with a list.

        Args:
            arr: The list of values to be compressed.

        Invalid or missing values (None, NaN) are skipped when building
        the mapping, ensuring consistent compression behavior.

        >>> arr = [100, None, 52, 83, float("nan")]
        >>> cc = CoordinateCompressor(arr)
        >>> cc.compress(100)
        2
        >>> cc.compress(None)
        -1
        >>> cc.compress(float("nan"))
        -1
        """
        # Store the original list
        self.original = list(arr)

        # Filter valid (comparable) values — ignore None and NaN
        valid_values = [
            x
            for x in arr
            if x is not None and not (isinstance(x, float) and math.isnan(x))
        ]

        # Sort and remove duplicates using dict.fromkeys for stable order
        unique_sorted = sorted(dict.fromkeys(valid_values))

        # Create mappings
        self.coordinate_map: dict[Any, int] = {
            v: i for i, v in enumerate(unique_sorted)
        }
        self.reverse_map: list[Any] = unique_sorted.copy()

        # Track invalid values (for reference, not essential)
        self.invalid_values: list[Any] = [
            x for x in arr if x is None or (isinstance(x, float) and math.isnan(x))
        ]

    def compress(self, original: Any) -> int:
        """
        Compress a single value to its coordinate index.

        Returns:
            int: The compressed index, or -1 if invalid or not found.

        >>> arr = [100, 10, 52, 83]
        >>> cc = CoordinateCompressor(arr)
        >>> cc.compress(10)
        0
        >>> cc.compress(7)
        -1
        >>> cc.compress(None)
        -1
        """
        # Handle invalid or missing values
        if original is None:
            return -1
        if isinstance(original, float) and math.isnan(original):
            return -1
        return self.coordinate_map.get(original, -1)

    def decompress(self, num: int) -> Any:
        """
        Decompress an integer coordinate back to its original value.

        Args:
            num: Compressed index to decompress.

        Returns:
            The original value for valid indices, otherwise -1.

        >>> arr = [100, 10, 52, 83]
        >>> cc = CoordinateCompressor(arr)
        >>> cc.decompress(0)
        10
        >>> cc.decompress(5)
        -1
        """
        if 0 <= num < len(self.reverse_map):
            return self.reverse_map[num]
        return -1


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    arr: list[Any] = [100, 10, 52, 83, None, float("nan")]
    cc = CoordinateCompressor(arr)

    print("Coordinate Compression Demo:\n")
    for original in arr:
        compressed = cc.compress(original)
        decompressed = cc.decompress(compressed)
        print(
            f"Original: {original!r:>6} | "
            f"Compressed: {compressed:>2} | "
            f"Decompressed: {decompressed!r}"
        )
