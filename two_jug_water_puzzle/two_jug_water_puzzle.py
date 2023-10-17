"Implementation of the two jug water puzzle."

def greatest_common_divisor(a, b):
    """Return the greatest common divisor of two numbers."""
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)
    
def pour_water(toJugCap,fromJugCap,d):
    "Pour water from one jug to another jug."
    "fromJugCap: capacity of the jug from which water is poured."
    "toJugCap: capacity of the jug to which water is poured."
    "d: amount of water to be poured."
    fromJug = fromJugCap
    toJug = 0
    step = 1
    while fromJug != d and toJug != d:
        temp = min(fromJug, toJugCap - toJug)
        toJug = toJug + temp
        fromJug = fromJug - temp
        step = step + 1
        if fromJug == d or toJug == d:
            break
        if fromJug == 0:
            fromJug = fromJugCap
            step = step + 1
        if toJug == toJugCap:
            toJug = 0
            step = step + 1
    return step

def findMinimumSteps(n,m,d):
    "Find the minimum number of steps required to get d litres of water."
    "n: capacity of the first jug."
    "m: capacity of the second jug."
    "d: amount of water to be poured."
    if n > m:
        temp = n
        n = m
        m = temp
    if (d % greatest_common_divisor(m,n)) != 0:
        return -1
    return min(pour_water(m,n,d),pour_water(n,m,d))

def main():
    "Main function."
    n = int(input("Enter the capacity of the first jug: "))
    m = int(input("Enter the capacity of the second jug: "))
    d = int(input("Enter the amount of water to be poured: "))
    print("Minimum number of steps required is: ",findMinimumSteps(n,m,d))
    
if __name__ == "__main__":
    
    main()