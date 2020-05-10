from math import sqrt,log10

"""
calculates the first fibonacci number to exceed
1000 digits using logs.
runs in constant time
"""
golden_ratio=0.5*(1+sqrt(5))


log_ratio=log10(golden_ratio)

print(int(1000/log_ratio-2))
