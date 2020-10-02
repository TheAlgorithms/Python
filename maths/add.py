"""
Addition of n numbers.
"""


def add(*a):
    a=[*a]
    try:
        total=sum(a)
        print('Sum is  ' + str(total))
    except:
        print('Addition valid for only numbers')

add(2,3) # output is 5
add(5,3,2,1) # output is 11
add(23,45,56,76,43,21) #output is 264.
