""" Read a given string, change the character at a given index and then print the modified string.

Input:-
abracadabra
5 k

Output:-
abrackdabra

Hackerank Link:-
https://www.hackerrank.com/challenges/python-mutations/problem """

def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

