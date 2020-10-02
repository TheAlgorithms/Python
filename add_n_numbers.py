  
"""
Addition of N numbers in Python.
"""


def add_n(*numbers):
    """
    >>> add(2, 2)
    4
    >>> add(2, 3,4,5)
    14
    """
    numbers_list=[*numbers]
    try:
        value=sum(numbers_list)
        print('Sum is  '+ str(value))
    except :
        print('ValueError')
  
if __name__ == "__main__":
    add_n(1,2,3,6,7) # Output is 19

    add_n(5,6,7) #Output is 18

    add_n(80+70+3+3+5+5+12) # output is 178


    
