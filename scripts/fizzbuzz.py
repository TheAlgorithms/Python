
def fizz_buzz(input):
    if (input % 15) == 0:
        return "fizz_buzz"

    if (input % 3) == 0:
        return "fizz"

    if (input % 5) == 0:
        return "buzz"

    return "khra tv"


print(fizz_buzz(55))
