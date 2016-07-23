def binarySearch(alist, item):
    
    first = 0
    last = len(alist)-1
    found = False
    
    while first<=last and not found:
        
        midpoint = (first + last)//2
        if alist[midpoint] == item:
             found = True
             print("Found")
        else:
            
            if item < alist[midpoint]:
                
                last = midpoint-1
            else:
                first = midpoint+1
        if found == False:
            
            print("Not found")
    return found
print("Enter numbers seprated by space")
s = input()
numbers = list(map(int, s.split()))
trgt =int( input('enter a single number to be found in the list '))
binarySearch(numbers, trgt)

