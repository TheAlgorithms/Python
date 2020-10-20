t = int(input())
for i in range(t):
    first = list(map(int,input().split())) # To take space separated integers input in python
    a_naive = list(map(int,input().split()))  
    a = []         
    for j in range(first[0]):
        b = []
        b.append(a_naive[j]//first[1])
        b.append(j+1)
        a.append(b)
    a = sorted(a, key=lambda x:x[0]) # To sort 2d list based on second row
    s = ''
    for j in range(first[0]):
        s = s + str(a[j][1])+' '
    print(s)
