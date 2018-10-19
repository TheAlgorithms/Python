def primeCheck(number):
    prime = True
<<<<<<< HEAD
    for i in range(2, int(number**(1/2)+1), 2):
        if i != 2:
            i = i - 1
=======
    for i in range(2, int(number**(0.5)+1), 2):
>>>>>>> 3577f97de113fca832f514b96b2b18d0acc2f39a
        if number % i == 0:
            prime = False
            break
    return prime

def main():
    print(primeCheck(37))
    print(primeCheck(100))
    print(primeCheck(77))

if __name__ == '__main__':
	main()
