with open("name_file.txt",'r',encoding = 'utf-8') as name_file:

# opening content.txt for read
with open("content.txt",'r',encoding = 'utf-8') as content_file:

# reading the file
body = content_file.read()

# looping the names in the name file
for names in name_file:
mails = "Hello "+name+content

# writing mails to every files
with open(names.strip()+".txt",'w',encoding = 'utf-8') as mail_file:
mail_file.write(mails)
