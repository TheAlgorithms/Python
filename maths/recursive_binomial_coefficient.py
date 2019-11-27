def recursive_binomial_coefficient(n,k):
    """Calculates the binomial coefficient, C(n,k), with n>=k using recursion
    Time complexity is O(k), so can calculate fairly quickly for large values of k.

    >>> recursive_binomial_coefficient(5,0)
    1

    >>> recursive_binomial_coefficient(8,2)
    28

    >>> recursive_binomial_coefficient(500,300)
    5054949849935535817667719165973249533761635252733275327088189563256013971725761702359997954491403585396607971745777019273390505201262259748208640

    >>> recursive_binomial_coefficient(4,5)
    'Invalid Inputs'

    """

    if k>n:
        return 'Invalid Inputs'
        #function is only defined for n>=k
    if k == 0 or n == k:
        #C(n,0) = C(n,n) = 1, so this is our base case.
        return 1
    if k > n/2:
        #C(n,k) = C(n,n-k), so if n/2 is sufficiently small, we can reduce the problem size.
        return recursive_binomial_coefficient(n,n-k)
    else:
        #else, we know C(n,k) = (n/k)C(n-1,k-1), so we can use this to reduce our problem size.
        return int((n/k)*recursive_binomial_coefficient(n-1,k-1))

