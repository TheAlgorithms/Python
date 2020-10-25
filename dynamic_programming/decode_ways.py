'''
A message containing letters from A-Z is being encoded to numbers using the
following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits,
determine the total number of ways to decode it.
'''

def num_decodings(s: str):
    '''
    >> num_decodings("12")
    2
    >> num_decodings("226")
    3
    '''
    if not s or int(s[0]) == 0:
        return 0
    
    last = 1
    second_last = 1
    
    for i in range(1, len(s)):
        
        # 0 is a special digit since it does not
        # correspond to any alphabet but can be
        # meaningful if preceeded by 1 or 2
        
        if s[i] == "0":
            if s[i-1] in {"1", "2"}:
                curr = second_last
            else:
                return 0
            
        elif 11 <= int(s[i-1:i+1]) <= 26:
            curr = second_last + last
        else:
            curr = last
        
        last, second_last = curr, last

    return last


if __name__ == "__main__":
    import doctest

    doctest.testmod()