s=[]
ch='y'
while (ch=='y'):
    print("1.Push")
    print("2.Pop")
    print("3.Display")
    choice=int(input("Enter your choice:"))
    if (choice==1):
        a=input("Enter any number:")
        b=input("name")
        c=(a,b)
        s.append(c)
    elif (choice==2):
        if (s==[]):
            print("Empty stack")
        else :
            print("Deleted item is:",s.pop())
    elif choice==3:
        if s==[]:
            print("Nothing to display.")
        else:
            l=len(s)
            for i in range(l-1,-1,-1):
                print(s[i])
    else:
        print("wrong entry.")
    ch=input("Do you want to continue or not(y or n):")
    
