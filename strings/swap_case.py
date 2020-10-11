'''
This algorithm helps you to swap cases.

User will give input and then program will perform swap cases.

In other words, convert all lowercase letters to uppercase letters and vice versa.
For example:
1)>>>Please input sentence: Algorithm.Python@89
  aLGORITHM.pYTHON@89
2)>>>Please input sentence: github.com/mayur200
  GITHUB.COM/MAYUR200

Constraints: Length of string should between 1 and 1000


'''
import re
'''
This re.compile() function saves the pattern from 'a' to 'z' and 'A' to 'Z' into 'regexp' variable
'''
regexp = re.compile('[^a-zA-Z]+')


def swap_case(sentence):
    """
    This function will convert all lowercase letters to uppercase letters and vice versa.
    >>>swap_case('Algorithm.Python@89')
    aLGORITHM.pYTHON@89
    """
    if len(sentence) < 1001:
        newstring = ''
        for word in sentence:
            if word.isupper() == True:
                newstring += word.lower()
            if word.islower() == True:
                newstring += word.upper()
            if regexp.search(word):
                newstring += word

    else:
        raise Exception("Charater length should be between 1 and 1000")
    return newstring


if __name__ == '__main__':
    s = input("Please input sentence:")
    result = swap_case(s)
    print(result)