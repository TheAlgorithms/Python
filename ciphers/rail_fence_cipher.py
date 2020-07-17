string = input("Enter string to be encrypted:")
print("Enter key for encryption (works best for small key values) : ", end = "")
key = int(input())

while key >= len(string):
	print("Please enter a smaller value: ", end = "")
	key = int(input())
	
def rail_fence_encrypt(string, key):
	a = [[None for i in range(len(string))] for j in range(key)]

	curr = 0
	findex = 0
	sindex = 0

	while curr < len(string):
		if findex < key:
			while findex < key and curr < len(string):
				a[findex][sindex] = string[curr]
				curr += 1
				findex += 1
				sindex += 1

		if findex == key:
			findex -= 1
			while findex > 0 and curr < len(string):
				findex -= 1
				a[findex][sindex] = string[curr]
				curr += 1
				sindex += 1
			findex += 1
	return a

encrypt_string = rail_fence_encrypt(string, key)

print("Rail fence matrix created: ")

encrypted_string = ""

for i in encrypt_string:
	l = [x for x in i if x is not None]
	encrypted_string += "".join(l)

print("Encrypted string:",encrypted_string)
