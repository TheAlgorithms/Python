"""Find Least Common Multiple."""

# https://en.wikipedia.org/wiki/Least_common_multiple


def find_lcm(num_1, num_2):
    """Find the least common multiple of two numbers.
       >>> find_lcm(5,2)
       10
       >>> find_lcm(12,76)
       228
    """
    if num_1>=num_2:
        max_num=num_1
    else:
        max_num=num_2
    
    lcm = max_num
    while True:
        if ((lcm % num_1 == 0) and (lcm % num_2 == 0)):
            break
        lcm += max_num
    return lcm


def main():
    """Use test numbers to run the find_lcm algorithm."""
    num_1 = int(input().strip()) 
    num_2 = int(input().strip()) 
    print(find_lcm(num_1, num_2))


if __name__ == '__main__':
    main()
