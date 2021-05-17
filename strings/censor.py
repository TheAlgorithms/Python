txt = input("Please enter the text from which you would like to censor a certain word: \n")
word = input("Please enter the word you would like to be censored from the text: \n")
txt_lst = txt.split()
for word1 in txt_lst:
  if word1 == word:
    txt_lst[txt_lst.index(word1)] = "*" * len(word1)
txt = ""
for word1 in txt_lst:
  txt += word1 + " "
txt = txt[:-1]
print(txt)