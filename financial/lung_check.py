def luhn_check(cardNo):
    nDigits = len(str(cardNo))
    nSum = 0
    isSecond = False

    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')

        if (isSecond == True):
            d = d * 2

        nSum += d // 10
        nSum += d % 10

        isSecond = not isSecond

    if (nSum % 10 == 0):
        return True
    else:
        return False



listofcards = [
    "371449635398431",
    "378734493671000",
    "5610591081018250",
    "30569309025904",
    "38520000023237",
    "6011111111111117",
    "6011000990139424",
    "3530111333300000",
    "3566002020360505",
    "5555555555554444",
    "5105105105105100",
    "4111111111111111",
    "4012888888881881",
    "4222222222222",
    "5019717010103742",
    "6331101999990016"
]

for x in listofcards:
    if (luhn_check(x)):
        print("This is a valid card")
    else:
        print("This is not a valid card")
 

