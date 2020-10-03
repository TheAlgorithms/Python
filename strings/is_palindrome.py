import time
def is_palindrome(s: str) -> bool:
    """
    Determine whether the string is palindrome
    :param s:
    :return: Boolean
    >>> is_palindrome("a man a plan a canal panama".replace(" ", ""))
    True
    >>> is_palindrome("Hello")
    False
    >>> is_palindrome("Able was I ere I saw Elba")
    True
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("Mr. Owl ate my metal worm?")
    True
    """
    # Since Punctuation, capitalization, and spaces are usually ignored while checking
    # Palindrome,  we first remove them from our string.
    t1=time.time()
    s = "".join([character for character in s.lower() if character.isalnum()])
    t2=time.time()
    print(t2-t1)
    return s == s[::-1]


def my_palindrome(s):
    t1=time.time()
    s=s.lower()
    s1=''
    for i in s:
        if ord(i)>=97 and ord(i)<=122:
            s1+=i
    s2=''
    for i in range(len(s1)-1,-1,-1):
        s2+=s1[i]
    t2=time.time()
    print(t2-t1)
    if s2==s1:
        print('Given string is palindrome')
    else:
        print('Given string is not palindrome')

if __name__ == "__main__":
    s = input("Enter string to determine whether its palindrome or not: ").strip()
    if is_palindrome(s):
        print("Given string is palindrome")
    else:
        print("Given string is not palindrome")
        
 
    my_palindrome(s)
    
    
    '''
    Brute Force approach:
                   with same time complexity(O(n)),
                   well understandable,
                   Same Execution Time.
   '''
