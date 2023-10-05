import re


def camel_to_snake_case(input_str: str) -> str:
    """
    Transforms a camelCase or PascalCase given string to snake_case

    >>> camel_to_snake_case("someRandomString")
    'some_random_string'

    >>> camel_to_snake_case("SomeRandomString")
    'some_random_string'

    >>> camel_to_snake_case("someRandomStringWithNumbers123")
    'some_random_string_with_numbers_123'

    >>> camel_to_snake_case("SomeRandomStringWithNumbers123")
    'some_random_string_with_numbers_123'

    >>> camel_to_snake_case(123)
    Traceback (most recent call last):
        ...
    ValueError: Expected string as input, found <class 'int'>
    """

    if not isinstance(input_str, str):
        msg = f"Expected string as input, found {type(input_str)}"
        raise ValueError(msg)

    # Use regular expression to split words on capital letters and numbers
    words = re.findall(r"[A-Z][a-z]*|\d+|[a-z]+", input_str)

    # Join the words with underscores and convert to lowercase
    return "_".join(words).lower()


if __name__ == "__main__":
    from doctest import testmod

    testmod()
