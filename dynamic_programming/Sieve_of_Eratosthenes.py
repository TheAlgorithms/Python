def primeNos(n):

    check = [False for i in range(n+1)]

    for i in range(2,n+1):
        x= 2
        while(x*i < n+1):
            check[x*i]=True
            x += 1

    for i in range(2,n+1):
        if(check[i]==False):
            print(i)    

if __name__ == '__main__':
    a = int(input("Prime numbers smaller than or equal to "))
    primeNos(a)
