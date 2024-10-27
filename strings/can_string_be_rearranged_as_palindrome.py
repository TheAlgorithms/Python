# Created by susmith98

from collections import Counter
from timeit import timeit

# Problem Description:
# Check if characters of the given string can be rearranged to form a palindrome.
# Counter is faster for long strings and non-Counter is faster for short strings.


def can_string_be_rearranged_as_palindrome_counter(
    input_str: str = "",
) -> bool:
    """
    A Palindrome is a String that reads the same forward as it does backwards.
    Examples of Palindromes mom, dad, malayalam
    >>> can_string_be_rearranged_as_palindrome("")
    True
    >>> can_string_be_rearranged_as_palindrome_counter("Momo")
    True
    >>> can_string_be_rearranged_as_palindrome_counter("Mother")
    False
    >>> can_string_be_rearranged_as_palindrome_counter("Father")
    False
    >>> can_string_be_rearranged_as_palindrome_counter("A man a plan a canal Panama")
    True
    """
    return sum(c % 2 for c in Counter(input_str.replace(" ", "").lower()).values()) < 2


def can_string_be_rearranged_as_palindrome(input_str: str = "") -> bool:
    """
    A Palindrome is a String that reads the same forward as it does backwards.
    Examples of Palindromes mom, dad, malayalam
    >>> can_string_be_rearranged_as_palindrome("Momo")
    True
    >>> can_string_be_rearranged_as_palindrome("Mother")
    False
    >>> can_string_be_rearranged_as_palindrome("Father")
    False
    >>> can_string_be_rearranged_as_palindrome_counter("A man a plan a canal Panama")
    True
    """
    if len(input_str) == 0:
        return True
    lower_case_input_str = input_str.replace(" ", "").lower()
    # character_freq_dict: Stores the frequency of every character in the input string
    character_freq_dict: dict[str, int] = {}

    for character in lower_case_input_str:
        character_freq_dict[character] = character_freq_dict.get(character, 0) + 1
    """
    Above line of code is equivalent to:
    1) Getting the frequency of current character till previous index
    >>> character_freq =  character_freq_dict.get(character, 0)
    2) Incrementing the frequency of current character by 1
    >>> character_freq = character_freq + 1
    3) Updating the frequency of current character
    >>> character_freq_dict[character] = character_freq
    """
    """
    OBSERVATIONS:
    Even length palindrome
    -> Every character appears even no.of times.
    Odd length palindrome
    -> Every character appears even no.of times except for one character.
    LOGIC:
    Step 1: We'll count number of characters that appear odd number of times i.e oddChar
    Step 2:If we find more than 1 character that appears odd number of times,
    It is not possible to rearrange as a palindrome
    """
    odd_char = 0

    for character_count in character_freq_dict.values():
        if character_count % 2:
            odd_char += 1
    return not odd_char > 1


def benchmark(input_str: str = "") -> None:
    """
    Benchmark code for comparing above 2 functions
    """
    print("\nFor string = ", input_str, ":")
    print(
        "> can_string_be_rearranged_as_palindrome_counter()",
        "\tans =",
        can_string_be_rearranged_as_palindrome_counter(input_str),
        "\ttime =",
        timeit(
            "z.can_string_be_rearranged_as_palindrome_counter(z.check_str)",
            setup="import __main__ as z",
        ),
        "seconds",
    )
    print(
        "> can_string_be_rearranged_as_palindrome()",
        "\tans =",
        can_string_be_rearranged_as_palindrome(input_str),
        "\ttime =",
        timeit(
            "z.can_string_be_rearranged_as_palindrome(z.check_str)",
            setup="import __main__ as z",
        ),
        "seconds",
    )


if __name__ == "__main__":
    check_str = input(
        "Enter string to determine if it can be rearranged as a palindrome or not: "
    ).strip()
    benchmark(check_str)
    status = can_string_be_rearranged_as_palindrome_counter(check_str)
    print(f"{check_str} can {'' if status else 'not '}be rearranged as a palindrome")
