"""Find Least Common Multiple."""

# https://en.wikipedia.org/wiki/Least_common_multiple


def find_lcm(num_1, num_2):
    """Find the LCM of two numbers."""
    max_num = num_1 if num_1 > num_2 else num_2
    lcm = max_num
    while True:
        if ((lcm % num_1 == 0) and (lcm % num_2 == 0)):
            break
        lcm += max_num
    return lcm


def main():
    """Use test numbers to run the find_lcm algorithm."""
    num_1 = 12
    num_2 = 76
    print(find_lcm(num_1, num_2))


if __name__ == '__main__':
    main()
