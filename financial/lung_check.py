#https://en.wikipedia.org/wiki/Luhn_algorithm
def luhn_check(card_no: str) -> bool:
    card_digits = len(str(card_no))
    luhn_sum = 0
    second = False

    for i in range(card_digits - 1, -1, -1):
        d = ord(card_no[i]) - ord('0')

        if (second == True):
            d = d * 2

        luhn_sum += d // 10
        luhn_sum += d % 10

        second = not second

    if (luhn_sum % 10 == 0):
        return True
    else:
        return False
