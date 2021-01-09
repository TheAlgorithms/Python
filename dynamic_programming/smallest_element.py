# You have given some element with its weight in an array, you task is to find the
# minimum possible weight element and print the weight.
# You can combine two elements and the resultant element will be the abs
# difference of the weight of these two elements.


def min_element(arr: [int], minimum: int, count: int) -> int:
    """
    >>> min_element([1, 1, 2, 6, 24, 120], 1, 0)
    0
    >>> min_element([10, 1, 20], 10, 0)
    1
    """

    if len(arr) == 1:
        return arr[0]

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

    arr.append(minimum)
    answer = min(arr)
    return answer


if __name__ == "__main__":

    import doctest

    doctest.testmod()
