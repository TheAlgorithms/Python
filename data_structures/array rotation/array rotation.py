a = [1,2,3,4,5,6,7,8]

x = 2

n = len(a)


def rotate(a,x):
    n = len(a)

    if x == 0 or x == n:
        return a

    if x == n -x:
        print(a)
        for i in range(x):
            a[i], a[(i-x+n) % n] = a[(i-x+n) % n], a[i]
        print(a)
        return a

    if x < n-x:
        print(a)
        for i in range(x):
            a[i], a[(i-x+n) % n] = a[(i-x+n) % n], a[i]
        print(a)
        rotate(a[:n-x],x)
    else:
        print(a)
        for i in range(n-x):
            a[i], a[(i-(n-x) + n) % n] = a[(i-(n-x) + n) % n] , a[i]
        print(a)
        rotate(a[n-x:], n-x)

rotate(a,x)
print(a)