def remainder(p,q):
    divisor = q
    dividend = p
    qoutient = int(dividend/divisor)
    result = p - qoutient*divisor
    return result

x = float(input("Enter the vale of dividend: "))
y = float(input("Enter the value of divisor: "))
r = remainder(x,y)
print("The remainder is :",'%.5a'%r)