import re


def camel_with_numbers_to_snake(camel_case) -> str:
    words = re.findall("[a-zA-Z][^A-Z]*", camel_case)
    return "_".join(w.lower() for w in words)


# Example usage
# camel_with_numbers_string = "exampleVariableName123"
# snake_case_with_numbers_string = camel_with_numbers_to_snake(camel_with_numbers_string)
# print(snake_case_with_numbers_string)  # Output: "example_variable_name123"
if __name__ == "__main__":
    from doctest import testmod

    testmod()
