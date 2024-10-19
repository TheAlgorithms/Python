def is_string_palindrome(words: str) -> bool:
    cleaned_phrase = ''.join(words.split()).lower()
    return cleaned_phrase == cleaned_phrase[::-1]

if __name__ == "__main__":
    n=input("Enter a word:-")
    print(is_string_palindrome(n))