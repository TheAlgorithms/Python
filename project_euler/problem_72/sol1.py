def count(limit: int) -> int:
    cfrac = list()
    s = 0

    for i in range(limit):
        cfrac.append(i)

    for i in range(2, limit):
        if cfrac[i] == i:
            for j in range(i, limit, i):
                cfrac[j] = (cfrac[j] * (i - 1)) / i
        s = s + cfrac[i]

    return s


if __name__ == "__main__":
    n = int(input().strip())
    print(count(n + 1))
