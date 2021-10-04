def squareRoot(n, l) :
    x = n
    count = 0
    while (1) :
        count += 1
        root = 0.5 * (x + (n / x))
        if (abs(root - x) < l) :
            break
        x = root
    return root
if __name__ == "__main__" :
    n = int(input("Enter a number:"))
    l = 0.00001 #Tolerance level(max difference between assumed root and exact root)
    print(squareRoot(n, l))