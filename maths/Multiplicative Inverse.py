def extended_euclidean(p, q):
    """
    >>> extended_euclidean(10, 23)
    [1, [7]]

    >>> extended_euclidean(11, 2)
    [1, [-5, -3]]
    """
    step = {'Q':0, 'r1':max(p, q), 'r2':min(p, q), 'r':0, 't1':0, 't2':1, 't':0} #Initalizing table of Extended Euclidean algorithm

    while(True):
        try:                                          #Break condition for loop
            step['r'] = step['r1'] % step['r2']
            if step['r'] < 0:
                break
        except:
            break
        step['q'] = (step['r1'] - step['r'])/step['r2'] 

        step['t'] = step['t1'] - step['t2'] * step['q']

        step['r1'] = step['r2']
        step['r2'] = step['r']

        step['t1'] = step['t2']
        step['t2'] = step['t']
    
    if step['t1'] > 0:                                #Returning [greatest_common_divisor, [multiplicative inverse(s)]]
        return [int(step['r1']), [int(step['t1'])]]
    return [int(step['r1']), [int(step['t1']), q + int(step['t1'])]]

if __name__=='__main__':
    p = int(input("ENter p: "))
    q = int(input("ENter Z's subscript: "))
    
    result = extended_euclidean(p, q)

    print(result)