"""
The stock span problem is a financial problem where we have a series of n daily
price quotes for a stock and we need to calculate span of stock's price for all n days.

The span Si of the stock's price on a given day i is defined as the maximum
number of consecutive days just before the given day, for which the price of the stock
on the current day is less than or equal to its price on the given day.
"""


def calculate_span(price: list[int]) -> list[int]:
    """
    Calculate the span values for a given list of stock prices.
    Args:
        price: List of stock prices.
    Returns:
        List of span values.

    >>> calculate_span([10, 4, 5, 90, 120, 80])
    [1, 1, 2, 4, 5, 1]
    >>> calculate_span([100, 50, 60, 70, 80, 90])
    [1, 1, 2, 3, 4, 5]
    >>> calculate_span([5, 4, 3, 2, 1])
    [1, 1, 1, 1, 1]
    >>> calculate_span([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> calculate_span([10, 20, 30, 40, 50])
    [1, 2, 3, 4, 5]
    >>> calculate_span([100, 80, 60, 70, 60, 75, 85])
    [1, 1, 1, 2, 1, 4, 6]
    """
    n = len(price)
    s = [0] * n
    # Create a stack and push index of fist element to it
    st = []
    st.append(0)

    # Span value of first element is always 1
    s[0] = 1

    # Calculate span values for rest of the elements
    for i in range(1, n):
        # Pop elements from stack while stack is not
        # empty and top of stack is smaller than price[i]
        while len(st) > 0 and price[st[-1]] <= price[i]:
            st.pop()

        # If stack becomes empty, then price[i] is greater
        # than all elements on left of it, i.e. price[0],
        # price[1], ..price[i-1]. Else the price[i]  is
        # greater than elements after top of stack
        s[i] = i + 1 if len(st) <= 0 else (i - st[-1])

        # Push this element to stack
        st.append(i)

    return s


# A utility function to print elements of array
def print_array(arr, n):
    for i in range(n):
        print(arr[i], end=" ")


# Driver program to test above function
price = [10, 4, 5, 90, 120, 80]

# Calculate the span values
S = calculate_span(price)

# Print the calculated span values
print_array(S, len(price))
