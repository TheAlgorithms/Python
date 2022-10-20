"""
this function focuses on converting camel case (eg: camelCase)
to snake case (snake_case)
-"Camel case" combines words by capitalizing all words following 
the first word and removing the space eg: userLoginCount 
This is a very popular way to combine words to form a single concept. 
It is often used as a convention in variable declaration in many languages.
-Snake case combines words by replacing each space with an underscore (_) and,
in the all caps version, all letters are capitalized eg: user_login_count 
This style, when capitalized, is often used as a convention 
in declaring constants in many languages. 
When lower cased, it is used conventionally in declaring database field names
"""


def to_snake_case(word: str) -> str:
    """
    This to_snake_case function converts camel case words (eg: camelCase)
    to snake case (eg: snake_case)

    >>> to_snake_case('helloWorld')
    'hello_world'
    >>> to_snake_case('camelCase')
    'camel_case'
    >>> to_snake_case('hacktoberFest')
    'hacktober_fest'
    >>> to_snake_case('')
    Traceback (most recent call last):
    ...
    TypeError: Provide camel case eg: helloWorld
    >>> to_snake_case('HelloWorld')
    Traceback (most recent call last):
    ...
    TypeError: Provide camel case eg: helloWorld
    >>> to_snake_case(' ')
    Traceback (most recent call last):
    ...
    TypeError: Provide camel case eg: helloWorld
    """

    # checks if the word has capital character in it,
    # and first character is not the capital.
    if word == word.lower() or word[0] == word[0].upper():
        # Raising the error if inputted data is not in the required format
        raise TypeError("Provide camel case eg: helloWorld")

    snake_case = ""
    index_list = []
    # check number of Capital letter and append their indexes in list
    for character in word:
        if character != character.lower():
            index_list.append(word.index(character))

    # append one more element
    index_list.append(100)

    # initializing few variables
    i = 0
    temp = 1

    # changing original string to lowercase
    word = word.lower()

    for index in index_list:  # iterates over list of indexes
        """
        # checks if the temp is less than length of the list
        # (temp variables checks the number of Capital letters index
        # as we don't want to add underscore at the end
        # of the return string)"""
        if temp < len(index_list):
            # adds substring to snake_case strings
            snake_case = snake_case + word[i:index] + "_"

        # if temp value more than the length of the index list
        # it executes this statement
        # as we don't want to add (_) at the end.
        elif temp >= len(index_list):
            snake_case = snake_case + word[i:]
        temp += 1
        i = index

    # Returns the string
    return snake_case

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example
    print(to_snake_case("helloWorld"))  # --> hello_world
