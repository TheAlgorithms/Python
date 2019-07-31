#https://projecteuler.net/problem=10
#using Sieve_of_Eratosthenes

def prime_sum(n):
    l=[0 for i in range(n+1)]

    l[0]=1
    l[1]=1
    for i in range(2,int(n**0.5)+1):
        if l[i]==0:
            for j in range(i * i, n+1, i):
                    l[j]=1
    s=0
    for i in range(n):
        if l[i] == 0:
            s+=i
    print(s)

if __name__ == '__main__':
    prime_sum(2000000)
