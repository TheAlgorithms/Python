# DarkCoder
def sumOfSeries(a, d, n):
    sum = ((n / 2) * (2 * a * (n - 1) * d))  # formula for sum of series
    print(sum)


def main():
    sumOfSeries(3, 4, 100)


if __name__ == "__main__":
    main()
