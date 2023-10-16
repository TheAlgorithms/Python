"""
Given a string and a positive number k, find the longest substring of the string containing k distinct characters.
If k is more than the total number of distinct characters in the string, return the whole string.
//https://medium.com/techie-delight/top-problems-on-sliding-window-technique-8e63f1e2b1fa
"""
# Define the character range
CHAR_RANGE = 128

# Function to find the longest substring of a given string containing
# `k` distinct characters using a sliding window
def find_longest_substring(input_str: str, k: int) -> str:
    """
    Find the longest substring of a given string containing at most k distinct characters.
    
    Args:
        input_str (str): The input string to search in.
        k (int): The maximum number of distinct characters allowed in the substring.
    
    Returns:
        str: The longest substring containing at most k distinct characters.
    
    Example:
        >>> find_longest_substring("abcbdbdbbdcdabd", 2)
        'bdbdbbd'
    """
    # Stores the longest substring boundaries
    end = begin = 0

    # Set to store distinct characters in a window
    window = set()

    # `freq` stores the frequency of characters present in the
    # current window. We can also use a dictionary instead.
    freq = [0] * CHAR_RANGE

    # `[low…high]` maintains the sliding window boundaries
    low = high = 0

    while high < len(input_str):
        window.add(input_str[high])
        freq[ord(input_str[high])] += 1

        # If the window size is more than `k`, remove characters from the left
        while len(window) > k:
            # If the leftmost character's frequency becomes 0 after
            # removing it from the window, remove it from the set as well
            freq[ord(input_str[low])] -= 1
            if freq[ord(input_str[low])] == 0:
                window.remove(input_str[low])
            low += 1  # Reduce window size

        # Update the maximum window size if necessary
        if end - begin < high - low:
            end = high
            begin = low

        high += 1

    # Return the longest substring found at `input_str[begin…end]`
    return input_str[begin:end + 1]

if __name__ == '__main':
    s = 'abcbdbdbbdcdabd'
    k = 2
    print(find_longest_substring(s, k))



 
