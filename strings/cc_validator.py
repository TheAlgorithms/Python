def validate_initial_digits(credit_card_number: str) -> bool:
    first_digit = int(credit_card_number[0])
    if first_digit == 4 or first_digit == 5 or first_digit == 6:
        return True
    elif first_digit == 3:
        second_digit = int(credit_card_number[1])
        if second_digit == 7 or second_digit == 4 or second_digit == 5:
            return True
        else:
            return False
    return False


def luhn_validation(credit_card_number: str) -> bool:
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

    if total % 10 == 0:
        return True

    return False


def validate_credit_card_number(number: str) -> None:
    """
    Function to validate the given credit card number
    """
    credit_card_number = str(number)
    if credit_card_number.isdigit():
        credit_card_number_length = len(credit_card_number)
        if credit_card_number_length >= 13 and credit_card_number_length <= 16:
            if validate_initial_digits(credit_card_number):
                if luhn_validation(credit_card_number):
                    print(f"Given number({number}) is Valid")
                else:
                    print(f"Invalid number({number}) given: Invalid Number")
            else:
                print(f"Invalid number({number}) given: Check starting number")
        else:
            print(f"Invalid number({number}) given: Check number length")
    else:
        print(
            f"Invalid number({number}) given: Contains alphabets or special characters"
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
