r"""
Description:
    Newton's second law of motion pertains to the behavior of objects for which
    all existing forces are not balanced.
    The second law states that the acceleration of an object is dependent upon
    two variables - the net force acting upon the object and the mass of the object.
    The acceleration of an object depends directly
    upon the net force acting upon the object,
    and inversely upon the mass of the object.
    As the force acting upon an object is increased,
    the acceleration of the object is increased.
    As the mass of an object is increased, the acceleration of the object is decreased.

Source: https://www.physicsclassroom.com/class/newtlaws/Lesson-3/Newton-s-Second-Law

Formulation: F_net = m • a

Diagrammatic Explanation::

              Forces are unbalanced
                        |
                        |
                        |
                        V
               There is acceleration
                        /\
                       /  \
                      /    \
                     /      \
                    /        \
                   /          \
                  /            \
    __________________      ____________________
   | The acceleration |    | The acceleration   |
   | depends directly |    | depends inversely  |
   | on the net force |    | upon the object's  |
   |                  |    | mass               |
   |__________________|    |____________________|

Units: 1 Newton = 1 kg • meters/seconds^2

How to use?

Inputs::

    ______________ _____________________ ___________
   | Name         | Units               | Type      |
   |--------------|---------------------|-----------|
   | mass         | in kgs              | float     |
   |--------------|---------------------|-----------|
   | acceleration | in meters/seconds^2 | float     |
   |______________|_____________________|___________|

Output::

    ______________ _______________________ ___________
   | Name         | Units                 | Type      |
   |--------------|-----------------------|-----------|
   | force        | in Newtons            | float     |
   |______________|_______________________|___________|

"""


def newtons_second_law_of_motion(mass: float, acceleration: float) -> float:
    """
    Calculates force from `mass` and `acceleration`

    >>> newtons_second_law_of_motion(10, 10)
    100
    >>> newtons_second_law_of_motion(2.0, 1)
    2.0
    """
    force = 0.0
    try:
        force = mass * acceleration
    except Exception:
        return -0.0
    return force


if __name__ == "__main__":
    import doctest

    # run doctest
    doctest.testmod()

    # demo
    mass = 12.5
    acceleration = 10
    force = newtons_second_law_of_motion(mass, acceleration)
    print("The force is ", force, "N")
