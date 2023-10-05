import re


def camel_with_numbers_to_snake(camel_case) -> str:
    words = re.findall("[a-zA-Z][^A-Z]*", camel_case)
    return "_".join(w.lower() for w in words)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
