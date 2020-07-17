#!/usr/bin/env python3
"""
This is a pure Python implementation of the Arithmetico–Geometric Sequence algorithm
https://en.wikipedia.org/wiki/Arithmetico%E2%80%93geometric_sequence
For doctests run following command:
python -m doctest -v arithmetico_geometric_sequence.py
or
python3 -m doctest -v arithmetico_geometric_sequence.py
For manual testing run:
python3 arithmetico_geometric_sequence.py
"""
class AGS:
    def __init__(self, a, d, b, r, n):
        self.a = a
        self.d = d
        self.b = b
        self.r = r
        self.n = n
    """Pure Python implementation of Arithmetico–Geometric Sequence algorithm
    :params a: Initial Value For Arithmetic Progression
            d: Difference For Arithmetic Progression
            b: Initial Value For Geometric Progression
            r: Common Ratio For Geometric Progression
            n: Number Of Terms
            k: Value Of K In K-th Term
    Examples:
    Enter Initial Value For A.P. : 2
    Enter Difference For A.P. : 3
    Enter Initial Value For G.P. : 4
    Enter Common Ratio For G.P. : 0.5
    Enter Number Of Terms : 5
    Full Series : 
    ['2.0 x 4.0', '(2.0 + 3.0) x 4.0x0.5^1', 
    '(2.0 + 6.0) x 4.0x0.5^2', '(2.0 + 9.0) x 4.0x0.5^3', 
    '(2.0 + 12.0) x 4.0x0.5^4']
    Value Of Last Term : 3.50
    Sum Of Your A.G.S. : 35.00
    Infinite Series Sum : 40.00
    Value Of Which Term You Want : 2
    Value Of 2-th Term : 10.00
    """
    def full_series(self):
        series = []
        for i in range(n):
            if i==0:
                series.append(str(a) + " x " + str(b))
            else:
                ap_part = str(a) + " + " + str(i * d)
                gp_part = str(b) + "x" + str(r) + "^" + str(i)
                series.append("(" + ap_part + ")" + " x " + gp_part)
        return series
    def last_term_value(self):
        return (a + (n - 1) * d) * (b * pow(r, n-1))
    def sum(self):
        return ((a * b)-((a + (n * d)) * (b * pow(r, n)))) / (1-r) + (d * b * r * (1 - pow(r, n)))/pow((1 - r), 2)
    def inf_sum(self):
        return (a * b) / (1 - r) + (d * b * r) / pow((1 - r), 2)
    def nth_term_value(self, k):
        return (a + (k - 1) * d) * (b * pow(r, k - 1))
if __name__=="__main__":
    run = True
    while run:
        try:
            a = float(input("\nEnter Initial Value For A.P. : "))
            run = False
        except ValueError:
            print("Please Give A Number For Corresponding Input!")
    run = True
    while run:
        try:
            d = float(input("Enter Difference For A.P. : "))
            run = False
        except ValueError:
            print("Please Give A Number For Corresponding Input!")
    run = True
    while run:
        try:
            b = float(input("Enter Initial Value For G.P. : "))
            run = False
        except ValueError:
                print("Please Give A Number For Corresponding Input!")
    run = True
    while run:
        try:
            r = float(input("Enter Common Ratio For G.P. : "))
            run = False
        except ValueError:
            print("Please Give A Number For Corresponding Input!")
    not_get_n = True
    while not_get_n:
        try:
            n = float(input("Enter Number Of Terms : "))
            if n == int(n):
                n=int(n)
                not_get_n = False
            else:
                print("Please Give An Integer For Corresponding Input!")
        except ValueError:
            print("Please Give An Integer As The Number Of Terms!")
    ags = AGS(a, d, b, r, n)
    print("\nFull Series : \n{}".format(ags.full_series()))
    print("\nValue Of Last Term : {:.2f}".format(ags.last_term_value()))
    print("Sum Of Your A.G.S. : {:.2f}".format(ags.sum()))
    print("Infinite Series Sum : {:.2f}".format(ags.inf_sum()))
    not_get_k = True
    while not_get_k:
        try:
            k = float(input("\nValue Of Which Term You Want : "))
            if k == int(k):
                if k<=n:
                    k=int(k)
                    not_get_k = False
                else:
                    print("Please Give An Integer Less Than Or Equal To The Numbet Of Terms!")
            else:
                print("Please Give An Integer For Corresponding Input!")
        except ValueError:
            print("Please Give An Integer For Corresponding Input!")
    print("Value Of {}-th Term : {:.2f}".format(k, ags.nth_term_value(k)))
