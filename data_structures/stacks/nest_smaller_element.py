"""
Description About this Code :
Next Smaller Element for an array element is the first element to the right of
that element which has a value strictly smaller than that element
if no such value exists print -1

"""

elements = [34, 2, 5, 2, 3, 23, 18, 23, 45]
expect = [2, -1, 2, -1, -1, -1, -1, -1, -1]


def next_smaller_element(elements):
    """
    Get the Next Smaller Element (NSE) for all elements in a list.

    >>> next_smaller_element(elements) == expect
    True

    """

    stack = []
    map = {}
    size = len(elements)

    stack.append(elements[0])

    for i in range(1, size):
        if len(stack) == 0:
            stack.append(elements[i])
            continue

        while len(stack) != 0 and stack[-1] > elements[i]:
            map[stack[-1]] = elements[i]
            stack.pop()

        stack.append(elements[i])

    while len(stack) != 0:
        map[stack[-1]] = -1
        stack.pop()

    answer = []
    for i in range(size):
        answer.append(map[elements[i]])

    return answer


if __name__ == "__main__":

    from doctest import testmod

    testmod()

    print(elements)
    print(next_smaller_element(elements))
