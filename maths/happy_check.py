"""Happy Check."""


def check_happy():
    
    #A happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit. 
    #For instance, 13 is a happy number because 1**2 + 3**2 = 10 , and 1**2 + 0**2 =1 . 
    #On the other hand, 4 is not a happy number because the sequence starting with 4**2 = 16 and 1**2 + 6**2 = 37 eventually reaches 2**2 + 0**2 = 4, the number that started the sequence, 
    #and so the process continues in an infinite cycle without ever reaching 1. A number which is not happy is called sad or unhappy. 
    
    #   >>> Enter number: 13
    #   13 is a happy number
    
    #   >>> Enter number: 45
    #   45 is a sad number
    
    #visit https://en.wikipedia.org/wiki/Happy_number for more clarification


    n=int(input('Enter number: '))
    starting_number=n
    number_cycle=[]
    while True:
        str_number=str(n)
        lst=[]
        lst[:0]= str_number
        n=sum(([int(i)**2 for i in lst]))
        
        if n==1:
            return print(f"{starting_number} is a happy number")
        elif n not in number_cycle :
            number_cycle.append(n)
        elif n in number_cycle:
            return print(f"{starting_number} is a sad number")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
