def swapList(newList): 
size = len(newList) 

# Swapping 
temp = newList[0] 
newList[0] = newList[size - 1] 
newList[size - 1] = temp 

return newList newList = [12, 35, 9, 56, 24] 

print(swapList(newList)) 

OUTPUT:-
[24, 35, 9, 56, 12]