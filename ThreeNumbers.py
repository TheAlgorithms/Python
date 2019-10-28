print('"Enter Three Numbers"')
n1=int(input())
n2=int(input())
n3=int(input())
if (n1==n2 and n2==n3):
    print("The Numbers are same")
elif(n1>n2 and n1>n3):
    print("The Largest Of the Numbers is")
    print(n1)
elif(n2>n3):
    print("The Largest Of the Numbers is")
    print(n2)
else:
    print("The Largest Of the Numbers is")
    print(n3)

