"""The following implementation assumes that the activities
are already sorted according to their finish time"""

"""Prints a maximum set of activities that can be done by a
single person, one at a time"""
# n --> Total number of activities
# start[]--> An array that contains start time of all activities
# finish[] --> An array that contains finish time of all activities


def print_max_activities(start: list[int], finish: list[int]) -> None:
    """
    >>> start = [1, 3, 0, 5, 8, 5]
    >>> finish = [2, 4, 6, 7, 9, 9]
    >>> print_max_activities(start, finish)
    The following activities are selected:
    0,1,3,4,
    """
    n = len(finish)
    print("The following activities are selected:")

    # The first activity is always selected
    i = 0
    print(i, end=",")

    # Consider rest of the activities
    for j in range(n):
        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if start[j] >= finish[i]:
            print(j, end=",")
            i = j


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]
    print_max_activities(start, finish)
