from itertools import permutations


def main():
    result = list(map("".join, permutations("0123456789")))
    print(result[999999])


if __name__ == "__main__":
    main()
