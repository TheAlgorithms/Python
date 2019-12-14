"""
This is a pure python implementation of the Geometric Series algorithm

For doctests run following command:
python -m doctest -v Geometric_Series.py
or
python3 -m doctest -v Geometric_Series.py

For manual testing run:
python3 Geometric_Series.py
"""


def Geometric_Series(nth_term, Start_term_a, Common_ratio_r):
    """Pure implementation of Geometric Series algorithm in Python

    :param nth_term: The Last term (nth term of Geometric Series)
    :param Start_term_a : The first term of Geometric Series
    :param Common_ratio_r :  The Common Ration Between all the terms
    :return: The Geometric Series starting from First term a and multiple of common ration with first term with increase in power  till Last term (nth term)
    Examples:
    >>> Geometric_Series(4,2,2)
    [2, '4.0', '8.0', '16.0']
    >>> Geometric_Series(0,100,500)
    []
    >>> Geometric_Series(1,1,1)
    [1]
    >>> Geometric_Series(0,0,0)
    []
    """
    if nth_term == "" or Start_term_a == "" or Common_ratio_r == "":
        return ""
    Series = []
    power = 1
    multiple = Common_ratio_r
    for temp in range(int(nth_term)):
        if Series == []:
            Series.append(Start_term_a)
        else:
            power = power + 1
            cal = float(Start_term_a) * float(multiple)
            Series.append(str(cal))
            multiple = pow(float(Common_ratio_r), power)
    return Series


if __name__ == "__main__":
    nth_term = input("Enter the Last number (n term) of the Geometric Series")
    Start_term_a = input("Enter the starting term (a) of the Geometric Series")
    Common_ratio_r = input(
        "Enter the Common Ratio between two terms (r) of the Geometric Series"
    )
    print("Formula of Geometric Series => a + ar + ar^2 ... +ar^n")
    print(Geometric_Series(nth_term, Start_term_a, Common_ratio_r))
