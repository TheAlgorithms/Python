from typing import List


def compare_string(string1: str, string2: str) -> str:
    """
    >>> compare_string('0010','0110')
    '0_10'

    >>> compare_string('0110','1101')
    'X'
    """
    l1 = list(string1)
    l2 = list(string2)
    count = 0
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            count += 1
            l1[i] = "_"
    if count > 1:
        return "X"
    else:
        return "".join(l1)


def check(binary: List[str]) -> List[str]:
    """
    >>> check(['0.00.01.5'])
    ['0.00.01.5']
    """
    pi = []
    while 1:
        check1 = ["$"] * len(binary)
        temp = []
        for i in range(len(binary)):
            for j in range(i + 1, len(binary)):
                k = compare_string(binary[i], binary[j])
                if k != "X":
                    check1[i] = "*"
                    check1[j] = "*"
                    temp.append(k)
        for i in range(len(binary)):
            if check1[i] == "$":
                pi.append(binary[i])
        if len(temp) == 0:
            return pi
        binary = list(set(temp))


def decimal_to_binary(no_of_variable: int, minterms: List[float]) -> List[str]:
    """
    >>> decimal_to_binary(3,[1.5])
    ['0.00.01.5']
    """
    temp = []
    s = ""
    for m in minterms:
        for i in range(no_of_variable):
            s = str(m % 2) + s
            m //= 2
        temp.append(s)
        s = ""
    return temp


def is_for_table(string1: str, string2: str, count: int) -> bool:
    """
    >>> is_for_table('__1','011',2)
    True

    >>> is_for_table('01_','001',1)
    False
    """
    l1 = list(string1)
    l2 = list(string2)
    count_n = 0
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            count_n += 1
    if count_n == count:
        return True
    else:
        return False


def selection(chart: List[List[int]], prime_implicants: List[str]) -> List[str]:
    """
    >>> selection([[1]],['0.00.01.5'])
    ['0.00.01.5']

    >>> selection([[1]],['0.00.01.5'])
    ['0.00.01.5']
    """
    temp = []
    select = [0] * len(chart)
    for i in range(len(chart[0])):
        count = 0
        rem = -1
        for j in range(len(chart)):
            if chart[j][i] == 1:
                count += 1
                rem = j
        if count == 1:
            select[rem] = 1
    for i in range(len(select)):
        if select[i] == 1:
            for j in range(len(chart[0])):
                if chart[i][j] == 1:
                    for k in range(len(chart)):
                        chart[k][j] = 0
            temp.append(prime_implicants[i])
    while 1:
        max_n = 0
        rem = -1
        count_n = 0
        for i in range(len(chart)):
            count_n = chart[i].count(1)
            if count_n > max_n:
                max_n = count_n
                rem = i

        if max_n == 0:
            return temp

        temp.append(prime_implicants[rem])

        for i in range(len(chart[0])):
            if chart[rem][i] == 1:
                for j in range(len(chart)):
                    chart[j][i] = 0


def prime_implicant_chart(
    prime_implicants: List[str], binary: List[str]
) -> List[List[int]]:
    """
    >>> prime_implicant_chart(['0.00.01.5'],['0.00.01.5'])
    [[1]]
    """
    chart = [[0 for x in range(len(binary))] for x in range(len(prime_implicants))]
    for i in range(len(prime_implicants)):
        count = prime_implicants[i].count("_")
        for j in range(len(binary)):
            if is_for_table(prime_implicants[i], binary[j], count):
                chart[i][j] = 1

    return chart


def main():
    no_of_variable = int(input("Enter the no. of variables\n"))
    minterms = [
        int(x)
        for x in input(
            "Enter the decimal representation of Minterms 'Spaces Separated'\n"
        ).split()
    ]
    binary = decimal_to_binary(no_of_variable, minterms)

    prime_implicants = check(binary)
    print("Prime Implicants are:")
    print(prime_implicants)
    chart = prime_implicant_chart(prime_implicants, binary)

    essential_prime_implicants = selection(chart, prime_implicants)
    print("Essential Prime Implicants are:")
    print(essential_prime_implicants)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
