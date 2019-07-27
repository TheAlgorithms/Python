"""Convert ANY Decimal Number to a Binary Number."""

def dtbconverter(num):
    """ Function inputs a float value and returns a list as output """
    decimal_accuracy = 7

    # The part before decimal point in List<string> format
    whole = []
    # The part after decimal point in List<string> format
    fractional = ['.']

    # Extract fractional number part of decimal
    mantissa = round(num % 1, decimal_accuracy)
    # Extract whole number part of decimal.
    w_num = int(num)

    i = 0     # Counter

    # Loop to find binary of mantissa part
    while i < decimal_accuracy:
        mantissa = mantissa * 2
        mantissa = int(mantissa // 1)
        fractional.append(str(mantissa))
        # Extacting mantissa
        mantissa = round(mantissa % 1, decimal_accuracy)
        if mantissa == 0:
            break  # Removes trailing zeros.
        i = i + 1

    # Loop to find binary of whole number part.
    while w_num != 0:
        whole.append(w_num % 2)
        w_num = w_num // 2
    whole.reverse()

    binary = whole + fractional
    return "".join(binary)


if __name__ == '__main__':
    # NUMBER = float(input("Enter ANY base-10 Number: "))
    NUMBER = 55.55
    print("The Binary Equivalant: " + dtbconverter(NUMBER))
