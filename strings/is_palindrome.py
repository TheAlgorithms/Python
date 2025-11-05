def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if __name__ == "__main__":
    print(is_palindrome("madam"))  # True
    print(is_palindrome("hello"))  # False
