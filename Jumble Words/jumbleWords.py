def unjumble(word: str) -> None:

    r"""
    This function converts given input jumbled word into its lowercase equivalent, sorts it, and
    then cross verifies with the same using each word from the file "words.txt", following which,
    it returns a list of possible correct outcomes.

    Define input and expected output:
    >>> unjumble('pplea')
    ['appel\n', 'apple\n', 'pepla\n']
    >>> unjumble('roltonc')
    ['control\n']
    """

    str = []
    str2 = []
    res = []

    for i in word:
        str.append(i)

    str.sort()
    f = open("words.txt","r")


    for line in f:
        i = line
        for x in i:
            str2.append(x)


        str2.pop()
        str2.sort()
        if str == str2:
            res.append(line)
        str2=[]



    print(res)
  
if __name__ == '__main__':
    import doctest
    import typing
    word = input("Enter the jumbled word : ") # type: str
    word = word.lower()
    doctest.testmod(name ='unjumble', verbose = True)