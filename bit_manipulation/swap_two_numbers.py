"""provided funtionality to swap two numbers in quickest way possible"""
def swap_Two_numbers(a,b):
    """
    below function is used to swap two numbers in quickest way possible 
    The idea is to use XOR operation to swap two number using bit manipulation
    """
    print("before swapping a:" + a + "b:" + b)
    a ^= b
    b ^= a
    a ^= b
    print("after swapping a:" + a + "b:" + b)


if __name__ == "__main__":
   a = int(input("enter first number"))
   b = int(input("enter second number"))
   
   swap_Two_numbers(a,b)
