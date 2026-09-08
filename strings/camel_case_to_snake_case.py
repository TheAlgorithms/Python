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
        msg = f"Expected string as input, found {type(input_str)}"
        raise ValueError(msg)

    snake_str = ""

    for index, char in enumerate(input_str):
        if char.isupper():
            snake_str += "_" + char.lower()

        # if char is lowercase but proceeded by a digit:
        elif input_str[index - 1].isdigit() and char.islower():
            snake_str += "_" + char

        # if char is a digit proceeded by a letter:
        elif input_str[index - 1].isalpha() and char.isnumeric():
            snake_str += "_" + char.lower()

        # if char is not alphanumeric:
        elif not char.isalnum():
            snake_str += "_"

        else:
            snake_str += char

    # remove leading underscore
    if snake_str[0] == "_":
        snake_str = snake_str[1:]

    return snake_str


if __name__ == "__main__":
    from doctest import testmod

    testmod()
