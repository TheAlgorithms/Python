arr = [7, 2, 8, 5, 1, 4, 6, 3];     
temp = 0;    
      
print("Elements of original array: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" ");    
        
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] > arr[j]):    
            temp = arr[i];    
            arr[i] = arr[j];    
            arr[j] = temp;    
     
print();    
      
    
print("Elements of array sorted in ascending order: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" ");    
