def lsearch(array:list, key:any)-> any:
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
    assert lsearch([45,90,1,24],1)
