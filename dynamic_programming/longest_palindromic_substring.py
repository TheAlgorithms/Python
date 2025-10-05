# reference :https://www.geeksforgeeks.org/dsa/longest-palindromic-substring/

def longest_palindromic_substring(s:str)->str:
    """
    This function returns the longest palindromic substring in a string using dynamic programming
    >>> longest_palindromic_substring("babad")
    'aba'
    >>> longest_palindromic_substring("cbbd")
    'bb'
    >>> longest_palindromic_substring("a")
    'a'
    >>> longest_palindromic_substring("ac")
    'a'
    >>> longest_palindromic_substring("")
    ''
    """
    n=len(s)

    dp=[[False for i in range(n)] for j in range(n)]
    start=0
    max_length=1

    for i in range(n):
        dp[i][i]=True
    
    # for length 2 palindrome check
    for i in range(n-1):
        if s[i]==s[i+1]:
            dp[i][i+1]=True
            start=i
            max_length=2

    # for length 3 and above
    for length in range(3,n+1):
        for i in range(n-length+1):
            j=i+length-1
            if s[i]==s[j] and dp[i+1][j-1]:
                dp[i][j]=True
                start=i
                max_length=length

    return s[start:start+max_length]

def manacher_algorithm(s:str)->str:
    """
    This function returns the longest palindromic substring in a string using Manacher's algorithm
    >>> longest_palindromic_substring("babad")
    'aba'
    >>> longest_palindromic_substring("cbbd")
    'bb'
    >>> longest_palindromic_substring("a")
    'a'
    >>> longest_palindromic_substring("ac")
    'a'
    >>> longest_palindromic_substring("")
    ''
    """
    T='^#'+'#'.join(s)+'#$'
    n=len(T)

    p=[0]*n
    c=0
    r=0

    for i in range(1,n-1):
        mirror=2*c-i
        if i<r:
            p[i]=min(r-i,p[mirror])
        while T[i+(1+p[i])]==T[i-(1+p[i])]:
            p[i]+=1
        if i+p[i]>r:
            c=i
            r=i+p[i]

    max_length=max(p)
    max_center=p.index(max_length)
    start=(max_center-max_length)//2
    return s[start:start+max_length]

if __name__ == "__main__":
    import doctest

    doctest.testmod()
