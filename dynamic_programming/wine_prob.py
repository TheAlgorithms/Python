"""Maximum profit from sale of wines"""

def count_max_sl_td(winePr, i, j, yr, dp):
    if i > j:
        return 0
    if dp[i][j] != 0:
        return dp[i][j]
    pr1 = winePr[i] * yr + count_max_sl_td(winePr, i + 1, j, yr + 1, dp)
    pr2 = winePr[j] * yr + count_max_sl_td(winePr, i, j - 1, yr + 1, dp)
    res = max(pr1, pr2)
    dp[i][j] = res
    return res


if __name__ == "__main__":
    winePr = list(map(int, input("Enter wine bottles's price :- ").split(" ")))
    no_bottle = len(winePr)
    dp = [[0 for i in range(100)] for j in range(100)]
    prc = count_max_sl_td(winePr, 0, no_bottle - 1, 1, dp)
    print("{}\n".format(prc))
