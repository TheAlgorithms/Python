from functools import partial
import operator


def strand_sort(arr: list, solution: list, _operator: callable):
    """
    Strand sort implementation
    source: https://en.wikipedia.org/wiki/Strand_sort

    :param arr: Unordered input list
    :param solution: Ordered output list
    :param _operator: Operator lt/gt to specify ascent/descent version

    Examples:
    >>> solution_1 = []
    >>> strand_sort([4, 2, 5, 3, 0, 1], solution_1, operator.gt)
    >>> solution_1
    [0, 1, 2, 3, 4, 5]

    >>> solution_2 = []
    >>> strand_sort([4, 2, 5, 3, 0, 1], solution_2, operator.lt)
    >>> solution_2
    [5, 4, 3, 2, 1, 0]
    """
    if not arr:
        return

    sublist = [arr.pop(0)]
    for i, item in enumerate(arr):
        if _operator(item, sublist[-1]):
            sublist.append(item)
            arr.pop(i)

    #  merging sublist into solution list
    if not solution:
        solution.extend(sublist)
    else:
        while sublist:
            item = sublist.pop(0)
            for i, xx in enumerate(solution):
                if not _operator(item, xx):
                    solution.insert(i, item)
                    break
            else:
                solution.append(item)

    strand_sort(arr, solution, _operator)


strand_asc = partial(strand_sort, _operator=operator.gt)
strand_desc = partial(strand_sort, _operator=operator.lt)

if __name__ == "__main__":
    solution = []
    strand_asc([4, 3, 5, 1, 2], solution)
    assert solution == [1, 2, 3, 4, 5]

    solution = []
    strand_desc([4, 3, 5, 1, 2], solution)
    assert solution == [5, 4, 3, 2, 1]
