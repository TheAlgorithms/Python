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
        else:
            temp = 1
            break
    while True:
        result = x * temp
        if (result < limit):
            xmulti.append(result)
            temp += 1
        else:
            break
    collection = list(set(xmulti+zmulti))
    return (sum(collection))
    
    
        
        
        
    
print (mulitples(1000))
