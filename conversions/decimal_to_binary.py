"""Convert a Decimal Number to a Binary Number."""


def decimal_to_binary(num):
    """Convert a Decimal Number to a Binary Number."""
    binary = []
    while num > 0:
        binary.insert(0, num % 2)
        num >>= 1
    return "".join(str(e) for e in binary)


def main():
    """Print binary equivelents of decimal numbers."""
    print("\n2 in binary is:")
    print(decimal_to_binary(2))  # = 10
    print("\n7 in binary is:")
    print(decimal_to_binary(7))  # = 111
    print("\n35 in binary is:")
    print(decimal_to_binary(35))  # = 100011
    print("\n")


if __name__ == '__main__':
    main()
