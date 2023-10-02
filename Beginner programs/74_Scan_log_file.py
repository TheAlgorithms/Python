# this program is for mine a log file whether it contains python string in it. 
with open("log.txt") as f:# this two method is for searching that string into both lower case or upper case
    content =f.read()     #  content =f.read().lower() 

if 'Python' in content.lower():     # if 'Python' in content.lower():
    print("Yes Python is present")
else:
    print("no Python is present")

