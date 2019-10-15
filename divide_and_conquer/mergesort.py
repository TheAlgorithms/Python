def merge(a,b,m,e):
    l=a[b:m+1]
    r=a[m+1:e+1]
    k=b
    i=0
    j=0
    while i<len(l) and j<len(r):
        #change sign for Descending order
        if l[i]<r[j]: 
            a[k]=l[i]
            i+=1
        else:
            a[k]=r[j]
            j+=1
        k+=1
    while i<len(l):
        a[k]=l[i]
        i+=1
        k+=1
    while j<len(r):
        a[k]=r[j]
        j+=1
        k+=1
    return a
    
def mergesort(a,b,e):
    """
    >>> mergesort([3,2,1],0,2)
    [1, 2, 3]
    >>> mergesort([3,2,1,0,1,2,3,5,4],0,8)
    [0, 1, 1, 2, 2, 3, 3, 4, 5]
    """
    if b<e:
        m = (b+e)//2
        #print("ms1",a,b,m)
        mergesort(a,b,m)
        #print("ms2",a,m+1,e)
        mergesort(a,m+1,e)
        #print("m",a,b,m,e)
        merge(a,b,m,e)
        return a

if __name__ == "__main__":
    import doctest
    doctest.testmod()
