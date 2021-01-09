# You have given some element with its weight in an array, you task is to find the
# minimum possible weight element and print the weight.
# You can combine two elements and the resultant element will be the abs
# difference of the weight of these two elements.


def min_element(arr: [int], minimum: int, count: int) -> int:

    if len(arr) == 1:
        return minimum

    if minimum == 0:
        return minimum

    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            count = count + 1
            temp = arr.copy()
            temp.pop(j)
            temp.pop(i)
            temp.append(abs(arr[i] - arr[j]))

            if minimum > abs(arr[i] - arr[j]):
                minimum = abs(arr[i] - arr[j])

                if minimum == 0:
                    return minimum

            min_element(temp, minimum, count)

    return minimum


def run_min_element(arr: [int]) -> int:
    """
    >>> run_min_element([1, 1, 2, 6, 24, 120])
    0
    >>> run_min_element([10, 1, 20])
    1
    """

    min_element_value = min_element(arr, arr[0], 0)
    arr.append(min_element_value)

    answer = min(arr)
    return answer


if __name__ == "__main__":

    import doctest

    doctest.testmod()
