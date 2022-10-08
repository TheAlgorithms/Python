resistors = input("Type individual resistor resistance seperated by a coma (,) ...\n")

resistence = resistors.split(",")
for i in range(0, len(resistence)):
    resistence[i] = int(resistence[i])

total_resistance = sum(resistence)
print(f"Your total resistence is {total_resistance} ohms.")
