from __future__ import annotations


def median(nums: list) -> int | float:
    """
    Find median of a list of numbers.
    Wiki: https://en.wikipedia.org/wiki/Median

    >>> median([0])
    0
    >>> median([4, 1, 3, 2])
    2.5
    >>> median([2, 70, 6, 50, 20, 8, 4])
    8

    Args:
        nums: List of nums

    Returns:
        Median.
    """
    # The sorted function returns list[SupportsRichComparisonT@sorted]
    # which does not support `+`
    sorted_list: list[int] = sorted(nums)
    length = len(sorted_list)
    mid_index = length >> 1
    return (
        (sorted_list[mid_index] + sorted_list[mid_index - 1]) / 2
        if length % 2 == 0
        else sorted_list[mid_index]
    )


def main():
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    main()
