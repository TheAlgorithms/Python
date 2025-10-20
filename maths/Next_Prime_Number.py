"""
In the ancient city of Numeria, legends speak of an oracle whose whispers could bend the very fabric of mathematics. 
Travelers from distant lands would bring her a number, and in return, she would reveal its future: the very next prime number.
Your task is to embody the oracle's wisdom. You will be given a number.
You must find the smallest prime number that is strictly greater than it.
"""
def check_prime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    temp=5
    while temp*temp<=n:
        if n%temp==0 or n%(temp+2)==0:
            return False
        temp+=6
    return True
n=int(input())
next_prime=n+1
while not check_prime(next_prime):
  next_prime+=1
print(next_prime)
