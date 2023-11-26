import timeit

####################################
# Levenshtein Distance Function
####################################
def levenshtein_distance(first_word: str, second_word: str) -> int:
    """
    Implementation of the Levenshtein distance in Python.

    Parameters:
    - first_word (str): The first word to measure the difference.
    - second_word (str): The second word to measure the difference.

    Returns:
    int: The Levenshtein distance between the two words.

    Examples:
    >>> levenshtein_distance("planet", "planetary")
    3
    >>> levenshtein_distance("", "test")
    4
    >>> levenshtein_distance("book", "back")
    2
    >>> levenshtein_distance("book", "book")
    0
    >>> levenshtein_distance("test", "")
    4
    >>> levenshtein_distance("", "")
    0
    >>> levenshtein_distance("orchestration", "container")
    10
    """
    # The longer word should come first
    if len(first_word) < len(second_word):
        return levenshtein_distance(second_word, first_word)

    if len(second_word) == 0:
        return len(first_word)

    previous_row = list(range(len(second_word) + 1))

    for i, c1 in enumerate(first_word):
        current_row = [i + 1]

        for j, c2 in enumerate(second_word):
            # Calculate insertions, deletions, and substitutions
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)

            # Get the minimum to append to the current row
            current_row.append(min(insertions, deletions, substitutions))

        # Store the previous row
        previous_row = current_row

    # Returns the last element (distance)
    return previous_row[-1]

####################################
# Optimized Levenshtein Distance Function
####################################
def levenshtein_distance_optimized(first_word: str, second_word: str) -> int:
    """
    Compute the Levenshtein distance between two words (strings).

    The function is optimized for efficiency by modifying rows in place.

    Parameters:
    - first_word (str): The first word to measure the difference.
    - second_word (str): The second word to measure the difference.

    Returns:
    int: The Levenshtein distance between the two words.

    Examples:
    >>> levenshtein_distance_optimized("planet", "planetary")
    3
    >>> levenshtein_distance_optimized("", "test")
    4
    >>> levenshtein_distance_optimized("book", "back")
    2
    >>> levenshtein_distance_optimized("book", "book")
    0
    >>> levenshtein_distance_optimized("test", "")
    4
    >>> levenshtein_distance_optimized("", "")
    0
    >>> levenshtein_distance_optimized("orchestration", "container")
    10
    """
    if len(first_word) < len(second_word):
        return levenshtein_distance_optimized(second_word, first_word)

    if len(second_word) == 0:
        return len(first_word)

    previous_row = list(range(len(second_word) + 1))

    for i, c1 in enumerate(first_word):
        current_row = [i + 1] + [0] * len(second_word)

        for j, c2 in enumerate(second_word):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row[j + 1] = min(insertions, deletions, substitutions)

        previous_row = current_row

    return previous_row[-1]

####################################
# Benchmarking Function
####################################
def benchmark_levenshtein_distance(name: str, func) -> None:
    """
    Benchmark the Levenshtein distance function.

    Parameters:
    - name (str): The name of the function being benchmarked.
    - func: The function to be benchmarked.
    """
    stmt = f"{func.__name__}('sitting', 'kitten')"
    setup = f"from __main__ import {func.__name__}"
    number = 1000
    result = timeit.timeit(stmt=stmt, setup=setup, number=number)
    print(f"{name:<35} finished {number:,} runs in {result:.5f} seconds")

####################################
# Main Execution
####################################
if __name__ == "__main__":
    # Get user input for words
    levenshtein_first_word = input("Enter the first word for Levenshtein distance:\n").strip()
    levenshtein_second_word = input("Enter the second word for Levenshtein distance:\n").strip()

    # Calculate and print Levenshtein distances
    levenshtein_result = levenshtein_distance(levenshtein_first_word, levenshtein_second_word)
    print(f"Levenshtein distance between {levenshtein_first_word} and {levenshtein_second_word} is {levenshtein_result}")

    levenshtein_optimized_result = levenshtein_distance_optimized(levenshtein_first_word, levenshtein_second_word)
    print(f"Levenshtein distance (optimized) between {levenshtein_first_word} and {levenshtein_second_word} is {levenshtein_optimized_result}")

    # Benchmark the Levenshtein distance functions
    benchmark_levenshtein_distance("Levenshtein Distance", levenshtein_distance)
    benchmark_levenshtein_distance("Optimized Levenshtein", levenshtein_distance_optimized)
