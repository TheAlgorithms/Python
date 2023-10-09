SYMBOLS = {
    ".": 1,
    "|": 5,
    "o": 0
}

def mayan_to_int(mayan_levels: []) -> int:
    decimal_number = 0

    for index in range(3):
        level_value = 0

        for symbol in mayan_levels[index]:
            level_value += SYMBOLS[symbol];
        print(level_value)
        decimal_number += level_value * (20 ** index)

    return decimal_number

test = ["....|", ".", "."]
result = mayan_to_int(test)
print(result)