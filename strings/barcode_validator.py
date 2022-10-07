def evalKey(code: int):
    code //= 10  # exclude the last digit
    checker = False
    s = 0

    # extract and check each digit
    while code != 0:
        mult = 1 if checker else 3
        s += mult * (code % 10)
        code //= 10
        checker = not checker

    return (10 - (s % 10)) % 10


def isValid(code: int):
    return len(str(code)) == 13 and evalKey(code) == code % 10


if __name__ == "__main__":
    barcode = input("Enter a barcode: ")
    number_barcode = int(barcode)
    if isValid(number_barcode):
        print(f"|{n}| is a valid Barcode")
    else:
        print(f"|{n}| is NOT is valid Barcode.")
