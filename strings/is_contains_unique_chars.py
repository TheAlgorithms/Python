def is_contains_unique_chars(input_str: str) -> bool:
    """
    Check if all characters in the string is unique or not.
    >>> is_contains_unique_chars("I_love.py")
    True
    >>> is_contains_unique_chars("I don't love Python")
    False

    Time complexity: O(n)
    Space compexity: O(1) 19320 bytes as we are having 144697 characters in unicode
    """
    bitmap = 0
    for ch in input_str:
        ch_unicode = ord(ch)
        ch_bit_index_on = pow(2, ch_unicode)

        if bitmap & ch_bit_index_on == ch_bit_index_on:
            return False

        bitmap |= ch_bit_index_on

    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
