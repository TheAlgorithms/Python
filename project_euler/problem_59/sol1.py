from itertools import permutations


def check_english(ascii1, ascii2):
    """
    function to check if the
    xor(exclusive or) of two ascii
    numbers entered is only letters
    used in common english
    """
    xor = ascii1 ^ ascii2
    return isAcceptable(chr(xor))

    # print (chr(xor))
    return False


def isAcceptable(myChar):
    return (
        "a" <= myChar <= "z"
        or "A" <= myChar <= "Z"
        or myChar == " "
        or myChar == "'"
        or myChar == ","
        or myChar == '"'
        or myChar == "["
        or myChar == "]"
        or myChar == ":"
        or "0" <= myChar <= "9"
        or myChar == "/"
        or myChar == "."
        or myChar == "("
        or myChar == ")"
        or myChar == ";"
        or myChar == "+"
    )


def solution() -> int:
    try:
        with open("cipher.txt", "r") as file:
            data = file.read().replace("\n", "")
            data = data.split(",")
            data = [int(x) for x in data]
            answer = 0
            for i in range(97, 123):
                for j in range(97, 123):
                    for k in range(97, 123):
                        possible_lists = set(list(permutations([i, j, k], 3)))
                        for possible_answer in possible_lists:
                            round_robin_count = 0
                            words = ""
                            valid = True
                            for d in data:
                                if check_english(d, possible_answer[round_robin_count]):
                                    words += chr(d ^ possible_answer[round_robin_count])
                                else:
                                    valid = False
                                    break
                                round_robin_count = (round_robin_count + 1) % 3
                            if valid:
                                for word in words:
                                    answer += ord(word)
                                return answer
    except BaseException:
        print("An exception occured while reading file")
    return answer


print(solution())

# Tests
if __name__ == "__main__":
    import doctest

    doctest.testmod()
