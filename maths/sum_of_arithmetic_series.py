def sumOfSeries(a, d, n):
    sum = (n / 2) * (2 * a (n - 1) * d)
    return sum

given_a = int(input("Enter the first value of the series: "))
given_d = int(input("Enter the difference of each term: "))
given_n = int(input("Enter the number of terms: "))

print(sumOfSeries(given_a, given_d, given_n))