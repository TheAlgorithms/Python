# You have given some element with its weight in an array, you task is to find the
# minimum possible weight element and print the weight.
# You can combine two elements and the resultant element will be the abs
# difference of the weight of these two elements.


def min_element(arr: [int], minimum_value: int, count: int) -> int:
    """
    >>> run_min_element([1, 1, 2, 6, 24, 120])
    0
    >>> run_min_element([30, 24, 10, 3, 1])
    0
    >>> run_min_element([11, 1, 20])
    1
    """

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

            min_element(temp, minimum_value, count)

    return minimum_value

def run_min_element(arr: [int]) -> None:
    count = 0
    minimum_value = arr[0]
    min_element_value = min_element(arr, minimum_value, count)
    elements.append(min_element_value)

    answer = min(elements)
    print(answer)

if __name__ == "__main__":
    elements = [1, 10, 2, 6, 24, 120]
    run_min_element(elements)
