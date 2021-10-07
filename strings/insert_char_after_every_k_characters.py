def insert_character_after_every_k_elements(input_string, k, character_to_insert):
    """
    Add charater after every k characters in given string
    >>> insertCharacterAfterEveryKelements("abcdef",2,'*')
    ['*abcdef', 'ab*cdef', 'abcd*ef']
    >>> insertCharacterAfterEveryKelements("abcdef",2,'*')
    ['*abcdef', 'abcd*ef']
    """
    result = []
    for i in range(0, len(input_string), k):
        result.append(input_string[:i] + character_to_insert + input_string[i:])
    return str(result)


input_string = input('Enter the string ')
k = int(input('Enter after which K element want to enter the string '))
"""
    k defines after which character we want to insert the given character in the string
"""
character_to_insert = input('Enter the character to insert in the string ')

result = insert_character_after_every_k_elements(input_string, k, character_to_insert)
print('Resulted string is',result)