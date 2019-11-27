def recursive_binomial_coefficient(n,k):
    """Calculates the binomial coefficient, C(n,k), with n>=k using recursion
    Time complexity is O(k), so can calculate fairly quickly for large values of k.

    """

    if k == 0 or n == k:
        #C(n,0) = C(n,n) = 1, so this is our base case.
        return 1
    if k > n/2:
        #C(n,k) = C(n,n-k), so if n/2 is sufficiently small, we can reduce the problem size.
        return recursive_binomial_coefficient(n,n-k)
    else:
        #else, we know C(n,k) = (n/k)C(n-1,k-1), so we can use this to reduce our problem size.
        return int((n/k)*recursive_binomial_coefficient(n-1,k-1))


print(recursive_binomial_coefficient(8,2))
print(recursive_binomial_coefficient(4,0))
print(recursive_binomial_coefficient(500,300))