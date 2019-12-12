"""
This is a pure python implementation of the Harmonic Series algorithm

For doctests run following command:
python -m doctest -v Harmonic_Series.py
or
python3 -m doctest -v Harmonic_Series.py

For manual testing run:
python3 Harmonic_Series.py
"""

def formate(Series):
    """
    Removing unnecessary chars to make string formated

    :param Series: Unformated string passed by Harmonic_Series function
    :return: Formated Harmonic Series

    Example:
    >>> formate("(('1', '+', '1/', 2), '+', '1/', 3)")
    1 + 1/2 + 1/3 + 1/4
    """
    Series=str(Series).replace("(","")
    Series=str(Series).replace(")","")
    Series=str(Series).replace("'","")
    Series=str(Series).replace(",","")
    return Series

def Harmonic_Series(n_term):
    """Pure implementation of Harmonic Series algorithm in Python

    :param Series: The Last term (nth term of Harmonic Series)
    :return: The Harmonic Series starting from 1 to Last term (nth term)

    Examples:
    >>> Harmonic_Series(4)
    1 + 1/2 + 1/3 + 1/4

    >>> Harmonic_Series()
    ""

    >>> Harmonic_Series(0)
    None

    >>> Harmonic_Series(1)
    1
    """
    if(n_term==""):
        return n_term
    Series= None
    for temp in range(int(n_term)):
        if(Series==None):
            Series="1"
        else:
            Series=Series," + ","1/",temp+1
            temp=temp+1
    Series=formate(Series)        
    return Series


if __name__ == "__main__":
    userInput = input("Enter the Last number (n term) of the Harmonic Series")
    print("Formula of Harmonic Series => 1+1/2+1/3 ..... 1/n")
    print(Harmonic_Series(userInput))
