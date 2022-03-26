def decrypt(txt: str, symbol: str) -> str:
    """
    >>> decrypt("o$ne", "$")
    one
    >>> decrypt("dec@rypt", "@")
    decrypt
    >>> decrypt("p#ython cod#e", "#")
    python code

    """
    #here we split the string we need to decypher into a list
    txt_lst = txt.split()
    res_str = ""
    #we create a for loop which loops through the newly created list
    for word1 in txt_lst:
      #here we convert the current word we got through the loop into a list of charachters
      word1_lst = list(word1)
      #we loop through each charachter in the newly created list of charachters form the word we are looping throuh
      for char1 in word1_lst:
        #we set a condition, where if the symbol the loop is currently on corresponds to the symbol we need to remove, we stop on it and examine it
        if char1 == symbol:
          #we find the charachters index from the word
          indx = word1.index(char1)
          #we remove the list (the list which contains every element and characahter from the word we are looping throuh) element with the same index from the list.
          word1_lst[indx] = ""
      res_wrd = ""
      #we loop throuh the list containing all the charachters from the word, and append those charachters to a new string
      for char1 in word1_lst:
        res_wrd += char1
      #here we add the newly created, decyphered word to a new string which will contain our full result
      res_str += res_wrd + " "
    res_str = res_str[:-1]
    #and here we print out the final result
    print(res_str)

if __name__ == "__main__":
  import doctest
  doctest.testmod()