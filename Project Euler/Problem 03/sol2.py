'''
Problem:
The prime factors of 13195 are 5,7,13 and 29. What is the largest prime factor of a given number N?
e.g. for 10, largest prime factor = 5. For 17, largest prime factor = 17.
'''
n=int(input())
prime=1
i=2
while(i*i<=n):
    while(n%i==0):
        prime=i
        n/=i
    i+=1
if(n>1):
    prime=n
print prime
