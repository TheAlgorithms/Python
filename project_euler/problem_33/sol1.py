def isDigitCancelling(num,den):
    if num != den:
        if num % 10 == den // 10:
            if (num // 10) / (den % 10) == num/den:
                return True

def solve():
    solutions = []
    den = 11 
    for num in range(11,99):
        while den <= 99:
            if (num != den) and (num % 10 == den // 10) and (den%10 != 0):
                if isDigitCancelling(num,den):
                    solutions.append("{}/{}".format(num,den))
            den += 1
        num += 1
        den = 10  
    return solutions


if __name__ == "__main__":
    print(*solve(),sep=" , ")
    
