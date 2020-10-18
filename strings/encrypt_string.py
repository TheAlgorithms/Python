'''
Problem statement :
Write a function that encrypts a given input with these steps:

Step 1: Reverse the input: "elppa"

Step 2: Replace all vowels using the following chart:

a => 0

e => 1

o => 2

u => 3

Step 3: Add "aca" to the end of the word

Input:  String 

Output:  String 

Sample Input: 'apple' 

Sample Output: "1lpp0aca"

'''


#My solution :
def reverse_string(s):
    s = s[::-1]
    return s
    
def replace_vowels(s):
    vowel_key = {'a':'0','e':'1','o':'2','u':'3'}
    for i in s:
        k = vowel_key.get(i,i)
        s = s.replace(i,k)
    return s

def add_ending(s):
    return s + 'aca'
    
def encrypt(input_word):
    input_word = reverse_string(input_word)
    input_word = replace_vowels(input_word)
    input_word = add_ending(input_word)
    return input_word
    
