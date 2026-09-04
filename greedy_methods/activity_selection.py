"""
The Activity Selection Problem is a classic problem in which a set of activities,
each with a start and end time, needs to be scheduled in such a way that
the maximum number of non-overlapping activities is selected.
This is a greedy algorithm where at each step,
we choose the activity that finishes the earliest
and does not conflict with previously selected activities.

Wikipedia: https://en.wikipedia.org/wiki/Activity_selection_problem
"""


def activity_selection(activities: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Solve the Activity Selection Problem using a greedy algorithm by selecting
    the maximum number of non-overlapping activities from a list of activities.

    Parameters:
    activities: A list of tuples where each tuple contains
                                        the start and end times of an activity.

    Returns:
    A list of selected activities that are non-overlapping.

    Example:
    >>> activity_selection([(1, 3), (2, 5), (3, 9), (6, 8)])
    [(1, 3), (6, 8)]

    >>> activity_selection([(0, 6), (1, 4), (3, 5), (5, 7), (5, 9), (8, 9)])
    [(1, 4), (5, 7), (8, 9)]

    >>> activity_selection([(1, 2), (2, 4), (3, 5), (0, 6)])
    [(1, 2), (2, 4)]

    >>> activity_selection([(5, 9), (1, 2), (3, 4), (0, 6)])
    [(1, 2), (3, 4), (5, 9)]
    """

    # Step 1: Sort the activities by their end time
    sorted_activities = sorted(activities, key=lambda activity: activity[1])

    # Step 2: Select the first activity (the one that finishes the earliest)
    # as the initial activity
    selected_activities = [sorted_activities[0]]

    # Step 3: Iterate through the sorted activities and select the ones
    # that do not overlap with the last selected activity
    for i in range(1, len(sorted_activities)):
        if sorted_activities[i][0] >= selected_activities[-1][1]:
            selected_activities.append(sorted_activities[i])

    return selected_activities
