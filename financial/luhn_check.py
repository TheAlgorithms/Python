#https://en.wikipedia.org/wiki/Luhn_algorithm

def luhn_check(cardNumber):
    cardDigits = len(str(cardNumber))
    totalSum = 0
    isSecond = False

    for i in range(cardDigits - 1, -1, -1):
        d = ord(cardNumber[i]) - ord('0')

        if (isSecond == True):
            d = d * 2

        totalSum += d // 10
        totalSum += d % 10

        isSecond = not isSecond

    if (totalSum % 10 == 0):
        return True
    else:
        return False
