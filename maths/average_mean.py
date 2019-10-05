"""Find mean of a list of numbers."""


def average(nums):
    """Find mean of a list of numbers."""
    sum = 0
    for x in nums:
        sum += x
    avg = sum / len(nums)
    print(avg)
    return avg


def main():
    """Call average module to find mean of a specific list of numbers."""
    average([2, 4, 6, 8, 20, 50, 70])


if __name__ == "__main__":
    main()
