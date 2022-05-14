fname = 0
lname = 1
number = 2
email = 3



def printallcontacts(arraylen, array):
    print("")
    print("== YOUR CONTACT LIST ==")
    print("|")
    i1 = 0
    # print all names
    while i1 < arraylen:
        print(f"|  {array[fname][i1]} {array[lname][i1]},  {array[number][i1]}  {array[email][i1]}")
        i1 += 1
    print("=======================")



def addnewcontact(arraylen, array):
    # get a new contact
    array[fname].append(input("First Name: "))
    array[lname].append(input("Last Name: "))
    array[number].append(input("Phone Number: "))
    array[email].append(input("email ID: "))
    return array



def deleteOldContact(arraylen, array):
    rmcontact = input("input FIRST NAME of contact ('/nSTOP' to stop):  ")
    if rmcontact == '/nSTOP':
        print("stopped on user command!")
    else:
        tempvar = 0
        rmvar = 0
        for i in range(arraylen):
            if array[fname][i].upper() == rmcontact.upper():
                tempvar += 1
                rmvar = i
        # if no cotacts found
        if tempvar == 0:
            print("no cantact matches first name provided")
        # if only one contact is found
        elif tempvar == 1:
            print("DO YOU WANT TO DELETE CONTACT")
            for i in range(4):
                print(array[i][rmvar])
            tempinp = input("y/n?  ")
            if tempinp == 'y' or tempinp == 'Y':
                for i in range(4):
                    del array[i][rmvar]
                print("contact REMOVED.")
            else:
                print("failed to REMOVE contact")
        # if more than one contact is found
        else:
            print("there are more than one contact with same name")
            # TODO
        # return new array
        return array



def sorTarray(arraylen, array):
    sortcounter = 1
    while sortcounter != 0:
        # reset counter
        sortcounter = 0
        arraylen = len(array[fname])
        for i in range(arraylen - 1):
            if array[fname][i].upper() > array[fname][i + 1].upper():
                for j in range(4):
                    temp = array[j][i]
                    array[j][i] = array[j][i + 1]
                    array[j][i + 1] = temp
                # add one for changing values
                    sortcounter += 1
            if array[fname][i].upper() == array[fname][i + 1].upper():
                # if first name are same, compare last
                if array[lname][i].upper() > array[lname][i + 1].upper():
                    for j in range(4):
                        temp = array[j][i]
                        array[j][i] = array[j][i + 1]
                        array[j][i + 1] = temp
                    # add one for changing values
                    sortcounter += 1
    # if no values are swapped, sortcounter = 0; no next loop
    print("CONTACTS ARE NOW SORTED")
    return array

