"""Maximum profit from sale of wines
Given n wines in a row, with integers denoting the cost of each wine respectively. 
Each year you can sale the first or the last wine in the row. 
However, the price of wines increases over time. 
Let the initial profits from the wines be P1, P2, P3…Pn. On the Yth year, 
the profit from the ith wine will be Y*Pi. For each year, 
your task is to print “beg” or “end” denoting whether first or last wine should be sold. 
Also, calculate the maximum profit from all the wines.
"""

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
