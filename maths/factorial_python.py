import math
def factorial(input_number: int) -> int:
    """
        Non-recursive algorithm of finding factorial of the
        input number.
        >>> factorial(1)
        1
        >>> factorial(6)
        720
        >>> factorial(0)
        1
        >>> factorial(23)
        25852016738884976640000
    """

    if input_number < 0:
        raise ValueError("Input input_number should be non-negative")
        
    return math.factorial(input_number)

