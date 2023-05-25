#Wikipedia link for understanding of Interests
# https://en.wikipedia.org/wiki/Interest


def simple_interest(p,t,r):
    print('The given principal amount is', p)
    print('The given time period is', t)
    print('The given rate of interest is',r)
     
    si = (p * t * r)/100
     
    print('The Simple Interest is', si)
    return si
