"""Find Minimum Number in a List."""


def main():
    """Find Minimum Number in a List."""
    def find_min(x):
        min_num = x[0]
        for i in x:
            if min_num > i:
                min_num = i
        return min_num

    print(find_min([0, 1, 2, 3, 4, 5, -3, 24, -56]))  # = -56


if __name__ == '__main__':
    main()
