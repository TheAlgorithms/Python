import hashlib as hsh

phonebook = {}

def hashthat(name):
    hashvalue = hsh.md5(name.encode())
    hashed = hashvalue.hexdigest()

    return hashed

def addContact(name, num):
    h = hashthat(name)

    phonebook[h] = {}
    phonebook[h]['name'] = name
    phonebook[h]['number'] = num

    print('Successfully saved contact!')

def findContact(name):
    h = hashthat(name)

    if h in phonebook:
        print(phonebook[h])
    else:
        print('No such contact in the phone book')

def removeContact(name):
    h = hashthat(name)

    if h in phonebook:
        del phonebook[h]
        print('Successfully deleted contact')
    else:
        print('No such contact in directory')

def showBook():
    print('Name \t Contact')
    for k in phonebook:
        print(phonebook[k]['name'], '\t', phonebook[k]['number'])

run = True

while run:
    print("Options: 'add' -> Add Contact \n 'find' -> Find Contact \n 'remove' > Remove Contact \n 'show' -> print phone book \n 'exit' -> Exit Phone Book ")
    a = input('Please choose option')

    if a == 'add':
        name = input("Enter Contact Name: ")
        num = input("Enter Phone Number: ")
        addContact(name, num)
    elif a == 'find':
        name = input("Enter Contact Name: ")
        findContact(name)
    elif a == 'remove':
        name = input("Enter Contact Name: ")
        removeContact(name)
    elif a == 'show':
        showBook()
    elif a == 'exit':
        run = False
    else:
        print('Wrong input')
