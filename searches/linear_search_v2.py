def search(array:list, key:any)-> any:
    """
    This is linear search algorithm 
    >>> search([1,2,45,98,4,56,3,7],7)
    7
    """
    size =len(array)
    found = False
    i= 0
    for i in range(size):
        if array[i] == key:
            print(i)
        else :
            if i == size-1:
                print("Not found")
        i = i+1        
if __name__ == "__main__":
    import doctest 
    doctest.testmod(name="search", verbose=True)
    
    
