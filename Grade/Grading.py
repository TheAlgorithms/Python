a = int(input())
b = int(input())
c = int(input())
Grade = (a + b + c)

if Grade >= 80:
    print ("A")
elif Grade >= 75:
    print("B+")
elif Grade >= 70:
    print("B")
elif Grade >= 65:
    print("C+")
elif Grade >= 60:
    print("C")
elif Grade >= 55:
    print("D+")
elif Grade >= 50:
    print("D")
else:
    print("F")
