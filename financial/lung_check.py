#https://en.wikipedia.org/wiki/Luhn_algorithm
def luhn_check(cardNo):
    cardDigits = len(str(cardNo))
    luhnSum = 0
    second = False

    for i in range(cardDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')

        if (second == True):
            d = d * 2

        luhnSum += d // 10
        luhnSum += d % 10

        second = not second

    if (luhnSum % 10 == 0):
        return True
    else:
        return False
