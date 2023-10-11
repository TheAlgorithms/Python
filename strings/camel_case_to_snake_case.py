def camel_to_snake_case(input_str: str) -> str:
    """
    Transforms a camelCase (or PascalCase) string to snake_case

    >>> camel_to_snake_case("someRandomString")
    'some_random_string'

    >>> camel_to_snake_case("SomeRandomStr#ng")
    'some_random_str_ng'

    >>> camel_to_snake_case("123someRandom123String123")
    '123_some_random_123_string_123'

    >>> camel_to_snake_case("123SomeRandom123String123")
    '123_some_random_123_string_123'

    >>> camel_to_snake_case(123)
    Traceback (most recent call last):
        ...
    ValueError: Expected string as input, found <class 'int'>

    """

    # check for invalid input type
    if not isinstance(input_str, str):
        raise ValueError(f"Expected string as input, found {type(input_str)}")

    snake_str = ""
    prev_char = ''

    for char in input_str:
        if char.isupper() and not prev_char.isdigit():
            snake_str += f"_{char.lower()}"
        elif char.islower() and prev_char.isdigit():
            snake_str += f"_{char}"
        elif char.isnumeric() and prev_char.isalpha():
            snake_str += f"_{char.lower()}"
        elif not char.isalnum():
            snake_str += "_"
        else:
            snake_str += char

        prev_char = char

    # remove leading underscore
    return snake_str.lstrip('_')


if __name__ == "__main__":
    from doctest import testmod

    testmod()
