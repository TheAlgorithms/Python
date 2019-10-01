# Eulers Totient function finds the number of relative primes of a number n from 1 to n
def totient(n):
    isPrime = [True for i in range(n+1)]
    totients = [i-1 for i in range(n+1)]
    primes = []
    for i in range(2, n+1):
        if (isPrime[i] == True):
            primes.append(i)
        for j in range(0, len(primes)):
            if (i*primes[j] >= n):
                break
            isPrime[i*primes[j]] = False

            if (i%primes[j] == 0):
                totients[i*primes[j]] = totients[i]*primes[j]
                break

            totients[i*primes[j]] = totients[i]*(primes[j] - 1)
    
    return totients

if __name__ == "__main__":
    n = 10
    totientCalculation = totient(n)
    for i in range(1, n):
        print(i, totientCalculation[i], sep=" ")
