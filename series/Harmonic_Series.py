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
    Series=str(Series).replace("(","")
    Series=str(Series).replace(")","")
    Series=str(Series).replace("'","")
    Series=str(Series).replace(",","")
    return Series

def Harmonic_Series(n_term):
    Series= None
    for temp in range(int(n_term)):
        if(Series==None):
            Series="1"
        else:
            Series=Series,"+","1/",temp+1
            temp=temp+1
    Series=formate(Series)        
    return Series


if __name__ == "__main__":
    userInput = input("Enter the Last number (n term) of the Harmonic Series")
    print(Harmonic_Series(userInput))
