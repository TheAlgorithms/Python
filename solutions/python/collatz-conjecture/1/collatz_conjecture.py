def steps(number):
    #determines the Collatz Conjecture
    if number<1 :
        raise ValueError("Only positive integers are allowed")
    counter=0
    while number!=1:
        if number%2==0:
            number/=2
        else:
            number = number*3 +1
        counter+=1
    return counter
