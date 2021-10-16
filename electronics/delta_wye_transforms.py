# Python project that calculates Delta - Wye and Wye - Delta Transforms

try:
    print("Do you want to perform a Delta-Wye Transform ? (Yes/No) ")
    operation = input()
    if operation.lower() == "yes":
        R12 = float(input("WHAT IS THE VALUE OF RESISTANCE, R12 ? "))
        R13 = float(input("WHAT IS THE VALUE OF RESISTANCE, R13 ? "))
        R23 = float(input("WHAT IS THE VALUE OF RESISTANCE, R23 ? "))
        S = (R12 + R13 + R23)
        r1 = (R13 * R12)/S
        r2 = (R23 * R12)/S
        r3 = (R13 * R23)/S
        print("Resistance R1 is given as " + str(r1))
        print("Resistance R2 is given as " + str(r2))
        print("Resistance R3 is given as " + str(r3))
    elif operation.lower() == "no":
        print("I would take it that you want to perform a Wye-Delta Transform ? (Yes/No ")
        operation2 = input()
        if operation2.lower() == "yes":
            R1 = float(input("WHAT IS THE VALUE OF RESISTANCE, R1 ? "))
            R2 = float(input("WHAT IS THE VALUE OF RESISTANCE, R2 ? "))
            R3 = float(input("WHAT IS THE VALUE OF RESISTANCE, R3 ? "))
            W = (R1 * R2) + (R2 * R3) + (R1 * R3)
            r23 = W/R1
            r13 = W/R2
            r12 = W/R3
            print("Resistance R12 is given as " + str(r12))
            print("Resistance R13 is given as " + str(r13))
            print("Resistance R23 is given as " + str(r23))
        else:
            print("I CAN ONLY PERFORM A DELTA-WYE OR WYE-DELTA TRANSFORM ")
    else:
        print("PLEASE ENTER EITHER YES OR NO.")
except ValueError:
    print("PLEASE INPUT NUMBERS FOR RESISTANCE VALUE.")
