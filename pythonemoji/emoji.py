import emoji
l = ['😃' ,'😄' ,'😅', '😆', '😉', '😊', '😋', '😎', '😍', '😘']
a=[]
for i in l:
       x = (emoji.demojize(i))
       a.append(x)

a.sort()
print(a)
