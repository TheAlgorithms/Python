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
            - A list of integers representing the pattern characters, with 0 for wildcards.

    Examples:
        >>> preprocess_text_and_pattern("abcabc", "abc*")
        ([1, 2, 3, 1, 2, 3], [1, 2, 3, 0])
        >>> preprocess_text_and_pattern("hello", "he*o")
        ([3, 2, 4, 4, 5], [3, 2, 0, 5])
    """

    unique_chars = set(text + pattern)
    char_to_int = {
        char: i + 1 for i, char in enumerate(unique_chars)
    }  # Unique non-zero integers

    # Replace pattern '*' with 0, other characters with their unique integers
    pattern_int = [char_to_int[char] if char != "*" else 0 for char in pattern]
    text_int = [char_to_int[char] for char in text]

    return text_int, pattern_int


def fft_convolution(input_seq_a: np.ndarray, input_seq_b: np.ndarray) -> np.ndarray:
    """Performs convolution using the Fast Fourier Transform (FFT).

    Args:
        input_seq_a: The first sequence (1D numpy array).
        input_seq_b: The second sequence (1D numpy array).

    Returns:
        The convolution of the two sequences.

    Examples:
        >>> fft_convolution(np.array([1, 2, 3]), np.array([0, 1, 0.5]))
        array([0. , 1. , 2.5, 3. , 1.5])
    """

    n = len(input_seq_a) + len(input_seq_b) - 1
    A = fft(input_seq_a, n)
    B = fft(input_seq_b, n)
    return np.real(ifft(A * B))


def compute_a_fft(text_int: list[int], pattern_int: list[int]) -> np.ndarray:
    """Computes the A array for the pattern matching algorithm.

    Args:
        text_int: The integer representation of the text.
        pattern_int: The integer representation of the pattern.

    Returns:
        The A array.

    Examples:
        >>> compute_a_fft([1, 2, 3, 1, 2, 3], [1, 2, 3, 0])
        array([...])  # Replace with the expected output based on your implementation
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

    # Calculate A[i] using the convolution results
    A = sum1[: n - m + 1] - 2 * sum2[: n - m + 1] + sum3[: n - m + 1]

    return A


# Main function to run the matching
if __name__ == "__main__":
    # Example test case
    text = "abcabc"
    pattern = "abc*"

    # Preprocess text and pattern
    text_int, pattern_int = preprocess_text_and_pattern(text, pattern)
    print("Preprocessed text:", text_int)
    print("Preprocessed pattern:", pattern_int)

    # Compute A array
    A = compute_a_fft(text_int, pattern_int)
    print("A array:", A)

    # Find matches
    matches = [i for i in range(len(A)) if np.isclose(A[i], 0)]
    print("Pattern matches at indices:", matches)
