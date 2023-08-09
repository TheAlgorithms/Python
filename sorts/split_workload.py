def split_list(
    timings: list[int | float | str],
) -> tuple[list[int | float], list[int | float], int | float]:
    """

    This algorithm is a brute-force search over (nearly) all 2^n
    possible partitions and was created for educational purposes.
    the asymptotic runtime of this code is: O(n * 2^n)

    this is a case of the partition problem.
    it accepts a multiset ( list ) of integers,
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
    Traceback (most recent call last):
    ValueError: Timings must be a list of numbers

    """

    for i, current_element in enumerate(timings):
        if (
            isinstance(current_element, str)
            and current_element.replace(".", "", 1).isdigit()
        ):
            is_current_elem_int = float(current_element).is_integer()
            if not is_current_elem_int:
                timings[i] = abs(float(current_element))
            else:
                timings[i] = abs(int(float(current_element)))
        elif isinstance(current_element, (int, float)):
            timings[i] = abs(current_element)
        else:
            raise ValueError("Timings must be a list of numbers")

    if len(timings) == 0:
        return ([], [], 0)
    elif len(timings) == 1:
        return ([timings[0]], [], timings[0])

    result = None
    n = len(timings)
    smallest_diff = float("inf")
    for i in range(1, 2**n - 1):
        indices = [j for j in range(n) if i & (1 << j) != 0]
        distributed_timings_1 = [timings[j] for j in indices]
        distributed_timings_2 = [timings[j] for j in range(n) if j not in indices]
        diff = abs(sum(distributed_timings_1) - sum(distributed_timings_2))
        if diff < smallest_diff:
            smallest_diff = diff
            result = (
                distributed_timings_1,
                distributed_timings_2,
                smallest_diff,
            )
    return result


if __name__ == "__main__":
    __import__("doctest").testmod()
