def lsearch(array:list, key:any)-> any:
    """This Function will helps to find the 
    element using linear search.
    >>>  lsearch([45,90,1,24],1)
    2
    >>> lsearch (['Tejas','linux','python'],'Tejas')
    0
    """
    size =len(array)
    found = False
    i= 0
    for i in range(size):
        if array[i] == key:
            print("Element found at ",i)
        else :
            if i == size-1:
                return f"Not found"
        i = i+1        
if __name__ == "__main__":
    import doctest 
    doctest.testmod(name="lsearch", verbose=True)
    
    
