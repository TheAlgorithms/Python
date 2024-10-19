#!/usr/bin/env python3

import doctest


def build_suffix_array(input_string: str) -> list[int]:
    """
    Build the suffix array for the given string.

    Parameters:
        input_string (str): The input string.

    Returns:
        list[int]: The suffix array (a list of starting indices of
                    suffixes in sorted order).

    Examples:
        >>> build_suffix_array("banana")
        [5, 3, 1, 0, 4, 2]
    """
    suffixes = [(input_string[i:], i) for i in range(len(input_string))]
    suffixes.sort()  # Sort the suffixes lexicographically
    suffix_array = [suffix[1] for suffix in suffixes]
    return suffix_array


def build_lcp_array(input_string: str, suffix_array: list[int]) -> list[int]:
    """
    Build the LCP array for the given string and suffix array.

    Parameters:
        input_string (str): The input string.
        suffix_array (list[int]): The suffix array.

    Returns:
        list[int]: The LCP array.

    Examples:
        >>> suffix_array = build_suffix_array("banana")
        >>> build_lcp_array("banana", suffix_array)
        [0, 1, 3, 0, 0, 2]
    """
    n = len(input_string)
    rank = [0] * n
    lcp = [0] * n

    # Compute the rank of each suffix
    for i, suffix_index in enumerate(suffix_array):
        rank[suffix_index] = i

    # Compute the LCP array
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = suffix_array[rank[i] - 1]
            while (
                (i + h < n)
                and (j + h < n)
                and (input_string[i + h] == input_string[j + h])
            ):
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1  # Decrease h for the next suffix
    return lcp


# Example usage
if __name__ == "__main__":
    s = "banana"
    suffix_array = build_suffix_array(s)
    lcp_array = build_lcp_array(s, suffix_array)

    print("Suffix Array:")
    for i in range(len(suffix_array)):
        print(f"{suffix_array[i]}: {s[suffix_array[i]:]}")

    print("\nLCP Array:")
    for i in range(1, len(lcp_array)):
        lcp_info = (
            f"LCP between {s[suffix_array[i - 1]:]} and "
            f"{s[suffix_array[i]]}: {lcp_array[i]}"
        )
        print(lcp_info)

# Run doctests
if __name__ == "__main__":
    doctest.testmod()
