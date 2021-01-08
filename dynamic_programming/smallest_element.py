# You have given some element with its weight in an array, you task is to find the
# minimum possible weight element and print the weight.
# You can combine two elements and the resultant element will be the abs
# difference of the weight of these two elements.


def min_element(arr: int) -> int:
    """Return the minimum element possible, an exact integer >= 0.

    >>> elements = [1, 1, 2, 6, 24, 120]
    >>> min_element(elements)
    0

    >>> elements = [30, 24, 10, 3, 1]
    >>> min_element(elements)
    0

    >>> elements = [11, 1, 20]
    >>> min_element(elements)
    1
    """

    global minimum_value, count

    if len(arr) == 1:
        return minimum_value

    if minimum_value == 0:
        return minimum_value

    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            count = count + 1
            temp = arr.copy()
            temp.pop(j)
            temp.pop(i)
            temp.append(abs(arr[i] - arr[j]))

            if minimum_value > abs(arr[i] - arr[j]):
                minimum_value = abs(arr[i] - arr[j])

                if minimum_value == 0:
                    return minimum_value

            min_element(temp)

    return minimum_value


if __name__ == "__main__":
    minimum_value = 0
    count = 0
    elements = [11, 1, 20]
    minimum_value = elements[0]
    min_element_value = min_element(elements)
    elements.append(min_element_value)

    answer = min(elements)
    print(answer)
