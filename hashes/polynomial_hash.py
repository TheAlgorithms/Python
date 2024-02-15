"""
Calculate the hash of a string using a polynomial rolling hash function.

Args:
s (str): The input string to be hashed.
p (int): A prime number to serve as the base for the polynomial hash (default is 31).
m (int): A large prime number to prevent integer overflow (default is 10^9 + 9).

Returns: int: The computed hash value.
Wikipedia :: https://en.wikipedia.org/wiki/Hash_function
"""


def polynomial_hash(s, p=31, m=10**9 + 9):
    hash_value = 0
    p_pow = 1
    for char in s:
        char_value = ord(char) - ord("a") + 1  # Convert character to a numerical value
        hash_value = (hash_value + char_value * p_pow) % m
        p_pow = (p_pow * p) % m
    return hash_value


print(polynomial_hash("PythonLanguage"))
# Output: 877483825
