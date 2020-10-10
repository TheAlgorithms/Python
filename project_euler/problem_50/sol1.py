


#fills the primes dict with prime numbers <=u 
#        primes: Global Dictionary To fill     
#       l: (optional) Starting value    
def prma(u:int,primes:dict, l:int=2)->None:
    """
    >>> primes = {}
    >>> prma(10,primes)
    >>> primes
    {2: 1, 3: 3, 5: 3, 7: 4}
    """
    
    if len(primes) <= 1:
        primes[2] = 1
        primes[3] = 2
    
    psrt = 2
    while l <= u:                               # while the number (l) is less than(or equal to ) the given
    
        if l > psrt**2:                         # if l exceeds the previous val of psrt

            psrt = (l**0.5)                     # psrt = sqrt(l)

        for i in primes:                          #for the primes currently in primes

            if i > psrt:                        # You need to only check till the sqrt(l) to see if it is a prime..
                primes[l] = len(primes)+1                 #if it exceeds the value then it must be prime..
                break

            if l % i == 0:                      # if it is divisible.. it jumps to the next number for l i.e: l++
                break
        l += 1




def solution(MX:int = 1000000)->int:
    """
    >>> solution()
    997651
    >>> solution(1000)  #lessthan 1000
    953
    """
    primes= {}      # using a dict To maintain order and o(1) searching..
    prma(MX,primes)    #fill dict with primes < MX
    primes_tuple = tuple(primes) 
    running_sum = 0
    count=0
    while running_sum<MX:
        running_sum+=primes_tuple[count]
        count+=1
    count-=1                    #deleting off the last prime..
    running_sum-=primes_tuple[count] 



    #counting from left 
    si = 0
    ei = count-1
    running_sum1 = running_sum
    while not running_sum1 in primes and ei>=0:
        running_sum1-=primes_tuple[ei]
        ei-=1
    countL = ei-si+1
    # print(countL,running_sum1,primes_tuple[0:ei])    #debug



    # counting from right
    ei = count-1
    running_sum2 = running_sum
    while not running_sum2 in primes and si<=ei:
        running_sum2-=primes_tuple[si]
        si+=1
    countR = ei-si+1
    # print(countR,running_sum2,primes_tuple[0:count]) #debug

    return running_sum1 if countL>countR else running_sum2

if __name__ == "__main__":
    print(solution())

