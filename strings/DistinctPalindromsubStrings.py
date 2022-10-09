# Python program Find all distinct palindromic sub-strings
# of a given string
 
# Function to print all distinct palindrome sub-strings of s
def palindromeSubStrs(s):
    m = dict()
    n = len(s)
 
    # table for storing results (2 rows for odd-
    # and even-length palindromes
    R = [[0 for x in range(n+1)] for x in range(2)]
 
    # Find all sub-string palindromes from the given input
    # string insert 'guards' to iterate easily over s
    s = "@" + s + "#"
 
    for j in range(2):
        rp = 0    # length of 'palindrome radius'
        R[j][0] = 0
 
        i = 1
        while i <= n:
 
            # Attempt to expand palindrome centered at i
            while s[i - rp - 1] == s[i + j + rp]:
                rp += 1 # Incrementing the length of palindromic
                        # radius as and when we find valid palindrome
 
            # Assigning the found palindromic length to odd/even
            # length array
            R[j][i] = rp
            k = 1
            while (R[j][i - k] != rp - k) and (k < rp):
                R[j][i+k] = min(R[j][i-k], rp - k)
                k += 1
            rp = max(rp - k, 0)
            i += k
 
    # remove guards
    s = s[1:len(s)-1]
 
    # Put all obtained palindromes in a hash map to
    # find only distinct palindrome
    m[s[0]] = 1
    for i in range(1,n):
        for j in range(2):
            for rp in range(R[j][i],0,-1):
                m[s[i - rp - 1 : i - rp - 1 + 2 * rp + j]] = 1
        m[s[i]] = 1
 
    # printing all distinct palindromes from hash map
    print ("Below are " + str(len(m)) + " pali sub-strings")
    for i in m:
        print (i)
 
# Driver program
palindromeSubStrs("abaaa")
