def median(nums):
    """
    Find median of a list of numbers.

    >>> median([0])
    0
    >>> median([4,1,3,2])
    2.5

    Args:
        nums: List of nums

    Returns:
        Median.
    """
    sorted_list = sorted(nums)
    med = None
    if len(sorted_list) % 2 == 0:
        mid_index_1 = len(sorted_list) // 2
        mid_index_2 = (len(sorted_list) // 2) - 1
        med = (sorted_list[mid_index_1] + sorted_list[mid_index_2]) / float(2)
    else:
        mid_index = (len(sorted_list) - 1) // 2
        med = sorted_list[mid_index]
    return med


def main():
    print("Odd number of numbers:")
    print(median([2, 4, 6, 8, 20, 50, 70]))
    print("Even number of numbers:")
    print(median([2, 4, 6, 8, 20, 50]))


if __name__ == "__main__":
    main()
