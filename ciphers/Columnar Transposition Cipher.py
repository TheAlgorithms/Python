in_key = input("Enter key: ")
inpl_txt = input("Enter plain text: ")


def columnartransposition(key, pl_txt):
    # Declaring grid to store plain text in format
    grid = []
    # Declaring res to store string chars
    res = []

    dp = []
    for char in pl_txt:
        if char != " ":
            dp.append(char)
            if len(dp) == len(key):
                grid.append(dp)
                dp = []

    if len(dp):
        while len(dp) != len(key):
            dp.append("?")
        grid.append(dp)

    grid.insert(0, list(key))

    print("This is Grid")
    for row in grid:
        print(row)
    print()

    for row in sorted(list(zip(*grid)), key=lambda x: x[0]):
        for alpha in row[1:]:
            if alpha != "?":
                res.append(alpha)

    return "".join(res)


print(columnartransposition(in_key, inpl_txt))
