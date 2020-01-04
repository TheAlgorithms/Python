def bubble_sort(list1): 
    for i, num in enumerate(list1): 
        try: 
            if list1[i+1] < num: 
                list1[i] = list1[i+1] 
                list1[i+1] = num 
                bubble_sort(list1) 
        except IndexError: 
            pass
    return list1 
  
list1 = []
print("Enter length of list elements:")
n = int(input())

for i in range(0,n):
    print("Enter",i+1,"element of list")
    element = input()
    list1.append(element)

    
bubble_sort(list1) 

if(len(list1) == 0):
    print("Empty list")
    
else:
  
    print("Sorted array:"); 
    for i in range(0, len(list1)): 
        print(list1[i], end=' ') 
