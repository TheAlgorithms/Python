#code to convert hexadecimal into binary
import math

hex_str = input("Enter you value: ").strip()
n = int(hex_str, 16)
bin_str = ""


"""
Here, we have used " >> " bitwise operator
Bitwise right shift: 
Shifts the bits of the number to the right and fills 0 on voids left as a result. 
Similar effect as of dividing the number with some power of two.
Example: 
a = 10
a >> 1 = 5 

"""
def convert(n, bin_str):
    while n>0:
        #print(n)
        m = str(n%2)
        bin_str = m + bin_str
        n=n>>1
    
    return str(bin_str)

print("Your value in BINARY is " + convert(n, bin_str))