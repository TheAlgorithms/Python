"""
Pythagoras Triplet Generator

Input: n = 5
Output: 5 12 13

Input: n = 123456789
Output: 123456789 7620789375095260 7620789375095261

I've written this algorithm myself so can't really find an article but this guy explains it really well-
https://www.youtube.com/watch?v=n6vL2KiWrD4

"""

def pythagoras_generator(n):
    """
    It gives you the pythagoras triplet of the given number
    It works literally on every number greater than 2
    
    >>> pythagoras_generator(10):
    10 24 26
    >>> pythagoras_generator(21):
    21 220 221
    """
    
    if n % 2 == 0:
        n = n // 2
        return 2*n, (n**2-1), (n**2+1)
    else:
        return n, (n**2-1)//2, (n**2+1)//2
      
n = int(input())

triplet = pythagoras_generator(n)

a, b, c = triplet

print(a, b, c)
