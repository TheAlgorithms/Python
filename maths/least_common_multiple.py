def find_lcm(first_num: int, second_num: int) -> int:
    """Find the least common multiple of two numbers.

       Learn more: https://en.wikipedia.org/wiki/Least_common_multiple

       >>> find_lcm(5,2)
       10
       >>> find_lcm(12,76)
       228
    """
    max_num = first_num if first_num >= second_num else second_num
    common_mult = max_num
    while (common_mult % first_num != 0) and (common_mult % second_num != 0):
        common_mult += max_num
    return common_mult


def main():
    """Use test numbers to run the find_lcm algorithm."""
    first_num = int(input().strip())
    second_num = int(input().strip())
    print(find_lcm(first_num, second_num))


if __name__ == "__main__":
    main()
