#!python3
"""
The problem is to find a given string has unique characters.

"""
def isUniqueSet(s):
    """
    This function uses set
    s -> string
    return type -> bool
 
    """

    hashSet = set()
    for i in s:
        if i in hashSet:
            return False
        hashSet.add(i)
    return True

def isUniqueHash(s):
    """
    This uses Hashes
    s -> string
    return type -> bool
 
    """

    if len(s)>256:
        return False
    hash = [False]*256
    for i in s:
        index = ord(i)
        if hash[index]:
            return False
        hash[index] = True
    return True

if __name__ == "__main__":
    print(isUniqueHash("nish"))