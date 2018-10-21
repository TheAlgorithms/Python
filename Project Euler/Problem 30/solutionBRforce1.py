def getN():
    for k in range(300000):
        i=0
        a=[int(j) for j in list(str(k))]
        for x in a:
                i+=x**5
        if k==i:
                print(k,a)
#this function prints all possible numbers, up> to 300000.
