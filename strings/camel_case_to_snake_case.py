def camel_to_snake_case(input_str: str) -> str:
    """
    Transforms a camelCase (or PascalCase) string to snake_case

    >>> camel_to_snake_case("someRandomString")
    'some_random_string'

    >>> camel_to_snake_case("SomeRandomString")
    'some_random_string'

    >>> camel_to_snake_case("123someRandom123String123")
    '123_some_random_123_string_123'

    >>> camel_to_snake_case("123SomeRandom123String123")
    '123_some_random_123_string_123'

    >>> camel_to_snake_case(123)
    Traceback (most recent call last):
        ...
    ValueError: Expected string as input, found <class 'int'>

    """

    import re

    # check for invalid input type
    if not isinstance(input_str, str):
        msg = f"Expected string as input, found {type(input_str)}"
        raise ValueError(msg)

    # Replace all characters that are not letters or numbers with the underscore
    snake_str = re.sub(r"[^a-zA-Z0-9]", "_", input_str)

    # Find where lowercase meets uppercase. Insert underscore between them
    snake_str = re.sub(r"([a-z])([A-Z])", r"\1_\2", snake_str).lower()

    # Find the sequence of digits at the beginning
    snake_str = re.sub(r"^(\d+)", r"\1_", snake_str)

    # Find the sequence of digits at the end
    snake_str = re.sub(r"(\d+)$", r"_\1", snake_str)

    # Find where letter meets digits
    snake_str = re.sub(r"([a-z])(\d+)", r"\1_\2", snake_str)

    # Find where digits meet letter
    snake_str = re.sub(r"(\d+)([a-z])", r"\1_\2", snake_str)

    return snake_str


if __name__ == "__main__":
    from doctest import testmod

    testmod()
