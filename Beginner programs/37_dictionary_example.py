from re import A


favlang={}
a=input("Enter your favourite language shubham\n")
b=input("Enter your favourite language Ankit\n")
c=input("Enter your favourite language Sonali\n")
d=input("Enter your favourite language harshita\n")

favlang['Shubham']=a
favlang['Ankit']=b                          # if two same names are in the dictionary then the latest value will considered
favlang['Sonali']=c
favlang['Harshita']=d
print(favlang)