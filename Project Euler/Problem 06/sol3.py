z=y=0
for x in range(1,101):
    z+=x*x
for x in range(1,101):
    y+=x
print(abs(z-y*y))
