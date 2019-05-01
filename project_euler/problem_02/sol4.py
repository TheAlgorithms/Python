import math
from decimal import *

getcontext().prec = 100
phi = (Decimal(5) ** Decimal(0.5) + 1) / Decimal(2)

n = Decimal(int(input()) - 1)

index = (math.floor(math.log(n * (phi + 2), phi) - 1)  // 3) * 3 + 2
num = round(phi ** Decimal(index + 1)) / (phi + 2)
sum = num // 2

print(int(sum))
