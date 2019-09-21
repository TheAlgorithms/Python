def pow_dnc(x, y):
    """
    This function calculates power of a number using divide
    and conquer

    Parameters:
        x(int,float)>=0:base number
        y(int):power number can be negative or positive

    Time Complexity: O(log n)
    """

    if y == 0:
        return 1
    temp = pow_dnc(x, int(y / 2))

    if y % 2 == 0:
        return temp * temp
    else:
        if y > 0:
            return x * temp * temp
        else:
            return (temp * temp) / x


# Driver Code
x, y = 2, -3
print("%.6f" % (pow_dnc(x, y)))
# output: 0.125000
