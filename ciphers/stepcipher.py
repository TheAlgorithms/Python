name=str()
def inputstep():
    global name
    name=input("Enter the code")
    n=int(input("Enter the step value: "))
    return(n)
def encrypt(t):
    global name
    global step
    l=list(name)
    for i in range(len(l)):
        l[i]=chr(ord(l[i])+step)
    print(*l) 


step=inputstep()
encrypt(step)

