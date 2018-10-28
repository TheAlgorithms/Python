import math
def primeCheck(number):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def main():
    print(primeCheck(37))
    print(primeCheck(100))
    print(primeCheck(77))

if __name__ == '__main__':
	main()
