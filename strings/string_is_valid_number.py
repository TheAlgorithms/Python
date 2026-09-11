"""
Solution By: Reniz Shah
Topic: Deterministic Finite Automaton (DFA)
Given a string s, return whether s is a valid number or not
Leetcode link: https://leetcode.com/problems/valid-number/description/
"""

from enum import Enum


class CharType(Enum):
    NUMERIC = "NUMERIC"
    SIGN = "SIGN"
    EXPONENT = "EXPONENT"
    DECIMAL = "DECIMAL"


class State(Enum):
    INITIAL = "INITIAL"
    SIGNED = "SIGNED"
    WHOLE = "WHOLE"
    FRACTIONAL = "FRACTIONAL"
    FRACTION = "FRACTION"
    EXPONENTIAL = "EXPONENTIAL"
    EXP_SIGN = "EXP_SIGN"
    EXP_NUMBER = "EXP_NUMBER"


state_machine: dict[State, dict[CharType, State]] = {
    State.INITIAL: {
        CharType.NUMERIC: State.WHOLE,
        CharType.SIGN: State.SIGNED,
        CharType.DECIMAL: State.FRACTIONAL,
    },
    State.SIGNED: {CharType.NUMERIC: State.WHOLE, CharType.DECIMAL: State.FRACTIONAL},
    State.WHOLE: {
        CharType.NUMERIC: State.WHOLE,
        CharType.DECIMAL: State.FRACTION,
        CharType.EXPONENT: State.EXPONENTIAL,
    },
    State.FRACTIONAL: {CharType.NUMERIC: State.FRACTION},
    State.FRACTION: {
        CharType.NUMERIC: State.FRACTION,
        CharType.EXPONENT: State.EXPONENTIAL,
    },
    State.EXPONENTIAL: {
        CharType.NUMERIC: State.EXP_NUMBER,
        CharType.SIGN: State.EXP_SIGN,
    },
    State.EXP_SIGN: {CharType.NUMERIC: State.EXP_NUMBER},
    State.EXP_NUMBER: {CharType.NUMERIC: State.EXP_NUMBER},
}


def classify_char(char: str) -> CharType | None:
    """
    Classifies a character into one of the following categories:

    - 'CharType.NUMERIC': if the character is a digit (0-9)
    - 'CharType.SIGN': if the character is a plus sign (+) or a minus sign (-)
    - 'CharType.EXPONENT': if the character is an 'e' or 'E'
        (used in exponential notation)
    - 'CharType.DECIMAL': if the character is a decimal point (.)
    - None: if the character does not fit into any of the above categories
    - None: if size of char is not 1

    Parameters:
    char (str): The character to be classified

    Returns:
    CharType: The classification of the character

    >>> classify_char('2')
    <CharType.NUMERIC: 'NUMERIC'>
    >>> classify_char('-')
    <CharType.SIGN: 'SIGN'>
    >>> classify_char('e')
    <CharType.EXPONENT: 'EXPONENT'>
    >>> classify_char('.')
    <CharType.DECIMAL: 'DECIMAL'>
    >>> classify_char('')

    >>> classify_char('0')
    <CharType.NUMERIC: 'NUMERIC'>
    >>> classify_char('01')
    """
    if len(char) != 1:
        return None
    if char.isdigit():
        return CharType.NUMERIC
    if char in "+-":
        return CharType.SIGN
    if char in "eE":
        return CharType.EXPONENT
    if char == ".":
        return CharType.DECIMAL
    return None


def is_valid_number(number_string: str) -> bool:
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

    valid_final_states = {State.WHOLE, State.FRACTION, State.EXP_NUMBER}
    current_state = State.INITIAL

    for char in number_string:
        char_type = classify_char(char)
        if char_type is None or char_type not in state_machine[current_state]:
            return False
        current_state = state_machine[current_state][char_type]

    return current_state in valid_final_states


if __name__ == "__main__":
    import doctest

    doctest.testmod()
