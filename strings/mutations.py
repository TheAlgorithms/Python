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
    #input string
    
    i, c = input().split()
    #input position and character
    
    #call a function
    s_new = mutate_string(s, int(i), c)
    
    print(s_new)
