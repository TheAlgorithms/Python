import time

#fast_exp_algorithm
def fast_exp(a, n, m, gcd):
    a = (a % m)

    if gcd == 1:
        n = n % (m - 1)

        potencia_aux = a
        potencia = 1
        delta = n % 2
        potencia = ((potencia_aux ** delta) * potencia)
        n = ((n - delta) / 2)

        while n != 0:
            delta = n % 2
            potencia_aux = (potencia_aux ** 2) % m
            potencia = ((potencia_aux ** delta) * potencia) % m
            n = ((n - delta) / 2)

        print(potencia,"( mod", m, ")")
    else:
        print("To implement this algorithm, make shure that (a,m) = 1")


# Principal
a = int(input())
n = int(input())
m = int(input())
gcd = 1  #for tests lets asume that gcd = 1

print("\n")

start = time.clock()
fast_exp(a, n, m, gcd)
end = time.clock()

print("Time of this calculus:", end - start, "\n")
