import random
s="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$&*"
def password():
    char=int(input("Enter the password character:"))
    pas="".join(random.sample(s,char))
    print(pas)


    ans=str(input("Enter if this password is okay :"))
    if ans=="yes":
        print("Your Password is :",pas)
    else:
        password()


password()