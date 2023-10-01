'''
ELECTRIC FILED AROUND A RING:-(Ignore the text below for lazy heads:) )

An electric field around any charge distribution can be found by creating an element out of infinitesimal point charges. 
In the case of a uniformly charged ring, the electric field on the axis of a ring, which is uniformly charged, can be found by superimposing the electric fields of an infinitesimal number of charged points. 
The ring is then treated as an element to derive the electric field of a uniformly charged disc.

source :- https://www.vedantu.com/jee-main/physics-electric-field-due-to-a-uniformly-charged-ring
'''



#VARIABLES TO CONSIDER (always a good pratice).

"""
@ A uniformly charged ring = Q
@ Strength of maximum electric field = E
@ The radius of the ring = R or A(whatever you like to declare)

@ Distance of the point from the centre of the ring at which the electric field is maximum = X

@ The permiability of free space = K= 
@ THUS EQUATION BECOMES -
 E = K * Q * X / (X**2 + A**2)**3/2 (Phew.. half are dead by now , That's why i'm here to help)
"""




# Now the final value of ELectric field
#E = K * Q * X / (X**2 + R**2)**3/2

def EF_onring(Q:float,X:float,R:float) ->float:
    """
    Calculate the electrostatic force of attraction or repulsion
    between two point charges

    >>> EF_onring(15.5, 20, 15)
    5706
    >>> EF_onring(1, 15, 5)
    4314
    >>> EF_onring(20, -50, 15)
    -222
    >>> EF_onring(-5, -8, 10)
    40751
    >>> EF_onring(50, 100, 50)
    12
    """
    return round((8.9875517923 * 10**9) * Q * X / (X**2 + R**2)**3/2)




if __name__ == "__main__":
    import doctest

    doctest.testmod()
