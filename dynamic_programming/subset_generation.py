from typing import List, Tuple, Union


def combination_util(
    arr: List[int], n: int, r: int, index: int, data: List[int], i: int
) -> Union[Tuple[int, ...], None]:
    """
    Generate all combinations of 'r' elements from a given set of 'n' elements.

    :param arr: List of input elements
    :param n: Number of elements in the input list
    :param r: Size of the combination to be generated
    :param index: Current index in the 'data' list
    :param data: Temporary list to store the current combination
    :param i: Current index in the 'arr' list
    :return: A tuple representing a combination of 'r' elements, or None if no more combinations are possible.
    """
    if index == r:
        return tuple(data)
    if i >= n:
        return None
    data[index] = arr[i]
    res1 = combination_util(arr, n, r, index + 1, data, i + 1)
    res2 = combination_util(arr, n, r, index, data, i + 1)
    if res1 is None:
        return res2
    elif res2 is None:
        return res1
    else:
        return res1, res2


def get_combinations(arr: List[int], n: int, r: int) -> List[Tuple[int, ...]]:
    """
    Generate all combinations of 'r' elements from the given list of elements.

    :param arr: List of input elements
    :param n: Number of elements in the input list
    :param r: Size of the combination to be generated
    :return: A list of tuples representing combinations of 'r' elements.
    """
    data = [0] * r
    return combination_util(arr, n, r, 0, data, 0)


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    print(get_combinations(arr, len(arr), 3))
