"""
Find the Percentage of two numbers

wikipdia
https://en.wikipedia.org/wiki/Percentage

>>> percent(30.0,75.0)
    40.0

"""

def percent(a: float , b: float) -> float:
    return (a / b) * 100
  
 

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)  # verbose so we can see methods missing tests

    
    print(f"Percent of these two numbers -> : {percent(30.0, 75.0) = }")
    
