def gcd(a, b):  
    if a == 0 : 
        return b  
      
    return gcd(b%a, a)

def main():
	print(modularExponential(3, 200, 13))


if __name__ == '__main__':
	main()
