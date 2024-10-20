"""
CheckKebabCase method checks the given string is in kebab-case or not.
Problem Source & Explanation: https://en.wikipedia.org/wiki/Naming_convention_(programming)
"""

import re


def is_kebab_case(var_name: str) -> bool:
    """
    CheckKebabCase method checks the given string is in kebab-case or not.
    Problem Source & Explanation: https://en.wikipedia.org/wiki/Naming_convention_(programming)
    >>> is_kebab_case('variable-name')
    True
    >>> is_kebab_case('VariableName')
    False
    >>> is_kebab_case('variable_name')
    False
    >>> is_kebab_case('variableName')
    False
    """

    if not isinstance(var_name, str):
        raise TypeError("Argument is not a string.")

    pat = r"(\w+)-(\w)([\w-]*)"
    return bool(re.match(pat, var_name)) and "_" not in var_name


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    input_var = input("Enter the variable name: ").strip()

    status = is_kebab_case(input_var)
    print(f"{input_var} is {'in ' if status else 'not in '}kebab-case.")
