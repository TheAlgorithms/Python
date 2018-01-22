def mulitples(limit):
    xmulti = []
    zmulti = []
    z = 3
    x = 5
    temp = 1
    while True:
        result = z * temp
        if (result < limit):
            zmulti.append(result)
            temp += 1
            continue
        else:
            temp = 1
            break
    while True:
        result = x * temp
        if (result < limit):
            xmulti.append(result)
            temp += 1
            continue
        else:
            temp = 1
            break
    return (sum(zmulti) + sum(xmulti))
    
    
        
        
        
    
print (mulitples(100))
