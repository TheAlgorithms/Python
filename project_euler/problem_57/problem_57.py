""" For the algorithm that approximates sqrt(2) (https://projecteuler.net/problem=57),
for the first 1000 iterations return the number of iterations in which the nominator
has more digits than the denominator.
"""
def solution():
    """
    Return the number of iterations in which the nominator has more digits than the denominator.
    >>> solution()
    153
    """
    def f(n): # Recursive helper function.
        if n==0: return (3,2) # End state for recursion.
        if n ==3: return (41,29) # Keeps recursion level<997.
        prev_nom, prev_denom = f(n-1)
        
        new_denom = prev_nom + prev_denom 
        new_nom = new_denom + prev_denom
        return (new_nom, new_denom)

    c = 0
    for i in range(998): # 1K iterations and calculate frequency.
        nom,denom = f(i)
        if len(str(nom)) > len(str(denom)): c+=1 # Check number of digits by converting to str.
    return c
if __name__ == "__main__":
    print(solution())
