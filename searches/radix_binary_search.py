"""Radix Binary Search: a prefix directory followed by bounded binary search.

Subtract the minimum value to obtain nonnegative keys. Their leading bits
identify buckets containing contiguous ranges of the sorted input. Store each
bucket's start, then use two adjacent starts as the bounds for binary search.

For example, [-8, -8, -1, 0, 7, 8] with bits=2 has minimum -8 and span 16.
The normalized keys are [0, 0, 7, 8, 15, 16]. Using their common five-bit
width, discard three low bits to get bucket numbers [0, 0, 0, 1, 1, 2].
The directory is [0, 3, 5, 6], so bucket 1 covers indices [3, 5): [0, 7].

Background: Kipf et al. (2019), "SOSD: A Benchmark for Learned Indexes",
Section 2: RadixBinarySearch (RBS).
https://arxiv.org/abs/1911.13014
"""

from collections.abc import Sequence
from itertools import pairwise


class RadixBinarySearch:
    """Prepare a reusable index over integers sorted in nondecreasing order.

    Keep a tuple snapshot so later changes to the caller's list cannot make
    the directory stale. Results are indices in that snapshot. Duplicates
    return their first index; missing targets return None.

    ``bits`` controls the maximum number of buckets: 2**bits. The limit of
    12 bounds the directory to 4096 buckets; zero uses a single bucket.
    This cap is a memory-budget choice, not a requirement of the algorithm.

    For n values and B buckets, preparation takes O(n + B) time and storage,
    including the snapshot. Searching a bucket with m values takes
    O(1 + log(m + 1)) time, O(log(n + 1)) worst case, and O(1) extra space.
    These bounds assume constant-time integer arithmetic and comparisons.
    Skewed data can put most values into one bucket. Reuse the index across
    queries to amortize preparation; faster lookup is not guaranteed.
    """

    def __init__(self, values: Sequence[int], *, bits: int = 12) -> None:
        """Validate the input, copy it, and build bucket boundaries.

        >>> RadixBinarySearch([2, 1])
        Traceback (most recent call last):
            ...
        ValueError: values must be sorted in nondecreasing order
        >>> RadixBinarySearch([1, 2.5])
        Traceback (most recent call last):
            ...
        TypeError: values must contain integers, excluding bool
        >>> RadixBinarySearch([], bits=13)
        Traceback (most recent call last):
            ...
        ValueError: bits must be between 0 and 12
        >>> RadixBinarySearch([], bits=True)
        Traceback (most recent call last):
            ...
        TypeError: bits must be an integer, excluding bool
        """
        # bool is an int subclass in Python, but is not a meaningful bit count.
        # Validate even for empty input so the parameter contract is consistent.
        if isinstance(bits, bool) or not isinstance(bits, int):
            raise TypeError("bits must be an integer, excluding bool")
        if not 0 <= bits <= 12:
            raise ValueError("bits must be between 0 and 12")

        # Retain input positions: sorting here would change the returned indices.
        # A tuple keeps this snapshot stable if the caller later edits their list.
        self._values = tuple(values)
        if any(
            isinstance(value, bool) or not isinstance(value, int)
            for value in self._values
        ):
            raise TypeError("values must contain integers, excluding bool")
        if any(left > right for left, right in pairwise(self._values)):
            raise ValueError("values must be sorted in nondecreasing order")

        # Empty input uses a harmless zero-width range and offsets [0, 0].
        # search() checks for emptiness before accessing either endpoint.
        self._minimum = self._values[0] if self._values else 0
        maximum = self._values[-1] if self._values else 0
        span = maximum - self._minimum

        # Subtracting the minimum preserves order and makes every key nonnegative.
        # All keys share the width implied by span; smaller keys have leading zeros.
        # Right-shifting by (width - bits) keeps at most `bits` prefix bits.
        # A zero shift keeps all bits. With bits=0 every key maps to bucket 0.
        self._shift = max(0, span.bit_length() - bits)
        # Bucket numbers start at zero, so include the maximum key's bucket.
        bucket_count = (span >> self._shift) + 1

        # The cursor only moves forward: total work is O(n + B).
        # Equal adjacent offsets describe an empty bucket. The extra offset
        # at the end is len(values), closing the final half-open interval.
        self._offsets: list[int] = []
        position = 0
        for bucket in range(bucket_count + 1):
            # A left shift converts a prefix back to its minimum normalized key.
            # Adding the minimum restores the corresponding input value.
            boundary = self._minimum + (bucket << self._shift)
            # Stop BEFORE equal values: every duplicate stays in the same bucket.
            # offsets[bucket] is the first index with value >= boundary.
            while position < len(self._values) and self._values[position] < boundary:
                position += 1
            self._offsets.append(position)

    def search(self, target: int) -> int | None:
        """Return the first matching index, or None if target is absent.

        >>> index = RadixBinarySearch([-8, -8, -1, 0, 7, 8], bits=2)
        >>> [index.search(target) for target in (-8, -1, 0, 7, 8)]
        [0, 2, 3, 4, 5]
        >>> [index.search(target) for target in (-9, 3, 9)]
        [None, None, None]
        >>> RadixBinarySearch([], bits=0).search(1) is None
        True
        >>> RadixBinarySearch([5, 5, 5], bits=0).search(5)
        0
        >>> RadixBinarySearch([-4, 0, 0, 9], bits=0).search(0)
        1
        >>> RadixBinarySearch([0, 100], bits=4).search(50) is None
        True
        >>> RadixBinarySearch([-10**100, 0, 10**100]).search(10**100)
        2
        >>> values = [1, 2, 3]
        >>> index = RadixBinarySearch(values)
        >>> values[0] = 99
        >>> index.search(1)
        0
        >>> index.search(True)
        Traceback (most recent call last):
            ...
        TypeError: target must be an integer, excluding bool
        """
        if isinstance(target, bool) or not isinstance(target, int):
            raise TypeError("target must be an integer, excluding bool")
        # Check the range before calculating a bucket: a smaller target could
        # produce a negative Python index, and a larger one could exceed the table.
        if not self._values or target < self._minimum or target > self._values[-1]:
            return None

        bucket = (target - self._minimum) >> self._shift
        left = self._offsets[bucket]
        stop = self._offsets[bucket + 1]
        # Search the half-open interval [left, right), without copying a slice.
        # Preserve stop because right shrinks during the lower-bound search.
        right = stop

        # Discard values strictly below target. On equality, retain the left half
        # so an earlier duplicate can still be found. The result is the first
        # index in this bucket whose value is >= target, or stop if none exists.
        while left < right:
            middle = (left + right) // 2
            if self._values[middle] < target:
                left = middle + 1
            else:
                right = middle

        # A lower bound can point at a larger value or at the end of the bucket.
        # Verify equality; the bounds check also handles empty buckets safely.
        if left < stop and self._values[left] == target:
            return left
        return None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
