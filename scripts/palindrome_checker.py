# palindrome_checker.py
# Simple palindrome checker
# Author: Ananth Sai


def is_palindrome(s: str) -> bool:
    s = "".join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]


def main():
    text = input("Enter a word or phrase: ").strip()
    if is_palindrome(text):
        print(f"✅ '{text}' is a palindrome!")
    else:
        print(f"❌ '{text}' is not a palindrome.")


if __name__ == "__main__":
    main()
