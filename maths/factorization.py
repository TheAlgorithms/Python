from sympy import *
from sympy.solvers import solve

exp = input('Enter an expression: ')
exps = (sympify(exp))
expss = str(factor(exps))
exps2 = expss.replace("**", "^")
exps2 = exps2.replace("*", "")
print(exps2)
