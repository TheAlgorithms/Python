#Framework Declaration
def _encrypt(text):
    vowelID=['a','e','o','u']
    text=list(text)
    text.reverse()
    for w in text:
        if w in vowelID:
            text[text.index(w)]=str(vowelID.index(w))
    txt=''
    for w in text:
        txt+=w
    del text
    return txt+'aca'


#Driver Code
print(_encrypt(input('Encrypt text using Karacas algorithm :')))
