import numpy as np
from numpy.fft import fft, ifft


def preprocess_text_and_pattern(text: str, pattern: str) -> tuple[list[int], list[int]]:
    """Preprocesses text and pattern for pattern matching.

    Args:
        text: The input text string.
        pattern: The input pattern string, potentially containing wildcards ('*').

    Returns:
        A tuple containing:
            - A list of integers representing the text characters.
            - A list of integers representing the pattern characters,
            with 0 for wildcards.
    """

    unique_chars = set(text + pattern)
    char_to_int = {
        char: i + 1 for i, char in enumerate(unique_chars)
    }  # Unique non-zero integers

    # Replace pattern '*' with 0, other characters with their unique integers
    pattern_int = [char_to_int[char] if char != "*" else 0 for char in pattern]
    text_int = [char_to_int[char] for char in text]

    return text_int, pattern_int


def fft_convolution(first_seq: list[int], second_seq: list[int]) -> np.ndarray:
    """Performs convolution using the Fast Fourier Transform (FFT).

    Args:
        first_seq: The first sequence.
        b: The second sequence.

    Returns:
        The convolution of the two sequences.
    """
    n = len(first_seq) + len(second_seq) - 1
    first_seq_fft = fft(first_seq, n)
    second_seq_fft = fft(second_seq, n)
    return np.real(ifft(first_seq_fft * second_seq_fft))


def compute_a_fft(text_int: list[int], pattern_int: list[int]) -> np.ndarray:
    """Computes the A array for the pattern matching algorithm.

    Args:
        text_int: The integer representation of the text.
        pattern_int: The integer representation of the pattern.

    Returns:
        The a array.
    """

    n = len(text_int)
    m = len(pattern_int)

    # Power transforms of the pattern and text based on the formula
    p1 = np.array(pattern_int)
    p2 = np.array([p**2 for p in pattern_int])
    p3 = np.array([p**3 for p in pattern_int])

    t1 = np.array(text_int)
    t2 = np.array([t**2 for t in text_int])
    t3 = np.array([t**3 for t in text_int])

    # Convolution to calculate the terms for A[i]
    sum1 = fft_convolution(p3[::-1], t1)
    sum2 = fft_convolution(p2[::-1], t2)
    sum3 = fft_convolution(p1[::-1], t3)

    # Calculate a[i] using the convolution results
    a = sum1[: n - m + 1] - 2 * sum2[: n - m + 1] + sum3[: n - m + 1]
    # Calculate A[i] using the convolution results
    a = sum1[: n - m + 1] - 2 * sum2[: n - m + 1] + sum3[: n - m + 1]

    return a


# Main function to run the matching
if __name__ == "__main__":
    # Example test case
    import doctest

    doctest.testmod()
    # Get text and pattern as input from the user
    # text = input("Enter the text: ")
    # pattern = input("Enter the pattern (use '*' for wildcard): ")

    text = "abcabc"
    pattern = "abc*"

    # Preprocess text and pattern
    text_int, pattern_int = preprocess_text_and_pattern(text, pattern)
    print("Preprocessed text:", text_int)
    print("Preprocessed pattern:", pattern_int)

    # Compute A array
    a = compute_a_fft(text_int, pattern_int)
    print("A array:", a)

    # Find matches
    matches = [i for i in range(len(a)) if np.isclose(a[i], 0)]
    print("Pattern matches at indices:", matches)
