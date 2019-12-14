"""
This is a pure python implementation of the Harmonic Series algorithm

For doctests run following command:
python -m doctest -v Harmonic_Series.py
or
python3 -m doctest -v Harmonic_Series.py

For manual testing run:
python3 Harmonic_Series.py
"""


def Harmonic_Series(n_term):
    """Pure implementation of Harmonic Series algorithm in Python

    :param Series: The Last term (nth term of Harmonic Series)
    :return: The Harmonic Series starting from 1 to Last term (nth term)

    Examples:
    >>> Harmonic_Series(5)
    ['1', '1/2', '1/3', '1/4', '1/5']

    >>> Harmonic_Series(0)
    []

    >>> Harmonic_Series(1)
    ['1']
    """
    if n_term == "":
        return n_term
    Series = []
    for temp in range(int(n_term)):
        if Series == []:
            Series.append("1")
        else:
            tmp = "1/" + str(temp + 1)
            Series.append(tmp)
            temp = temp + 1
    return Series


if __name__ == "__main__":
    userInput = input("Enter the Last number (n term) of the Harmonic Series")
    print("Formula of Harmonic Series => 1+1/2+1/3 ..... 1/n")
    print(Harmonic_Series(userInput))
