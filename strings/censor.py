def censor(txt, word):
  txt_lst = txt.split()
  #here we loop through a list which consists of words from the text we should censor
  for word1 in txt_lst:
    if word1 == word:
      txt_lst[txt_lst.index(word1)] = "*" * len(word1)
  txt = ""
  #here we combine all of the split words in txt_lst into one string
  for word1 in txt_lst:
    txt += word1 + " "
  txt = txt[:-1]
  print(txt)

censor("one two three", "one")