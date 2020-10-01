for i in range(int(input("How manyy no. u want to calculate: "))-1):
    if i == 0:
        num1 = int(input("Enter First Number: "))
        total = num1
    command = input("Enter Command: ")
    num2 = int(input("Enter Another Number: "))
    if command == "+":
        total += num2
    if command == "-":
        total -= num2
    if command == "*":
        total *= num2
    if command == "/":
        total /= num2

print(f"Answer is {total}")