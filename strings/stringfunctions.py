''' These are the implementations of the basic string functions in python, 
like isupper(), islower() and so on'''


#function to check whether the string is in uppercase
def is_upper(string):
    if not string: 
        return False
    for character in string:
        if ord(character) > 96 and ord(character) < 123: 
            return False
    return True

#function to check whether the string is in lowercase
def is_lower(string):
    for character in string:
        if ord(character) in range(65, 97):
            return False
    return True


#function to check whether all characters in a string are alphabetical
def is_alpha(string):
    if(not string): 
        return False
    for character in string:
        if ((ord(character) in range(65, 91)) or (ord(character) in range(97, 123))):
            continue
        else:
            return False
    return True

#function to check for only alphanumeric characters
def is_alnum(string):
    if(not string): return False
    for character in string:
        if ((ord(character) in range(65, 91)) or (ord(character) in range(97, 123)) or (ord(character) in range(48, 58))):
            continue
        else:
            return False
    return True

#function to check for digits only
def is_decimal(string):
    if(not string): return False
    for character in string:
        if(ord(character) not in range(48, 58)):
            return False 
    return True

#function to check for spaces, tabs and newlines
def is_space(string):
    if(not string): return False
    for character in string:
        if(character !=' '):        #solve for newline pending
            return False
    return True

#function to check whether first letter of each word is capital
def is_title(s):
    for substring in s.split():
        if(ord(substring[0]) not in range(65, 91)):
            return False
        for character in range(1, len(substring)):
            if(is_upper(substring[character])): 
                return False
    return True

print(is_upper("HEY"))                          # True
print(is_lower("there"))                        # True
print(is_alpha("you"))                          # True
print(is_alnum("are3"))                         # True
print(is_decimal("400"))                        # True
print(is_space("   "))                          # True
print(is_title("Times Pretty"))                 # True
            