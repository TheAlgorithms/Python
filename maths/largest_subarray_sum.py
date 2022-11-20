from sys import maxsize


def max_sub_array_sum(a: list, size: int = 0):
    """
    >>> max_sub_array_sum([-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7])
    -3
    """
    size = size or len(a)
    max_so_far = -maxsize - 1
    max_ending_here = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        max_so_far = max(max_so_far, max_ending_here)
        max_ending_here = max(max_ending_here, 0)
    return max_so_far


if __name__ == "__main__":
    a = [-13, -3, -25, -20, 1, -16, -23, -12, -5, -22, -15, -4, -7]
    print(("Maximum contiguous sum is", max_sub_array_sum(a, len(a))))
