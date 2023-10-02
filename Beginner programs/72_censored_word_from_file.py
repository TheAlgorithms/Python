# this program is for censored some bad words from a file like in this program we have censored the donkey work with special symbols
with open("sample.txt") as f:
    content =f.read()

content = content.replace("donkey", "$%^@$^#")

with open("sample.txt","w") as f:
    f.write(content)