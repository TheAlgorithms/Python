"""Prime numbers calculation."""


def primes(max):
    max += 1
    numbers = [False] * max
    ret = []
    for i in range(2, max):
        if not numbers[i]:
            for j in range(i, max, i):
                numbers[j] = True
            ret.append(i)
    return ret



def main():
    print("Calculate primes up to:\n>> ", end="")
    n = int(input())
    print(primes(n))


if __name__ == "__main__":
    main()
