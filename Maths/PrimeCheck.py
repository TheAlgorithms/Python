def primeCheck(number):
    prime = True
    for i in range(2, int(number**(0.5)+1), 2):
        if number % i == 0:
            prime = False
            break
    return prime

def main():
    print(primeCheck(37))
    print(primeCheck(100))

if __name__ == '__main__':
	main()
