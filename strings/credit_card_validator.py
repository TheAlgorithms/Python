def validate_initial_digits(credit_card_number: str) -> bool:
    """
    Function to validate initial digits of a given credit card number.
    >>> valid = "4111111111111111 41111111111111 34 35 37 412345 523456 634567"
    >>> all(validate_initial_digits(cc) for cc in valid.split())
    True
    >>> invalid = "32323 36111111111111"
     >>> all(validate_initial_digits(cc) is False for cc in invalid.split())
    True
    """
    first_digit = int(credit_card_number[0])
    if first_digit in (4, 5, 6):
        return True
    elif first_digit == 3:
        second_digit = int(credit_card_number[1])
        return second_digit in (4, 5, 7)

    return False


def luhn_validation(credit_card_number: str) -> bool:
    """
    Function to luhn algorithm validation for a given credit card number.
    >>> luhn_validation('4111111111111111')
    True
    >>> luhn_validation('36111111111111')
    True
    >>> luhn_validation('41111111111111')
    False
    """
    cc_number = credit_card_number
    total = 0
    half_len = len(cc_number) - 2
    for i in range(half_len, -1, -2):
        #  double the value of every second digit
        digit = int(cc_number[i])
        digit *= 2
        # If doubling of a number results in a two digit number
        # i.e greater than 9(e.g., 6 × 2 = 12),
        # then add the digits of the product (e.g., 12: 1 + 2 = 3, 15: 1 + 5 = 6),
        # to get a single digit number.
        if digit > 9:
            digit %= 10
            digit += 1
        cc_number = cc_number[:i] + str(digit) + cc_number[i + 1 :]
        total += digit

    # Sum up the remaining digits
    for i in range(len(cc_number) - 1, -1, -2):
        total += int(cc_number[i])

    return total % 10 == 0


def validate_credit_card_number(number: str) -> bool:
    """
    Function to validate the given credit card number.
    >>> validate_credit_card_number('4111111111111111')
    Given number(4111111111111111) is Valid
    >>> validate_credit_card_number('helloworld$')
    Invalid number(helloworld$) given: Contains alphabets or special characters
    >>> validate_credit_card_number('32323')
    Invalid number(32323) given: Check number length
    >>> validate_credit_card_number('32323323233232332323')
    Invalid number(32323323233232332323) given: Check number length
    >>> validate_credit_card_number('36111111111111')
    Invalid number(36111111111111) given: Check starting number
    >>> validate_credit_card_number('41111111111111')
    Invalid number(41111111111111) given: Invalid Number
    """
    error_message = f"Invalid number({number}) given: "
    credit_card_number = str(number)
    if not credit_card_number.isdigit():
        print(error_message + "Contains alphabets or special characters")
        return False

    credit_card_number_length = len(credit_card_number)
    if credit_card_number_length < 13 and credit_card_number_length > 16:
        print(error_message + "Check number length")
        return False

    if not validate_initial_digits(credit_card_number):
        print(error_message + "Check starting number")
        return False

    if not luhn_validation(credit_card_number):
        print(error_message + "Invalid Number")
        return False
    
    print(f"Given number({number}) is Valid")
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
