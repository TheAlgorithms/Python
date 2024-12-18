def join(separator: str, separated: list[str]) -> str:
    """
    Custom implementation of the join() function.
    This function manually concatenates the strings in the list,
    using the provided separator, without relying on str.join().

    :param separator: The separator to place between strings.
    :param separated: A list of strings to join.

    :return: A single string with elements joined by the separator.
    
    :raises Exception: If any element in the list is not a string.
    """
    if not all(isinstance(word_or_phrase, str) for word_or_phrase in separated):
        raise Exception("join() accepts only strings")

    # Manually handle concatenation
    result = ""
    for i, element in enumerate(separated):
        result += element
        if i < len(separated) - 1:  # Add separator only between elements
            result += separator

    return result


if __name__ == "__main__":
    from doctest import testmod

    testmod()
