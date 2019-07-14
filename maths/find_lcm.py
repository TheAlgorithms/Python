"""Find Least Common Multiple."""

# https://en.wikipedia.org/wiki/Least_common_multiple


def find_lcm(num_1, num_2):
    """Find the LCM of two numbers."""
    if num_1>=num_2:
        max_num=num_1
    else:
        max_num = num2
    
    lcm = max_num
    while True: #Run the loop until lcm value becomes divisible by both num_1 and num_2
        if ((lcm % num_1 == 0) and (lcm % num_2 == 0)): 
            break
        lcm += max_num
    return lcm


def main():
    """Use test numbers to run the find_lcm algorithm."""
    num_1 = int(input())   #get the number1 input from user 
    num_2 = int(input())   # get the number 2 input from user
    print(find_lcm(num_1, num_2)) # calls th lcm function


if __name__ == '__main__':
    main()
