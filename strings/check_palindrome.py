# -*- coding: utf-8 -*-

"""
  check_palindrome.py: Checks if a string is a palindrome.

  Author: Joaquin Cabezas github.com/joaquincabezas
  Date: 07/04/2020

"""

def check_palindrome(input_string: str, exact_string: bool=True) -> bool:
  """
  A Palindrome String is a sequence of characters  which reads the same backward as forward.

  Parameters
  ----------
  input_string : str
      The string to be checked as a palindrome
  exact_string : bool
      If True: every character will be considered. 
      If False: only letters will be considered
        (thus removing spaces, punctuation and 
        any other characters)
  
  Returns
  -------
  bool
      True if the string is a palindrome

  >>> check_palindrome("Rats live on no evil star")
  True
  >>> check_palindrome("Was it a car or a cat I saw?")
  False
  >>> check_palindrome("Was it a car or a cat I saw?",False)
  True
  """

  # There is no difference between lowercase and uppercase letters, so we convert everything to lowercase
  input_string = input_string.lower()

  # If we are not considering the full set of characters, we first remove everything except letters
  if not exact_string:
    # Only english characters
    valid_characters = "abcdefghijklmnopqrstuvwxyz"
    # We remove everything except those characters
    input_string = ''.join(filter(valid_characters.__contains__, input_string))

  # Compares a string with its reverse
  return input_string==input_string[::-1]


if __name__ == "main":
    input_string = "Was it a car or a cat I saw?"
    palindrome = check_palindrome(input_string, False)
    print(f"'{input_string}' is {'' if palindrome else 'not '}a palindrome string")
