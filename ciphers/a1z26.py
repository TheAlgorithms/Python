def encode(plain):
	result = []
	for elem in plain:
		result.append(ord(elem) - 96)
	return result

def decode(encoded):
	result = ""
	for elem in encoded:
		result += chr(elem + 96)
	return result

def main():
	inp = input("->")
	lowered = inp.lower()
	encoded = encode(lowered)
	print("Encoded: ", encoded)
	decoded = decode(encoded)
	print("Decoded:", decoded)

if __name__ == "__main__":
	main()
