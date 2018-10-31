'''
Boyer–Moore string-search algorithm is an efficient string-searching algorithm that is the standard benchmark for practical string-search literature.
references: https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm
'''
class last_index(object):
    # Generate a dictionary with the last index of each letter
    def __init__(self, pattern, alphabet):
        self.index = dict()
        for letter in alphabet:
            '''
            rfind() method is returns the last index
            str1 = 'abcdef', str2 = 'e'
            str1.rfind(str2) -> 2
            '''
            self.index[letter] = pattern.rfind(letter)
    def __call__(self, letter):
        '''
        Return last position of the specified letter inside the pattern.
        Return -1 if letter not found in pattern.
        '''
        return self.index[letter]

def boyer_moore(text, pattern):
    #Find index of pattern in text.
    alphabet = set(text)
    last = last_index(pattern, alphabet)
    m = len(pattern)
    n = len(text)
    i = m - 1  # text index
    j = m - 1  # pattern index
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            l = last(text[i])
            i = i + m - min(j, 1 + l)
            j = m - 1
    return -1

def show_result(text, pattern):
    print('Text:  %s' % text)
    p = boyer_moore(text, pattern)
    if p == -1:
        return False
    else:
        print('Match: %s%s' % ('.' * p, pattern))
        return True

if __name__ == '__main__':
    '''
    manual operation
    text = str(input())
    pattern = str(input())
    show_result(text, pattern)
    '''
     # Test 1
    text = "BAB"
    pattern = "AB"
    show_result(text, pattern)
     # Test 2
    text = "ABAABABBAAABAAB"
    pattern = "AAAB"
    show_result(text, pattern)
     # Test 3
    text = 'A simple little idea, that will change everything'
    pattern = 'will'
    show_result(text, pattern)
     # Test 4
    text = "Aimer C'est savoir dire Je t'aime sans parler"
    pattern = "sans"
    show_result(text, pattern)
