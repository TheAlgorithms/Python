def pattern(x):
    a=1
    i=1
    for index in range(x):
        for number in range(a):
            print(int(i))
            i = i+1
        a = a+1
        print("\n")

p = int(input("Enter the number of rows in pattern: "))
pattern(p)
