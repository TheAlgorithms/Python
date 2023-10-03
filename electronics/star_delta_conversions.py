# https://www.electrical4u.com/delta-star-transformation-star-delta-transformation/#:~:text=The%20relation%20of%20delta%20%E2%80%93%20star,of%20the%20delta%20connected%20resistances.
# https://en.wikipedia.org/wiki/Y-%CE%94_transform

def star_to_delta(
    resistor_a: float, resistor_b: float, resistor_c: float,
)->list[float]:
     

     """

     Convert's star resistor arrangment to delta 
     
     >>> star_to_delta(5,7.5,3.0)
     [15.0, 10.0, 25.0]
     >>> star_to_delta(5,75,12)
     [267.0, 17.8, 111.25]
     >>> star_to_delta(-5,75,12)
     Traceback (most recent call last):
       ...
     ValueError: resistance value is zero or negative
     """
     
     
     if (
        resistor_a    <= 0
        or resistor_b <= 0
        or resistor_c <= 0
    ):
        raise ValueError("resistance value is zero or negative")
     
     delta_arrangment = []
     resistance_chain = resistor_a * resistor_b + resistor_b * resistor_c + resistor_c * resistor_a
     delta_arrangment.append(resistance_chain / resistor_a)
     delta_arrangment.append(resistance_chain / resistor_b)
     delta_arrangment.append(resistance_chain / resistor_c)

     return delta_arrangment



def delta_to_star(
    resistor_a: float, resistor_b: float, resistor_c: float,
)->list[float]:


    """

    Convert's delta resistor arrangment to star
    
    Exaples:
    >>> delta_to_star(10,25,15)
    [5.0, 7.5, 3.0]
    >>> delta_to_star(6,6,6)
    [2.0, 2.0, 2.0]
    >>> delta_to_star(-6,5,6)
    Traceback (most recent call last):
       ...
    ValueError: resistance value is zero or negative
    """

    if (
        resistor_a    <= 0
        or resistor_b <= 0
        or resistor_c <= 0
    ):
        raise ValueError("resistance value is zero or negative")

    star_arrangment = []
    resistance_sum  = resistor_a + resistor_b + resistor_c
    star_arrangment.append( ( resistor_a * resistor_b ) / resistance_sum )
    star_arrangment.append( ( resistor_b * resistor_c ) / resistance_sum )
    star_arrangment.append( ( resistor_c * resistor_a ) / resistance_sum )

    return star_arrangment


if __name__ == "__main__":
    import doctest

    doctest.testmod()