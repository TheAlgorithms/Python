def check(x):
    """
    This function checks if a credit card number is valid. If yes, then it returns the name of the payment gateway of the credit card.
    Doctests cannot be included in order to ensure privacy.
    """
    list_of_digits = [i for i in x]
    list_1 = []
    sum1 = 0
    for i in range(len(x) - 2, -1, -2):
        a = str(2 * (int(list_of_digits[i])))
        list_1.append(a)
        for j in range(len(a)):
            sum1 += int(a[j])
    sum2 = sum1
    for i in range(len(x) - 1, -1, -2):
        sum2 += int(list_of_digits[i])
    if (sum2) % 10 == 0:
        if len(x) == 15:
            return "AMEX"
        elif (len(x) == 16 or len(x) == 13) and x[0] == '4':
            return "VISA"
        else:
            return "MASTERCARD"
    else:
        return "INVALID"
