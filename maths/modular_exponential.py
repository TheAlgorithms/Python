def modularExponential(base, power, mod):
    if power < 0:
        return -1
    result = 1
    for i in range(power): 
        result = result * base % mod
    return result

def main():
	print(modularExponential(3, 200, 13))


if __name__ == '__main__':
	main()
