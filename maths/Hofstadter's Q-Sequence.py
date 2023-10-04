from sys import setrecursionlimit

# Set the recursion limit to avoid reaching the maximum recursion depth
setrecursionlimit(10000)

def hofstadter(n):
    """
    Recursive function to calculate Hofstadter H(n) using the given recurrence relation.

    Args:
        n (int): The positive integer for which to calculate Hofstadter H(n).

    Returns:
        int: The result of Hofstadter H(n) calculation.

    Raises:
        RecursionError: If the recursion limit is reached.

    Note:
        The recurrence relation is: H(n) = H(n - H(n - 1)) + H(n - H(n - 2))
    """
    if n <= 1 or n == 2:
        return 1
    elif n in result:
        return result[n]
    else:
        # Calculate H(n) recursively and store the result in the result dictionary
        res = hofstadter(n - hofstadter(n - 1)) + hofstadter(n - hofstadter(n - 2))
        result[n] = res
        return res

result = {}  # Dictionary to store previously calculated results
value = int(input("Enter the positive integer value:"))
print(hofstadter(value))
