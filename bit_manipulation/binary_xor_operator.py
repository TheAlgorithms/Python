def binary_xor(a, b):
    """
    Take in 2 integers, perform binary & operation,
    convert the number to binary and print.

    binary_xor(25, 32)
    111001
    binary_xor(37, 50)
    10111
    binary_xor(0, -1)
    Traceback (most recent call last): ...
    ValueError: the value of both input must be positive
    """
    if a < 0 or b < 0:
        raise ValueError("the value of both input must be positive")
        
    c = a ^ b
    decToBinary(c)

def decToBinary(n): 
      
    # array to store binary number 
    if (n == 0):
        print("0")
    binaryNum = [0] * n; 
  
    # counter for binary array 
    i = 0; 
    while (n > 0):  
  
        # storing remainder in binary array 
        binaryNum[i] = n % 2; 
        n = int(n / 2); 
        i += 1; 
  
    # printing binary array in reverse order 

    for j in range(i - 1, -1, -1):
        print(binaryNum[j], end = "");
    print()



if __name__ == "__main__":
    binary_xor(25, 32)
    binary_xor(37, 50)