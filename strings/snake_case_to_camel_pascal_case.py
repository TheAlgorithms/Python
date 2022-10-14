def snake_to_camel_case(input_str: str, use_pascal: bool = False) -> str:
    """
    Transforms a snake_case given string to camelCase (or PascalCase if indicated)
    (defaults to not use Pascal)

    >>> snake_to_camel_case("some_random_string")
    'someRandomString'

    >>> snake_to_camel_case("some_random_string", use_pascal=True)
    'SomeRandomString'

    >>> snake_to_camel_case("some_random_string_with_numbers_123")
    'someRandomStringWithNumbers123'

    >>> snake_to_camel_case("some_random_string_with_numbers_123", use_pascal=True)
    'SomeRandomStringWithNumbers123'

    >>> snake_to_camel_case(123)
    Traceback (most recent call last):
        ...
    ValueError: Expected string as input, found <class 'int'>

    >>> snake_to_camel_case("some_string", use_pascal="True")
    Traceback (most recent call last):
        ...
    ValueError: Expected boolean as use_pascal parameter, found <class 'str'>
    """

    if not isinstance(input_str, str):
        raise ValueError(f"Expected string as input, found {type(input_str)}")
    if not isinstance(use_pascal, bool):
        raise ValueError(
            f"Expected boolean as use_pascal parameter, found {type(use_pascal)}"
        )

    words = input_str.split("_")

    start_index = 0 if use_pascal else 1

    words_to_capitalize = words[start_index:]

    capitalized_words = [word[0].upper() + word[1:] for word in words_to_capitalize]

    initial_word = "" if use_pascal else words[0]

    return "".join([initial_word] + capitalized_words)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
