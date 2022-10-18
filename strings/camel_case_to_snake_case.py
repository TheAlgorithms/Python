"""
this function focuses on converting camel case (eg: camelCase)
to snake case (snake_case)
"""


def to_snake_case(word: str) -> str:
    """
    This to_snake_case function convert camel case words (eg: camelCase)
    to snake case (eg: snake_case)

    >>> to_snake_case('helloWorld')
    'hello_world'
    >>> to_snake_case('camelCase')
    'camel_case'
    >>> to_snake_case('hacktoberFest')
    'hacktober_fest'
    >>> to_snake_case('')
    Traceback (most recent call last):
    Exception: Provide camel case eg: helloWorld
    >>> to_snake_case('HelloWorld')
    Traceback (most recent call last):
    Exception: Provide camel case eg: helloWorld
    >>> to_snake_case(' ')
    Traceback (most recent call last):
    Exception: Provide camel case eg: helloWorld
    """

    """
    Raising the error if inputted data is not in the required format
    """

    # checks if the word has capital character in it,
    # and first character is not the capital.
    if word != word.lower() and word[0] == word[0].lower():
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

    else:
        raise Exception("Provide camel case eg: helloWorld")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example
    # print(to_snake_case("helloWorld"))  # --> hello_world
