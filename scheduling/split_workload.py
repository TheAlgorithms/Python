from math import fabs


def split_list(timings: list) -> tuple:
    """

    this is a case of the partition problem.
    it accepts a multiset ( list ) of positive integers,
    distributes them, and returns a tuple, containing two lists,
    with minimal difference between their sums

    >>> split_list([27, 21, 92, 87, 1, 32])
    ([27, 21, 87], [92, 1, 32], 10)
    >>> split_list([52, 385, 9956, 25, 2367, 1111, 17, 925])
    ([9956], [52, 385, 25, 2367, 1111, 17, 925], 5074)
    >>> split_list([12, 10, 11, 9])
    ([10, 11], [12, 9], 0)
    >>> split_list([-1551, 2712, 2325, 2623])
    ([1551, 2712], [2325, 2623], 685)
    >>> split_list(["12.5", "10", "11", "9"])
    ([10, 11], [12.5, 9], 0.5)
    >>> split_list(["twelve", "ten", "eleven", "nine"])
    ([0], [0, 0, 0], 0)

    """

    result = None

    def split_workload(arr: list) -> tuple:
        if len(arr) == 0:
            return ([], [], 0)
        if len(arr) == 1:
            return ([arr[0]], [], 1)
        else:
            n = len(arr)
            smallest_diff = float("inf")
            if any(c < 0 for c in arr):
                raise ValueError("Numbers can only be non-negative")
            for i in range(1, 2**n - 1):
                indices = [j for j in range(n) if (i & (1 << j)) != 0]
                distributed_timings_1 = [arr[j] for j in indices]
                distributed_timings_2 = [arr[j] for j in range(n) if j not in indices]
                diff = abs(sum(distributed_timings_1) - sum(distributed_timings_2))
                if diff < smallest_diff:
                    smallest_diff = diff
                    result = (
                        distributed_timings_1,
                        distributed_timings_2,
                        smallest_diff,
                    )
            return result

    try:
        result = split_workload(timings)
    except TypeError:
        for val in range(0, len(timings)):
            current_element = timings[val]
            if (
                isinstance(current_element, str)
                and current_element.replace(".", "", 1).isdigit()
            ):
                is_current_elem_int = float(current_element).is_integer()
                if not is_current_elem_int:
                    timings[val] = fabs(float(current_element))
                else:
                    timings[val] = abs(int(float(current_element)))
            else:
                timings[val] = 0
        result = split_workload(timings)

    except ValueError:
        timings = [c * -1 if c < 0 else c for c in timings]
        result = split_workload(timings)

    return result


if __name__ == "__main__":
    __import__("doctest").testmod()
