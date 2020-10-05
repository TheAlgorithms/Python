"""
    Euler Problem : 92
    @author : sandeep gupta
    @time   : 5 October 2020, 18:30
    @Solution: Tried doing a top bottom memoziation, to calculate the squares
    at each step and run through 10 million numbers to calculate the numbers
    ending at 89, returning the answer at the end.
    @answer     : 8581146

"""
def solution() -> int:
    square_hash = {}
    answer = 0
    square_hash[89] = 89
    square_hash[1] = 1
    square = {}
    square[0] = 0
    square[1] = 1
    square[2] = 4
    square[3] = 9
    square[4] = 16
    square[5] = 25
    square[6] = 36
    square[7] = 49
    square[8] = 64
    square[9] = 81
    for i in range(1, 10000000):
        number = i
        while True:
            if number in square_hash:
                if square_hash[number] == 89:
                    square_hash[i] = 89
                    answer += 1
                    break
                elif square_hash[number] == 1:
                    square_hash[i] = 1
                    break
                else:
                    number = square_hash[number]
            string_number = str(number)
            number = 0
            for j in string_number:
                number += square[int(j)]
            square_hash[int(string_number)] = number
    return answer

print(solution())


# Tests
if __name__ == "__main__":
    import doctest

    doctest.testmod()
