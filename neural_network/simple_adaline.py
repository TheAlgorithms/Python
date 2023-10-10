def wght_cng_or(wgt, T, al):
    O = wgt[0] * 0 + wgt[1] * 0
    if O <= T:
        Ol = wgt[0] * 0 + wgt[1] * 1
        if Ol >= T:
            Ole = wgt[0] * 1 + wgt[1] * 0
            if Ole >= T:
                Ola = wgt[0] * 1 + wgt[1] * 1
                if Ola >= T:
                    return wgt
                else:
                    wgt[0] = wgt[0] + al * 1 * 1
                    wgt[1] = wgt[1] + al * 1 * 1
                    return wght_cng_or(wgt, T, al)
            else:
                wgt[0] = wgt[0] + al * 1 * 1
                wgt[1] = wgt[1] + al * 1 * 0
                return wght_cng_or(wgt, T, al)
        else:
            wgt[0] = wgt[0] + al * 1 * 0
            wgt[1] = wgt[1] + al * 1 * 1
            return wght_cng_or(wgt, T, al)
    else:
        T += al
        return wght_cng_or(wgt, T, al)


def wght_cng_and(wgt, T, al):
    O = wgt[0] * 0 + wgt[1] * 0
    if O <= T:
        Ol = wgt[0] * 0 + wgt[1] * 1
        if Ol <= T:
            Ole = wgt[0] * 1 + wgt[1] * 0
            if Ole <= T:
                Ola = wgt[0] * 1 + wgt[1] * 1
                if Ola >= T:
                    return wgt
                else:
                    wgt[0] = wgt[0] + (al * 1 * 1)
                    wgt[1] = wgt[1] + (al * 1 * 1)
                    return wght_cng_and(wgt, T, al)
            else:
                wgt[0] = wgt[0] - (al * 1 * 1)
                wgt[1] = wgt[1] - (al * 1 * 0)
                return wght_cng_and(wgt, T, al)
        else:
            wgt[0] = wgt[0] - (al * 1 * 0)
            wgt[1] = wgt[1] - (al * 1 * 1)
            return wght_cng_and(wgt, T, al)
    else:
        T += al
        return wght_cng_and(wgt, T, al)


def and_gate(wgt, A, B, T, al):
    wgt = wght_cng_and(wgt, T, al)
    O = wgt[0] * A + wgt[1] * B
    if O >= T:
        return 1
    else:
        return 0


def or_gate(wgt, A, B, T, al):
    wgt = wght_cng_or(wgt, T, al)
    O = wgt[0] * A + wgt[1] * B
    if O >= T:
        return 1
    else:
        return 0


weight = [1.2, 0.6]
weight2 = [1.2, 0.6]
T = 1
al = 0.5
A, B = input("Input the value of A and B:").split()
A = int(A)
B = int(B)
print("\nThe output of OR is:", or_gate(weight, A, B, T, al))
print("\nThe output of AND is:", and_gate(weight2, A, B, T, al))
