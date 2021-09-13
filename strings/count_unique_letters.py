'''
This Algorithm will help you to find the unique letters in a string, the algorithm returns a dictionary
of the form letter:occurences

Example,
1. Enter word: abbccc
    {'a': 1, 'b': 2, 'c': 3}
2. Enter word: mellow
    {'m': 1, 'e': 1, 'l': 2, 'o': 1, 'w': 1}
'''

def unique_letters(word):

    '''
    The function prints the dictionary with letters and occurences as key value pairs.
    >>> Enter word : abbccc
    {'m': 1, 'e': 1, 'l': 2, 'o': 1, 'w': 1}
    >>> Enter word : mellow 
    {'m': 1, 'e': 1, 'l': 2, 'o': 1, 'w': 1}
    '''

    dct = {}
    for i in word:
        if (i == " "):
            pass
        else:
            if i in dct.keys():
                dct[i]+=1
            else:
                dct[i] = 1

    print(dct)


if __name__ == '__main__':
    word = input("Enter word: ")
    unique_letters(word)
