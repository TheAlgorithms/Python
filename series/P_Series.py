"""
This is a pure python implementation of the P-Series algorithm

For doctests run following command:
python -m doctest -v P-Series.py
or
python3 -m doctest -v P-Series.py

For manual testing run:
python3 P-Series.py
"""


def P_Series(userInput_N, userInput_P):
    """Pure implementation of P-Series algorithm in Python

    :param Series: The Last term (nth term of P-Series)
    :return: The P-Series starting from 1 to Last term (nth term)

    Examples:
    >>> P_Series(5,2)
    [1, '1/4', '1/9', '1/16', '1/25']

    >>> P_Series(0,0)
    []

    >>> P_Series(1,1)
    [1]
    """
    if userInput_N == "":
        return userInput_N
    Series = []
    for temp in range(int(userInput_N)):
        if Series == []:
            Series.append(temp + 1)

        else:
            tmp = "1/" + str(pow(int(temp + 1), int(userInput_P)))
            Series.append(tmp)
            temp = temp + 1
    return Series


if __name__ == "__main__":
    userInput_N = input("Enter the Last number (n term) of the P-Series")
    userInput_P = input("Enter the Power for  P-Series")
    print("Formula of P-Series => 1+1/2^p+1/3^p ..... 1/n^p")
    print(P_Series(userInput_N, userInput_P))
