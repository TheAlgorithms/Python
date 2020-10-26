#S= √ (p * (p - a)*(p - b)*(p - c))
#p=(a+b+c)/2;
#a,b,c - sides triangle


def treug(a,b,c):
    p=(a+b+c)/2
    S=(p * (p - a)*(p - b)*(p - c))**(1/2)
    return(S)
