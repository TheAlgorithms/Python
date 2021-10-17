
# Function to allocate memory to  
# blocks as per First fit algorithm  
def first_fit(block_size, m, process_size, n): 
      
    # Stores block id of the  
    # block allocated to a process  
    allocation = [-1] * n  
  
    # Initially no block is assigned to any process 
  
    # pick each process and find suitable blocks  
    # according to its size ad assign to it  
    for i in range(n): 
        for j in range(m): 
            if block_size[j] >= process_size[i]: 
                  
                # allocate block j to p[i] process  
                allocation[i] = j  
  
                # Reduce available memory in this block.  
                block_size[j] -= process_size[i]  
  
                break
  
    print(" Process No. Process Size      Block no.") 
    for i in range(n): 
        print(" ", i + 1, "      ", process_size[i],  
                          "      ", end = " ")  
        if allocation[i] != -1:  
            print(allocation[i] + 1)  
        else: 
            print("Not Allocated") 
  
# Driver code  
if __name__ == '__main__':  
    block_size = [100, 500, 200, 300, 600]  
    process_size = [212, 417, 112, 426] 
    m = len(block_size) 
    n = len(process_size) 
  
    first_fit(block_size, m, process_size, n) 