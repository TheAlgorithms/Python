# po = int(input("ENTER NUMBER OF TRIALS : "))
po = 1
for _l in range(po):
    # i = str(input("ENTER NUMBER OF ROWS AND COLUMNS : ").strip())
    i = "2 3"
    kpo = str(i).split(" ")
    a = int(kpo[0])
    b = int(kpo[1])

    def matrix(r: int, c: int) -> None:
        _symbols = [".", "+", "-", "|"]
        t = c * 2 + 1
        # first two lines
        print(_symbols[0] * 2, end="")
        c = 2
        for _i in range(t - 2):
            if c % 2 == 0:
                print(_symbols[1], end="")
            else:
                print(_symbols[2], end="")
            c = c + 1
        print()
        # second row
        m = 2
        print(_symbols[0] * 2, end="")
        for _i in range(t - 2):
            if m % 2 == 0:
                print(_symbols[3], end="")
            else:
                print(_symbols[0], end="")
            m = m + 1
        print()
        # third row onwards

        f = 2 * r + 1
        j = 2
        for _i in range(f - 2):
            if j % 2 == 0:
                p = 2
                for _ka in range(t):
                    if p % 2 == 0:
                        print(_symbols[1], end="")
                    else:
                        print(_symbols[2], end="")
                    p = p + 1
            else:
                o = 2
                for _kam in range(t):
                    if o % 2 == 0:
                        print(_symbols[3], end="")
                    else:
                        print(_symbols[0], end="")
                    o = o + 1

            j = j + 1
            print()


if __name__ == "__main__":
    import doctest

    matrix(a, b)
    doctest.testmod()
