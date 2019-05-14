'''Given a tower with h floors and e identical eggs, how many drops will it take to find the lowest floow where the
egg breaks? The egg will break on some unknown floor, if it breaks on floor h then it will break above floor h aswell.
If the egg doesn't break then the egg isn't damaged.'''


def egg_drop(h, e):
    lst = [[0 for j in range(e + 1)] for i in range(h + 1)]

    for i in range(0, len(lst[0])):
        lst[0][i] = 0
        lst[1][i] = 1

    for i in range(0, h + 1):
        lst[i][1] = i

    for x in range(2, h + 1):
        bestDrops = None
        for j in range(2, e + 1):
            for n in range(1, x + 1):
                drop = 1 + max(lst[x - n][e], lst[n - 1][e - 1])
                if bestDrops is None:
                    bestDrops = drop
                else:
                    bestDrops = min(bestDrops, drop)
                lst[x][j] = bestDrops
    return lst[h][e]
