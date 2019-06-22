from array import array
from random import random


floats = array('d', (random() for _ in range(10**7)))
print(floats)
