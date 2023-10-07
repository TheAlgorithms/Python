"""
The function below will convert hours to minutes.

>>> hours_to_minutes(2)
120

>>> hours_to_minutes(0)
0

>>> hours_to_minutes(-3)
-180

>>> hours_to_minutes(1.5)
90
"""

def hours_to_minutes(hours: float) -> float:
    """
    Convert hours to minutes.

    Parameters:
        hours (float): The number of hours to convert.

    Returns:
        float: The equivalent time in minutes.
    """
    return int(hours * 60)

if __name__ == "__main__":
    from doctest import testmod

    testmod()
    
