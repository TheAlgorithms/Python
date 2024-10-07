"""
interval scheduling is a class of problems. The programs take a number of tasks into account. Every task is represented by an interval that indicates the amount of time it should take a machine to complete it. If there is no overlap between any two intervals on the system or resource, a subset of intervals is compatible.

The goal of the interval scheduling maximization problem is to identify the largest compatible set or a collection of intervals with the least possible overlap. The idea is to optimize throughput by completing as many tasks as you can.

"""


def interval_scheduling(stimes, ftimes):
    index = list(range(len(stimes)))
    # sort according to finish times
    index.sort(key=lambda item: ftimes[item])

    maximal_set = set()
    prev_finish_time = 0
    for item in index:
        if stimes[item] >= prev_finish_time:
            maximal_set.add(item)
            prev_finish_time = ftimes[item]

    return maximal_set


n = int(input("Enter number of activities: "))
stimes = input("Enter the start time of the {} activities in order: .{n}").split()
stimes = [int(st) for st in stimes]
ftimes = input("Enter the finish times of the {} activities in order:.{n}").split()
ftimes = [int(ft) for ft in ftimes]

ans = interval_scheduling(stimes, ftimes)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
