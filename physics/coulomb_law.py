"""
Description : The law states that the magnitude of the electrostatic force of attraction or repulsion between two point charges is directly proportional 
to the product of the magnitudes of charges and inversely proportional to the square of the distance between them.
Coulomb studied the repulsive force between bodies having electrical charges of the same sign.

The unit of Electrostatic force is Newton.

Coulomb’s Law gives an idea about the force between two point charges. 
By the word point charge, we mean that in physics, the size of linear charged bodies is very small as against the distance between them. 
Therefore, we consider them as point charges as it becomes easy for us to calculate the force of attraction/ repulsion between them.

Charles-Augustin de Coulomb, a French physicist in 1784, measured the force between two point charges and he came up with 
the theory that the force is inversely proportional to the square of the distance between the charges. 
He also found that this force is directly proportional to the product of charges (magnitudes only).

We can show it with the following explanation. Let’s say that there are two charges q1 and q2. 
The distance between the charges is ‘r’, and the force of attraction/repulsion between them is ‘F’. Then

F  ∝ q1q2

Or, F  ∝  1/r^2

F  = k*q1*q2/ r^2

where k is proportionality constant and equals to 1/4πε0. 

Here, ε0 is the epsilon naught and it signifies permittivity of a vacuum. The value of k comes 9 × 10^9 Nm^2/ C^2 
when we take the S.I unit of value of ε0 is 8.854 × 10^-12 C^2 N^-1 m^-2.

The unit of Electrostatic force is newton.Mathematically it is written as:
F = (k*q1*q2)/(r**2)

Where, F is the Electrostatic force,q1 q2 are the intensity of two charges respecticvely ,
r is the radius and k is coulombs constant and its value is 9×10^9 N⋅m^2⋅C^−2 .

https://www.toppr.com/guides/physics/electric-charges-and-fields/coulombs-law/
"""

def coulombs_law(q1: float, q2: float, radius: float) -> float:
    """
    The Electrostatic Force formula is given as: (k*q1*q2)/(r**2)
    >>> round(coulombs_law(15.5,20,15),2)
    12400000000.0
    >>> round(coulombs_law(1,15,5),2)
    5400000000.0
    >>> round(coulombs_law(20,-50,15),2)
    -40000000000.0
    >>> round(coulombs_law(-5,-8,10),2)
    3600000000.0
    >>> round(coulombs_law(50,100,50),2)
    18000000000.0
    """
    
    if radius <= 0:
        raise ValueError("The radius is always a positive non zero integer")
    return ((9*10**9)*q1*q2) /(radius**2)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
