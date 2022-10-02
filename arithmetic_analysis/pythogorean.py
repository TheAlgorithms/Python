"""
Description: triplet(n) function displays all the possible pythagorean triplets where one of the number is n

>>> triplet(5)
5 12 13
3 4 5
Count:  2
>>> triplet(17)
17 144 145
8 15 17
Count:  2
>>> triplet(35)
35 84 91
35 120 125
12 35 37
35 612 613
21 28 35
Count:  5
>>> triplet(31)
31 480 481
Count:  1
>>> triplet(30)
30 40 50
30 224 226
16 30 34
30 72 78
18 24 30
Count:  5
>>>

"""

def triplet(n):
    ans = set()
    for i in range(1,int(n)+1):                              # triplets where a^2 + n^2 = b^2
        if (n*n)%i == 0:
            c = i
            d = (n*n)//i
            a = (c+d)/2
            b = (d-c)/2
            if a%1 == 0 and b%1 == 0 and a>0 and b>0:
                ans.add(tuple(sorted([a,b,n])))

                
    for a in range(1 , n+1):                                # triplets where a^2 + b^2 = n^2
        b = (n**2 - a**2)**0.5
        if b%1 == 0 and b>0:
            ans.add(tuple(sorted([a,b,n])))
    c = 0
    for (x,y,z) in ans:
        print(int(x) , int(y)  , int(z))
        c += 1
    print("Count: ",c)