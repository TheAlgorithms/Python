# Performing division operation without the use of arithmetic operator
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Division by zero")
    if dividend == 0:
        return 0

    negative = (dividend < 0) ^ (divisor < 0)

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1

    if negative:
        quotient = -quotient

    # Ensure the result is within the 32-bit signed integer range
    max_int = 2**31 - 1
    min_int = -2**31
    return max(min(quotient, max_int), min_int)

# Test cases
print(divide(10, 3))  # Output should be 3
print(divide(7, -3))  # Output should be -2
print(divide(0, 1))   # Output should be 0
print(divide(1, 0))   # This will raise a ZeroDivisionError
