import sys
def palindrome(string):
    string_rev = string[::-1]
    if string_rev == string:
        return 'Yes'
    else:
        return 'No'

n_inp = int(input()) #Numbers of case test

for item in range(n_inp):
    size = int(input()) # Size of string
    n = input() # String
    if len(n) > size:
        print("Oversized or is different.")
        sys.exit()
    print(palindrome(n))
