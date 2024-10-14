def is_palindrome(s: str) -> bool:
    """
    Helper function to check if a given string is a palindrome.

    Args:
    s (str): The string to check.

    Returns:
    bool: True if s is a palindrome, False otherwise.
    """
    return s == s[::-1]


def backtrack(start: int, path: list, result: list, s: str):
    """
    Backtracking function to find all palindrome partitions of the string s.

    Args:
    start (int): Starting index of the substring to consider.
    path (list): The current path (partition) being constructed.
    result (list): The final list of all valid palindrome partitions.
    s (str): The input string.
    """
    # If we've reached the end of the string, add the current path to the result
    if start == len(s):
        result.append(path[:])  # Add a copy of the current path to the result
        return

    # Try every possible partition starting from 'start'
    for end in range(start + 1, len(s) + 1):
        # If the current substring is a palindrome, we can proceed
        if is_palindrome(s[start:end]):
            path.append(s[start:end])  # Choose the current palindrome substring
            backtrack(end, path, result, s)  # Explore further partitions
            path.pop()  # Backtrack and remove the last chosen partition


def partition(s: str) -> list:
    """
    Main function to find all palindrome partitions of a string.

    Args:
    s (str): The input string.

    Returns:
    list: A list of lists containing all valid palindrome partitions.
    """
    result = []  # List to store all partitions
    backtrack(0, [], result, s)  # Start the backtracking process
    return result


# Example usage:
s = "aab"
print(partition(s))  # Output: [['a', 'a', 'b'], ['aa', 'b']]
