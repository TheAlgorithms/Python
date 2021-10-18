def unjumble(word: str) -> None:        # Function to show possible unjumbled words

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
        str.append(i)       # converts the entered word into a list

    str.sort()      # sorting the list in ascending order
    f = open("words.txt","r")       # accessing the txt file containing all the dictionary words


    for line in f:
        i = line        # getting each word from the txt file 
        for x in i:         
            str2.append(x)      # Converting each word from the txt file and storing it in another list   


        str2.pop()      # removing the '\n' character from the list for every word from the file
        str2.sort()     # sorting the second list in ascending order as well

        # making both lists sorted enables quick comparision between both of them

        if str == str2:     # checking if the list from the original input jumbled word matched with the list from the txt file
            res.append(line)    # if it matches, Then adding the particular word to result list

        str2=[]



    print(res)      # printing the resultant list containing all the possible outcomes for the input word
  
if __name__ == '__main__':
    import doctest
    import typing
    word = input("Enter the jumbled word : ")       # Asking user to enter the jubled word
    word = word.lower()     # Converting the input word to lower case
    doctest.testmod(name ='unjumble', verbose = True)