"""
Implementation of the Suffix Array construction algorithm in Python.

This algorithm takes a text string as input and produces its Suffix Array.
A Suffix Array is a sorted array of all suffixes of a given string.
It is a data structure used in, among others, bioinformatics and data compression.
"""


def build_suffix_array(text: str) -> list[int]:
    """
    Builds the Suffix Array for a given text string.

    The construction involves:
    1. Generating all suffixes of the string.
    2. Storing each suffix along with its original starting index.
    3. Sorting these (suffix, index) pairs lexicographically based on the suffix.
    4. Extracting the indices into a list, which is the Suffix Array.

    Args:
        text: The input text string. It's common to append a special
              character (lexicographically smallest, like '$') to the end
              of the string to ensure all suffixes are unique and to
              simplify certain suffix array algorithms, though this
              implementation will work without it too by relying on Python's
              string comparison. For canonical behavior, consider appending it.

    Returns:
        list[int]: The Suffix Array, which is a list of starting
                   indices of sorted suffixes.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> build_suffix_array("banana") # Using "banana" without a special end char
        [5, 3, 1, 0, 4, 2]
        Suffixes:
        "a" (5)
        "ana" (3)
        "anana" (1)
        "banana" (0)
        "na" (4)
        "nana" (2)

        >>> build_suffix_array("banana$")
        [6, 5, 3, 1, 0, 4, 2]
        Suffixes:
        "$" (6)
        "a$" (5)
        "ana$" (3)
        "anana$" (1)
        "banana$" (0)
        "na$" (4)
        "nana$" (2)

        >>> build_suffix_array("abracadabra")
        [10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]

        >>> build_suffix_array("")
        []

        >>> build_suffix_array("aaa")
        [2, 1, 0]  (or any order of 0,1,2 if suffixes are identical like "a", "a", "a")
        Python's sort is stable, so for identical suffixes,
        the one with larger original index comes later if we consider '$' implicitly.
        If we list them: "a" (2), "aa" (1), "aaa" (0)
        Sorted by suffix: "a", "aa", "aaa" -> indices [2, 1, 0]
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    n = len(text)
    if n == 0:
        return []

    # 1. Generate all suffixes and store them with their original starting indices.
    #    A suffix is defined by its starting position in the original text.
    #    Example: text = "banana"
    #    Suffixes are:
    #    (0, "banana")
    #    (1, "anana")
    #    (2, "nana")
    #    (3, "ana")
    #    (4, "na")
    #    (5, "a")

    suffixes = []
    for i in range(n):
        suffixes.append((text[i:], i))  # Store (suffix_string, original_index)

    # 2. Sort the (suffix, index) pairs.
    #    Python's default sort for tuples will sort based on the first element
    #    (the suffix string), and then by the second element (the index) if
    #    suffixes are identical. This lexicographical sort is the core of
    #    Suffix Array construction. The sort is stable, meaning if two suffixes
    #    are identical (which shouldn't happen if a unique terminator like '$'
    #    is used), their relative order base on original index would be preserved
    #    if that was a secondary sort key. Here, we just need to sort by the suffix
    #    string. suffixes.sort(key=lambda x: x[0])

    # 3. Extract the indices into a list.
    #    This list of sorted indices is the Suffix Array.
    suffix_array = [item[1] for item in suffixes]

    return suffix_array


def print_suffixes_and_array(text: str, sa: list[int]):
    """Helper function to print suffixes in sorted order along with their indices."""
    if not sa:
        print("  (Empty string has no suffixes)")
        return
    print("  Sorted Suffixes (index: suffix):")
    for i in sa:
        print(f"    {i}: {text[i:]}")
    print(f"  Suffix Array: {sa}")


def main():
    """
    Main function to demonstrate Suffix Array construction.
    """
    print("### Suffix Array Construction Demonstration ###\n")

    test_cases = [
        "banana",
        "banana$",  # With a unique terminator
        "abracadabra",
        "mississippi",
        "GATTACA",
        "aaaaa",
        "abcde",
        "",  # Empty string
    ]

    for text_to_process in test_cases:
        print(f'Original string: "{text_to_process}"')
        try:
            suffix_arr = build_suffix_array(text_to_process)
            print_suffixes_and_array(text_to_process, suffix_arr)
            print("")  # Newline for better readability
        except TypeError as e:
            print(f"  Error: {e}\n")

    # Example with user input
    print("--- Test with user input ---")
    try:
        user_input = input(
            "Enter a string to build its Suffix Array (e.g., 'banana'): "
        )
        # It's good practice to suggest adding '$' if needed for specific use cases
        # print("(Consider adding a unique character like '$' to the end if not
        # present)")
        if (
            user_input is not None
        ):  # Check if input is not None (Ctrl+D might give None)
            sa_output = build_suffix_array(user_input)
            print_suffixes_and_array(user_input, sa_output)
        else:
            print("  No string entered.")  # Should not happen with input() unless EOF
    except TypeError as e:
        print(f"  Error: {e}")
    except EOFError:  # Handles Ctrl+D
        print("\n  Input cancelled.")
    except KeyboardInterrupt:
        print("\n  Process interrupted by user.")


if __name__ == "__main__":
    main()
