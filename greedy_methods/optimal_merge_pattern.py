"""
This is a pure Python implementation of the greedy-merge-sort algorithm
reference: https://www.geeksforgeeks.org/optimal-file-merge-patterns/

For doctests run following command:
python3 -m doctest -v greedy_merge_sort.py

Objective
Merge a set of sorted files of different length into a single sorted file.
We need to find an optimal solution, where the resultant file
will be generated in minimum time.

Approach
If the number of sorted files are given, there are many ways
to merge them into a single sorted file.
This merge can be performed pair wise.
To merge a m-record file and a n-record file requires possibly m+n record moves
the optimal choice being,
merge the two smallest files together at each step (greedy approach).
"""


def optimal_merge_pattern(files: list) -> float:
    """Function to merge all the files with optimum cost

    Args:
        files [list]: A list of sizes of different files to be merged

    Returns:
        optimal_merge_cost [int]: Optimal cost to merge all those files

    Examples:
    >>> optimal_merge_pattern([2, 3, 4])
    14
    >>> optimal_merge_pattern([5, 10, 20, 30, 30])
    205
    >>> optimal_merge_pattern([8, 8, 8, 8, 8])
    96
    """
    optimal_merge_cost = 0
    while len(files) > 1:
        temp = 0
        # Consider two files with minimum cost to be merged
        for _ in range(2):
            min_index = files.index(min(files))
            temp += files[min_index]
            files.pop(min_index)
        files.append(temp)
        optimal_merge_cost += temp
    return optimal_merge_cost


if __name__ == "__main__":
    import doctest

    doctest.testmod()
