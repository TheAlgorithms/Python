def camel_to_snake(camel_str: str) -> str:
    import re

    """
    >>> camel_to_snake('someRandomStringWithNumbers123')
    'some_random_string_with_numbers_1_2_3'
    >>> camel_to_snake('someRandomString')
    'some_random_string'
    >>> camel_to_snake(123)
    Traceback (most recent call last):
        ...
    ValueError: Expected string as input, found <class 'int'>

    """

    # Raises an error if the input is not a string
    if not isinstance(camel_str, str):
        msg = f"Expected string as input, found {type(camel_str)}"
        raise ValueError(msg)

    """ Use regular expressions to find all occurrences of capital letters
        followed by lowercase letters or digits. """
    pattern = re.compile(r"(?<=[a-z0-9])([A-Z0-9])")

    # Replace the capital letter or digit with an underscore and the lowercase version.
    snake_str = re.sub(pattern, r"_\1", camel_str)

    # Convert the result to lowercase to get snake_case
    snake_str = snake_str.lower()

    # If the string starts with a capital letter, add an underscore at the beginning.
    if camel_str[0].isupper():
        snake_str = "_" + snake_str

    return snake_str


if __name__ == "__main__":
    import doctest

    doctest.testmod()