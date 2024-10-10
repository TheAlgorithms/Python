def camel_to_snake_case(girdi_str: str) -> str:
    """
    camelCase (veya PascalCase) biçimindeki bir dizeyi snake_case biçimine dönüştürür.

    # Organiser: K. Umut Araz

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
    ValueError: Girdi olarak bir dize bekleniyordu, bulunan <class 'int'>

    """

    # Geçersiz girdi türü kontrolü
    if not isinstance(girdi_str, str):
        msg = f"Girdi olarak bir dize bekleniyordu, bulunan {type(girdi_str)}"
        raise ValueError(msg)

    snake_str = ""

    for index, char in enumerate(girdi_str):
        if char.isupper():
            snake_str += "_" + char.lower()

        # Eğer karakter küçük harf ve önünde bir rakam varsa:
        elif index > 0 and girdi_str[index - 1].isdigit() and char.islower():
            snake_str += "_" + char

        # Eğer karakter bir rakam ve önünde bir harf varsa:
        elif index > 0 and girdi_str[index - 1].isalpha() and char.isnumeric():
            snake_str += "_" + char.lower()

        # Eğer karakter alfanümerik değilse:
        elif not char.isalnum():
            snake_str += "_"

        else:
            snake_str += char

    # Baştaki alt çizgiyi kaldır
    if snake_str and snake_str[0] == "_":
        snake_str = snake_str[1:]

    return snake_str


if __name__ == "__main__":
    from doctest import testmod

    testmod()
