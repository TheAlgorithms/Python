print(
    "INSTRUCTIONS: USE 'and' / 'or' / 'not' when entering equation. For booleans use True/False or 1/0"
)

print()
while True:
    try:
        eq = input("Enter equation: ")

        print(eval(eq))
    except:
        pass
