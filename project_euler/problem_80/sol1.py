"""
    Euler Problem : 80
    @author : Sandeep Gupta
    @time   : 5 October 2020, 18:30
    @Solution: Used decimal python module to calculate the decimal
    places up to 100, the most important thing would be take calculate
    a few extra places for decimal otherwise there will be rounding
    error.
    @answer     : 40886
"""
import decimal


def solution() -> int:
    answer = 0
    dot100 = decimal.Context(prec=105)
    for i in range(2, 100):
        number = decimal.Decimal(i)
        sqrt_number = number.sqrt(dot100)
        if len(str(sqrt_number)) > 1:
            answer += int(str(sqrt_number)[0])
            sqrt_number = str(sqrt_number)[2:101]
            answer += sum([int(x) for x in sqrt_number])
        return answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(solution())
