def odd_or_even(n: int) -> str:
    """
    whether a given number is odd or even using bitwise AND
    
    >>> odd_or_even(1)
    Odd
    >>> sum_of_digits(14)
    Even
    """
    if(n & 1 == 0):
        return "Odd"
    else:
        return "Even"


if(__name__=='__main__'):
    num=11
    print(num, " is ", odd_or_even(num))
