def primeCheck(number):
    prime = True
    for i in range(2, int(number**(0.5)+2), 2):
        if i != 2:
            i = i - 1
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
