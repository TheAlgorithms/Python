# Program to find the product of a,b,c which are Pythagorean Triplet that satisfice the following:
# 1. a < b < c
# 2. a**2 + b**2 = c**2
# 3. a + b + c = 1000

print("Please Wait...")
for a in range(300):
    for b in range(400):
        for c in range(500):
            if(a < b < c):
                if((a**2) + (b**2) == (c**2)):
                    if((a+b+c) == 1000):
                        print("Product of",a,"*",b,"*",c,"=",(a*b*c))
                        break
