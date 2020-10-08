# Self powers -> Problem 48

# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000

def solution():
    total_sum = 0
    for i in range(1,1001):
        total_sum += pow(i,i)
    total_sum = str(total_sum)
    print(str(total_sum)[-10:])

solution()
