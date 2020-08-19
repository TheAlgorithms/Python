def check_anagrams(string_A: str, string_B: str) -> bool:
    """
    Two strings are anagrams if they are made of the same letters
    arranged differently (ignoring the case).
    >>> check_anagram('Silent','Listen')
    True
    >>> check_anagram('This is a string','Is this a string')
    True
    >>> check_anagram('There','Their')
    False
    """
    sorted_list_A = sorted(string_A.lower())
    sorted_list_B = sorted(string_B.lower())
    return sorted_list_A == sorted_list_B


if __name__ == "__main__":
    input_A = input("Enter the first string ").strip()
    input_B = input("Enter the second string ").strip()

    status = check_anagrams(input_A, input_B)
    print(
        f"{input_A} and {input_B} are {'anagrams.' if status else 'not anagrams.' = }"
    )
