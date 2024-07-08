"""
Solution By: Reniz Shah
Topic: Deterministic Finite Automaton (DFA)
Given a string s, return whether s is a valid number or not
Input: s = -90E3
Output: True
Leetcode link: https://leetcode.com/problems/valid-number/description/
"""


def classify_char(char):
    """
    Classifies a character into one of the following categories:

    - 'numeric': if the character is a digit (0-9)
    - 'ign': if the character is a plus sign (+) or a minus sign (-)
    - 'exponent': if the character is an 'e' or 'E' (used in exponential notation)
    - 'decimal': if the character is a decimal point (.)
    - None: if the character does not fit into any of the above categories

    Parameters:
    char (str): The character to be classified

    Returns:
    str: The classification of the character

    >>> classify_char('2')
    'numeric'
    >>> classify_char('-')
    'sign'
    >>> classify_char('e')
    'exponent'
    >>> classify_char('.')
    'decimal'
    >>> classify_char('r')

    """

    if char.isdigit():
        return "numeric"
    if char in "+-":
        return "sign"
    if char in "eE":
        return "exponent"
    if char == ".":
        return "decimal"
    return None


def is_valid_number(s: str) -> bool:
    """
    This function checks if the input string represents a valid number.

    It uses a finite state machine to parse the input string,
    transitioning between states based on the character type.
    The function returns True if the input string represents a valid number,
    and False otherwise.

    A valid number is defined as a string that can be parsed into an
    integer, decimal, or exponent.

    >>> is_valid_number("2")
    True
    >>> is_valid_number("0089")
    True
    >>> is_valid_number("-0.1")
    True
    >>> is_valid_number("+3.14")
    True
    >>> is_valid_number("4.")
    True
    >>> is_valid_number("-.9")
    True
    >>> is_valid_number("2e10")
    True
    >>> is_valid_number("-90E3")
    True
    >>> is_valid_number("3e+7")
    True
    >>> is_valid_number("+6e-1")
    True
    >>> is_valid_number("53.5e93")
    True
    >>> is_valid_number("-123.456e789")
    True


    >>> is_valid_number("abc")
    False
    >>> is_valid_number("1a")
    False
    >>> is_valid_number("1e")
    False
    >>> is_valid_number("e3")
    False
    >>> is_valid_number("99e2.5")
    False
    >>> is_valid_number("--6")
    False
    >>> is_valid_number("-+3")
    False
    >>> is_valid_number("95a54e53")
    False
    >>> is_valid_number(".")
    False
    """

    state_machine = {
        "initial": {"numeric": "whole", "sign": "signed", "decimal": "fractional"},
        "signed": {"numeric": "whole", "decimal": "fractional"},
        "whole": {"numeric": "whole", "decimal": "Fraction", "exponent": "exponential"},
        "fractional": {"numeric": "Fraction"},
        "Fraction": {"numeric": "Fraction", "exponent": "exponential"},
        "exponential": {"numeric": "Exp_number", "sign": "Exp_sign"},
        "Exp_sign": {"numeric": "Exp_number"},
        "Exp_number": {"numeric": "Exp_number"},
    }

    valid_final_states = {"whole", "Fraction", "Exp_number"}
    current_state = "initial"

    for char in s:
        char_type = classify_char(char)
        if char_type is None or char_type not in state_machine[current_state]:
            return False
        current_state = state_machine[current_state][char_type]

    return current_state in valid_final_states


if __name__ == "__main__":
    import doctest

    doctest.testmod()
