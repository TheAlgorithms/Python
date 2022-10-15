"""
    Problem Statement : https://www.spoj.com/problems/HISTOGRA/
"""


histogram = [3, 5, 11, 7, 5, 9]
max_area = 25

histogram2 = [3, 5, 1, 7, 5, 9]
max_area2 = 15


def max_rectangle_area_histogram(histogram):

    """

    the area of largest rectangle inside the histogram is :
    >>> max_rectangle_area_histogram(histogram) == max_area
    True
    >>> max_rectangle_area_histogram(histogram2) == max_area2
    True

    """

    stack = []

    max_area = 0
    index = 0
    while index < len(histogram):

        if (not stack) or (histogram[stack[-1]] <= histogram[index]):
            stack.append(index)
            index += 1

        else:

            top_of_stack = stack.pop()

            area = histogram[top_of_stack] * (
                (index - stack[-1] - 1) if stack else index
            )

            max_area = max(max_area, area)

    while stack:

        top_of_stack = stack.pop()

        area = histogram[top_of_stack] * ((index - stack[-1] - 1) if stack else index)

        max_area = max(max_area, area)

    return max_area


if __name__ == "__main__":

    from doctest import testmod

    testmod()

    print("Histogram", histogram)
    print(
        "Maximum area of the rectangle inside the histogram : ",
        max_rectangle_area_histogram(histogram),
    )
