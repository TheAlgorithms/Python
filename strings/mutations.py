""" Read a given string, change the character at a given index and then print the modified string.

Input:-
abracadabra
5 k

Output:-
abrackdabra

Hackerank Link: https://www.hackerrank.com/challenges/python-mutations/problem """

def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

if __name__ == "__main__":
    s = input()
    """
    >>> string = "abracadabra
    >>> l = list(string)
    """

    i, c = input().split()
    """
    >>> l[5] = 'k'
    >>> string = ''.join(l)
    """

    s_new = mutate_string(s, int(i), c)
    """
    >>> print string
    """
    print(s_new)
