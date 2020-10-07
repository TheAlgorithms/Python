#nCr = n! / (n - r)! https://en.wikipedia.org/wiki/Permutation

#Calculate factorial (!)
def fact(n):
    count = 1
    for i in range (2, n+1):
        count *= i
    return count

#Calculate nPr (Permutations)
def nPr(n, r):
    return (fact(n) / fact(n - r))

#Asking for n & r value
n = int(input("n = "))
r = int(input("r = "))
print(int(nPr(n, r)))

if __name__ == "__main__":
    from doctest import testmod

    testmod()
