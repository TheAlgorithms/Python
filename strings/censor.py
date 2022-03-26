def censor(txt: str, word: str) -> str:
    """
    >>> censor("one two three", "one")
    *** two three
    >>> censor("email, password", "password")
    email, ********
    >>> censor("pin: 2536", "2536")
    pin: ****

    """

    txt_lst = txt.split()
    #here we loop through a list which consists of words from the text we should censor
    for index, word1 in enumerate(txt_lst):
      if word1 == word:
        txt_lst[index] = "*" * len(word1)
    txt = ""
    #here we combine all of the split words in txt_lst into one string
    for word1 in txt_lst:
      txt += word1 + " "
    txt = txt[:-1]
    return txt
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()