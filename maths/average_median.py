"""
Find median of a list of numbers.

Read more about medians:
    https://en.wikipedia.org/wiki/Median
"""


def median(nums):
    """Find median of a list of numbers."""
    # Sort list
    sorted_list = sorted(nums)
    print("List of numbers:")
    print(sorted_list)

    # Is number of items in list even?
    if len(sorted_list) % 2 == 0:
        # Find index for first middle value.
        mid_index_1 = len(sorted_list) / 2
        # Find index for second middle value.
        mid_index_2 = -(len(sorted_list) / 2) - 1
        # Divide middle values by 2 to get average (mean).
        med = (sorted_list[mid_index_1] + sorted_list[mid_index_2]) / float(2)
        return med  # Return makes `else:` unnecessary.
    # Number of items is odd.
    mid_index = (len(sorted_list) - 1) / 2
    # Middle index is median.
    med = sorted_list[mid_index]
    return med


def main():
    """Call average module to find median of a specific list of numbers."""
    print("Odd number of numbers:")
    print(median([2, 4, 6, 8, 20, 50, 70]))
    print("Even number of numbers:")
    print(median([2, 4, 6, 8, 20, 50]))


if __name__ == '__main__':
    main()
