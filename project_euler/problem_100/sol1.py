b = 15
n = 21
target = 1000000000000
 
while(n < target):
    btemp = 3 * b + 2 * n - 2
    ntemp = 4 * b + 3 * n - 3
 
    b = btemp
    n = ntemp

print("number of blue discs ",b)