"""
Matris üstelik kullanarak n'inci Fibonacci sayısını bulma uygulaması.
Zaman karmaşıklığı yaklaşık O(log(n)*8)'dir; burada 8, 2'ye 2 boyutundaki matris
çarpımının karmaşıklığıdır.
Diğer yandan, zorlayıcı çözümün karmaşıklığı O(n)'dir.
Bildiğimiz gibi

Organiser: K. Umut Araz

    f[n] = f[n-1] + f[n-2]
Bunu matrise dönüştürdüğümüzde,
    [f(n),f(n-1)] = [[1,1],[1,0]] * [f(n-1),f(n-2)]
->  [f(n),f(n-1)] = [[1,1],[1,0]]^2 * [f(n-2),f(n-3)]
    ...
    ...
->  [f(n),f(n-1)] = [[1,1],[1,0]]^(n-1) * [f(1),f(0)]
Yani, sadece [1,1],[1,0] matrisinin n kez çarpımına ihtiyacımız var.
n kez çarpımı, böl ve fethet yaklaşımını takip ederek azaltabiliriz.
"""

def multiply(matrix_a: list[list[int]], matrix_b: list[list[int]]) -> list[list[int]]:
    matrix_c = []
    n = len(matrix_a)
    for i in range(n):
        list_1 = []
        for j in range(n):
            val = 0
            for k in range(n):
                val += matrix_a[i][k] * matrix_b[k][j]
            list_1.append(val)
        matrix_c.append(list_1)
    return matrix_c

def identity(n: int) -> list[list[int]]:
    return [[1 if row == column else 0 for column in range(n)] for row in range(n)]

def nth_fibonacci_matrix(n: int) -> int:
    """
    >>> nth_fibonacci_matrix(100)
    354224848179261915075
    >>> nth_fibonacci_matrix(-100)
    -100
    """
    if n <= 1:
        return n
    res_matrix = identity(2)
    fibonacci_matrix = [[1, 1], [1, 0]]
    n -= 1
    while n > 0:
        if n % 2 == 1:
            res_matrix = multiply(res_matrix, fibonacci_matrix)
        fibonacci_matrix = multiply(fibonacci_matrix, fibonacci_matrix)
        n //= 2
    return res_matrix[0][0]

def nth_fibonacci_bruteforce(n: int) -> int:
    """
    >>> nth_fibonacci_bruteforce(100)
    354224848179261915075
    >>> nth_fibonacci_bruteforce(-100)
    -100
    """
    if n <= 1:
        return n
    fib0, fib1 = 0, 1
    for _ in range(2, n + 1):
        fib0, fib1 = fib1, fib0 + fib1
    return fib1

def main() -> None:
    for ordinal in "0th 1st 2nd 3rd 10th 100th 1000th".split():
        n = int("".join(c for c in ordinal if c in "0123456789"))  # 1000th --> 1000
        print(
            f"{ordinal} Fibonacci sayısı matris üstelik kullanarak "
            f"{nth_fibonacci_matrix(n)} ve zorlayıcı yöntemle "
            f"{nth_fibonacci_bruteforce(n)}'dir.\n"
        )
    # from timeit import timeit
    # print(timeit("nth_fibonacci_matrix(1000000)",
    #              "from main import nth_fibonacci_matrix", number=5))
    # print(timeit("nth_fibonacci_bruteforce(1000000)",
    #              "from main import nth_fibonacci_bruteforce", number=5))
    # 2.3342058970001744
    # 57.256506615000035

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
