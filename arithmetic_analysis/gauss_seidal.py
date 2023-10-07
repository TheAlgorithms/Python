def seidel(a, x, b):
    # Finding length of a(3)
    n = len(a)
    # for loop for 3 times as to calculate x, y , z
    for j in range(0, n):
        # temp variable d to store b[j]
        d = b[j]

        # to calculate respective xi, yi, zi
        for i in range(0, n):
            if j != i:
                d -= a[j][i] * x[i]
        # updating the value of our solution
        x[j] = d / a[j][j]
    # returning our updated solution
    return x


if __name__ == "__main__":
    # int(input())input as number of variable to be solved
    n = 3
    a = []
    b = []
    # initial solution depending on n(here n=3)
    x = [0, 0, 0]
    a = [[4, 3, 2], [3, 5, 1], [1, 1, 3]]
    b = [4, 7, 3]
    print(x)

    # loop run for m times depending on m the error value
    for i in range(0, 25):
        x = seidel(a, x, b)
        # print each time the updated solution
        print(x)
