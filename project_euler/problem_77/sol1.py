'''

Problem 77

Link - https://projecteuler.net/problem=77

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?



'''

def solution(m):
    
    m = int(m)

    max_number = 1000

    combinations = [0]*(max_number+1)

    combinations[0] = 1

    primes =[]

    for i in range(2,max_number+2):
        is_prime = True
    
        for p in primes:
            if p * p > i:
                break
            if i%p==0:
                is_prime = False
                break
    
        if is_prime == True:
            primes.append(i)
        
            for pos in range(max_number-i+1):
                combinations[pos+i]+=combinations[pos]
    
    
    for i in range(max_number+2):
        if combinations[i] >= m:
            return(str(i))
    

if __name__ == "__main__":
    num = input(("Enter a number from 1-48278613741845757   : "))
    ans = solution(int(num))
    print("The first value which can be written as the sum of primes in over",num,"different ways is",ans)
  
 '''
By - https://github.com/aditya113141

 '''   