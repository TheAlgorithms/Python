''' these="              Yash ia a good boy                "
print(these)
print(these.strip()) '''

# second method
# this below code is for remove the word and split the string and strip also
def remove_and_split(string, word):
    newstr=string.replace(word, "")
    return newstr.strip()

these="              Yash ia a good                "
n=remove_and_split(these, "Yash")
print(n)    