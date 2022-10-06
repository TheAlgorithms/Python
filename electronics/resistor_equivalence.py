def resistor_parallel(resistors : list[float]): #Req = 1/ (1/R1 + 1/R2 + ... + 1/Rn)
    firstSum = 0
    index = 0
    for resistor in resistors:
        if resistor < 0:
            raise ValueError(f"Resistor at index {index} has a negative value!")
        firstSum += 1/resistor
        index += 1
    return (1/firstSum)


def resistor_series(resistors : list[float]): #Req = R1 + R2 + ... + Rn
    sum = 0
    index = 0
    for resistor in resistors:

        sum += resistor
        if resistor < 0:
            raise ValueError(f"Resistor at index {index} has a negative value!")
        index += 1
        print(sum)
    return sum




if __name__ == "__main__":
    print(resistor_parallel([3.21389, 2, 3]))
