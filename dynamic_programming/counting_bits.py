def countBits(num: int):
    '''
    >>
    '''
    ones = [0, 1]
    anchor = 2
    
    if num < 2:
        return ones[:num+1]
    
    while(True):
        j = 0
        while(j<anchor):
            if len(ones) == num+1:
                return ones
            ones.append(ones[j]+1)
            j += 1

        anchor = anchor + j

print(countBits(5))