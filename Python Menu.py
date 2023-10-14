def add():
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter a second number: "))
    res = num1 + num2
    print("The result is:", res)

def subtract():
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter a second number: "))
    res = num1 - num2
    print("The result is:", res)

def multi():
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter a second number: "))
    res = num1 * num2
    print("The result is:", res)

def divide():
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter a second number: "))
    res = num1 / num2
    print("The result is:", res)

def decbin():
    decimal = float(input("Enter a number: "))
    binario = ""
    cociente = int(decimal)
    while cociente != 1 :
        residuo =  cociente % 2
        cociente = cociente // 2
        binario = binario + str(residuo)

    binario = binario + str(residuo)
    res = binario [::-1]

    print(res)

def bindec():
    binario = input("Enter a binary number: ")
    decimal = 0
    longitud = len(binario)
    contador = 0
    binario_rev = binario[::-1]
    while contador < longitud:
        if binario_rev[contador] == "1":
            decimal += 2**contador
        contador +=1
    
    print( decimal)

def exit():
    print("See you!")
    sys.exit()

while True:
    print("Option Menu")
    print("1. Convert from binary to decimal")
    print("2. Convert from decimal to binary")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")
    print("5. Add two numbers")
    print("6. Subtract two numbers")
    print("7. Exit")
    
    opcion = input("Enter your option: ")
    
    if opcion == "1":
        bindec()
    elif opcion == "2":
        decbin()
    elif opcion == "3":
        multi()
    elif opcion == "4":
        divide()
    elif opcion == "5":
        add()
    elif opcion == "6":
        subtract()
    elif opcion == "7":
        exit()
    else:
        print("Invalid Option")