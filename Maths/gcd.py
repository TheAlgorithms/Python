def gcd(a, b):  
    if a == 0 : 
        return b  
      
    return gcd(b%a, a)

def main():
	print(gcd(3, 6))


if __name__ == '__main__':
	main()
