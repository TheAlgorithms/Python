from __future__ import annotations
import math 

from typing import NamedTuple


class Result(NamedTuple):
    root_type: str
    root1: str
    root2: str


def equationroots(a: float, b: float, c: float) ->tuple:
    """
    This function calculate the roots of the quadratic equation.
    a = coefficient of x^2
    b = coefficient of x
    c = constant
    >>> equationroots(a=1,b=-6,c=8)
    Result(root_type='Real and different roots.', root1=4.0, root2=2.0)
    >>> equationroots(a=1,b=-4,c=4)
    Result(root_type='Real and same root.', root1=2.0, root2=2.0)
    >>> equationroots(a=1 ,b= 1,c=1)
    Result(root_type='Complex roots.', root1='-0.5 + i(1.7320508075688772)', root2='-0.5 - i(1.7320508075688772)')
    >>> equationroots(a=0,b=1,c=2)
    Traceback (most recent call last):
        ...
    ValueError: Invalid quadratic equation. 
    """
    if a==0:
        raise ValueError("Invalid quadratic equation.") 
 
    # calculating discriminant using formula
    dis = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis)) 
     
    # checking condition for discriminant
    if dis > 0: 
        return Result("Real and different roots.", ((-b + sqrt_val)/(2 * a)), ((-b - sqrt_val)/(2 * a))) 
     
    elif dis == 0: 
        return Result("Real and same root.", (-b / (2 * a)),(-b / (2 * a))) 
     
    # when discriminant is less than 0
    else:
        return Result("Complex roots.", (str(- b / (2 * a))+' + i('+str(sqrt_val)+')'), (str(- b / (2 * a))+' - i('+str(sqrt_val)+')')) 





if __name__ == "__main__":
    import doctest

    doctest.testmod()
