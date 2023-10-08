import re


def is_us_phone_number(phone: str) -> bool:
    """
    Determine whether the string is a valid US phone number or not.
    Valid formats: (123) 456-7890, 123-456-7890, 123.456.7890, 1234567890, +31636363634

    >>> is_us_phone_number("(123) 456-7890")
    True
    >>> is_us_phone_number("123-456-7890")
    True
    >>> is_us_phone_number("123.456.7890")
    True
    >>> is_us_phone_number("1234567890")
    True
    >>> is_us_phone_number("+31636363634")
    True
    >>> is_us_phone_number("555-5555")
    False
    >>> is_us_phone_number("1234-567-890")
    False
    >>> is_us_phone_number("1-800-555-5555")
    True
    """

    # Define a regular expression pattern for US phone numbers
    pattern = re.compile(r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$|\+\d{11}$")

    return bool(re.search(pattern, phone))


if __name__ == "__main__":
    phone = "+1 (123) 456-7890"

    print(is_us_phone_number(phone))
