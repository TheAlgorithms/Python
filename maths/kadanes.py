"""
Kadane's algorithm to get maximum subarray sum
https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d
https://en.wikipedia.org/wiki/Maximum_subarray_problem
"""
test_data: tuple = ([-2, -8, -9], [2, 8, 9], [-1, 0, 1], [0, 0], [])


def negative_exist(arr: list) -> int:
    """
    >>> negative_exist([-2,-8,-9])
    -2
    >>> [negative_exist(arr) for arr in test_data]
    [-2, 0, 0, 0, 0]
    """
    arr = arr or [0]
    max = arr[0]
    for i in arr:
        if i >= 0:
            return 0
        elif max <= i:
            max = i
    return max


def kadanes(arr: list) -> int:
    """
    If negative_exist() returns 0 than this function will execute
    else it will return the value return by negative_exist function

    For example: arr = [2, 3, -9, 8, -2]
        Initially we set value of max_sum to 0 and max_till_element to 0 than when
        max_sum is less than max_till particular element it will assign that value to
        max_sum and when value of max_till_sum is less than 0 it will assign 0 to i
        and after that whole process, return the max_sum
    So the output for above arr is 8

    >>> kadanes([2, 3, -9, 8, -2])
    8
    >>> [kadanes(arr) for arr in test_data]
    [-2, 19, 1, 0, 0]
    """
    max_sum = negative_exist(arr)
    if max_sum < 0:
        return max_sum

    max_sum = 0
    max_till_element = 0

    for i in arr:
        max_till_element += i
        if max_sum <= max_till_element:
            max_sum = max_till_element
        if max_till_element < 0:
            max_till_element = 0
    return max_sum


if __name__ == "__main__":
    try:
        print("Enter integer values sepatated by spaces")
        arr = [int(x) for x in input().split()]
        print(f"Maximum subarray sum of {arr} is {kadanes(arr)}")
    except ValueError:
        print("Please enter integer values.")
