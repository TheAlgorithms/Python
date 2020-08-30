def check_anagrams(a: str, b: str) -> bool:
    """
    Two strings are anagrams if they are made of the same letters
    arranged differently (ignoring the case).
    >>> check_anagrams('Silent', 'Listen')
    True
    >>> check_anagrams('This is a string', 'Is this a string')
    True
    >>> check_anagrams('There', 'Their')
    False
    """
    return sorted(a.lower()) == sorted(b.lower())


if __name__ == "__main__":
    input_A = input("Enter the first string ").strip()
    input_B = input("Enter the second string ").strip()

    status = check_anagrams(input_A, input_B)
    print(f"{input_A} and {input_B} are {'' if status else 'not '}anagrams.")
