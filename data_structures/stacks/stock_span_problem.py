"""
The stock span problem is a financial problem where we have a series of n daily
price quotes for a stock and we need to calculate span of stock's price for all n days.

The span span_values[i] of the stock's price on a given day i is defined as the maximum
number of consecutive days just before the given day, for which the price of the stock
on the current day is less than or equal to its price on the given day.
"""


def calculate_span(prices: list[int]) -> list[int]:
    """
    function to calculate the span values
    and store them in the array (2nd parameter)
    >>> calculate_span([10, 4, 5, 90, 120, 80])
    [1, 1, 2, 4, 5, 1, 0]
    >>> calculate_span([])
    []
    >>> calculate_span([0,0,0,0])
    [1, 2, 3, 4, 0]
    >>> calculate_span([0,-1,-2,0])
    [1, 1, 2, 4, 0]
    """
    n = len(prices)
    if n == 0:
        return []
    span_values = [0 for _ in range(n + 1)]
    # Create a stack and push index of fist element to it
    stack = []
    stack.append(0)

    # Span value of first element is always 1
    span_values[0] = 1

    # Calculate span values for rest of the elements
    for i in range(1, n):
        # Pop elements from stack while stack is not
        # empty and top of stack is smaller than prices[i]
        while len(stack) > 0 and prices[stack[0]] <= prices[i]:
            stack.pop()

        # If stack becomes empty, then prices[i] is greater
        # than all elements on left of it, i.e. prices[0],
        # prices[1], ..prices[i-1]. Else the prices[i]  is
        # greater than elements after top of stack
        if len(stack) == 0:
            span_values[i] = i + 1
        else:
            span_values[i] = i - stack[0]

        # Push this element to stack
        stack.append(i)
    return span_values


# A utility function to print elements of array
def print_array(array: list[int], length: int) -> None:
    for i in range(length):
        print(array[i], end=" ")
    print()


# Driver program to test above function
if __name__ == "__main__":
    from doctest import testmod

    testmod()

    prices = [10, 4, 5, 90, 120, 80]

    # Fill the span values in array span_values[]
    span_values = calculate_span(prices)

    # Print the calculated span values
    print_array(span_values, len(prices))
