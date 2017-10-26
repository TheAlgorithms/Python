'''
Problem:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers which is less than N.
'''
n=int(input())
for i in range(n-1,10000,-1):
    temp=str(i)
    if(temp==temp[::-1]):
        j=999
        while(j!=99):
            if((i%j==0) and (len(str(i/j))==3)):
                print i
                exit(0)
            j-=1
