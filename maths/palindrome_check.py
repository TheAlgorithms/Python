''' A palindromic number (also known as a numeral palindrome or a numeric palindrome) 
is a number (such as 16461) that remains the same when its digits are reversed. ''' 


def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Input a word or phrase
word_or_phrase = input("Enter a word or phrase: ")

if is_palindrome(word_or_phrase):
    print(f"{word_or_phrase} is a palindrome!")
else:
    print(f"{word_or_phrase} is not a palindrome.")
