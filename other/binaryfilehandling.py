import pickle
def addemployee():
    f= open("employee.bin","wb") #opens a binary file in your computer
    l=[]
    while True:
        eid=int(input('Enter the employee id::  '))
        name=input("Enter the name:: ")
        des=input("Enter your designation:: ")
        salary=int(input("Enter your salary:: "))
        x=[eid,name,des,salary
           ]
        l.append(x)
        op=int(input("Enter 1 to add more data:/n Enter 2 to go to main menu ::"))
        if op==2:
            break
    pickle.dump(l,f)
    f.close()
def display():
    f=open("employee.bin","rb")
    x=pickle.load(f)
    for i in x:
        if i[3]>=25000 and i[3]<=30000:
            print("em id  --name-- designation--salary")
            print(i)
    f.close()
def displayall():
    f=open("employee.bin","rb")
    x=pickle.load(f)
    for i in x:
        print("em id  --name-- designation--salary")
        print(i)
while True:
    print("_________Employee management________")
    print("++++++++++++++++++++++++++++++++++++++++++++++")
    print("Enter 'a' to add employee.")
    print("Enter 'd' to display all content")
    print("Enter 'p' to display employee with salary in between 25000 and 30000.")
    
    print("Enter 'e' to exit>")
    print("++++++++++++++++++++++++++++++++++++++++++++++")
    g=input("Enter your option::::   ")
    if g=="a":
        addemployee()
    elif g=="d":
        displayall()
    elif g=="p":
        display()
    else:
        break
    
    

        
