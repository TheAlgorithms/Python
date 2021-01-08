# You have given some element with its weight in an array, you task is to find the
# minimum possible weight element and print the weight.
# You can combine two elements and the resultant element will be the abs
# difference of the weight of these two elements.


def min_element(arr) -> int:
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


    global min, count

    if len(arr) == 1:
        return min

    if min == 0:
        return min

    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            count = count + 1
            temp = arr.copy()
            temp.pop(j)
            temp.pop(i)
            temp.append(abs(arr[i] - arr[j]))

            if min > abs(arr[i] - arr[j]):
                min = abs(arr[i] - arr[j])

                if min == 0:
                    return min

            min_element(temp)

    return min


if __name__ == "__main__":
    min = 0
    count = 0
    elements = [100, 90, 19, 88, 95]
    min = elements[0] + 1
    answer = min_element(elements)
    print(answer)
