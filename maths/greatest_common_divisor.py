"""
Greatest Common Divisor.

Wikipedia reference: https://en.wikipedia.org/wiki/Greatest_common_divisor
"""      
def gcd(a, b):
    """Calculate Greatest Common Divisor (GCD)."""
    return b if a == 0 else gcd(b % a, a)


"""
Below method is more efficient.
This method is not acquire more memory cause is no use of any stacks(chunk of a memory space).
while above method is good one but acquire more memory for huge number because of more recursive call to evaluate GCD. 
 
"""
def gcd_by_iterative(x,y):
    while y:   #-->when y=0 then loop will  terminate and return x as final GCD.
        x,y=y,x%y
    return x 

def main():
    """Call GCD Function."""
    try:
        nums = input("Enter two Integers separated by comma (,): ").split(",")
        num_1 = int(nums[0])
        num_2 = int(nums[1])
        
        print(f"gcd({num_1}, {num_2}) = {gcd(num_1, num_2)}")
        print(f"By iterative gcd({num_1}, {num_2}) = {gcd_by_iterative(num_1, num_2)}")
       
    except (IndexError, UnboundLocalError, ValueError):
        print("Wrong Input")
        
if __name__ == "__main__":
    main()
    
