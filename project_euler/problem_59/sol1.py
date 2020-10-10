"""
Euler Problem : 59
author : sandeep gupta
time   : 4 October 2020, 18:30
"""
from itertools import permutations
import os

def check_english(ascii1, ascii2):
    """
    function to check if the
    xor(exclusive or) of two ascii
    numbers entered is only letters
    used in common english
    """
    xor = ascii1 ^ ascii2
    return isAcceptable(chr(xor))

    # print (chr(xor))
    return False


def isAcceptable(myChar):
    return (
        "a" <= myChar <= "z"
        or "A" <= myChar <= "Z"
        or myChar == " "
        or myChar == "'"
        or myChar == ","
        or myChar == '"'
        or myChar == "["
        or myChar == "]"
        or myChar == ":"
        or "0" <= myChar <= "9"
        or myChar == "/"
        or myChar == "."
        or myChar == "("
        or myChar == ")"
        or myChar == ";"
        or myChar == "+"
    )


def solution() -> int:
    """
    I would say this is slightly tricky question to solve
    getting a sense of common english word is something like in the
    isAcceptable function, otherthan that iterated over all the possible
    passwords key and later checking with the is a commonly used function.

    Input to the solution is from cipher file.
    >>> solution()
    129448

    """
    script_dir = os.path.abspath(os.path.dirname(__file__))
    cipher = os.path.join(script_dir, "cipher.txt")
    answer = 0
    try:
        with open(cipher, "r") as file:
            data = file.read().replace("\n", "")
            data = data.split(",")
            data = [int(x) for x in data]
            for i in range(97, 123):
                for j in range(97, 123):
                    for k in range(97, 123):
                        possible_lists = set(list(permutations([i, j, k], 3)))
                        for possible_answer in possible_lists:
                            round_robin_count = 0
                            words = ""
                            valid = True
                            for d in data:
                                if check_english(d, possible_answer[round_robin_count]):
                                    words += chr(d ^ possible_answer[round_robin_count])
                                else:
                                    valid = False
                                    break
                                round_robin_count = (round_robin_count + 1) % 3
                            if valid:
                                for word in words:
                                    answer += ord(word)
                                return answer
    except BaseException:
        print("An exception occurred while reading file")
    return answer


print(solution())

# Tests
if __name__ == "__main__":
    import doctest

    doctest.testmod()
