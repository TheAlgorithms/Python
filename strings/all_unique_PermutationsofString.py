# program will generate all unique permutation of string
def permutation(lst): 

    if len(lst) == 0: 
        return [] 

    if len(lst) == 1: 
        return [lst] 


    l = [] 

    for i in range(len(lst)): 
       m = lst[i] 
       remLst = lst[:i] + lst[i+1:] 

       for p in permutation(remLst): 
           l.append(m + p) 
    return l 

inp="12345"
for p in permutation(inp): 
    print(p) 
