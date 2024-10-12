import numpy as np
from numpy.fft import fft, ifft

def preprocess_text_and_pattern(text, pattern):
    """Preprocesses text and pattern for pattern matching.

    Args:
        text: The input text string.
        pattern: The input pattern string, potentially containing wildcards ('*').

    Returns:
        A tuple containing:
            - A list of integers representing the text characters.
            - A list of integers representing the pattern characters, with 0 for wildcards.
    """

    unique_chars = set(text + pattern)
    char_to_int = {char: i + 1 for i, char in enumerate(unique_chars)}  # Unique non-zero integers

    # Replace pattern '*' with 0, other characters with their unique integers
    pattern_int = [char_to_int[char] if char != '*' else 0 for char in pattern]
    text_int = [char_to_int[char] for char in text]

    return text_int, pattern_int

def fft_convolution(a, b):
    """Performs convolution using the Fast Fourier Transform (FFT).

    Args:
        a: The first sequence.
        b: The second sequence.

    Returns:
        The convolution of the two sequences.
    """

    n = len(a) + len(b) - 1
    A = fft(a, n)
    B = fft(b, n)
    return np.real(ifft(A * B))

def compute_A_fft(text_int, pattern_int):
    """Computes the A array for the pattern matching algorithm.

    Args:
        text_int: The integer representation of the text.
        pattern_int: The integer representation of the pattern.

    Returns:
        The A array.
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
    A = sum1[:n - m + 1] - 2 * sum2[:n - m + 1] + sum3[:n - m + 1]

    return A

# Main function to run the matching
if __name__ == "__main__":

    import doctest
    doctest.testmod()
    # Get text and pattern as input from the user
    # text = input("Enter the text: ")
    # pattern = input("Enter the pattern (use '*' for wildcard): ")

    text = "abcabc"
    pattern = "abc*"




    text_int, pattern_int = preprocess_text_and_pattern(text, pattern)
    A = compute_A_fft(text_int, pattern_int)

    # Matches occur where A[i] == 0
    matches = [i for i in range(len(A)) if np.isclose(A[i], 0)]
    print("Pattern matches at indices:", matches)
    