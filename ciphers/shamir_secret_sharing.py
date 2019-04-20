import random
from math import ceil

def combine_shares(shares,t):
    '''Use Lagranges Interpolation method to attempt combining the 'shares' and regenerate the secret. t is the threshold of the scheme'''
    sums = 0
    prod_arr = []
    if len(shares) < t:
        raise Exception("Shares provided less than threshold. Secret generation not possible")
    for j in range(len(shares)):
        xj,yj = shares[j][0],shares[j][1]
        prod = 1
        for i in range(len(shares)):
            xi = shares[i][0]
            if i != j: prod *= xi/(xi-xj)  
        prod *= yj
        sums += prod
    return ceil(sums)
            
def polynom(x,coeff):
    '''Evaluate the value of a polynomial with coefficeints given in the 'coeff' list in decreasing order at value 'x'''
    y = 0
    for i in range(len(coeff)):
        y += (x**(len(coeff)-i-1)) * coeff[i]
    return y

def coeff(t,secret):
    '''Generates random polynomial coefficeints used for Shamir Polynomial and returns all coefficients in decreasing order as list'''
    coeff = []
    for i in range(t-1):
        coeff.append(random.randrange(0,secret))
    coeff.append(secret)
    return coeff

def shares(n,m,secret):
    '''Split the 'secret' value among 'n' parties such that a minimum of 'm' parties (threshold) can combine their shares to regenerate 'secret'
    Return a list of ordered pairs (x,y) where x is share number and y = f(x), i.e. value of Shamir Polynomial at input = x''' 
    cfs = coeff(m,secret)
    shares = []
    for i in range(1,n+1):
        shares.append([i,polynom(i,cfs)])
    return shares




    
