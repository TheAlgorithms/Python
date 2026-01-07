def is_palindrome(number: int) -> bool:
    """
    Determines if an integer is a palindrome without string conversion.

    Logic:
    1. Filter out negative numbers and multiples of 10.
    2. Reverse the second half of the number.
    3. Compare the two halves.
    """
    if number < 0 or (number % 10 == 0 and number != 0):
        return False

    reversed_half = 0
    while number > reversed_half:
        reversed_half = (reversed_half * 10) + (number % 10)
        number //= 10

    return number == reversed_half or number == reversed_half // 10
